from app.base.crud_page import CrudPage
from app.dialogs.supplier_dialog import SupplierDialog
from app.services.supplier_service import SupplierService
from app.ui.generated.ui_supplier_page import Ui_SuppliersWindow


class SuppliersPage(CrudPage):

    PAGE_TITLE = "Suppliers"

    ENTITY_NAME = "Supplier"

    RECORD_NAME = "suppliers"

    TABLE_COLUMNS = [
        ("supplier_code", "Code"),
        ("supplier_name", "Supplier Name"),
        ("contact_person", "Contact Person"),
        ("phone", "Phone"),
        ("email", "Email"),
        ("address", "Address"),
        ("status", "Status"),
        ("notes", "Notes"),
    ]

    SEARCH_FIELDS = [
        "supplier_code",
        "supplier_name",
        "contact_person",
        "phone",
        "email",
        "address",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SuppliersWindow()
        self.ui.setupUi(self)

        # Configure the shared CRUD framework
        self.service = SupplierService
        self.dialog_class = SupplierDialog
        self.table = self.ui.tblSuppliers
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
        self.ui.txtSearch.textChanged.connect(self.search)

        self.ui.btnAdd.clicked.connect(self.add_record)
        self.ui.btnEdit.clicked.connect(self.edit_record)
        self.ui.btnDelete.clicked.connect(self.delete_record)
        self.ui.btnRefresh.clicked.connect(self.refresh)

        # Optional: double-click a supplier to edit it.
        self.ui.tblSuppliers.itemDoubleClicked.connect(
            lambda _item: self.edit_record()
        )