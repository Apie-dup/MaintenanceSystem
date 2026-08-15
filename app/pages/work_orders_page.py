from app.base.crud_page import CrudPage
from app.dialogs.work_order_dialog import WorkOrderDialog
from app.services.work_order_service import WorkOrderService
from app.ui.generated.ui_work_orders_page import Ui_WorkOrdersPage


class WorkOrdersPage(CrudPage):

    PAGE_TITLE = "Work Orders"
    ENTITY_NAME = "Work Order"
    RECORD_NAME = "work orders"

    TABLE_COLUMNS = [
        ("work_order_number", "Work Order"),
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("title", "Title"),
        ("priority", "Priority"),
        ("status", "Status"),
        ("technician_display", "Technician"),
        ("due_date", "Due Date"),
        ("notes", "Notes"),
    ]

    SEARCH_FIELDS = [
        "work_order_number",
        "asset_number",
        "asset_name",
        "title",
        "description",
        "priority",
        "status",
        "requested_by",
        "employee_number",
        "first_name",
        "last_name",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_WorkOrdersPage()
        self.ui.setupUi(self)

        self.service = WorkOrderService
        self.dialog_class = WorkOrderDialog
        self.table = self.ui.tblWorkOrders
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.setup_page()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.search_widget.textChanged.connect(
            self.search
        )

        self.ui.btnAdd.clicked.connect(
            self.add_record
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_record
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.table.itemDoubleClicked.connect(
            lambda _item: self.edit_record()
        )