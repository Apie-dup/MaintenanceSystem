from app.models.asset_model import AssetModel

class AssetService:

    @staticmethod
    def get_all():
        return AssetModel.get_all()
    
    @staticmethod
    def get(asset_id):
        return AssetModel.get_by_id(asset_id)
    
    @staticmethod
    def add(record):
        AssetModel.insert(record)

    @staticmethod
    def update(record):
        AssetModel.update(record)

    @staticmethod
    def delete(asset_id):
        AssetModel.delete(asset_id)

    @staticmethod
    def searc(text):
        return AssetModel.search(text)
    
    # Asset-specific business logic
    @staticmethod
    def get_next_asset_number():
        return AssetModel.get_next_asset_number()