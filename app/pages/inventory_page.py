from app.base.crud_page import CrudPage
from app.dialogs.inventory_dialog import InventoryDialog
from app.services.inventory_service import InventoryService
from app.ui.generated.ui_inventory_page import Ui_InventoryPage
from app.helpers.format_helper import FormatHelper
from app.core.permissions import Permissions
from app.helpers.table_helper import TableHelper

class InventoryPage(CrudPage):

    PAGE_TITLE = "Inventory"
    ENTITY_NAME = "Inventory Item"
    RECORD_NAME = "inventory items"

    TABLE_COLUMNS = [
        ("part_number", "Part Number"),
        ("part_name", "Part Name"),
        ("category", "Category"),
        ("supplier_name", "Supplier"),
        ("unit", "Unit"),
        ("quantity", "Quantity"),
        ("minimum_quantity", "Minimum"),
        ("reorder_quantity", "Reorder"),
        ("unit_cost", "Unit Cost"),
        ("location", "Location"),
        ("status", "Status"),
    ]

    SEARCH_FIELDS = [
        "part_number",
        "part_name",
        "description",
        "category",
        "supplier_code",
        "supplier_name",
        "location",
        "barcode",
        "status",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_InventoryPage()
        self.ui.setupUi(self)

        self.resize(700, 700)

        self.setMinimumSize(
            700,
            700,    
        )

        self.setMaximumWidth(
            900
        )

        self.service = InventoryService
        self.dialog_class = InventoryDialog
        self.table = self.ui.tblInventory
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
            "inventory.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "inventory.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "inventory.delete"
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
        record_id = TableHelper.selected_id(
            self.table
        )

        if record_id is None:
            return

        # Normal edit access
        if Permissions.has_permission(
            self.role,
            "inventory.edit"
        ):
            self.edit_record()
            return

        # Read-only access
        if Permissions.has_permission(
            self.role,
            "inventory"
        ):
            dialog = self.dialog_class(
                parent=self
            )

            dialog.edit_record(
                record_id
            )

            if hasattr(
                dialog,
                "set_inventory_read_only"
            ):
                dialog.set_inventory_read_only(
                    True
                )

            dialog.exec()

    def populate_table(self, records):

        super().populate_table(records)

        unit_cost_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.TABLE_COLUMNS)
                if field == "unit_cost"
            ),
            None
        )

        if unit_cost_column is None:
            return

        for row in range(
            self.table.rowCount()
        ):
            item = self.table.item(
                row,
                unit_cost_column
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

    def add_record(self):
        if not Permissions.has_permission(
            self.role,
            "inventory.create"
        ):
            self.warning(
                "Inventory",
                "You do not have permission "
                "to add inventory items."
            )
            return

        super().add_record()


    def edit_record(self):

        if not Permissions.has_permission(
            self.role,
            "inventory.edit"
        ):
            self.warning(
                "Inventory",
                "You do not have permission "
                "to edit inventory items."
            )
            return

        super().edit_record()


    def delete_record(self):

        if not Permissions.has_permission(
            self.role,
            "inventory.delete"
        ):
            self.warning(
                "Inventory",
                "You do not have permission "
                "to delete inventory items."
            )
            return

        super().delete_record()
        