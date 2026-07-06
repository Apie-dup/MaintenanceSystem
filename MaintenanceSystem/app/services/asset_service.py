from app.models.asset_model import AssetModel


class AssetService:

    @staticmethod
    def get_assets():
        return AssetModel.get_all()

    @staticmethod
    def add_asset(asset):
        AssetModel.insert(asset)

    @staticmethod
    def get_next_asset_number():
        return AssetModel.get_next_asset_number()
    
    @staticmethod
    def get_asset(asset_id):
        return AssetModel.get_by_id(asset_id)
    
    @staticmethod
    def update_asset(asset):
        AssetModel.update(asset)

    @staticmethod
    def delete_asset(asset_id):
        AssetModel.delete(asset_id)