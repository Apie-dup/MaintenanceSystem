from PySide6.QtWidgets import (
    QMainWindow,
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

    def add_asset(self):

        dialog = AddAssetController()
        dialog.exec()