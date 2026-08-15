from app.models.work_order_model import WorkOrderModel
from app.services.asset_service import AssetService
from app.services.technician_service import TechnicianService
from app.services.work_order_parts_service import WorkOrderPartService
from app.helpers.date_helper import DateHelper
from app.services.work_order_history_service import (
    WorkOrderHistoryService
)



class WorkOrderService:

    VALID_STATUS_TRANSITIONS = {
    "Open": {
        "Assigned",
        "In Progress",
        "Cancelled",
    },
    "Assigned": {
        "In Progress",
        "On Hold",
        "Cancelled",
    },
    "In Progress": {
        "On Hold",
        "Completed",
        "Cancelled",
    },
    "On Hold": {
        "In Progress",
        "Cancelled",
    },
    "Completed": {
        "Closed",
    },
    "Closed": set(),
    "Cancelled": set(),
}

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

        save_data["actual_cost"] = (
            WorkOrderService.calculate_labour_cost(
                save_data
            )
        )

        work_order_id = WorkOrderModel.insert(
            save_data
        )

        WorkOrderHistoryService.log_created(
            work_order_id
        )

        return work_order_id


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

        # Work with a copy so we do not modify
        # the dictionary supplied by the dialog.
        save_data = dict(data)

        # Apply automatic status rules.
        save_data = (
            WorkOrderService.apply_automatic_status(
                existing,
                save_data
            )
        )

        # Validate the resulting data.
        WorkOrderService.validate_data(
            save_data
        )

        # Validate status workflow.
        WorkOrderService.validate_status_transition(
            existing["status"],
            save_data["status"]
        )

        # Check duplicate Work Order number.
        if WorkOrderModel.number_exists(
            save_data["work_order_number"],
            exclude_id=record_id
        ):
            raise ValueError(
                "Work Order Number already exists."
            )

        # Preserve PM relationship.
        save_data["pm_id"] = existing["pm_id"]

        # Recalculate actual cost.
        save_data["actual_cost"] = (
            WorkOrderService.calculate_actual_cost(
                record_id,
                save_data
            )
        )

        # Save Work Order.
        WorkOrderModel.update(
            record_id,
            save_data
        )

        # Record changes.
        WorkOrderService.log_changes(
            record_id,
            existing,
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
    def validate_status_transition(
        old_status,
        new_status
    ):
        if old_status == new_status:
            return

        allowed = (
            WorkOrderService
            .VALID_STATUS_TRANSITIONS
            .get(old_status, set())
        )

        if new_status not in allowed:
            raise ValueError(
                f"Cannot change Work Order status "
                f"from '{old_status}' to '{new_status}'."
            )

    @staticmethod
    def get_open_count():
        return WorkOrderModel.get_open_count()

    @staticmethod
    def get_urgent(limit=10):
        return WorkOrderModel.get_urgent(limit)

    @staticmethod
    def open_pm_work_order_exists(pm_id):
        return WorkOrderModel.open_pm_work_order_exists(
            pm_id
        )

    @staticmethod
    def get_pm_history(pm_id):
        return WorkOrderModel.get_pm_history(pm_id)

    
    @staticmethod
    def get_by_pm_id(pm_id):
        # Backward-compatible alias used by PM dialog history loading.
        return WorkOrderModel.get_pm_history(pm_id)

    @staticmethod
    def calculate_labour_cost(data):

        technician_id = data.get(
            "technician_id"
        )

        if technician_id is None:
            return 0.00

        technician = TechnicianService.get_by_id(
            technician_id
        )

        if technician is None:
            return 0.00

        hourly_rate = float(
            technician["hourly_rate"] or 0
        )

        labour_hours = float(
            data.get("labour_hours", 0) or 0
        )

        return labour_hours * hourly_rate


    @staticmethod
    def calculate_actual_cost(
        work_order_id,
        data
    ):

        labour_cost = (
            WorkOrderService.calculate_labour_cost(
                data
            )
        )

        material_cost = 0.00

        if work_order_id is not None:
            material_cost = (
                WorkOrderPartService.get_total_cost(
                    work_order_id
                )
            )

        return labour_cost + material_cost

    
    @staticmethod
    def complete_work_order(record_id):
        work_order = WorkOrderModel.get_by_id(
            record_id
        )

        if work_order is None:
            raise ValueError(
                "Work Order not found."
            )

        if work_order["status"] == "Closed":
            raise ValueError(
                "A closed Work Order cannot be completed."
            )

        if work_order["status"] == "Completed":
            raise ValueError(
                "This Work Order is already completed."
            )

        if work_order["technician_id"] is None:
            raise ValueError(
                "Please assign a technician before "
                "completing the Work Order."
            )

        if float(work_order["labour_hours"] or 0) <= 0:
            raise ValueError(
                "Please enter Labour Hours before "
                "completing the Work Order."
            )

        completed_date = DateHelper.today_string()

        WorkOrderModel.complete(
            record_id,
            completed_date
        )

        WorkOrderHistoryService.log_completed(
            record_id
        )

        if work_order["pm_id"] is not None:
            from app.services.preventive_maintenance_service import (
                PreventiveMaintenanceService
            )

            PreventiveMaintenanceService.complete_schedule(
                work_order["pm_id"],
                completed_date
            )


    @staticmethod
    def close_work_order(record_id):

        work_order = WorkOrderModel.get_by_id(
            record_id
        )

        if work_order is None:
            raise ValueError(
                "Work Order not found."
            )

        if work_order["status"] == "Closed":
            raise ValueError(
                "This Work Order is already closed."
            )

        if work_order["status"] != "Completed":
            raise ValueError(
                "Only a completed Work Order can be closed."
            )

        WorkOrderModel.close(
            record_id,
            DateHelper.today_string()
        )

        WorkOrderHistoryService.log_closed(
            record_id
        )

    @staticmethod
    def log_changes(
        work_order_id,
        existing,
        new_data
    ):

        field = {
            "asset_id": "Asset",
            "title": "Title",
            "description": "Description",
            "priority": "Priority",
            "status": "Status",
            "technician_id": "Technician",
            "requested_by": "Requested By",
            "date_created": "Date Created",
            "due_date": "Due Date",
            "estimated_cost": "Estimated Cost",
            "actual_cost": "Actual Cost",
            "labour_hours": "Labour Hours",
            "notes": "Notes",
        }

        for field_name, display_name in field.items():

            old_value = existing[field_name]
            new_value = new_data.get(field_name)

            # ---------------------------------------------
            # Friendly display values
            # ---------------------------------------------

            if field_name == "asset_id":

                old_text = (
                    WorkOrderService.asset_display(
                        old_value
                    )
                )

                new_text = (
                    WorkOrderService.asset_display(
                        new_value
                    )
                )

            elif field_name == "technician_id":

                old_text = (
                    WorkOrderService.technician_display(
                        old_value
                    )
                )

                new_text = (
                    WorkOrderService.technician_display(
                        new_value
                    )
                )

            else:

                old_text = (
                    ""
                    if old_value is None
                    else str(old_value)
                )

                new_text = (
                    ""
                    if new_value is None
                    else str(new_value)
                )

                if old_text == new_text:
                    continue

            WorkOrderHistoryService.add(
                work_order_id,
                action="Updated",
                field_name=display_name,
                old_value=old_text,
                new_value=new_text,
            )

    @staticmethod
    def asset_display(asset_id):

        if asset_id is None:
            return ""

        asset = AssetService.get_by_id(
            asset_id
        )

        if asset is None:
            return str(asset_id)

        return (
            f'{asset["asset_number"]} - '
            f'{asset["asset_name"]}'
        )


    @staticmethod
    def technician_display(technician_id):

        if technician_id is None:
            return "Unassigned"

        technician = TechnicianService.get_by_id(
            technician_id
        )

        if technician is None:
            return str(technician_id)

        return (
            f'{technician["employee_number"]} - '
            f'{technician["first_name"]} '
            f'{technician["last_name"]}'
        )

    @staticmethod
    def apply_automatic_status(
        existing,
        data
    ):
        current_status = existing["status"]
        selected_status = data.get("status")

        # Open -> Assigned
        if (
            current_status == "Open"
            and data.get("technician_id") is not None
            and selected_status == "Open"
        ):
            data["status"] = "Assigned"

        # Assigned -> In Progress
        elif (
            current_status == "Assigned"
            and float(
                data.get("labour_hours", 0) or 0
            ) > 0
            and selected_status == "Assigned"
        ):
            data["status"] = "In Progress"

        return data