from app.models.asset_model import AssetModel


class AssetService:

    @staticmethod
    def get_assets():
        return AssetModel.get_all()