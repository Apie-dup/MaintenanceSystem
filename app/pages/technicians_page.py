from app.base.crud_page import CrudPage
from app.dialogs.technician_dialog import TechnicianDialog
from app.services.technician_service import TechnicianService
from app.ui.generated.ui_technicians_page import Ui_TechniciansWindow
from app.helpers.format_helper import FormatHelper
from app.core.permissions import Permissions
from app.helpers.table_helper import TableHelper


class TechniciansPage(CrudPage):

    PAGE_TITLE = "Technicians"
    ENTITY_NAME = "Technician"
    RECORD_NAME = "technicians"

    TABLE_COLUMNS = [
        ("employee_number", "Employee Number"),
        ("first_name", "First Name"),
        ("last_name", "Last Name"),
        ("phone", "Phone"),
        ("email", "Email"),
        ("trade", "Trade"),
        ("department", "Department"),
        ("hourly_rate", "Hourly Rate"),
        ("status", "Status"),
    ]

    SEARCH_FIELDS = [
        "employee_number",
        "first_name",
        "last_name",
        "phone",
        "email",
        "trade",
        "department",
        "status",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_TechniciansWindow()
        self.ui.setupUi(self)

        self.service = TechnicianService
        self.dialog_class = TechnicianDialog
        self.table = self.ui.tblTechnicians
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.user = getattr(
            parent,
            "user",
            {}
        )

        self.role = self.user.get(
            "role",
            ""
        )

        self.setup_page()

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.apply_permissions()
        self.load_data()

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "technicians.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "technicians.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "technicians.delete"
        )

        self.ui.btnAdd.setVisible(
            can_create
        )

        can_edit = (
            Permissions.has_permission(
                self.role,
                "work_orders.edit"
            )
            or
            Permissions.has_permission(
                self.role,
                "work_orders.update"
            )
        )

        self.ui.btnEdit.setVisible(
            can_edit
        )

        self.ui.btnDelete.setVisible(
            can_delete
        )

    def connect_signals(self):
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

        self.search_widget.textChanged.connect(
            self.search
        )

        self.table.itemDoubleClicked.connect(
            self.handle_double_click
        )

    def handle_double_click(self, _item):

        record_id = TableHelper.selected_id(
            self.table
        )

        if record_id is None:
            return

        #Full edit
        if Permissions.has_permission(
            self.role,
            "work_orders.edit"
        ):

            self.edit_record()
            return

        # Technician operational update
        if Permissions.has_permission(
            self.role,
            "work_orders.update"
        ):
            self.open_technician_work_order(
                record_id
            )
            return

        # Viewer
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
            "technicians.create"
        ):
            self.warning(
                "Technicians",
                "You do not have permission "
                "to add technicians."
            )
            return

        super().add_record()


    def edit_record(self):

        if Permissions.has_permission(
            self.role,
            "work_orders.edit"
        ):
            super().edit_record()
            return

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
                    "Please select a work order"
                )
                return

            self.open_technician_work_order(
                record_id
            )

            return

        self.warning(
            "Work Orders",
            "You do not have permission "
            "to edit work orders."
        )


    def delete_record(self):

        if not Permissions.has_permission(
            self.role,
            "technicians.delete"
        ):
            self.warning(
                "Technicians",
                "You do not have permission "
                "to delete technicians."
            )
            return

        super().delete_record()

    def populate_table(self, records):

        super().populate_table(records)

        hourly_rate_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.TABLE_COLUMNS)
                if field == "hourly_rate"
            ),
            None
        )

        if hourly_rate_column is None:
            return

        for row in range(
            self.table.rowCount()
        ):
            item = self.table.item(
                row,
                hourly_rate_column
            )

            if item is None:
                continue

            try:
                value = float(
                    item.text() or 0
                )

                item.setText(
                    FormatHelper.currency(
                        value
                    )
                )
                
            except ValueError:
                continue
        