from PySide6.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem, QHeaderView, QMessageBox
from app.services.asset_service import AssetService
from app.ui.generated.ui_assets_page import Ui_AssetsWindow
from app.controllers.add_asset_controller import AddAssetController

class AssetsPage(QWidget):


    def __init__(self):
        super().__init__()

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.ui.tblAssets.setAlternatingRowColors(True)
        self.ui.tblAssets.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tblAssets.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tblAssets.horizontalHeader().setStretchLastSection(True)

        self.load_assets()

        self.ui.btnRefresh.clicked.connect(self.load_assets)
        self.ui.btnAdd.clicked.connect(self.add_asset)
        self.ui.btnEdit.clicked.connect(self.edit_asset)
        self.ui.btnDelete.clicked.connect(self.delete_asset)
        self.ui.txtSearch.textChanged.connect(self.search_assets)
        self.ui.tblAssets.doubleClicked.connect(self.edit_asset)
        
    def load_assets(self):

        assets = AssetService.get_assets()
        self.populate_table(assets)

    def populate_table(self, assets):
        
        self.ui.tblAssets.setRowCount(len(assets))
        self.ui.tblAssets.setColumnCount(11)

        for row, asset in enumerate(assets):
            values = list(asset)
            if len(values) < 11:
                values += [""] * (11 - len(values))

            for column, value in enumerate(values[:11]):
                item = self.ui.tblAssets.item(row, column)
                if item is None:
                    item = QTableWidgetItem()
                    self.ui.tblAssets.setItem(row, column, item)

                item.setText(str(value if value is not None else ""))

        self.ui.tblAssets.setColumnHidden(0, True)

        header = self.ui.tblAssets.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tblAssets.setAlternatingRowColors(True)
        self.ui.tblAssets.setSortingEnabled(True)
        self.ui.lblStatus.setText(
            f"Showing {len(assets)} assets"
        )
    
    def add_asset(self):

        dialog = AddAssetController()
        
        if dialog.exec():
            self.load_assets()


    def edit_asset(self):

        row = self.ui.tblAssets.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Edit Asset",
                "Please select an asset."
            )
            return

        asset_id = int(self.ui.tblAssets.item(row, 0).text())

        dialog = AddAssetController(asset_id)

        if dialog.exec():
            self.load_assets()

    def delete_asset(self):
        row = self.ui.tblAssets.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Delete Asset",
                "Please select an asset to delete."
            )
            return

        asset_id = int(
            self.ui.tblAssets.item(row, 0).text()
        )

        asset_number = self.ui.tblAssets.item(row, 1).text()
        asset_name = self.ui.tblAssets.item(row, 2).text()

        reply = QMessageBox.question(
            self,
            "Delete Asset",
            f"Delete asset '{asset_number} - {asset_name}'?\n\n"
            "This action cannot be undone.",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            AssetService.delete_asset(asset_id)

            QMessageBox.information(
                self,
                "Deleted",
                "Asset deleted successfully."
            )

            self.load_assets()

    def search_assets(self):
        text = self.ui.txtSearch.text().strip()
        if text == "":
            assets = AssetService.get_assets()
        else:
            assets = AssetService.search_assets(text)
        self.populate_table(assets)

