from PySide6.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem, QHeaderView, QMessageBox
from app.services.asset_service import AssetService
from app.ui.generated.ui_assets_page import Ui_AssetsWindow
from app.controllers.add_asset_controller import AddAssetController
from app.core.signals import signals
from app.core.crud_page import CrudPage

class AssetsPage(CrudPage):


    def __init__(self):
        super().__init__()

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.table = self.ui.tblAssets
        self.status_label = self.ui.lblStatus

        self.record_name = "assets"

        self.service = AssetService

        self.dialog = AddAssetController

        self.configure_table(self.table)

        self.load_data()

        self.connect_signals()

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

        self.ui.txtSearch.textChanged.connect(
            self.search
        )

        self.table.doubleClicked.connect(
            self.edit_record
        )

    
