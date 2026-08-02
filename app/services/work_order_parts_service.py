from app.database.connection import Database
from app.models.inventory_model import InventoryModel
from app.models.work_order_model import WorkOrderModel
from app.models.work_order_parts_model import WorkOrderPartModel


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

        try:

            inventory = InventoryModel.get_by_id(
                data["inventory_id"]
            )

            if inventory is None:
                raise ValueError(
                    "Inventory item not found."
                )

            available = inventory["quantity"]

            if data["quantity"] <= 0:
                raise ValueError(
                    "Quantity must be greater than zero."
                )

            if data["quantity"] > available:
                raise ValueError(
                    f"Only {available} available."
                )

            unit_cost = inventory["unit_cost"]

            total_cost = (
                data["quantity"] * unit_cost
            )

            WorkOrderPartModel.insert(
                {
                    "work_order_id":
                        data["work_order_id"],

                    "inventory_id":
                        data["inventory_id"],

                    "quantity":
                        data["quantity"],

                    "unit_cost":
                        unit_cost,

                    "total_cost":
                        total_cost,

                    "notes":
                        data["notes"],
                },
                connection=conn
            )

            InventoryModel.update_quantity(
                data["inventory_id"],
                available - data["quantity"],
                connection=conn
            )

            material_cost = WorkOrderPartModel.get_total_cost(
                data["work_order_id"],
                connection=conn
            )

            WorkOrderModel.update_actual_cost(
                data["work_order_id"],
                material_cost,
                connection=conn
            )

            conn.commit()

        except Exception:

            conn.rollback()

            raise

        finally:

            conn.close()

    @staticmethod
    def remove_part(record_id):

        conn = Database.connect()

        try:
            cursor = conn.cursor()

            # Get the issued-part record using this transaction.
            cursor.execute("""
                SELECT
                    id,
                    work_order_id,
                    inventory_id,
                    quantity
                FROM work_order_parts
                WHERE id = ?
            """, (record_id,))

            issued_part = cursor.fetchone()

            if issued_part is None:
                raise ValueError(
                    "Issued part record not found."
                )

            work_order_id = issued_part["work_order_id"]
            inventory_id = issued_part["inventory_id"]
            issued_quantity = float(
                issued_part["quantity"] or 0
            )

            # Read current inventory quantity.
            cursor.execute("""
                SELECT quantity
                FROM inventory
                WHERE id = ?
            """, (inventory_id,))

            inventory = cursor.fetchone()

            if inventory is None:
                raise ValueError(
                    "The related inventory item could not be found."
                )

            current_quantity = float(
                inventory["quantity"] or 0
            )

            restored_quantity = (
                current_quantity + issued_quantity
            )

            # Restore stock.
            InventoryModel.update_quantity(
                inventory_id,
                restored_quantity,
                connection=conn
            )

            # Delete the issued-part record.
            WorkOrderPartModel.delete(
                record_id,
                connection=conn
            )

            # Recalculate material cost after deletion.
            material_cost = (
                WorkOrderPartModel.get_total_cost(
                    work_order_id,
                    connection=conn
                )
            )

            # Update work-order cost.
            WorkOrderModel.update_actual_cost(
                work_order_id,
                material_cost,
                connection=conn
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()
