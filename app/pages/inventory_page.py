from operator import index

from app.base.crud_page import CrudPage
from app.dialogs.inventory_dialog import InventoryDialog
from app.services.inventory_service import InventoryService
from app.ui.generated.ui_inventory_page import Ui_InventoryPage
from app.helpers.format_helper import FormatHelper


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

        self.setup_page()

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

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
        