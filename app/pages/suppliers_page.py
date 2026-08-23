from app.base.crud_page import CrudPage
from app.dialogs.supplier_dialog import SupplierDialog
from app.services.supplier_service import SupplierService
from app.ui.generated.ui_supplier_page import Ui_SuppliersWindow
from app.core.permissions import Permissions

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
        "status",
        "notes",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SuppliersWindow()
        self.ui.setupUi(self)

        self.service = SupplierService
        self.dialog_class = SupplierDialog
        self.table = self.ui.tblSuppliers
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
            "suppliers.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "suppliers.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "suppliers.delete"
        )

        self.ui.btnAdd.setVisible(
            can_create
        )

        self.ui.btnEdit.setVisible(
            can_edit
        )

        self.ui.btnDelete.setVisible(
            can_delete
        )

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

    def handle_double_click(self, _item):

        if Permissions.has_permission(
            self.role,
            "suppliers.edit"
        ):
            self.edit_record()

    def add_record(self):

        if not Permissions.has_permission(
            self.role,
            "suppliers.create"
        ):
            self.warning(
                "Suppliers",
                "You do not have permission "
                "to add suppliers."
            )
            return

        super().add_record()


    def edit_record(self):

        if not Permissions.has_permission(
            self.role,
            "suppliers.edit"
        ):
            self.warning(
                "Suppliers",
                "You do not have permission "
                "to edit suppliers."
            )
            return

        super().edit_record()


    def delete_record(self):

        if not Permissions.has_permission(
            self.role,
            "suppliers.delete"
        ):
            self.warning(
                "Suppliers",
                "You do not have permission "
                "to delete suppliers."
            )
            return

        super().delete_record()