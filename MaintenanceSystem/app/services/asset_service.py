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