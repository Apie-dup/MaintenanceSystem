from app.base.crud_page import CrudPage
from app.dialogs.asset_dialog import AssetDialog
from app.services.asset_service import AssetService
from app.ui.generated.ui_assets_page import Ui_AssetsWindow


class AssetsPage(CrudPage):

    PAGE_TITLE = "Assets"
    ENTITY_NAME = "Asset"
    RECORD_NAME = "assets"

    TABLE_COLUMNS = [
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset Name"),
        ("description", "Description"),
        ("category", "Category"),
        ("location", "Location"),
        ("manufacturer", "Manufacturer"),
        ("model", "Model"),
        ("serial_number", "Serial Number"),
        ("purchase_date", "Purchase Date"),
        ("warranty_expiry", "Warranty Expiry"),
        ("status", "Status"),
        ("notes", "Notes"),
    ]

    SEARCH_FIELDS = [
        "asset_number",
        "asset_name",
        "description",
        "category",
        "location",
        "manufacturer",
        "model",
        "serial_number",
        "status",
        "notes",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.service = AssetService
        self.dialog_class = AssetDialog
        self.table = self.ui.tblAssets
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.setup_page()

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

    def connect_signals(self):
        self.ui.btnRefresh.clicked.connect(
            self.refresh
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

        self.search_widget.textChanged.connect(
            self.search
        )

        self.table.itemDoubleClicked.connect(
            lambda _item: self.edit_record()
        )