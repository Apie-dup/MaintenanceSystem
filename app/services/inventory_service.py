from app.models.inventory_model import InventoryModel
from app.services.supplier_service import SupplierService
from app.database.connection import Database
from app.services.inventory_transaction_service import (
    InventoryTransactionService
)


class InventoryService:

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return InventoryModel.get_all()

    @staticmethod
    def get_by_id(record_id):
        return InventoryModel.get_by_id(
            record_id
        )

    @staticmethod
    def search(search_text):
        return InventoryModel.search(
            search_text
        )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @staticmethod
    def get_next_part_number():
        return InventoryModel.get_next_part_number()

    @staticmethod
    def supplier_lookup():
        return SupplierService.get_active_suppliers()

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def validate(data):

        if not data["part_number"].strip():
            raise ValueError(
                "Part Number is required."
            )

        if not data["part_name"].strip():
            raise ValueError(
                "Part Name is required."
            )

        if not data["category"].strip():
            raise ValueError(
                "Category is required."
            )

        if not data["unit"].strip():
            raise ValueError(
                "Unit is required."
            )

        if data["quantity"] < 0:
            raise ValueError(
                "Quantity cannot be negative."
            )

        if data["minimum_quantity"] < 0:
            raise ValueError(
                "Minimum Quantity cannot be negative."
            )

        if data["reorder_quantity"] < 0:
            raise ValueError(
                "Reorder Quantity cannot be negative."
            )

        if data["unit_cost"] < 0:
            raise ValueError(
                "Unit Cost cannot be negative."
            )

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(
        data,
        user=None
    ):

        InventoryService.validate(data)

        if InventoryModel.part_number_exists(
            data["part_number"]
        ):
            raise ValueError(
                "Part Number already exists."
            )

        conn = Database.connect()

        try:

            opening_quantity = float(
                data["quantity"] or 0
            )

            inventory_id = (
                InventoryModel.insert(
                    data,
                    connection=conn
                )
            )

            if opening_quantity > 0:

                InventoryTransactionService.record(
                    inventory_id=inventory_id,
                    transaction_type=(
                        InventoryTransactionService
                        .OPENING_STOCK
                    ),
                    quantity_change=opening_quantity,
                    previous_quantity=0,
                    new_quantity=opening_quantity,
                    unit_cost=float(
                        data["unit_cost"] or 0
                    ),
                    reference="Opening Stock",
                    notes=(
                        "Opening stock recorded "
                        "when inventory item was created."
                    ),
                    user=user,
                    connection=conn,
                )

            conn.commit()

            return inventory_id

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(
        record_id,
        data
    ):

        existing = InventoryModel.get_by_id(
            record_id
        )

        if existing is None:
            raise ValueError(
                "Inventory item not found."
            )

        save_data = dict(data)

        # Stock quantity is controlled only through
        # inventory transaction workflows.
        save_data["quantity"] = float(
            existing["quantity"] or 0
        )

        InventoryService.validate(
            save_data
        )

        if InventoryModel.part_number_exists(
            save_data["part_number"],
            exclude_id=record_id,
        ):
            raise ValueError(
                "Part Number already exists."
            )

        InventoryModel.update(
            record_id,
            save_data
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        InventoryModel.delete(
            record_id
        )

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    @staticmethod
    def get_low_stock():
        return InventoryModel.get_low_stock()

    @staticmethod
    def get_total_stock_value():
        return InventoryModel.get_total_stock_value()

    @staticmethod
    def get_low_stock():

        return (
            InventoryModel.get_low_stock()
        )