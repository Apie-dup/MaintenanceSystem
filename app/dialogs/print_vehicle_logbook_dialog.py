from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from app.ui.generated.ui_print_vehicle_logbook_dialog import (
    Ui_PrintVehicleLogbookDialog
)
from app.services.asset_service import AssetService

class PrintVehicleLogbookDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PrintVehicleLogbookDialog()
        self.ui.setupUi(self)

        self.load_vehicles()
        self.setup_dates()
        self.connect_signals()

    def load_vehicles(self):

        self.ui.cmbVehicle.clear()

        assets = AssetService.get_all()

        for asset in assets:

            asset_id = asset["id"]
            asset_number = asset["asset_number"]
            asset_name = asset["asset_name"]

            text = (
                f"{asset_number} - {asset_name}"
            )

            self.ui.cmbVehicle.addItem(
                text,
                asset_id
            )

    def setup_dates(self):

        today = QDate.currentDate()

        first_day = QDate(
            today.year(),
            today.month(),
            1
        )

        self.ui.dtFromDate.setDate(
            first_day
        )

        self.ui.dtToDate.setDate(
            today
        )

    def connect_signals(self):

        self.ui.btnCancel.clicked.connect(
            self.reject
        )

        self.ui.btnCreatePdf.clicked.connect(
            self.validate_and_accept
        )

    def validate_and_accept(self):

        if self.ui.cmbVehicle.currentIndex() < 0:
            return

        if (
            self.ui.dtFromDate.date()
            > self.ui.dtToDate.date()
        ):
            return

        self.accept()

    def asset_id(self):
        return self.ui.cmbVehicle.currentData()

    def asset_text(self):
        return self.ui.cmbVehicle.currentText()

    def from_date(self):
        return self.ui.dtFromDate.date().toString(
            "yyyy-MM-dd"
        )

    def to_date(self):
        return self.ui.dtToDate.date().toString(
            "yyyy-MM-dd"
        )