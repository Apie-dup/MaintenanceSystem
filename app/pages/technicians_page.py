from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView

from app.ui.generated.ui_technicians_page import Ui_TechniciansWindow
from app.services.technician_service import TechnicianService
from app.controllers.add_technician_controller import AddTechnicianController


class TechniciansPage(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_TechniciansWindow()
        self.ui.setupUi(self)

        self.initialize_window()

    def initialize_window(self):
        self.load_technicians()

        self.ui.btnAdd.clicked.connect(self.add_technician)
        self.ui.btnEdit.clicked.connect(self.edit_technician)
        self.ui.btnDelete.clicked.connect(self.delete_technician)
        self.ui.btnRefresh.clicked.connect(self.load_technicians)
        self.ui.btnClose.clicked.connect(self.close)

        self.ui.txtSearch.textChanged.connect(self.search_technicians)

    def load_technicians(self):
        technicians = TechnicianService.get_all()
        self.populate_table(technicians)

    def populate_table(self, technicians):
        self.ui.tblTechnicians.setRowCount(len(technicians))

        for row, technician in enumerate(technicians):
            for column, value in enumerate(technician):
                item = QTableWidgetItem("" if value is None else str(value))
                self.ui.tblTechnicians.setItem(
                    row,
                    column,
                    item
                )

        self.ui.tblTechnicians.setColumnHidden(0, True)

        header = self.ui.tblTechnicians.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tblTechnicians.setAlternatingRowColors(True)
        self.ui.tblTechnicians.setSortingEnabled(True)

        self.ui.lblStatus.setText(
            f"Showing {len(technicians)} technicians"
        )

    def add_technician(self):
        dialog = AddTechnicianController()

        if dialog.exec():
            self.load_technicians()

    def edit_technician(self):
        row = self.ui.tblTechnicians.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Select Technician",
                "Please select a technician."
            )
            return

        technician_id = int(
            self.ui.tblTechnicians.item(row, 0).text()
        )

        dialog = AddTechnicianController(technician_id)

        if dialog.exec():
            self.load_technicians()

    def delete_technician(self):
        row = self.ui.tblTechnicians.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "Select Technician",
                "Please select a technician."
            )
            return

        technician_id = int(
            self.ui.tblTechnicians.item(row, 0).text()
        )

        reply = QMessageBox.question(
            self,
            "Delete Technician",
            "Delete this technician?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            TechnicianService.delete_technician(technician_id)
            self.load_technicians()

    def search_technicians(self, text):
        search_text = text.strip()

        if search_text:
            technicians = TechnicianService.search_technicians(search_text)
        else:
            technicians = TechnicianService.get_all()

        self.populate_table(technicians)

    def refresh(self):
        self.load_technicians()
