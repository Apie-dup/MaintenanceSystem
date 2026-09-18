from app.dialogs.work_order_dialog import WorkOrderDialog


class AddWorkOrderController(WorkOrderDialog):
    """Compatibility wrapper for the legacy Add Work Order controller tests."""

    def __init__(self, work_order_id=None, parent=None):
        super().__init__(parent=parent)
        self.record_id = work_order_id

        if work_order_id is None:
            self.new_record()
            return

        try:
            self.load_record(work_order_id)
        except Exception:
            self.ui.txtWorkOrderNumber.setText("")
