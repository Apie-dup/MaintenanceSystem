from PySide6.QtWidgets import (
    QWidget,
    QAbstractItemView,
    QHeaderView,
    QMessageBox,
    QTableWidgetItem
)

from PySide6.QtCore import Qt

from app.base.crud_page import CrudPage
from app.services.supplier_service import SupplierService
from app.ui.generated.ui_supplier_page import Ui_SuppliersWindow

class SuppliersPage(CrudPage):

    def __init__(self, parent = None):
        super().__init__(parent)

        PAGE_TITLE = "Suppliers"

        TABLE_COLUMNS = [
            ("supplier_code", "Code"),
            ("supplier_name", "Supplier Name"),
            ("contac_person", "Contact Person"),
            ("phone", "Phone"),
            ("email", "Email"),
            ("address", "Address"),
            ("status", "Status"),
            ("notes", "Notes"),
        ]

        SEARCH_FIELDS = [
            "supplier_code",
            "supplier_name",
            "contact_person",
            "phone",
            "email",
            "address",
        ]

        self.ui = Ui_SuppliersWindow()
        self.ui.setupUi(self)

        self.setup_page()

    def setup_page(self):

        self.setup_table()
        self.connect_signals()
        self.load_data()

    def connect_signals(self):

        self.ui.txtSearch.textChanged.connect(self.search)

        self.ui.btnAdd.clicked.connect(self.add_record)
        self.ui.btnEdit.clicked.connect(self.edit_record)
        self.ui.btnDelete.clicked.connect(self.delete_record)
        self.ui.btnRefresh.clicked.connect(self.load_data)

        self.ui.tblSuppliers.itemSelectionChanged.connect(
            self.selection_changed
        )

    def setup_table(self):

        table = self.ui.tblSuppliers

        headers = [
            "Code",
            "Supplier",
            "Contact",
            "Phone",
            "Email",
            "address,"
            "Status",
            "notes"
        ]

        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )



    def load_data(self):

        rows = SupplierService.get_all()

        self.populate_table(rows)

    def populate_table(self, rows):

        table = self.ui.tblSuppliers

        table.setRowCount(0)

        for supplier in rows:

            row = table.rowCount()
            table.insertRow(row)

            item = QTableWidgetItem(supplier["supplier_code"])
            item.setData(Qt.UserRole, supplier["id"])

            table.setItem(row, 0, item)

            table.setItem(
                row,
                1,
                QTableWidgetItem(supplier["supplier_name"])
            )

            table.setItem(
                row,
                2,
                QTableWidgetItem(supplier["contact_person"] or "")
            )

            table.setItem(
                row,
                3,
                QTableWidgetItem(supplier["phone"] or "")
            )

            table.setItem(
                row,
                4,
                QTableWidgetItem(supplier["email"] or "")
            )

            table.setItem(
                row,
                5,
                QTableWidgetItem(supplier["address"] or "")
            )

            table.setItem(
                row,
                6,
                QTableWidgetItem(supplier["status"] or "")
            )

            table.setItem(
                row,
                7,
                QTableWidgetItem(supplier["notes"])
            )

    def search(self):

        text = self.ui.txtSearch.text().strip()

        rows = SupplierService.search(text)

        self.populate_table(rows)

    def selection_changed(self):

        row = self.ui.tblSuppliers.currentRow()

        if row < 0:
            return None

        return self.ui.tblSuppliers.item(
            row,
            0
        ).data(Qt.UserRole)

    def add_record(self):

        QMessageBox.information(
            self,
            "Suppliers",
            "Suppliers dialog cumming next"
        )

    def edit_record(self):

        supplier_id = self.selected_id()

        if supplier_id is None:
            return

        print(supplier_id)
              

    def delete_record(self):

        supplier_id = self.selected_id()

        if supplier_id is None:
            return

        SupplierService.delete_supplier(supplier_id)

        self.load_data()