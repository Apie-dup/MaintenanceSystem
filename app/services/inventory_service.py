from app.models.inventory_model import InventoryModel
from app.services.supplier_service import SupplierService


class InventoryService:

    # ---------------------------------------------------------
    # Get All
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return InventoryModel.get_all()

    # ---------------------------------------------------------
    # Get By ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        return InventoryModel.get_by_id(record_id)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        return InventoryModel.search(search_text)

    # ---------------------------------------------------------
    # Next Part Number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_part_number():
        return InventoryModel.get_next_part_number()

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

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

        return InventoryModel.insert(data)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

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

        InventoryModel.update(
            record_id,
            data
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        InventoryModel.delete(record_id)

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
    def supplier_lookup():
        return SupplierService.get_active_suppliers()