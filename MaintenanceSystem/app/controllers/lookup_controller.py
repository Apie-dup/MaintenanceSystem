from PySide6.QtWidgets import(
    QMainWindow,
    QMessageBox,
    QInputDialog,
    QTableWidgetItem,
    QHeaderView
)

from app.ui.generated.ui_lookups import Ui_LookupWindow
from app.services.lookup_service import LookupService

class LookupController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LookupWindow()
        self.ui.setupUi(self)

        self.initialize_window()

    def initialize_window(self):
        self.ui.cmbLookupType.addItems([
            "Trades",
            "Departments",
            "Priorities",
            "Statuses",
            "Asset Categories",
            "Asset Locations",
            "Manufacturers",
            "Inventory Categories",
            "Units of Measure"
        ])

        self.load_lookup()

        self.ui.cmbLookupType.currentTextChanged.connect(
            self.load_lookup
        )

        self.ui.txtSearch.textChanged.connect(
            self.search_lookup
        )

        self.ui.btnAdd.clicked.connect(
            self.add_lookup
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_lookup
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_lookup
        )

        self.ui.btnRefresh.clicked.connect(
            self.load_lookup
        )

        self.ui.btnClose.clicked.connect(
            self.close
        )

    def load_lookup(self):
        lookup_type = self.ui.cmbLookupType.currentText()

        rows = LookupService.get_lookup_values(
            lookup_type
        )

        self.populate_table(rows)

    def populate_table(self, rows):
        self.ui.tblLookup.setRowCount(len(rows))

        for row, data in enumerate(rows):
            for column, value in enumerate(data):
                self.ui.tblLookup.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        self.ui.tblLookup.setColumnHidden(0, True)

        header = self.ui.tblLookup.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tblLookup.setAlternatingRowColors(True)

        self.ui.lblStatus.setText(
            f"Showing {len(rows)} records"
        )

    def search_lookup(self):
        search = self.ui.txtSearch.text().lower()

        for row in range(self.ui.tblLookup.rowCount()):
            item = self.ui.tblLookup.item(row, 1)

            if item:
                self.ui.tblLookup.setRowHidden(
                    row,
                    search not in item.text().lower()
                )

    def add_lookup(self):
        lookup_type = self.ui.cmbLookupType.currentText()

        value, ok = QInputDialog.getText(
            self,
            f"Add {lookup_type}",
            "Name:"
        )

        if ok and value.strip():
            LookupService.add_lookup_value(
                lookup_type,
                value.strip()
            )

            self.load_lookup()

    def edit_lookup(self):
        row = self.ui.tblLookup.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Edit",
                "Please select a record."
            )
            return

        lookup_id = int(
            self.ui.tblLookup.item(row, 0).text()
        )

        current_value = self.ui.tblLookup.item(row, 1).text()

        lookup_type = self.ui.cmbLookupType.currentText()

        value, ok = QInputDialog.getText(
            self,
            "Edit",
            "Name:",
            text=current_value
        )

        if ok and value.strip():
            LookupService.update_lookup_value(
                lookup_type,
                lookup_id,
                value.strip()
            )

            self.load_lookup()

    def delete_lookup(self):
        row = self.ui.tblLookup.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Delete",
                "Please select a record."
            )
            return

        reply = QMessageBox.question(
            self,
            "Delete",
            "Delete selected record?"
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        lookup_id = int(
            self.ui.tblLookup.item(row, 0).text()
        )

        lookup_type = self.ui.cmbLookupType.currentText()

        LookupService.delete_lookup_value(
            lookup_type,
            lookup_id
        )

        self.load_lookup()
