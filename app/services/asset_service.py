from app.models.asset_model import AssetModel

class AssetService:

    @staticmethod
    def get_all():
        return AssetModel.get_all()
    
    @staticmethod
    def get(record_id):
        return AssetModel.get_by_id(record_id)
    
    @staticmethod
    def add(record):
        AssetModel.insert(record)

    @staticmethod
    def update(record):
        AssetModel.update(record)

    @staticmethod
    def delete(record_id):
        AssetModel.delete(record_id)

    @staticmethod
    def search(text):
        return AssetModel.search(text)

    @staticmethod
    def searc(text):
        return AssetService.search(text)
    
    # Asset-specific business logic
    @staticmethod
    def get_next_asset_number():
        return AssetModel.get_next_asset_number()