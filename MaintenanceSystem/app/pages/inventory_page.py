from PySide6.QtWidgets import (
    QWidget,
    QAbstractItemView,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox
)

from app.ui.generated.ui_inventory_page import Ui_InventoryWindow
from app.services.inventory_service import InventoryService
from app.controllers.add_inventory_controller import AddInventoryController
from app.core.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self):
        super().__init__()

        self.ui = Ui_InventoryWindow()
        self.ui.setupUi(self)

        
        self.configure_table(
            self.ui.tblInventory
        )

    def connect_signals(self):

        self.ui.btnRefresh.clicked.connect(
            self.load_inventory
        )

        self.ui.btnAdd.clicked.connect(
            self.add_inventory
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_inventory
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_inventory
        )

        self.ui.btnClose.clicked.connect(
            self.close
        )

        self.ui.txtSearch.textChanged.connect(
            self.search_inventory
        )

        self.ui.tblInventory.doubleClicked.connect(
            self.edit_inventory
        )

    def load_inventory(self):

        inventory = InventoryService.get_all()

        self.populate_table(inventory)

    def populate_table(self, inventory):

        self.ui.tblInventory.setRowCount(len(inventory))

        for row, part in enumerate(inventory):

            for column, value in enumerate(part):

                self.ui.tblInventory.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        self.ui.tblInventory.setColumnHidden(0, True)

        header = self.ui.tblInventory.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.ui.lblStatus.setText(
            f"Showing {len(inventory)} parts"
        )

    def search_inventory(self):
        
        text = self.ui.txtSearch.text().strip()
        
        if text:
            assets = InventoryService.get_asset()

            self.populate_table(
                self.ui.tblAssets,
                assets,
                self.ui.lblStatus,
                "assets"
            )

    def add_inventory(self):

        dialog = AddInventoryController()

        if dialog.exec():

            self.load_inventory()

    def edit_inventory(self):

        row = self.ui.tblInventory.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Edit Part",
                "Please select a part."
            )

            return

        part_id = int(
            self.ui.tblInventory.item(row, 0).text()
        )

        dialog = AddInventoryController(part_id)

        if dialog.exec():

            self.load_inventory()

    def delete_inventory(self):

        row = self.ui.tblInventory.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Delete Part",
                "Please select a part."
            )

            return

        part_id = int(
            self.ui.tblInventory.item(row, 0).text()
        )

        part_number = self.ui.tblInventory.item(row, 1).text()
        part_name = self.ui.tblInventory.item(row, 2).text()

        reply = QMessageBox.question(
            self,
            "Delete Part",
            f"Delete '{part_number} - {part_name}'?\n\n"
            "This action cannot be undone.",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:

            InventoryService.delete_inventory(part_id)

            QMessageBox.information(
                self,
                "Deleted",
                "Inventory item deleted successfully."
            )

            self.load_inventory()