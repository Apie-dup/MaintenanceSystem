from app.models.asset_model import AssetModel


class AssetService:

    # ---------------------------------------------------------
    # Get all assets
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return AssetModel.get_all()

    # ---------------------------------------------------------
    # Get asset by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        return AssetModel.get_by_id(record_id)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        return AssetModel.search(search_text)

    # ---------------------------------------------------------
    # Next asset number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_asset_number():
        return AssetModel.get_next_asset_number()

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        if not data["asset_name"].strip():
            raise ValueError(
                "Asset Name is required."
            )

        if not data["category"].strip():
            raise ValueError(
                "Category is required."
            )

        if not data["status"].strip():
            raise ValueError(
                "Status is required."
            )

        if AssetModel.get_by_number(
            data["asset_number"]
        ):
            raise ValueError(
                "Asset Number already exists."
            )

        if not data["category"].strip():
            raise ValueError(
                "Category is required."
        )

        if AssetModel.number_exists(
            data["asset_number"]
    ):
            raise ValueError(
            "Asset Number already exists."
        )

        return AssetModel.insert(data)


    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        if not data["asset_name"].strip():
            raise ValueError(
                "Asset Name is required."
        )

        if not data["category"].strip():
            raise ValueError(
                "Category is required."
        )

        if AssetModel.number_exists(
            data["asset_number"],
            exclude_id=record_id
        ):
            raise ValueError(
                "Asset Number already exists."
        )

        AssetModel.update(
            record_id,
            data
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        AssetModel.delete(record_id)

    @staticmethod
    def get_active_assets():
        return AssetModel.get_active_assets()