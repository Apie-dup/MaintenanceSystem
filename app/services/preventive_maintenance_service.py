from app.models.preventive_maintenance_model import (
    PreventiveMaintenanceModel
)
from app.models.asset_model import AssetModel
from app.helpers.date_helper import DateHelper
from app.services.work_order_service import WorkOrderService

   


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

        PreventiveMaintenanceService.validate(data)

        data["next_due_date"] = (
            PreventiveMaintenanceService.calculate_next_due_date(
                data
            )
        )

        return PreventiveMaintenanceModel.insert(data)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        PreventiveMaintenanceService.validate(data)

        data["next_due_date"] = (
            PreventiveMaintenanceService.calculate_next_due_date(
                data
            )
        )

        PreventiveMaintenanceModel.update(
            record_id,
            data
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

        if not data["asset_id"]:
            raise ValueError(
                "Please select an asset."
            )

        if not data["task"].strip():
            raise ValueError(
                "Task is required."
            )

        if data["frequency_value"] <= 0:
            raise ValueError(
                "Frequency Value must be greater than zero."
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

        if WorkOrderService.open_pm_work_order_exists(
            pm["pm_number"]
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

            "labour_hours":
                float(pm["estimated_hours"] or 0),

            "notes":
                (
                    "Generated from Preventive Maintenance "
                    f'{pm["pm_number"]}.'
                ),

            "pm_id":
                pm["id"]
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