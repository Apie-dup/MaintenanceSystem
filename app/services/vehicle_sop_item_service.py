from app.models.vehicle_sop_item_model import (
    VehicleSopItemModel
)
from app.models.vehicle_sop_model import VehicleSopModel


class VehicleSopItemService:
    """
    Business logic for Vehicle SOP checklist items.
    """

    @staticmethod
    def get_by_sop_id(sop_id):
        return VehicleSopItemModel.get_by_sop_id(
            sop_id
        )

    @staticmethod
    def get_by_id(item_id):
        return VehicleSopItemModel.get_by_id(
            item_id
        )

    @staticmethod
    def get_next_sequence(sop_id):
        return VehicleSopItemModel.get_next_sequence(
            sop_id
        )

    @staticmethod
    def validate(data):
        sop_id = data.get("sop_id")

        description = str(
            data.get("check_description") or ""
        ).strip()

        if not sop_id:
            raise ValueError(
                "Vehicle SOP is required."
            )

        sop = VehicleSopModel.get_by_id(sop_id)

        if sop is None:
            raise ValueError(
                "Vehicle SOP does not exist."
            )

        if not description:
            raise ValueError(
                "Check Description is required."
            )

        sequence = data.get("sequence")

        if sequence is None:
            raise ValueError(
                "Sequence is required."
            )

        try:
            sequence = int(sequence)
        except (TypeError, ValueError):
            raise ValueError(
                "Sequence must be a whole number."
            )

        if sequence < 1:
            raise ValueError(
                "Sequence must be greater than zero."
            )

    @staticmethod
    def create(data):
        VehicleSopItemService.validate(data)

        clean_data = dict(data)

        clean_data["sequence"] = int(
            data["sequence"]
        )

        clean_data["check_description"] = str(
            data["check_description"]
        ).strip()

        clean_data["required"] = (
            1 if data.get("required", True) else 0
        )

        return VehicleSopItemModel.create(
            clean_data
        )

    @staticmethod
    def update(data):
        item_id = data.get("id")

        if not item_id:
            raise ValueError(
                "SOP Checklist Item ID is required."
            )

        existing = VehicleSopItemModel.get_by_id(
            item_id
        )

        if existing is None:
            raise ValueError(
                "SOP checklist item does not exist."
            )

        VehicleSopItemService.validate(data)

        clean_data = dict(data)

        clean_data["sequence"] = int(
            data["sequence"]
        )

        clean_data["check_description"] = str(
            data["check_description"]
        ).strip()

        clean_data["required"] = (
            1 if data.get("required", True) else 0
        )

        return VehicleSopItemModel.update(
            clean_data
        )

    @staticmethod
    def delete(item_id):
        existing = VehicleSopItemModel.get_by_id(
            item_id
        )

        if existing is None:
            raise ValueError(
                "SOP checklist item does not exist."
            )

        return VehicleSopItemModel.delete(
            item_id
        )