from app.models.inventory_model import InventoryModel
from app.services.supplier_service import SupplierService


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
    def create(data):

        InventoryService.validate(data)

        if InventoryModel.part_number_exists(
            data["part_number"]
        ):
            raise ValueError(
                "Part Number already exists."
            )

        return InventoryModel.insert(data)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        InventoryService.validate(data)

        if InventoryModel.part_number_exists(
            data["part_number"],
            exclude_id=record_id,
        ):
            raise ValueError(
                "Part Number already exists."
            )

        InventoryModel.update(
            record_id,
            data
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