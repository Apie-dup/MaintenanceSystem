from app.base.crud_page import CrudPage
from app.dialogs.work_order_dialog import WorkOrderDialog
from app.services.work_order_service import WorkOrderService
from app.ui.generated.ui_work_orders_page import Ui_WorkOrdersPage
from app.core.permissions import Permissions
from app.helpers.table_helper import TableHelper


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
        
        self.user = getattr(
            parent,
            "user", 
            {}
        )

        self.role = self.user.get(
            "role",
            ""
        )
                
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
        self.apply_permissions()
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
            self.handle_double_click
        )

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "work_orders.create"
        )

        can_edit = (
            Permissions.has_permission(
                self.role,
                "work_orders.edit"
            )
            or Permissions.has_permission(
                self.role,
                "work_orders.update"
            )
        )

        self.ui.btnAdd.setVisible(
            can_create
        )

        self.ui.btnEdit.setVisible(
            can_edit
        )

        # Delete should normally stay unavailable
        # unless you explicitly create a permission for it.
        if hasattr(self.ui, "btnDelete"):
            self.ui.btnDelete.setVisible(False)

    def handle_double_click(self, _item):

        record_id = TableHelper.selected_id(
            self.table
        )

        if record_id is None:
            return

        #------------------------------------------------
        # Administrator / Maintenance Manager
        #------------------------------------------------

        if Permissions.has_permission(
            self.role,
            "work_orders.edit"
        ):
            self.edit_record()
            return

        #------------------------------------------------
        # Technician
        #------------------------------------------------

        if Permissions.has_permission(
            self.role,
            "work_orders.update"
        ):
            self.open_technician_work_order(
                record_id
            )
            return

        #------------------------------------------------
        # Viewer
        #------------------------------------------------

        if Permissions.has_permission(
            self.role,
            "work_orders"
        ):

            dialog = self.dialog_class(
                parent=self
            )

            dialog.edit_record(
                record_id
            )

            dialog.set_work_order_read_only(
                True
            )

            dialog.exec()

    def add_record(self):

        if not Permissions.has_permission(
            self.role,
            "work_orders.create"
        ):
            self.warning(
                "Work Orders",
                "You do not have permission "
                "to create work orders."
            )
            return

        super().add_record()


    def edit_record(self):

        #------------------------------------------------
        # Administrator / Maintenance Manager
        #------------------------------------------------

        if Permissions.has_permission(
            self.role,
            "work_orders.edit"
        ):
            super().edit_record()
            return

        #------------------------------------------------
        # Technician
        #------------------------------------------------

        if Permissions.has_permission(
            self.role,
            "work_orders.update"
        ):

            record_id = TableHelper.selected_id(
                self.table
            )

            if record_id is None:
                self.warning(
                    "Work Orders",
                    "Please select a work order."
                )
                return

            self.open_technician_work_order(
                record_id
            )
            return

        #------------------------------------------------
        # No edit permission
        #------------------------------------------------

        self.warning(
            "Work Orders",
            "You do not have permission "
            "to edit work orders."
        )
            
    def open_technician_work_order(
        self,
        record_id
    ):

        dialog = self.dialog_class(
        parent=self
    )

        dialog.edit_record(
        record_id
        )

        work_order = self.service.get_by_id(
            record_id
        )

        if (
            work_order is not None
            and work_order["status"] not in {
                "Completed",
                "Closed",
                "Cancelled"
            }
        ):
            dialog.set_technician_mode(
                True
            )

        dialog.exec()

        self.load_data()