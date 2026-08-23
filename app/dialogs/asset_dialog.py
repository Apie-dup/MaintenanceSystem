from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QFormLayout, QSizePolicy

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

        self.setSizeGripEnabled(True)
        
        self.setSizePolicy(
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Expanding,
        )

        self.apply_form_standards()
        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.connect_signals()
        self.configure_layout()

        self.set_read_only(
            self.ui.txtAssetCode
        )

    def configure_layout(self):
        self.setWindowFlag(
            Qt.WindowType.WindowMaximizeButtonHint,
            True,
        )

        

        for layout_name in (
            "formGeneralInfo",
            "formLocation",
            "formManufacturer",
            "formPurchaseInfo",
        ):
            form_layout = getattr(
                self.ui,
                layout_name,
                None,
            )

            if form_layout is not None:
                form_layout.setFieldGrowthPolicy(
                    QFormLayout.FieldGrowthPolicy
                    .AllNonFixedFieldsGrow
                )

    # ---------------------------------------------------------
    # Lookups
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtAssetCode.setText(
            AssetService.get_next_asset_number()
        )

        self.ui.txtAssetName.clear()
        self.ui.txtDescription.clear()
        self.ui.txtManufacturer.clear()
        self.ui.txtModel.clear()
        self.ui.txtSerialNumber.clear()

        if self.ui.cmbCategory.count() > 0:
            self.ui.cmbCategory.setCurrentIndex(0)

        if self.ui.cmbLocation.count() > 0:
            self.ui.cmbLocation.setCurrentIndex(0)

        self.ui.cmbStatus.setCurrentText(
            "Active"
        )

        self.ui.txtNotes.clear()

        today = QDate.currentDate()

        self.ui.dtPurchaseDate.setDate(today)
        self.ui.dtWarrantyExpiry.setDate(today)

        self.ui.dsbPurchaseCost.setValue(
            0.00
        )

        self.set_focus(
            self.ui.txtAssetName
        )

    # ---------------------------------------------------------
    # Data mapping
    # ---------------------------------------------------------
    def get_form_data(self):
        return {
            "asset_number":
                self.ui.txtAssetCode.text().strip(),

            "asset_name":
                self.ui.txtAssetName.text().strip(),

            "description":
                self.ui.txtDescription.text().strip(),

            "category":
                self.ui.cmbCategory.currentText().strip(),

            "location":
                self.ui.cmbLocation.currentText().strip(),

            "manufacturer":
                self.ui.txtManufacturer.text().strip(),

            "model":
                self.ui.txtModel.text().strip(),

            "serial_number":
                self.ui.txtSerialNumber.text().strip(),

            "purchase_date":
                self.ui.dtPurchaseDate.date().toString(
                    "yyyy-MM-dd"
                ),

            "purchase_cost":
                self.ui.dsbPurchaseCost.value(),

            "warranty_expiry":
                self.ui.dtWarrantyExpiry.date().toString(
                    "yyyy-MM-dd"
                ),

            "status":
                self.ui.cmbStatus.currentText().strip(),

            "notes":
                self.ui.txtNotes.toPlainText().strip(),
        }

    def set_form_data(self, asset):
        self.ui.txtAssetCode.setText(
            asset["asset_number"] or ""
        )

        self.ui.txtAssetName.setText(
            asset["asset_name"] or ""
        )

        self.ui.txtDescription.setText(
            asset["description"] or ""
        )

        self.ui.cmbCategory.setCurrentText(
            asset["category"] or ""
        )

        self.ui.cmbLocation.setCurrentText(
            asset["location"] or ""
        )

        self.ui.txtManufacturer.setText(
            asset["manufacturer"] or ""
        )

        self.ui.txtModel.setText(
            asset["model"] or ""
        )

        self.ui.txtSerialNumber.setText(
            asset["serial_number"] or ""
        )

        self.ui.cmbStatus.setCurrentText(
            asset["status"] or "Active"
        )

        self.ui.txtNotes.setPlainText(
            asset["notes"] or ""
        )

        self.set_date_value(
            self.ui.dtPurchaseDate,
            asset["purchase_date"],
        )

        self.ui.dsbPurchaseCost.setValue(
            float(
                asset["purchase_cost"]
                or 0
            )
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

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):
        asset = AssetService.get_by_id(
            record_id
        )

        if asset is None:
            self.error(
                "Asset",
                "Asset not found.",
            )
            self.reject()
            return

        self.set_form_data(asset)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["asset_name"],
                "Asset Name",
            ),
        ):
            self.set_focus(
                self.ui.txtAssetName
            )
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

        if (
            self.ui.dtWarrantyExpiry.date()
            < self.ui.dtPurchaseDate.date()
        ):
            self.warning(
                "Validation",
                (
                    "Warranty Expiry cannot be earlier "
                    "than Purchase Date."
                ),
            )

            self.ui.dtWarrantyExpiry.setFocus()
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            self.record_id = AssetService.create(data)
        else:
            AssetService.update(
                self.record_id,
                data,
            )

    def set_asset_read_only(
        self,
        read_only=True
    ):

        # ---------------------------------------------
        # Text fields
        # ---------------------------------------------

        self.ui.txtAssetName.setReadOnly(
            read_only
        )

        self.ui.txtDescription.setReadOnly(
            read_only
        )

        self.ui.txtManufacturer.setReadOnly(
            read_only
        )

        self.ui.txtModel.setReadOnly(
            read_only
        )

        self.ui.txtSerialNumber.setReadOnly(
            read_only
        )

        self.ui.txtNotes.setReadOnly(
            read_only
        )

        # Asset code is always read-only
        self.ui.txtAssetCode.setReadOnly(
            True
        )

        # ---------------------------------------------
        # Comboboxes
        # ---------------------------------------------

        self.ui.cmbCategory.setEnabled(
            not read_only
        )

        self.ui.cmbLocation.setEnabled(
            not read_only
        )

        self.ui.cmbStatus.setEnabled(
            not read_only
        )

        # ---------------------------------------------
        # Dates and cost
        # ---------------------------------------------

        self.ui.dtPurchaseDate.setEnabled(
            not read_only
        )

        self.ui.dtWarrantyExpiry.setEnabled(
            not read_only
        )

        self.ui.dsbPurchaseCost.setReadOnly(
            read_only
        )

        # ---------------------------------------------
        # Save button
        # ---------------------------------------------

        save_button = (
            self.ui.buttonBox.button(
                self.ui.buttonBox
                .StandardButton.Save
            )
        )

        if save_button is not None:
            save_button.setVisible(
                not read_only
            )

        if read_only:
            self.setWindowTitle(
                "View Asset"
            )