from PySide6.QtCore import QDate

from app.base.base_dialog import BaseDialog
from app.constants import (
    ASSET_CATEGORIES,
    ASSET_LOCATIONS,
    ASSET_STATUSES,
)
from app.core.lookup_manager import LookupManager
from app.services.asset_service import AssetService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_add_asset import Ui_AddAssetDialog


class AssetDialog(BaseDialog):

    ENTITY_NAME = "Asset"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddAssetDialog()
        self.ui.setupUi(self)

        self.setup_dialog()

    def setup_dialog(self):

        self.load_lookup_values()
        self.connect_signals()

        self.ui.txtAssetCode.setReadOnly(True)
        self.ui.dtPurchaseDate.setCalendarPopup(True)
        self.ui.dtWarrantyExpiry.setCalendarPopup(True)

    def load_lookup_values(self):

        LookupManager.load(
            self.ui.cmbCategory,
            "Asset Categories",
            ASSET_CATEGORIES,
        )

        LookupManager.load(
            self.ui.cmbLocation,
            "Asset Locations",
            ASSET_LOCATIONS,
        )

        LookupManager.load(
            self.ui.cmbStatus,
            "Statuses",
            ASSET_STATUSES,
        )

        # Department is optional in data model but present in UI.
        LookupManager.load(
            self.ui.cmbDepartment,
            "Departments",
            [],
        )

    def connect_signals(self):

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    def clear_fields(self):

        self.ui.txtAssetCode.setText(
            AssetService.get_next_asset_number()
        )

        self.ui.txtAssetName.clear()
        self.ui.txtDescription.clear()
        self.ui.txtManufacturer.clear()
        self.ui.txtModel.clear()
        self.ui.txtSerialNumber.clear()
        self.ui.txtNotes.clear()

        self.ui.cmbCategory.setCurrentIndex(0)
        self.ui.cmbDepartment.setCurrentIndex(0)
        self.ui.cmbLocation.setCurrentIndex(0)
        self.ui.cmbStatus.setCurrentText("Active")

        today = QDate.currentDate()

        self.ui.dtPurchaseDate.setDate(today)
        self.ui.dtWarrantyExpiry.setDate(today)

        self.ui.txtAssetName.setFocus()

    def get_form_data(self):

        return {
            "asset_number": self.ui.txtAssetCode.text().strip(),
            "asset_name": self.ui.txtAssetName.text().strip(),
            "description": self.ui.txtDescription.text().strip(),
            "category": self.ui.cmbCategory.currentText().strip(),
            "location": self.ui.cmbLocation.currentText().strip(),
            "manufacturer": self.ui.txtManufacturer.text().strip(),
            "model": self.ui.txtModel.text().strip(),
            "serial_number": self.ui.txtSerialNumber.text().strip(),
            "purchase_date": self.ui.dtPurchaseDate.date().toString("yyyy-MM-dd"),
            "warranty_expiry": self.ui.dtWarrantyExpiry.date().toString("yyyy-MM-dd"),
            "status": self.ui.cmbStatus.currentText().strip(),
        }

    def set_form_data(self, asset):

        self.ui.txtAssetCode.setText(asset["asset_number"])
        self.ui.txtAssetName.setText(asset["asset_name"])
        self.ui.txtDescription.setText(asset["description"] or "")
        self.ui.cmbCategory.setCurrentText(asset["category"] or "")
        self.ui.cmbLocation.setCurrentText(asset["location"] or "")
        self.ui.txtManufacturer.setText(asset["manufacturer"] or "")
        self.ui.txtModel.setText(asset["model"] or "")
        self.ui.txtSerialNumber.setText(asset["serial_number"] or "")
        self.ui.cmbStatus.setCurrentText(asset["status"] or "Active")

        self.set_date_value(
            self.ui.dtPurchaseDate,
            asset["purchase_date"],
        )

        self.set_date_value(
            self.ui.dtWarrantyExpiry,
            asset["warranty_expiry"],
        )

    @staticmethod
    def set_date_value(date_widget, value):

        if not value:
            return

        date_value = QDate.fromString(
            value,
            "yyyy-MM-dd",
        )

        if date_value.isValid():
            date_widget.setDate(date_value)

    def load_record(self, record_id):

        asset = AssetService.get_by_id(record_id)

        if asset is None:
            self.error(
                "Asset",
                "Asset not found.",
            )
            self.reject()
            return

        self.set_form_data(asset)

    def validate(self):

        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["asset_name"],
                "Asset Name",
            ),
        ):
            self.ui.txtAssetName.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["category"],
                "Category",
            ),
        ):
            self.ui.cmbCategory.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["status"],
                "Status",
            ),
        ):
            self.ui.cmbStatus.setFocus()
            return False

        if self.ui.dtWarrantyExpiry.date() < self.ui.dtPurchaseDate.date():
            self.warning(
                "Validation",
                "Warranty Expiry cannot be earlier than Purchase Date.",
            )
            self.ui.dtWarrantyExpiry.setFocus()
            return False

        return True

    def save(self):

        data = self.get_form_data()

        if self.is_add:
            AssetService.create(data)
        else:
            AssetService.update(
                self.record_id,
                data,
            )
