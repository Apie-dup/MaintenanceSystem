from app.database.connection import Database
from app.models.vehicle_logbook_model import VehicleLogbookModel
from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)
from app.models.asset_meter_reading_model import AssetMeterReadingModel


class VehicleLogbookService:

    @staticmethod
    def get_all():
        return VehicleLogbookModel.get_all()

    @staticmethod
    def get_by_id(record_id):
        return VehicleLogbookModel.get_by_id(
            record_id
        )

    @staticmethod
    def get_by_asset(asset_id):
        return VehicleLogbookModel.get_by_asset(
            asset_id
        )

    @staticmethod
    def create(data, user=None):

        asset_id = data.get("asset_id")
        log_date = (
            data.get("log_date") or ""
        ).strip()

        start_meter = float(
            data.get("start_meter") or 0
        )

        end_meter = float(
            data.get("end_meter") or 0
        )

        if not asset_id:
            raise ValueError(
                "Vehicle is required."
            )

        if not log_date:
            raise ValueError(
                "Log Date is required."
            )

        if start_meter < 0:
            raise ValueError(
                "Start Meter cannot be negative."
            )

        if end_meter < 0:
            raise ValueError(
                "End Meter cannot be negative."
            )

        if end_meter < start_meter:
            raise ValueError(
                "End Meter cannot be less than Start Meter."
            )

        distance = (
            end_meter - start_meter
        )

        record_data = dict(data)

        record_data["start_meter"] = (
            start_meter
        )

        record_data["end_meter"] = (
            end_meter
        )

        record_data["distance"] = (
            distance
        )

        record_data["user_id"] = (
            user.get("id")
            if user
            else None
        )

        record_data["username"] = (
            user.get("username")
            if user
            else None
        )

        conn = Database.connect()

        try:

            logbook_id = (
                VehicleLogbookModel.create(
                    record_data,
                    conn=conn,
                )
            )

            AssetMeterReadingService.add_reading(
                asset_id=asset_id,
                meter_type="Kilometers",
                reading=end_meter,
                reading_date=log_date,
                notes=(
                    "Recorded from vehicle "
                    "logbook entry."
                ),
                source_type="Vehicle Logbook",
                logbook_id=logbook_id,
                conn=conn,
            )

            conn.commit()

            return logbook_id

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def update(
        record_id,
        data,
    ):

        existing = (
            VehicleLogbookModel.get_by_id(
                record_id
            )
        )

        if existing is None:
            raise ValueError(
                "Vehicle Logbook entry not found."
            )

        asset_id = data.get("asset_id")

        log_date = (
            data.get("log_date") or ""
        ).strip()

        start_meter = float(
            data.get("start_meter") or 0
        )

        end_meter = float(
            data.get("end_meter") or 0
        )

        if not asset_id:
            raise ValueError(
                "Vehicle is required."
            )

        if not log_date:
            raise ValueError(
                "Log date is required."
            )

        if start_meter < 0:
            raise ValueError(
                "Start Meter cannot be negative."
            )

        if end_meter < 0:
            raise ValueError(
                "End Meter cannot be negative."
            )

        if end_meter < start_meter:
            raise ValueError(
                "End Meter cannot be less than Start Meter."
            )

        record_data = dict(data)

        record_data["start_meter"] = (
            start_meter
        )

        record_data["end_meter"] = (
            end_meter
        )

        record_data["distance"] = (
            end_meter - start_meter
        )

        conn = Database.connect()

        try:

            VehicleLogbookModel.update(
                record_id,
                record_data,
                conn=conn
            )

            meter_record = (
                AssetMeterReadingModel
                .get_by_logbook_id(
                    record_id,
                    conn=conn,
                )
            )

            if meter_record is not None:

                AssetMeterReadingModel.update_logbook_reading(
                    logbook_id=record_id,
                    asset_id=asset_id,
                    reading=end_meter,
                    reading_date=log_date,
                    conn=conn,
                )

            else:

                AssetMeterReadingService.add_reading(
                    asset_id=asset_id,
                    meter_type="Kilometers",
                    reading=end_meter,
                    reading_date=log_date,
                    notes=(
                        "Recorded from vehicle "
                        "log entry."
                    ),
                    source_type="Vehicle Logbook",
                    logbook_id=record_id,
                    conn=conn,
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def delete(record_id):

        record = (
            VehicleLogbookModel.get_by_id(
                record_id
            )
        )

        if record is None:
            raise ValueError(
                "Vehicle Logbook entry not found."
            )

        conn = Database.connect()

        try:

            AssetMeterReadingModel.delete_by_logbook_id(
                record_id,
                conn=conn,
            )

            VehicleLogbookModel.delete(
                record_id,
                conn=conn,
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def search(text):

        if not text.strip():
            return VehicleLogbookModel.get_all()

        return VehicleLogbookModel.search(
            text.strip()
    )

    @staticmethod
    def get_by_asset_and_date_range(
        asset_id,
        from_date,
        to_date
    ):

        return VehicleLogbookModel.get_by_asset_and_date_range(
            asset_id,
            from_date,
            to_date
        )

    @staticmethod
    def link_work_order(
        logbook_id,
        work_order_id
    ):

        if not logbook_id:
            raise ValueError(
                "Vehicle Logbook entry is required."
            )

        if not work_order_id:
            raise ValueError(
                "Work Order is required."
            )

        VehicleLogbookModel.set_work_order_id(
            logbook_id,
            work_order_id
        )

    @staticmethod
    def get_unresolved_defects():

        return (
            VehicleLogbookModel
            .get_unresolved_defects()
        )