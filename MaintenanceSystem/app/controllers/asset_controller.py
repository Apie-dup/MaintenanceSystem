from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTableWidgetItem
)

from PySide6.QtWidgets import QAbstractItemView

from app.ui.generated.ui_assets import Ui_AssetsWindow
from app.services.asset_service import AssetService
from app.controllers.add_asset_controller import AddAssetController


class AssetsController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.ui.tblAssets.setAlternatingRowColors(True)
        self.ui.tblAssets.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tblAssets.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tblAssets.horizontalHeader().setStretchLastSection(True)

        self.setWindowTitle("Assets")

        self.load_assets()

        self.ui.btnRefresh.clicked.connect(self.load_assets)
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnAdd.clicked.connect(self.add_asset)
        self.ui.btnEdit.clicked.connect(self.edit_asset)
        self.ui.btnDelete.clicked.connect(self.delete_asset)
        
    def load_assets(self):

        assets = AssetService.get_assets()

        self.ui.tblAssets.setRowCount(len(assets))

        for row, asset in enumerate(assets):

            for column, value in enumerate(asset):

                self.ui.tblAssets.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

                #Hide database ID
                self.ui.tblAssets.hideColumn(0)

    def add_asset(self):

        dialog = AddAssetController()
        dialog.exec()


    def edit_asset(self):

        row = self.ui.tblAssets.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Edit Asset", "Please select an asset")
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
