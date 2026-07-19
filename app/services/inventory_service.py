from app.models.inventory_model import InventoryModel


class InventoryService:

    @staticmethod
    def get_all():
        return InventoryModel.get_all()

    @staticmethod
    def get(part_id):
        return InventoryModel.get_by_id(part_id)

    @staticmethod
    def get_next_part_number():
        return InventoryModel.get_next_part_number()

    @staticmethod
    def add(record):
        InventoryModel.insert(record)

    @staticmethod
    def update(record):
        InventoryModel.update(record)

    @staticmethod
    def delete(part_id):
        InventoryModel.delete(part_id)

    @staticmethod
    def search(text):
        return InventoryModel.search(text)

    @staticmethod
    def get_low_stock_items():
        return InventoryModel.get_low_stock()

    @staticmethod
    def get_total_stock_value():
        return InventoryModel.get_total_stock_value()