from PySide6.QtCore import QDate

from app.base.base_dialog import BaseDialog
from app.core.lookup_manager import LookupManager
from app.helpers.date_helper import DateHelper
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)
from app.services.validation_service import ValidationService
from app.ui.generated.ui_add_pm_dialog import (
    Ui_PreventiveMaintenanceDialog
)


class PreventiveMaintenanceDialog(BaseDialog):

    ENTITY_NAME = "Preventive Maintenance"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PreventiveMaintenanceDialog()
        self.ui.setupUi(self)

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.load_assets()
        self.configure_widgets()
        self.connect_signals()

    def configure_widgets(self):
        self.ui.txtPMNumber.setReadOnly(True)

        self.ui.dtLastService.setCalendarPopup(True)
        self.ui.dtNextDue.setCalendarPopup(True)

        # Next Due is calculated by the application.
        self.ui.dtNextDue.setReadOnly(True)

        self.ui.spnFrequencyValue.setMinimum(1)
        self.ui.spnFrequencyValue.setMaximum(9999)

        self.ui.dsbEstimatedHours.setDecimals(2)
        self.ui.dsbEstimatedHours.setMinimum(0.00)
        self.ui.dsbEstimatedHours.setMaximum(999999.99)

        self.ui.dsbEstimatedCost.setDecimals(2)
        self.ui.dsbEstimatedCost.setMinimum(0.00)
        self.ui.dsbEstimatedCost.setMaximum(999999999.99)

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.cmbFrequencyType.currentTextChanged.connect(
            self.calculate_next_due
        )

        self.ui.spnFrequencyValue.valueChanged.connect(
            self.calculate_next_due
        )

        self.ui.dtLastService.dateChanged.connect(
            self.calculate_next_due
        )

    # ---------------------------------------------------------
    # Lookups
    # ---------------------------------------------------------

    def load_lookup_values(self):
        LookupManager.load(
            self.ui.cmbFrequencyType,
            "Frequency Types"
        )

        LookupManager.load(
            self.ui.cmbPriority,
            "Priorities"
        )

    def load_assets(self):
        self.ui.cmbAsset.clear()

        assets = PreventiveMaintenanceService.asset_lookup()

        for asset in assets:
            display_text = (
                f'{asset["asset_number"]} - '
                f'{asset["asset_name"]}'
            )

            self.ui.cmbAsset.addItem(
                display_text,
                asset["id"]
            )

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtPMNumber.setText(
            PreventiveMaintenanceService.get_next_pm_number()
        )

        self.ui.txtTask.clear()
        self.ui.teDescription.clear()
        self.ui.teNotes.clear()

        if self.ui.cmbAsset.count() > 0:
            self.ui.cmbAsset.setCurrentIndex(0)

        self.ui.cmbFrequencyType.setCurrentText(
            "Monthly"
        )

        self.ui.spnFrequencyValue.setValue(1)

        today = QDate.currentDate()

        self.ui.dtLastService.setDate(today)

        self.ui.dsbEstimatedHours.setValue(0.00)
        self.ui.dsbEstimatedCost.setValue(0.00)

        self.ui.cmbPriority.setCurrentText(
            "Medium"
        )

        self.ui.chkActive.setChecked(True)

        self.calculate_next_due()

        self.ui.txtTask.setFocus()

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "pm_number":
                self.ui.txtPMNumber.text().strip(),

            "asset_id":
                self.ui.cmbAsset.currentData(),

            "task":
                self.ui.txtTask.text().strip(),

            "description":
                self.ui.teDescription.toPlainText().strip(),

            "frequency_type":
                self.ui.cmbFrequencyType.currentText().strip(),

            "frequency_value":
                self.ui.spnFrequencyValue.value(),

            "last_service_date":
                self.ui.dtLastService.date().toString(
                    "yyyy-MM-dd"
                ),

            "next_due_date":
                self.ui.dtNextDue.date().toString(
                    "yyyy-MM-dd"
                ),

            "estimated_hours":
                self.ui.dsbEstimatedHours.value(),

            "estimated_cost":
                self.ui.dsbEstimatedCost.value(),

            "priority":
                self.ui.cmbPriority.currentText().strip(),

            "active":
                1 if self.ui.chkActive.isChecked() else 0,

            "notes":
                self.ui.teNotes.toPlainText().strip(),
        }

    def set_form_data(self, pm):
        self.ui.txtPMNumber.setText(
            pm["pm_number"]
        )

        self.ui.txtTask.setText(
            pm["task"] or ""
        )

        self.ui.teDescription.setPlainText(
            pm["description"] or ""
        )

        self.ui.cmbFrequencyType.setCurrentText(
            pm["frequency_type"] or ""
        )

        self.ui.spnFrequencyValue.setValue(
            int(pm["frequency_value"] or 1)
        )

        self.set_date_value(
            self.ui.dtLastService,
            pm["last_service_date"]
        )

        self.set_date_value(
            self.ui.dtNextDue,
            pm["next_due_date"]
        )

        self.ui.dsbEstimatedHours.setValue(
            float(pm["estimated_hours"] or 0)
        )

        self.ui.dsbEstimatedCost.setValue(
            float(pm["estimated_cost"] or 0)
        )

        self.ui.cmbPriority.setCurrentText(
            pm["priority"] or ""
        )

        self.ui.chkActive.setChecked(
            bool(pm["active"])
        )

        self.ui.teNotes.setPlainText(
            pm["notes"] or ""
        )

        asset_index = self.ui.cmbAsset.findData(
            pm["asset_id"]
        )

        if asset_index >= 0:
            self.ui.cmbAsset.setCurrentIndex(
                asset_index
            )

    @staticmethod
    def set_date_value(date_widget, value):
        if not value:
            return

        parsed_date = QDate.fromString(
            value,
            "yyyy-MM-dd"
        )

        if parsed_date.isValid():
            date_widget.setDate(parsed_date)

    # ---------------------------------------------------------
    # Load record
    # ---------------------------------------------------------

    def load_record(self, record_id):
        pm = PreventiveMaintenanceService.get_by_id(
            record_id
        )

        if pm is None:
            self.error(
                "Preventive Maintenance",
                "Preventive Maintenance record not found."
            )
            self.reject()
            return

        self.set_form_data(pm)

    # ---------------------------------------------------------
    # Next due calculation
    # ---------------------------------------------------------

    def calculate_next_due(self, *_args):
        frequency_type = (
            self.ui.cmbFrequencyType.currentText().strip()
        )

        frequency_value = (
            self.ui.spnFrequencyValue.value()
        )

        if not frequency_type or frequency_value <= 0:
            return

        last_service_text = (
            self.ui.dtLastService.date().toString(
                "yyyy-MM-dd"
            )
        )

        try:
            last_service = DateHelper.from_string(
                last_service_text
            )

            next_due = DateHelper.calculate_next_due_date(
                last_service,
                frequency_type,
                frequency_value
            )

        except ValueError:
            return

        qt_next_due = QDate.fromString(
            DateHelper.to_string(next_due),
            "yyyy-MM-dd"
        )

        if qt_next_due.isValid():
            self.ui.dtNextDue.setDate(
                qt_next_due
            )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if data["asset_id"] is None:
            self.warning(
                "Validation",
                "Please select an asset."
            )
            self.ui.cmbAsset.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["task"],
                "Task"
            )
        ):
            self.ui.txtTask.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["frequency_type"],
                "Frequency Type"
            )
        ):
            self.ui.cmbFrequencyType.setFocus()
            return False

        if data["frequency_value"] <= 0:
            self.warning(
                "Validation",
                "Frequency Value must be greater than zero."
            )
            self.ui.spnFrequencyValue.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["priority"],
                "Priority"
            )
        ):
            self.ui.cmbPriority.setFocus()
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            PreventiveMaintenanceService.create(
                data
            )
        else:
            PreventiveMaintenanceService.update(
                self.record_id,
                data
            )