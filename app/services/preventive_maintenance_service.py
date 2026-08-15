from app.models.preventive_maintenance_model import (
    PreventiveMaintenanceModel
)
from app.models.asset_model import AssetModel
from app.helpers.date_helper import DateHelper
from app.services.work_order_service import WorkOrderService
from app.models.work_order_model import WorkOrderModel

   


class PreventiveMaintenanceService:

    # ---------------------------------------------------------
    # Get All
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return PreventiveMaintenanceModel.get_all()

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

        save_data.setdefault(
            "pm_id",
            None
        )

        WorkOrderService.validate_data(
            save_data
        )

        if WorkOrderModel.number_exists(
            save_data["work_order_number"]
        ):
            raise ValueError(
                "Work Order Number already exists."
        )

        return WorkOrderModel.insert(
            save_data
        )

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        existing = WorkOrderModel.get_by_id(
            record_id
        )

        if existing is None:
            raise ValueError(
                "Work Order not found."
            )

        save_data = dict(data)

        WorkOrderService.validate_data(
            save_data
        )

        if WorkOrderModel.number_exists(
            save_data["work_order_number"],
            exclude_id=record_id,
        ):
            raise ValueError(
                "Work Order Number already exists."
            )

        save_data["pm_id"] = existing["pm_id"]

        WorkOrderModel.update(
            record_id,
            save_data
        )

        completed_statuses = {
            "Completed",
            "Closed",
        }

        was_completed = (
            existing["status"]
            in completed_statuses
        )

        is_completed = (
            save_data["status"]
            in completed_statuses
        )

        if (
            not was_completed
            and is_completed
            and existing["pm_id"] is not None
        ):
            from app.services.preventive_maintenance_service import (
                PreventiveMaintenanceService
            )

            PreventiveMaintenanceService.complete_schedule(
                existing["pm_id"]
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

        if not data["frequency_type"].strip():
            raise ValueError(
                "Frequency Type is required."
            )

        if data["frequency_value"] <= 0:
            raise ValueError(
                "Frequency Value must be greater than zero."
            )

        if not data["last_service_date"]:
            raise ValueError(
                "Last Service Date is required."
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

        return DateHelper.to_string(

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
        return PreventiveMaintenanceModel.get_due_today()

    @staticmethod
    def get_overdue():
        return PreventiveMaintenanceModel.get_overdue()
    
    @staticmethod
    def get_due_this_week():
        return PreventiveMaintenanceModel.get_due_this_week()

    @staticmethod
    def get_due_today_count():
        return len(
            PreventiveMaintenanceModel.get_due_today()
        )


    @staticmethod
    def get_due_this_week_count():
        return len(
            PreventiveMaintenanceModel.get_due_this_week()
        )


    @staticmethod
    def get_overdue_count():
        return len(
            PreventiveMaintenanceModel.get_overdue()
        )

    @staticmethod
    def get_due_list(limit=10):
        return PreventiveMaintenanceModel.get_due_list(
            limit
    )

    # ---------------------------------------------------------
    # Generate Work Order
    # ---------------------------------------------------------
    

    @staticmethod
    def generate_work_order(pm_id):

        pm = PreventiveMaintenanceModel.get_by_id(pm_id)

        if pm is None:
            raise ValueError(
                "Preventive Maintenance schedule not found."
            )

        if not bool(pm["active"]):
            raise ValueError(
                "An inactive PM schedule cannot generate a work order."
            )

        if not pm["next_due_date"]:
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
                pm["next_due_date"],

            "estimated_cost":
                float(pm["estimated_cost"] or 0),

            "actual_cost":
                0.00,

            "labour_hours":0.00,

            "notes": (
                "Generated from Preventive Maintenance "
                f'{pm["pm_number"]}.\n'
                f'Estimated labour: '
                f'{float(pm["estimated_hours"] or 0):.2f} hours.'
        ),
        }

        return WorkOrderService.create(data)

    @staticmethod
    def complete_schedule(
        pm_id,
        completion_date=None
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

        frequency_value = int(
            pm["frequency_value"] or 0
        )

        if frequency_value <= 0:
            raise ValueError(
            "The PM schedule has an invalid frequency value."
            )

        if completion_date is None:
            completion_date = DateHelper.today()

        elif isinstance(completion_date, str):
            completion_date = DateHelper.from_string(
                completion_date
            )

        next_due_date = (
            DateHelper.calculate_next_due_date(
                completion_date,
                pm["frequency_type"],
                int(pm["frequency_value"]),
            )
        )

        PreventiveMaintenanceModel.update_service_dates(
            pm_id,
            DateHelper.to_string(completion_date),
            DateHelper.to_string(next_due_date)
        )