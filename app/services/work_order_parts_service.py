from app.database import connection
from app.database.connection import Database
from app.models.inventory_model import InventoryModel
from app.models.work_order_model import WorkOrderModel
from app.models.work_order_parts_model import WorkOrderPartModel
from app.services.work_order_history_service import (
    WorkOrderHistoryService
)


class WorkOrderPartService:

    # ---------------------------------------------------------
    # Get parts for a work order
    # ---------------------------------------------------------

    @staticmethod
    def get_by_work_order(work_order_id):
        return WorkOrderPartModel.get_by_work_order(
            work_order_id
        )

    # ---------------------------------------------------------
    # Total material cost
    # ---------------------------------------------------------

    @staticmethod
    def get_total_cost(work_order_id):
        return WorkOrderPartModel.get_total_cost(
            work_order_id
        )

    # ---------------------------------------------------------
    # Inventory lookup
    # ---------------------------------------------------------

    @staticmethod
    def inventory_lookup():
        return InventoryModel.get_all()

    # ---------------------------------------------------------
    # Issue Part
    # ---------------------------------------------------------

    @staticmethod
    def issue_part(data):

        conn = Database.connect()

        status_changed = False
        inventory = None
        unit_cost = 0.00

        try:
            inventory = InventoryModel.get_by_id(
                data["inventory_id"]
            )

            if inventory is None:
                raise ValueError(
                    "Inventory item not found."
                )

            available = float(
                inventory["quantity"] or 0
            )

            quantity = float(
                data["quantity"] or 0
            )

            if quantity <= 0:
                raise ValueError(
                    "Quantity must be greater than zero."
                )

            if quantity > available:
                raise ValueError(
                    f"Only {available} available."
                )

            unit_cost = float(
                inventory["unit_cost"] or 0
            )

            total_cost = (
                quantity * unit_cost
            )

            # -------------------------------------------------
            # Insert issued part
            # -------------------------------------------------

            WorkOrderPartModel.insert(
                {
                    "work_order_id":
                        data["work_order_id"],

                    "inventory_id":
                        data["inventory_id"],

                    "quantity":
                        quantity,

                    "unit_cost":
                        unit_cost,

                    "total_cost":
                        total_cost,

                    "notes":
                        data["notes"],
                },
                connection=conn
            )

            # -------------------------------------------------
            # Reduce inventory quantity
            # -------------------------------------------------

            InventoryModel.update_quantity(
                data["inventory_id"],
                available - quantity,
                connection=conn
            )

            # -------------------------------------------------
            # Recalculate full actual cost
            # Labour + Materials
            # -------------------------------------------------

            actual_cost = (
                WorkOrderModel.calculate_actual_cost(
                    data["work_order_id"],
                    connection=conn
                )
            )

            WorkOrderModel.update_actual_cost(
                data["work_order_id"],
                actual_cost,
                connection=conn
            )

            # -------------------------------------------------
            # Assigned -> In Progress
            # -------------------------------------------------

            cursor = conn.cursor()

            cursor.execute("""
                SELECT status
                FROM work_orders
                WHERE id = ?
            """, (
                data["work_order_id"],
            ))

            work_order = cursor.fetchone()

            if (
                work_order is not None
                and work_order["status"] == "Assigned"
            ):
                WorkOrderModel.set_status(
                    data["work_order_id"],
                    "In Progress",
                    connection=conn
                )

                status_changed = True

            # Everything succeeded.
            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

        # -------------------------------------------------
        # History
        # Only after successful transaction
        # -------------------------------------------------

        if status_changed:
            WorkOrderHistoryService.add(
                data["work_order_id"],
                action="Updated",
                field_name="Status",
                old_value="Assigned",
                new_value="In Progress",
                notes=(
                    "Status changed automatically "
                    "when a part was issued."
                ),
            )

        WorkOrderHistoryService.add(
            data["work_order_id"],
            action="Part Issued",
            field_name="Material",
            old_value=None,
            new_value=(
                f'{quantity:g} x '
                f'{inventory["part_name"]}'
            ),
            notes=(
                f'Part {inventory["part_number"]} issued '
                f'at unit cost {unit_cost:.2f}.'
            ),
        )

    @staticmethod
    def set_status(
        work_order_id,
        status,
        connection=None
    ):
        owns_connection = (
            connection is None
        )

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE work_orders
                SET status = ?
                WHERE id = ?
            """, (
                status,
                work_order_id,
            ))

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    @staticmethod
    def remove_part(record_id):

        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    work_order_parts.id,
                    work_order_parts.work_order_id,
                    work_order_parts.inventory_id,
                    work_order_parts.quantity,
                    inventory.part_number,
                    inventory.part_name
                FROM work_order_parts
                LEFT JOIN inventory
                    ON work_order_parts.inventory_id = inventory.id
                WHERE work_order_parts.id = ?
            """, (record_id,))

            issued_part = cursor.fetchone()

            if issued_part is None:
                raise ValueError(
                    "Issued part record not found."
                )
            work_order_id = (
                issued_part["work_order_id"]
            )
            inventory_id = (
                issued_part["inventory_id"]
            )

            issued_quantity = float(
                issued_part["quantity"] or 0
            )

            part_number = (
                issued_part["part_number"] or ""
            )

            part_name = (
                issued_part["part_name"] or ""
            )

            cursor.execute("""
                SELECT quantity
                FROM inventory
                WHERE id = ?
            """, (
                inventory_id,
            ))

            inventory = cursor.fetchone()

            if inventory is None:
                raise ValueError(
                    "The related inventory item "
                    "could not be found."
                )

            current_quantity = float(
                inventory["quantity"] or 0
            )

            restored_quantity = (
                current_quantity
                + issued_quantity
            )

            InventoryModel.update_quantity(
                inventory_id,
                restored_quantity,
                connection=conn
            )

            WorkOrderPartModel.delete(
                record_id,
                connection=conn
            )

            actual_cost = (
                WorkOrderModel.calculate_actual_cost(
                    work_order_id,
                    connection=conn
                )
            )

            WorkOrderModel.update_actual_cost(
                work_order_id,
                actual_cost,
                connection=conn
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

        # Only log after successful commit.
        WorkOrderHistoryService.add(
            work_order_id,
            action="Part Returned",
            field_name="Material",
            old_value=(
                f"{issued_quantity} x "
                f"{part_name}"
            ),
            new_value=None,
            notes=(
                f"Part {part_number} returned "
                "to inventory."
            ),
        )