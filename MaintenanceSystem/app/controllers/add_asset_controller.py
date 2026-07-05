from PySide6.QtWidgets import (
    QDialog,
    QMessageBox
)

from app.ui.generated.ui_add_asset import Ui_AddAssetDialog
from app.services.asset_service import AssetService


class AddAssetController(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_AddAssetDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):

        # Generate next asset number
        self.ui.txtAssetNumber.setText(
            AssetService.get_next_asset_number()
        )

        # Prevent editing
        self.ui.txtAssetNumber.setReadOnly(True)

        # Categories
        self.ui.cmbCategory.clear()
        self.ui.cmbCategory.addItems([
            "Electrical",
            "Mechanical",
            "HVAC",
            "Plumbing",
            "Kitchen",
            "Laundry",
            "Vehicle",
            "IT",
            "Fire Safety"
        ])

        # Locations
        self.ui.cmbLocation.clear()
        self.ui.cmbLocation.addItems([
            "Reception",
            "Office",
            "Kitchen",
            "Workshop",
            "Laundry",
            "Restaurant",
            "Bar",
            "Guest Rooms",
            "Solar Plant",
            "Borehole",
            "Parking",
            "Swimming Pool"
        ])

        # Status
        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems([
            "Active",
            "Inactive",
            "Under Repair",
            "Disposed",
            "Wait for Parts"
        ])

        # Enable popup calendars
        self.ui.dtPurchaseDate.setCalendarPopup(True)
        self.ui.dtWarrantyExpiry.setCalendarPopup(True)

        # Connect dialog buttons
        self.ui.buttonBox.accepted.connect(self.save_asset)
        self.ui.buttonBox.rejected.connect(self.reject)

    def save_asset(self):

        asset_name = self.ui.txtAssetName.text().strip()

        if not asset_name:
            QMessageBox.warning(
                self,
                "Validation",
                "Asset Name is required."
            )
            return

        asset = (
            self.ui.txtAssetNumber.text(),
            asset_name,
            self.ui.cmbCategory.currentText(),
            self.ui.cmbLocation.currentText(),
            self.ui.txtManufacturer.text().strip(),
            self.ui.txtModel.text().strip(),
            self.ui.txtSerialNumber.text().strip(),
            self.ui.dtPurchaseDate.date().toString("yyyy-MM-dd"),
            self.ui.dtWarrantyExpiry.date().toString("yyyy-MM-dd"),
            self.ui.cmbStatus.currentText()
        )

        AssetService.add_asset(asset)

        QMessageBox.information(
            self,
            "Success",
            "Asset saved successfully."
        )

        self.accept()