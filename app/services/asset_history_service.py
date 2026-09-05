from app.models.asset_history_model import AssetHistoryModel


class AssetHistoryService:

    @staticmethod
    def get_history(asset_id):

        if not asset_id:
            raise ValueError(
                "Asset is required."
            )

        return AssetHistoryModel.get_history(
            asset_id
        )