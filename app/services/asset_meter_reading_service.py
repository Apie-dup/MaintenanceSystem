from app.models.asset_meter_reading_model import (
    AssetMeterReadingModel
)


class AssetMeterReadingService:

    @staticmethod
    def add_reading(
        asset_id,
        meter_type,
        reading,
        reading_date,
        notes=None,
    ):

        reading = float(reading)

        if reading < 0:
            raise ValueError(
                "Meter reading cannot be negative."
            )

        latest = (
            AssetMeterReadingModel.get_latest_reading(
                asset_id,
                meter_type,
            )
        )

        if latest is not None:
            previous = float(
                latest["reading"] or 0
            )

            if reading < previous:
                raise ValueError(
                    "Meter reading cannot be lower "
                    "than the previous reading."
                )

        return AssetMeterReadingModel.add(
            asset_id,
            meter_type,
            reading,
            reading_date,
            notes,
        )

    @staticmethod
    def get_latest_reading(
        asset_id,
        meter_type,
    ):
        return (
            AssetMeterReadingModel.get_latest_reading(
                asset_id,
                meter_type,
            )
        )

    @staticmethod
    def get_history(
        asset_id,
        meter_type=None,
    ):
        return AssetMeterReadingModel.get_history(
            asset_id,
            meter_type,
        )

    @staticmethod
    def get_latest_reading_value(
        asset_id,
        meter_type
    ):
        latest = AssetMeterReadingService.get_latest_reading(
            asset_id,
            meter_type
        )

        if latest is None:
            return None

        return float(
            latest["reading"] or 0
        )