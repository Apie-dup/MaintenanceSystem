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
        user_id=None,
        username=None,
        conn=None,
    ):
        return WorkOrderHistoryModel.add(
            work_order_id,
            action,
            field_name,
            old_value,
            new_value,
            notes,
            user_id=user_id,
            username=username,
            conn=conn,
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
    def log_created(
        work_order_id,
        user_id=None,
        username=None,
    ):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Created",
            notes="Work Order created.",
            user_id=user_id,
            username=username,
        )

    @staticmethod
    def log_completed(
        work_order_id,
        old_status,
        user_id=None,
        username=None,
        conn=None,
    ):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Completed",
            field_name="Status",
            old_value=old_status,
            new_value="Completed",
            notes="Work Order completed.",
            user_id=user_id,
            username=username,
            conn=conn,
        )

    @staticmethod
    def log_closed(
        work_order_id,
        old_status,
        user_id=None,
        username=None,
        conn=None,
    ):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Closed",
            field_name="Status",
            old_value=old_status,
            new_value="Closed",
            notes="Work Order closed.",
            user_id=user_id,
            username=username,
            conn=conn,
        )

    @staticmethod
    def log_reopened(
        work_order_id,
        reason,
        user_id=None,
        username=None,
        conn=None,
    ):
        return WorkOrderHistoryService.add(
            work_order_id,
            action="Reopened",
            field_name="Status",
            old_value="Completed",
            new_value="In Progress",
            notes=reason,
            user_id=user_id,
            username=username,
            conn=conn,
        )