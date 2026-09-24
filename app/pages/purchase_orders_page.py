from app.base.crud_page import CrudPage
from app.dialogs.purchase_order_dialog import (
    PurchaseOrderDialog,
)
from app.services.purchase_order_service import (
    PurchaseOrderService,
)
from app.ui.generated.ui_purchase_orders_page import (
    Ui_PurchaseOrdersPage,
)
from app.helpers.format_helper import FormatHelper


class PurchaseOrdersPage(CrudPage):

    PAGE_TITLE = "Purchase Orders"

    ENTITY_NAME = "Purchase Order"
    RECORD_NAME = "Purchase Orders"

    TABLE_COLUMNS = [
        ("purchase_order_number", "PO Number"),
        ("supplier_name", "Supplier"),
        ("order_date", "Order Date"),
        ("expected_date", "Expected Date"),
        ("status", "Status"),
        ("reference", "Reference"),
        ("total", "Total"),
    ]

    SEARCH_FIELDS = [
        "purchase_order_number",
        "supplier_code",
        "supplier_name",
        "status",
        "reference",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.user = getattr(
            parent,
            "user",
            {},
        )

        self.ui = Ui_PurchaseOrdersPage()
        self.ui.setupUi(self)

        self.service = PurchaseOrderService
        self.dialog_class = PurchaseOrderDialog

        self.table = self.ui.tblPurchaseOrders
        self.search_widget = self.ui.txtSearch

        self.setup_page()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

    def connect_signals(self):
        self.ui.txtSearch.textChanged.connect(
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

        self.ui.tblPurchaseOrders.itemDoubleClicked.connect(
            self.edit_record
        )

    def populate_table(self, records):
        super().populate_table(records)

        total_column = 6

        for row in range(
            self.table.rowCount()
        ):
            item = self.table.item(
                row,
                total_column,
            )

            if item is None:
                continue

            try:
                value = float(
                    item.text() or 0
                )

                item.setText(
                    FormatHelper.currency(value)
                )

            except ValueError:
                pass