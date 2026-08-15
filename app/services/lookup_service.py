from app.models.lookup_model import LookupModel


class LookupService:

    @staticmethod
    def get_all(lookup_type):
        return LookupModel.get_all(
            lookup_type
        )

    @staticmethod
    def get(record_id):
        return LookupModel.get(
            record_id
        )

    @staticmethod
    def search(lookup_type, text):
        return LookupModel.search(
            lookup_type,
            text
        )

    @staticmethod
    def add_lookup_value(
        lookup_type,
        value
    ):
        value = value.strip()

        if not value:
            raise ValueError(
                "Lookup value is required."
            )

        # Default new lookup settings
        record = (
            lookup_type,
            value,
            0,      # sort_order
            1,      # active
        )

        return LookupModel.insert(
            record
        )

    @staticmethod
    def update_lookup_value(
        lookup_type,
        lookup_id,
        value
    ):
        value = value.strip()

        if not value:
            raise ValueError(
                "Lookup value is required."
            )

        existing = LookupModel.get(
            lookup_id
        )

        if existing is None:
            raise ValueError(
                "Lookup record not found."
            )

        record = (
            lookup_type,
            value,
            existing["sort_order"],
            existing["active"],
            lookup_id,
        )

        LookupModel.update(
            record
        )

    @staticmethod
    def delete_lookup_value(
        lookup_type,
        lookup_id
    ):
        # lookup_type is supplied by the controller,
        # but the ID is sufficient for deletion.
        LookupModel.delete(
            lookup_id
        )