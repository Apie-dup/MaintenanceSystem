from app.models.asset_model import AssetModel


class AssetService:

    @staticmethod
    def get_all():
        return AssetModel.get_all()

    @staticmethod
    def get_by_id(record_id):
        return AssetModel.get_by_id(record_id)

    @staticmethod
    def search(search_text):
        return AssetModel.search(search_text)

    @staticmethod
    def get_next_asset_number():
        return AssetModel.get_next_asset_number()

    @staticmethod
    def create(data):
        return AssetModel.insert(data)

    @staticmethod
    def update(record_id, data):
        AssetModel.update(
            record_id,
            data
        )

    @staticmethod
    def delete(record_id):
        AssetModel.delete(record_id)