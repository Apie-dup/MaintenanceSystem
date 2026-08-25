from app.models.preventive_maintenance_model import (
    PreventiveMaintenanceModel
)
from app.models.asset_model import AssetModel
from app.helpers.date_helper import DateHelper
from app.services.work_order_service import WorkOrderService
from app.models.work_order_model import WorkOrderModel
from app.services.asset_meter_reading_service import AssetMeterReadingService

   


class PreventiveMaintenanceService:

    METER_FREQUENCY_TYPES = {
        "Running Hours",
        "Kilometers",
        "Cycles",
    }


    # ---------------------------------------------------------
    # Get All
    # ---------------------------------------------------------

    @staticmethod
    def get_all():

        rows = PreventiveMaintenanceModel.get_all()

        result = []

        for row in rows:

            pm = dict(row)

            frequency_type = (
                pm["frequency_type"] or ""
            ).strip()

            if (
                frequency_type
                in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
            ):

                latest = (
                    AssetMeterReadingService
                    .get_latest_reading_value(
                        pm["asset_id"],
                        frequency_type,
                    )
                )

                if latest is None:
                    pm["current_meter"] = float(
                        pm["last_service_meter"] or 0
                    )

                else:
                    pm["current_meter"] = latest

                pm["due_status"] = (
                    PreventiveMaintenanceService
                    .get_meter_due_status(pm)
                )

            else:
                pm["current_meter"] = None

                pm["due_status"] = (
                    pm["calendar_due_status"]
                )

            result.append(pm)

        return result

    # ---------------------------------------------------------
    # Get By ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        return PreventiveMaintenanceModel.get_by_id(record_id)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        return PreventiveMaintenanceModel.search(search_text)

    # ---------------------------------------------------------
    # Next PM Number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_pm_number():
        return PreventiveMaintenanceModel.get_next_pm_number()

    # ---------------------------------------------------------
    # Asset Lookup
    # ---------------------------------------------------------

    @staticmethod
    def asset_lookup():
        return AssetModel.get_all()

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        save_data = dict(data)

        PreventiveMaintenanceService.validate(
            save_data
        )

        if (
            save_data["frequency_type"]
            in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        ):

            save_data["next_due_date"] = None

        else:
            save_data["next_due_date"] = (
                PreventiveMaintenanceService.calculate_next_due_date(
                    save_data
                )
            )

        return PreventiveMaintenanceModel.create(
            save_data
        )

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        save_data = dict(data)

        PreventiveMaintenanceService.validate(
            save_data
        )

        if (
            save_data["frequency_type"]
            in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        ):
            save_data["next_due_date"] = None

        else:
            save_data["next_due_date"] = (
                PreventiveMaintenanceService.calculate_next_due_date(
                    save_data
                )
            )

        PreventiveMaintenanceModel.update(
            record_id,
            save_data
        )

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        PreventiveMaintenanceModel.delete(record_id)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def validate(data):

        if not data["pm_number"].strip():
            raise ValueError(
                "PM Number is required."
            )

        if data["asset_id"] is None:
            raise ValueError(
                "Please select an asset."
            )

        if not data["task"].strip():
            raise ValueError(
                "Task is required."
            )

        frequency_type = (
            data["frequency_type"].strip()
        )

        if not frequency_type:
            raise ValueError(
                "Frequency Type is required."
            )

        if data["frequency_value"] <= 0:
            raise ValueError(
                "Frequency Value must be greater than zero."
            )

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        is_meter_based = (
            frequency_type 
            in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        )

        if is_meter_based:

            if data.get("last_service_meter") is None:
                raise ValueError(
                    "Last Service Meter is required."
                )

            if data.get("next_due_meter") is None:
                raise ValueError(
                    "Next Due Meter is required."
                )

            if float(
                data["last_service_meter"]
            ) < 0:
                raise ValueError(
                    "Last Service Meter cannot be negative."
                )

            if float(
                data["next_due_meter"]
            ) <= float(
                data["last_service_meter"]
            ):
                raise ValueError(
                    "Next Due Meter must be greater "
                    "than Last Service Meter."
                )

        else:

            if not data["last_service_date"]:
                raise ValueError(
                    "Last Service Date is required."
                )

            if not data["next_due_date"]:
                raise ValueError(
                    "Next Due Date is required."
                )

        if not data["priority"].strip():
            raise ValueError(
                "Priority is required."
            )

        if data["estimated_hours"] < 0:
            raise ValueError(
                "Estimated Hours cannot be negative."
            )

        if data["estimated_cost"] < 0:
            raise ValueError(
                "Estimated Cost cannot be negative."
            )

    # ---------------------------------------------------------
    # Calculate Next Due Date
    # ---------------------------------------------------------

    @staticmethod
    def calculate_next_due_date(data):

        last_service = DateHelper.from_string(
            data["last_service_date"]
        )

        return DateHelper.to.string(
            DateHelper.calculate_next_due_date(
                last_service,
                data["frequency_type"],
                data["frequency_value"]
            )
        )

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    @staticmethod
    def get_due_today():

        records = PreventiveMaintenanceService.get_all()

        return [
            pm
            for pm in records
            if pm["due_status"] in {
                "Due",
                "Due Today",
            }
        ]

    @staticmethod
    def get_overdue():

        records = PreventiveMaintenanceService.get_all()

        return [
            pm
            for pm in records
            if pm["due_status"] == "Overdue"
        ]
    
    @staticmethod
    def get_due_this_week():

        records = PreventiveMaintenanceService.get_all()

        return [
            pm
            for pm in records
            if pm["due_status"] in {
                "Due",
                "Due Today",
                "Due Soon",
            }
        ]

    @staticmethod
    def get_due_today_count():
        return len(
            PreventiveMaintenanceService.get_due_today()
        )


    @staticmethod
    def get_due_this_week_count():
        return len(
            PreventiveMaintenanceService.get_due_this_week()
        )


    @staticmethod
    def get_overdue_count():
        return len(
            PreventiveMaintenanceService.get_overdue()
        )

    @staticmethod
    def get_due_list(limit=10):

        records = PreventiveMaintenanceService.get_all()

        priority_order = {
            "Overdue": 0,
            "Due": 1,
            "Due Today": 1,
            "Due Soon": 2,
            "Scheduled": 3,
            "Inactive": 4,
        }

        due_records = [
            pm
            for pm in records
            if pm["due_status"] in {
                "Overdue",
                "Due",
                "Due Today",
                "Due Soon",
            }
        ]

        due_records.sort(
            key=lambda pm: (
                priority_order.get(
                    pm["due_status"],
                    99
                ),
            )
        )

        return due_records[:limit]

    # ---------------------------------------------------------
    # Generate Work Order
    # ---------------------------------------------------------
    

    @staticmethod
    def generate_work_order(
        pm_id,
        user=None,
    ):

        pm = PreventiveMaintenanceModel.get_by_id(pm_id)

        if pm is None:
            raise ValueError(
                "Preventive Maintenance schedule not found."
            )

        if not bool(pm["active"]):
            raise ValueError(
                "An inactive PM schedule cannot generate a work order."
            )

        frequency_type = (
            pm["frequency_type"] or ""
        ).strip()

        is_meter_based = (
            frequency_type
            in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        )

        if (
            not is_meter_based
            and not pm["next_due_date"]
        ):
            raise ValueError(
                "The PM schedule does not have a next due date."
            )

        if WorkOrderService.open_pm_work_order_exists(
            pm_id
        ):
            raise ValueError(
                "An open work order already exists "
                "for this PM schedule."
            )

        data = {
            "work_order_number":
                WorkOrderService.get_next_work_order_number(),

            "asset_id":
                pm["asset_id"],

            "title":
                pm["task"],

            "description":
                pm["description"] or pm["task"],

            "priority":
                pm["priority"],

            "status":
                "Open",

            "technician_id":
                None,

            "requested_by":
                f'PM Schedule {pm["pm_number"]}',

            "date_created":
                DateHelper.today_string(),

            "due_date":
                (
                    DateHelper.today_string()
                    if is_meter_based
                    else pm["next_due_date"]
                ),

            "meter_reading":
                None,

            "estimated_cost":
                float(pm["estimated_cost"] or 0),

            "actual_cost":
                0.00,

            "estimated_hours":
                float(pm["estimated_hours"] or 0),

            "labour_hours":
                0.00,

            "notes": (
                "Generated from Preventive Maintenance "
                f'{pm["pm_number"]}.\n'
                f'Estimated labour: '
                f'{float(pm["estimated_hours"] or 0):.2f} hours.'
        ),
            "pm_id":
                pm["id"]
        }

        return WorkOrderService.create(
            data,
            user=user
        )

    @staticmethod
    def complete_schedule(
        pm_id,
        completion_date=None,
        meter_reading=None,
    ):

        pm = PreventiveMaintenanceModel.get_by_id(pm_id)

        if pm is None:
            raise ValueError(
                "Preventive Maintenance schedule not found."
            )

        if not bool(pm["active"]):
            raise ValueError(
            "An inactive PM schedule cannot be completed."
            )

        frequency_value = float(
            pm["frequency_value"] or 0
        )

        if frequency_value <= 0:
            raise ValueError(
            "The PM schedule has an invalid frequency value."
            )

        frequency_type = pm["frequency_type"]

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        #---------------------------------------------------------
        # Meter-based Pm
        #---------------------------------------------------------

        if frequency_type in meter_types:

            if meter_reading is None:
                raise ValueError(
                    "A meter reading is required to "
                    "complete this PM schedule."
                )

            meter_reading = float(
                meter_reading
            )

            if meter_reading < 0:
                raise ValueError(
                    "Meter reading cannot be negative."
                )

            previous_meter = float(
                pm["last_service_meter"] or 0
            )

            if meter_reading < previous_meter:
                raise ValueError(
                    "Meter reading cannot be less than "
                    "the previous service meter reading."
                )

            next_due_meter = (
                meter_reading
                + frequency_value
            )

            PreventiveMaintenanceModel.update_service_meter(
                pm_id,
                meter_reading,
                next_due_meter,
            )

            return

        #---------------------------------------------------------
        # Calendar-based PM

        if completion_date is None:
            completion_date = DateHelper.today()

        elif isinstance(
            completion_date, 
            str
        ):
            completion_date = DateHelper.from_string(
                completion_date
            )

        next_due_date = (
            DateHelper.calculate_next_due_date(
                completion_date,
                frequency_type,
                int(frequency_value),
            )
        )

        PreventiveMaintenanceModel.update_service_dates(
            pm_id,
            DateHelper.to_string(
                completion_date
            ),
            DateHelper.to_string(
                next_due_date
            ),
        )

    @staticmethod
    def get_meter_due_status(pm):

        frequency_type = (
            pm["frequency_type"] or ""
        ).strip()

        if (
            frequency_type
            not in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        ):
            return None

        next_due_meter = float(
            pm["next_due_meter"] or 0
        )

        frequency_value = float(
            pm["frequency_value"] or 0
        )

        latest = (
            AssetMeterReadingService
            .get_latest_reading(
                pm["asset_id"],
                frequency_type,
            )
        )

        if latest is None:
            current_meter = float(
                pm["last_service_meter"] or 0
            )
        else:
            current_meter = float(
                latest["reading"] or 0
            )

        if not bool(pm["active"]):
            return "Inactive"

        if next_due_meter <= 0:
            return "Scheduled"

        remaining = (
            next_due_meter
            - current_meter
        )

        if remaining < 0:
            return "Overdue"

        if remaining == 0:
            return "Due"

        due_soon_threshold = max(
            frequency_value * 0.10,
            1.0,
        )

        if remaining <= due_soon_threshold:
            return "Due Soon"

        return "Scheduled"