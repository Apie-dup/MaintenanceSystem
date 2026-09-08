from app.models.work_order_model import WorkOrderModel
from app.services.asset_service import AssetService
from app.services.technician_service import TechnicianService
from app.services.work_order_parts_service import WorkOrderPartService
from app.helpers.date_helper import DateHelper
from app.services.work_order_history_service import (
    WorkOrderHistoryService
)
from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)
from app.database.connection import Database
from app.services.pm_service_history_service import (
    PMServiceHistoryService
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
    def create(
        data,
        user=None
    ):

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
            work_order_id,
            user_id=(
                user.get("id")
                if user
                else None
            ),
            username=(
                user.get("username")
                if user
                else None
            ),
        )

        return work_order_id


    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, 
               data,
               user=None
            ):

        existing = WorkOrderModel.get_by_id(
            record_id
        )

        if existing is None:
            raise ValueError(
                "Work Order not found."
            )

        requested_status = (
            data.get("status") or ""
        ).strip()

        if (
            existing["status"] != "Completed"
            and requested_status == "Completed"
        ):
            raise ValueError(
                "Work Order must be completed using "
                "the Complete Work Order workflow."
            )

        if (
            existing["status"] != "Closed"
            and requested_status == "Closed"
        ):
            raise ValueError(
                "Work Order must be closed using "
                "the Close Work Order workflow."
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
            save_data,
            user=user,
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
    def complete_work_order(
        record_id,
        user=None,
        meter_reading=None
    ):

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

        if float(
            work_order["labour_hours"] or 0
        ) <= 0:
            raise ValueError(
                "Please enter Labour Hours before "
                "completing the Work Order."
            )

        old_status = work_order["status"]

        completed_date = (
            DateHelper.today_string()
        )

        pm_id = work_order["pm_id"]

        pm_schedule = None
        is_meter_based = False
        frequency_type = ""

        # ---------------------------------------------------
        # Validate linked PM
        # ---------------------------------------------------

        if pm_id is not None:

            from app.services.preventive_maintenance_service import (
                PreventiveMaintenanceService
            )

            pm_schedule = (
                PreventiveMaintenanceService.get_by_id(
                    pm_id
                )
            )

            if pm_schedule is None:
                raise ValueError(
                    "The Preventive Maintenance schedule "
                    "linked to this Work Order no longer exists."
                )

            frequency_type = (
                pm_schedule["frequency_type"] or ""
            ).strip()

            is_meter_based = (
                frequency_type 
                in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
            )

        # ---------------------------------------------------
        # Validate meter reading
        # ---------------------------------------------------

        if is_meter_based:

            if meter_reading is None:
                raise ValueError(
                    "Meter Reading is required before "
                    "completing this Work Order."
                )

            try:
                meter_reading = float(
                    meter_reading
                )

            except (TypeError, ValueError):
                raise ValueError(
                    "Meter Reading must be a valid number."
                )

            if meter_reading <= 0:
                raise ValueError(
                    "Meter Reading must be greater than zero."
                )

            last_service_meter = float(
                pm_schedule["last_service_meter"]
                or 0
            )

            if meter_reading < last_service_meter:
                raise ValueError(
                    "Meter Reading cannot be lower "
                    "than the previous service meter reading."
                )

            latest_reading = (
                AssetMeterReadingService
                .get_latest_reading(
                    work_order["asset_id"],
                    frequency_type,
                )
            )

            if latest_reading is not None:

                previous_reading = float(
                    latest_reading["reading"] or 0
                )

                if meter_reading < previous_reading:
                    raise ValueError(
                        "Meter Reading cannot be lower "
                        "than the asset's latest meter reading."
                    )

        # ---------------------------------------------------
        # Complete Work Order transaction
        # ---------------------------------------------------

        conn = Database.connect()

        try:

            #-------------------------------------------
            # Complete Work Order
            #-------------------------------------------

            WorkOrderModel.complete(
                record_id,
                completed_date,
                meter_reading=(
                    meter_reading
                    if is_meter_based
                    else None
                ),
                conn=conn
            )

            # ---------------------------------------------------
            # Audit
            # ---------------------------------------------------
        
            WorkOrderHistoryService.log_completed(
                record_id,
                old_status=old_status,
                user_id=(
                    user.get("id")
                    if user
                    else None
                ),
                username=(
                    user.get("username")
                    if user
                    else None
                ),
                conn=conn
            )
    

            # ---------------------------------------------------
            # Record asset meter reading
            # ---------------------------------------------------

            if is_meter_based:

                AssetMeterReadingService.add_reading(
                    asset_id=work_order["asset_id"],
                    meter_type=frequency_type,
                    reading=meter_reading,
                    reading_date=completed_date,
                    notes=(
                        "Recorded on completion of "
                        f'{work_order["work_order_number"]}.'
                    ),
                    source_type="Work Order",
                    work_order_id=record_id,
                    conn=conn
                )

            # ---------------------------------------------------
            # PM Service History
            #----------------------------------------------------

            if pm_id is not None:

                PMServiceHistoryService.create(
                    {
                        "pm_id": pm_id,
                        "work_order_id": record_id,
                        "asset_id": work_order["asset_id"],
                        "service_date": completed_date,
                        "meter_type": (
                            frequency_type
                            if is_meter_based
                            else None
                        ),
                        "meter_reading": (
                            meter_reading
                            if is_meter_based
                            else None
                        ),
                        "notes": (
                            f"Completed from "
                            f'{work_order["work_order_number"]}.'
                        ),

                    },
                    conn=conn
                )

            # ---------------------------------------------------
            # Advance PM schedule
            # ---------------------------------------------------

            if pm_id is not None:

                PreventiveMaintenanceService.complete_schedule(
                    pm_id,
                    completion_date=completed_date,
                    meter_reading=(
                        meter_reading
                        if is_meter_based
                        else None
                    ),
                    conn=conn
                )

            #---------------------------------------------------
            # Everything succeeded
            #---------------------------------------------------

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()
                

    @staticmethod
    def close_work_order(
        record_id,
        user=None
    ):

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

        old_status = work_order["status"]

        conn = Database.connect()

        try:

            WorkOrderModel.close(
                record_id,
                DateHelper.today_string()
            )

            WorkOrderHistoryService.log_closed(
            record_id,
            old_status=old_status,
            user_id=(
                user.get("id")
                if user
                else None
            ),
            username=(
                user.get("username")
                if user
                else None
            ),
                conn=conn

            )

            conn.commit()

        except Exception:

            conn.rollback()

            raise

        finally:

            conn.close()

    @staticmethod
    def log_changes(
        work_order_id,
        existing,
        new_data,
        user=None,
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

            if field_name in {
                "estimated_cost",
                "labour_hours",
            }:
                try:
                    old_number = float(
                        old_value or 0
                    )

                    new_number = float(
                        new_value or 0
                    )

                    if old_number == new_number:
                        continue

                except (TypeError, ValueError):
                    pass

            #---------------------------------------------
            # Ignore unchanged values
            #---------------------------------------------

            if old_text == new_text:
                    continue

            WorkOrderHistoryService.add(
                work_order_id,
                action="Updated",
                field_name=display_name,
                old_value=old_text,
                new_value=new_text,
                user_id=(
                    user.get("id")
                    if user
                    else None
                ),
                username=(
                    user.get("username")
                    if user
                    else None
                ),
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

    @staticmethod
    def reopen_work_order(
        record_id,
        reason,
        user=None,
    ):

        work_order = WorkOrderModel.get_by_id(
            record_id
        )

        if work_order is None:
            raise ValueError(
                "Work Order not found."
            )

        if work_order["status"] == "Closed":
            raise ValueError(
                "A closed Work Order cannot be reopened."
            )

        if work_order["status"] != "Completed":
            raise ValueError(
                "Only a completed Work Order can be reopened."
            )

        if work_order["pm_id"] is not None:
            raise ValueError(
                "A Work Order generated from Preventive Maintenance "
                "cannot be reopened after completion."
            )

        if not (reason or "").strip():
            raise ValueError(
                "A reason is required when reopening a Work Order."
            )

        conn = Database.connect()

        try:

            WorkOrderModel.reopen(
                record_id,
                conn=conn
            )

            WorkOrderHistoryService.log_reopened(
                record_id,
                reason,
                user_id=(
                    user.get("id")
                    if user
                    else None
                ),
                username=(
                    user.get("username")
                    if user
                    else None
                ),
                conn=conn,
            )

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()



    @staticmethod
    def pm_cycle_exists(
        pm_id,
        pm_due_date=None,
        pm_due_meter=None,
    ):

        return WorkOrderModel.pm_cycle_exists(
            pm_id,
            pm_due_date=pm_due_date,
            pm_due_meter=pm_due_meter,
        )