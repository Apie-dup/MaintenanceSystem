from PySide6.QtWidgets import (
    QDialog,
    QMessageBox
)
from PySide6.QtCore import QDate

from app.ui.generated.ui_add_asset import Ui_AddAssetDialog
from app.services.asset_service import AssetService
from app.constants import (
    ASSET_CATEGORIES,
    ASSET_LOCATIONS,
    ASSET_STATUSES
)
from app.utils.validators import Validator



class AddAssetController(QDialog):

    def __init__(self, asset_id=None):
        super().__init__()

        self.asset_id = asset_id

        self.ui = Ui_AddAssetDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):
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

        if self.asset_id is None:
            # ADD MODE
            self.ui.txtAssetNumber.setText(
                AssetService.get_next_asset_number()
            )
        else:
            # EDIT MODE
            asset = AssetService.get_asset(self.asset_id)

            (
                _,
                asset_number,
                asset_name,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                purchase_date,
                warranty_expiry,
                status
            ) = asset

            self.ui.txtAssetNumber.setText(asset_number)
            self.ui.txtAssetName.setText(asset_name)
            self.ui.cmbCategory.setCurrentText(category)
            self.ui.cmbLocation.setCurrentText(location)
            self.ui.txtManufacturer.setText(manufacturer)
            self.ui.txtModel.setText(model)
            self.ui.txtSerialNumber.setText(serial_number)

            if purchase_date:
                self.ui.dtPurchaseDate.setDate(
                    QDate.fromString(
                        purchase_date,
                        "yyyy-MM-dd"
                    )
                )

            if warranty_expiry:
                self.ui.dtWarrantyExpiry.setDate(
                    QDate.fromString(
                        warranty_expiry,
                        "yyyy-MM-dd"
                    )
                )

            self.ui.cmbStatus.setCurrentText(status)
            self.ui.txtAssetNumber.setReadOnly(True)

        # Connect dialog buttons
        self.ui.buttonBox.accepted.connect(self.save_asset)
        self.ui.buttonBox.rejected.connect(self.reject)

        if self.asset_id is None:
            self.setWindowTitle("Add Asset")
        else:
            self.setWindowTitle("Edit Asset")

    def save_asset(self):

        asset_name = self.ui.txtAssetName.text().strip()

        if not Validator.required(
            self,
            asset_name,
            "Asset Name"
        ):
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

        if self.asset_id is None:
            AssetService.add_asset(asset)

            QMessageBox.information(
                self,
                "Success",
                "Asset added successfully."
            )

        else:
            update_asset = (
                asset_name,
                self.ui.cmbCategory.currentText(),
                self.ui.cmbLocation.currentText(),
                self.ui.txtManufacturer.text().strip(),
                self.ui.txtModel.text().strip(),
                self.ui.txtSerialNumber.text().strip(),
                self.ui.dtPurchaseDate.date().toString("yyyy-MM-dd"),
                self.ui.dtWarrantyExpiry.date().toString("yyyy-MM-dd"),
                self.ui.cmbStatus.currentText(),
                self.asset_id
            )
            AssetService.update_asset(update_asset)
            QMessageBox.information(
                self,
                "Success",
                "Asset updated successfully."
            )