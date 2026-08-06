from app.models.work_order_model import WorkOrderModel
from app.services.asset_service import AssetService
from app.services.technician_service import TechnicianService



class WorkOrderService:

    # ---------------------------------------------------------
    # Get all work orders
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        return WorkOrderModel.get_all()

    # ---------------------------------------------------------
    # Get work order by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        return WorkOrderModel.get_by_id(record_id)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        return WorkOrderModel.search(search_text)

    # ---------------------------------------------------------
    # Next work-order number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_work_order_number():
        return WorkOrderModel.get_next_work_order_number()

    # ---------------------------------------------------------
    # Asset lookup
    # ---------------------------------------------------------

    @staticmethod
    def asset_lookup():
        return AssetService.get_active_assets()

    # ---------------------------------------------------------
    # Technician lookup
    # ---------------------------------------------------------

    @staticmethod
    def technician_lookup():
        return TechnicianService.get_active_technicians()

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        # Allow forms that do not include PM linkage.
        if "pm_id" not in data:
            data["pm_id"] = None

        WorkOrderService.validate_data(data)

        if WorkOrderModel.number_exists(
            data["work_order_number"]
        ):
            raise ValueError(
                "Work Order Number already exists."
            )

        return WorkOrderModel.insert(data)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):

        existing = WorkOrderModel.get_by_id(record_id)

        if existing is None:
            raise ValueError("Work Order not found.")

        WorkOrderService.validate_data(data)

        if WorkOrderModel.number_exists(
            data["work_order_number"],
            exclude_id=record_id
        ):
            raise ValueError(
                "Work Order Number already exists."
            )

        # Preserve the PM relationship

        data["pm_id"] = existing["pm_id"]

        WorkOrderModel.update(
            record_id,
            data
        )

        completed_statuses = {
            
            "Completed",
            "Closed",
        }

        was_completed = (
            existing["status"] in completed_statuses
        )

        is_completed = (
            data["status"] in completed_statuses
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
        WorkOrderModel.delete(record_id)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def validate_data(data):

        if not data["work_order_number"].strip():
            raise ValueError(
                "Work Order Number is required."
            )

        if data["asset_id"] is None:
            raise ValueError(
                "Asset is required."
            )

        if not data["title"].strip():
            raise ValueError(
                "Title is required."
            )

        if not data["priority"].strip():
            raise ValueError(
                "Priority is required."
            )

        if not data["status"].strip():
            raise ValueError(
                "Status is required."
            )

        if not data["date_created"].strip():
            raise ValueError(
                "Date Created is required."
            )

        if not data["due_date"].strip():
            raise ValueError(
                "Due Date is required."
            )

        if data["estimated_cost"] < 0:
            raise ValueError(
                "Estimated Cost cannot be negative."
            )

        if data["actual_cost"] < 0:
            raise ValueError(
                "Actual Cost cannot be negative."
            )

        if data["labour_hours"] < 0:
            raise ValueError(
                "Labour Hours cannot be negative."
            )

    @staticmethod
    def get_open_count():
        return WorkOrderModel.get_open_count()

    @staticmethod
    def get_urgent(limit=10):
        return WorkOrderModel.get_urgent(limit)

    @staticmethod
    def open_pm_work_order_exists(pm_number):
        return WorkOrderModel.open_pm_work_order_exists(
            pm_number
        )
    @staticmethod
    def get_pm_history(pm_id):
        return WorkOrderModel.get_pm_history(pm_id)

    @staticmethod
    def get_by_pm_id(pm_id):
        # Backward-compatible alias used by PM dialog history loading.
        return WorkOrderModel.get_pm_history(pm_id)
    