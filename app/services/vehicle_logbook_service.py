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

        start_hours_value = data.get("start_hours")
        end_hours_value = data.get("end_hours")

        has_hours = (
            start_hours_value not in (None, "")
            or end_hours_value not in (None, "")
        )

        start_hours = (
            float(start_hours_value or 0)
            if has_hours
            else 0
        )

        end_hours = (
            float(end_hours_value or 0)
            if has_hours
            else 0
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

        if start_hours < 0:
            raise ValueError(
                "Start Hours cannot be negative."
            )

        if end_hours < 0:
            raise ValueError(
                "End Hours cannot be negative."
            )

        if end_hours < start_hours:
            raise ValueError(
                "End Hours cannot be less than Start Hours."
            )

        distance = (
            end_meter - start_meter
        )

        hours_used = (
            end_hours - start_hours
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

        record_data["start_hours"] = (
            start_hours
        )

        record_data["end_hours"] = (
            end_hours
        )

        record_data["hours_used"] = (
            hours_used
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

            latest_kilometers = (
                AssetMeterReadingModel.get_latest_reading(
                    asset_id,
                    "Kilometers",
                    conn=conn,
                )
            )

            previous_kilometers = None

            if latest_kilometers is not None:
                previous_kilometers = float(
                    latest_kilometers["reading"] or 0
                )

            if (
                previous_kilometers is None
                or end_meter > previous_kilometers
            ):
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

            if has_hours:

                AssetMeterReadingService.add_reading(
                    asset_id=asset_id,
                    meter_type="Running Hours",
                    reading=end_hours,
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

        start_hours_value = data.get("start_hours")
        end_hours_value = data.get("end_hours")

        has_hours = (
            start_hours_value not in (None, "")
            or end_hours_value not in (None, "")
        )

        start_hours = (
            float(start_hours_value or 0)
            if has_hours
            else 0
        )

        end_hours = (
            float(end_hours_value or 0)
            if has_hours
            else 0
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

        if start_hours < 0:
            raise ValueError(
                "Start Hours cannot be negative."
            )

        if end_hours < 0:
            raise ValueError(
                "End Hours cannot be negative."
            )

        if end_hours < start_hours:
            raise ValueError(
                "End Hours cannot be less than Start Hours."
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

        record_data["start_hours"] = (
            start_hours
        )

        record_data["end_hours"] = (
            end_hours
        )

        record_data["hours_used"] = (
            end_hours - start_hours
        )

        conn = Database.connect()

        try:

            VehicleLogbookModel.update(
                record_id,
                record_data,
                conn=conn
            )

            # -------------------------------------------------
            # Kilometers
            # -------------------------------------------------
            kilometer_record = (
                AssetMeterReadingModel
                .get_by_logbook_id(
                    record_id,
                    "Kilometers",
                    conn=conn,
                )
            )

            if kilometer_record is not None:

                AssetMeterReadingModel.update_logbook_reading(
                    logbook_id=record_id,
                    meter_type="Kilometers",
                    asset_id=asset_id,
                    reading=end_meter,
                    reading_date=log_date,
                    conn=conn,
                )

            else:

                latest_kilometers = (
                    AssetMeterReadingModel.get_latest_reading(
                        asset_id,
                        "Kilometers",
                        conn=conn,
                    )
                )

                previous_kilometers = None

                if latest_kilometers is not None:
                    previous_kilometers = float(
                        latest_kilometers["reading"] or 0
                    )

                if (
                    previous_kilometers is None
                    or end_meter > previous_kilometers
                ):
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
                        logbook_id=record_id,
                        conn=conn,
                    )

            # -------------------------------------------------
            # Running Hours
            # -------------------------------------------------

            hours_record = (
                AssetMeterReadingModel
                .get_by_logbook_id(
                    record_id,
                    "Running Hours",
                    conn=conn,
                )
            )

            if has_hours:

                if hours_record is not None:

                    AssetMeterReadingModel.update_logbook_reading(
                        logbook_id=record_id,
                        meter_type="Running Hours",
                        asset_id=asset_id,
                        reading=end_hours,
                        reading_date=log_date,
                        conn=conn,
                    )

                else:

                    AssetMeterReadingService.add_reading(
                        asset_id=asset_id,
                        meter_type="Running Hours",
                        reading=end_hours,
                        reading_date=log_date,
                        notes=(
                            "Recorded from vehicle "
                            "logbook entry."
                        ),
                        source_type="Vehicle Logbook",
                        logbook_id=record_id,
                        conn=conn,
                    )

            elif hours_record is not None:

                AssetMeterReadingModel.delete_by_logbook_id_and_meter_type(
                    logbook_id=record_id,
                    meter_type="Running Hours",
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