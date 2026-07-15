from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QMessageBox
)

from app.ui.generated.ui_pm_page import Ui_PMWindow
from app.services.pm_service import PMService
from app.controllers.add_pm_controller import AddPMController


class PMPage(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_PMWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(
            "Preventive Maintenance"
        )

        self.ui.tblPM.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.ui.tblPM.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.load_pm()

        self.ui.btnRefresh.clicked.connect(
            self.load_pm
        )

        self.ui.btnAdd.clicked.connect(
            self.add_pm
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_pm
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_pm
        )

        self.ui.txtSearch.textChanged.connect(
            self.search_pm
        )

        self.ui.tblPM.doubleClicked.connect(
            self.edit_pm
        )


    def load_pm(self):

        schedules = PMService.get_pm_schedules()

        self.populate_table(
            schedules
        )


    def populate_table(self, schedules):

        self.ui.tblPM.setRowCount(
            len(schedules)
        )

        for row, schedule in enumerate(schedules):

            for column, value in enumerate(schedule):

                self.ui.tblPM.setItem(
                    row,
                    column,
                    QTableWidgetItem(
                        str(value)
                    )
                )


        self.ui.tblPM.setColumnHidden(
            0,
            True
        )

        header = self.ui.tblPM.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.ui.lblStatus.setText(
            f"Showing {len(schedules)} PM schedules"
        )


    def add_pm(self):

        dialog = AddPMController()

        if dialog.exec():

            self.load_pm()


    def edit_pm(self):

        row = self.ui.tblPM.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Edit PM",
                "Please select a PM schedule."
            )
            return


        pm_id = int(
            self.ui.tblPM.item(row, 0).text()
        )

        dialog = AddPMController(
            pm_id
        )

        if dialog.exec():

            self.load_pm()


    def delete_pm(self):

        row = self.ui.tblPM.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Delete PM",
                "Please select a PM schedule."
            )
            return


        pm_id = int(
            self.ui.tblPM.item(row, 0).text()
        )


        reply = QMessageBox.question(
            self,
            "Delete PM",
            "Delete this PM schedule?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )


        if reply == QMessageBox.StandardButton.Yes:

            PMService.delete_pm(
                pm_id
            )

            self.load_pm()


    def search_pm(self):

        text = self.ui.txtSearch.text().strip()

        if text:

            schedules = PMService.search_pm(
                text
            )

        else:

            schedules = PMService.get_pm_schedules()


        self.populate_table(
            schedules
        )