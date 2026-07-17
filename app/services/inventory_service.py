from app.models.inventory_model import InventoryModel


class InventoryService:

    @staticmethod
    def get_inventory():
        return InventoryModel.get_all()

    @staticmethod
    def get_inventory_item(part_id):
        return InventoryModel.get_by_id(part_id)

    @staticmethod
    def get_next_part_number():
        return InventoryModel.get_next_part_number()

    @staticmethod
    def add_inventory(part):
        InventoryModel.insert(part)

    @staticmethod
    def update_inventory(part):
        InventoryModel.update(part)

    @staticmethod
    def delete_inventory(part_id):
        InventoryModel.delete(part_id)

    @staticmethod
    def search_inventory(search_text):
        return InventoryModel.search(search_text)

    @staticmethod
    def get_low_stock_items():
        return InventoryModel.get_low_stock()

    @staticmethod
    def get_total_stock_value():
        return InventoryModel.get_total_stock_value()