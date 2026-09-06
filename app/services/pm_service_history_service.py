from app.models.pm_service_history_model import (
    PMServiceHistoryModel
)


class PMServiceHistoryService:

    @staticmethod
    def create(data, conn=None):

        if not data.get("pm_id"):
            raise ValueError(
                "PM schedule is required."
            )

        if not data.get("asset_id"):
            raise ValueError(
                "Asset is required."
            )

        if not data.get("service_date"):
            raise ValueError(
                "Service date is required."
            )

        return PMServiceHistoryModel.create(
            data,
            conn=conn
        )

    @staticmethod
    def get_by_pm_id(pm_id):

        return PMServiceHistoryModel.get_by_pm_id(
            pm_id
        )

    @staticmethod
    def get_by_asset_id(asset_id):

        return PMServiceHistoryModel.get_by_asset_id(
            asset_id
        )