from operator import index

from app.base.crud_page import CrudPage
from app.dialogs.technician_dialog import TechnicianDialog
from app.services.technician_service import TechnicianService
from app.ui.generated.ui_technicians_page import Ui_TechniciansWindow
from app.helpers.format_helper import FormatHelper


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

        self.setup_page()

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

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
            lambda _item: self.edit_record()
        )

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
        