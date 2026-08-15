from app.models.work_order_history_model import (
    WorkOrderHistoryModel
)


class WorkOrderHistoryService:

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    @staticmethod
    def add(
        work_order_id,
        action,
        field_name=None,
        old_value=None,
        new_value=None,
        notes=None,
    ):
        return WorkOrderHistoryModel.add(
            work_order_id,
            action,
            field_name,
            old_value,
            new_value,
            notes,
        )

    # ---------------------------------------------------------
    # Get history
    # ---------------------------------------------------------

    @staticmethod
    def get_history(work_order_id):
        return WorkOrderHistoryModel.get_history(
            work_order_id
        )

    # ---------------------------------------------------------
    # Convenience helpers
    # ---------------------------------------------------------

    @staticmethod
    def log_created(work_order_id):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Created",
            notes="Work Order created.",
        )

    @staticmethod
    def log_completed(work_order_id):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Completed",
            field_name="Status",
            old_value=None,
            new_value="Completed",
            notes="Work Order completed.",
        )

    @staticmethod
    def log_closed(work_order_id):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Closed",
            field_name="Status",
            old_value="Completed",
            new_value="Closed",
            notes="Work Order closed.",
        )