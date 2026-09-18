from app.pages.work_orders_page import WorkOrdersPage


class WorkOrderController(WorkOrdersPage):
    """Compatibility wrapper for legacy controller-style tests."""

    def __init__(self, parent=None):
        super().__init__(parent)
