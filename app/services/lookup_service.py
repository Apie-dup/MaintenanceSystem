from app.models.inventory_model import InventoryModel


class InventoryService:

    @staticmethod
    def get_inventory():
        return InventoryModel.get_all()

    @staticmethod
    def get_item(part_id):
        return InventoryModel.get(part_id)

    @staticmethod
    def get_next_part_number():
        return InventoryModel.get_next_part_number()

    @staticmethod
    def add_item(part):
        InventoryModel.insert(part)

    @staticmethod
    def update_item(part):
        InventoryModel.update(part)

    @staticmethod
    def delete_item(part_id):
        InventoryModel.delete(part_id)

    @staticmethod
    def search_items(search_text):
        return InventoryModel.search(search_text)

    @staticmethod
    def get_low_stock_items():
        return InventoryModel.get_low_stock()

    @staticmethod
    def get_total_stock_value():
        return InventoryModel.get_total_stock_value()