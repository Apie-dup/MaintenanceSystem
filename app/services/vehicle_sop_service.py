from app.models.vehicle_sop_model import VehicleSopModel
from app.models.asset_model import AssetModel


class VehicleSopService:
    """
    Business logic for Vehicle SOP definitions.
    """

    FREQUENCIES = [
        "Daily",
        "Weekly",
        "Monthly",
    ]

    @staticmethod
    def get_all():
        return VehicleSopModel.get_all()

    @staticmethod
    def get_by_id(sop_id):
        return VehicleSopModel.get_by_id(sop_id)

    @staticmethod
    def search(text):
        text = (text or "").strip()

        if not text:
            return VehicleSopModel.get_all()

        return VehicleSopModel.search(text)

    @staticmethod
    def get_next_sop_number():
        return VehicleSopModel.get_next_sop_number()

    @staticmethod
    def get_frequencies():
        return VehicleSopService.FREQUENCIES.copy()

    @staticmethod
    def validate(data):
        sop_number = str(
            data.get("sop_number") or ""
        ).strip()

        sop_name = str(
            data.get("sop_name") or ""
        ).strip()

        frequency = str(
            data.get("frequency") or ""
        ).strip()

        asset_id = data.get("asset_id")

        if not sop_number:
            raise ValueError(
                "SOP Number is required."
            )

        if not asset_id:
            raise ValueError(
                "Vehicle / Asset is required."
            )

        if not sop_name:
            raise ValueError(
                "SOP Name is required."
            )

        if frequency not in VehicleSopService.FREQUENCIES:
            raise ValueError(
                "Frequency must be Daily, Weekly, or Monthly."
            )

        asset = AssetModel.get_by_id(asset_id)

        if asset is None:
            raise ValueError(
                "The selected Vehicle / Asset does not exist."
            )

    @staticmethod
    def create(data):
        VehicleSopService.validate(data)

        clean_data = dict(data)

        clean_data["sop_number"] = str(
            data["sop_number"]
        ).strip()

        clean_data["sop_name"] = str(
            data["sop_name"]
        ).strip()

        clean_data["frequency"] = str(
            data["frequency"]
        ).strip()

        clean_data["description"] = str(
            data.get("description") or ""
        ).strip()

        clean_data["notes"] = str(
            data.get("notes") or ""
        ).strip()

        clean_data["active"] = (
            1 if data.get("active", True) else 0
        )

        return VehicleSopModel.create(clean_data)

    @staticmethod
    def update(data):
        sop_id = data.get("id")

        if not sop_id:
            raise ValueError(
                "SOP ID is required."
            )

        existing = VehicleSopModel.get_by_id(sop_id)

        if existing is None:
            raise ValueError(
                "Vehicle SOP does not exist."
            )

        VehicleSopService.validate(data)

        clean_data = dict(data)

        clean_data["sop_number"] = str(
            data["sop_number"]
        ).strip()

        clean_data["sop_name"] = str(
            data["sop_name"]
        ).strip()

        clean_data["frequency"] = str(
            data["frequency"]
        ).strip()

        clean_data["description"] = str(
            data.get("description") or ""
        ).strip()

        clean_data["notes"] = str(
            data.get("notes") or ""
        ).strip()

        clean_data["active"] = (
            1 if data.get("active", True) else 0
        )

        return VehicleSopModel.update(clean_data)

    @staticmethod
    def delete(sop_id):
        existing = VehicleSopModel.get_by_id(sop_id)

        if existing is None:
            raise ValueError(
                "Vehicle SOP does not exist."
            )

        return VehicleSopModel.delete(sop_id)

    @staticmethod
    def get_active():

        return [
            sop
            for sop in VehicleSopModel.get_all()
            if sop["active"]
        ]