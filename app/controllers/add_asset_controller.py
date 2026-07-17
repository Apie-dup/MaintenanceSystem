from PySide6.QtWidgets import (
    QDialog,
    QMessageBox
)
from PySide6.QtCore import QDate

from app.ui.generated.ui_add_asset import Ui_AddAssetDialog
from app.services.asset_service import AssetService
from app.services.lookup_service import LookupService
from app.constants import (
    ASSET_CATEGORIES,
    ASSET_LOCATIONS,
    ASSET_STATUSES
)
from app.utils.validators import Validator
from app.core.signals import signals



class AddAssetController(QDialog):

    def __init__(self, asset_id=None):
        super().__init__()

        self.asset_id = asset_id

        self.ui = Ui_AddAssetDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):
        self.load_lookup_values()

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

            if not asset:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Asset not found."
                )
                self.reject()
                return

            (
                _,
                asset_number,
                asset_name,
                description,
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
            self.ui.teDescription.setPlainText(
                description if description else "")
            self.ui.cmbCategory.setCurrentText(category)
            self.ui.cmbLocation.setCurrentText(location)
            self.ui.txtManufacturer.setText(manufacturer)
            self.ui.txtModel.setText(model)
            self.ui.txtSerialNumber.setText(serial_number)

            if purchase_date:
                date = QDate.fromString(purchase_date, "yyyy-MM-dd")
                if date.isValid():
                 self.ui.dtPurchaseDate.setDate(date)
                

            if warranty_expiry:
                date = QDate.fromString(warranty_expiry, "yyyy-MM-dd")
                if date.isValid():
                 self.ui.dtWarrantyExpiry.setDate(date)

            self.ui.cmbStatus.setCurrentText(status)
            self.ui.txtAssetNumber.setReadOnly(True)

        # Connect dialog buttons
        self.ui.buttonBox.accepted.connect(self.save_asset)
        self.ui.buttonBox.rejected.connect(self.reject)

        if self.asset_id is None:
            self.setWindowTitle("Add Asset")
        else:
            self.setWindowTitle("Edit Asset")

    def load_lookup_values(self):
        self.ui.cmbCategory.clear()
        category_rows = LookupService.get_lookup_values("Asset Categories")
        if category_rows:
            self.ui.cmbCategory.addItems([value for _, value in category_rows])
        else:
            self.ui.cmbCategory.addItems(ASSET_CATEGORIES)

        self.ui.cmbLocation.clear()
        location_rows = LookupService.get_lookup_values("Asset Locations")
        if location_rows:
            self.ui.cmbLocation.addItems([value for _, value in location_rows])
        else:
            self.ui.cmbLocation.addItems(ASSET_LOCATIONS)

        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems(ASSET_STATUSES)


    def save_asset(self):

        asset_name = self.ui.txtAssetName.text().strip()

        if not Validator.required(
            self,
            asset_name,
            "Asset Name"
        ):
            return

        asset_number = self.ui.txtAssetNumber.text()

        asset = (
            asset_number,
            asset_name,
            self.ui.teDescription.toPlainText().strip(),
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

            signals.data_changed.emit("assets")

            QMessageBox.information(
                self,
                "Success",
                "Asset added successfully."
            )

        else:
            update_asset = (
                asset_number,
                asset_name,
                self.ui.teDescription.toPlainText().strip(),
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

            signals.data_changed.emit("assets")

            
            QMessageBox.information(
                self,
                "Success",
                "Asset updated successfully."
            )