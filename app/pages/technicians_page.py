from app.base.crud_page import CrudPage
from app.dialogs.technician_dialog import TechnicianDialog
from app.services.technician_service import TechnicianService
from app.ui.generated.ui_technicians_page import Ui_TechniciansWindow


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

        # Shared CRUD framework configuration
        self.service = TechnicianService
        self.dialog_class = TechnicianDialog
        self.table = self.ui.tblTechnicians
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

        self.ui.txtSearch.textChanged.connect(
            self.search
        )

        self.ui.tblTechnicians.itemDoubleClicked.connect(
            lambda _item: self.edit_record()
        )