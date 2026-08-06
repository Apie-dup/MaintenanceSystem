from tkinter import dialog

from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QColor

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
from app.helpers.table_helper import TableHelper
from app.services.work_order_service import WorkOrderService
from app.helpers.form_helper import FormHelper


class PreventiveMaintenanceDialog(BaseDialog):

    ENTITY_NAME = "Preventive Maintenance"

    HISTORY_COLUMNS = [
        ("work_order_number", "Work Order"),
        ("date_created", "Created"),
        ("due_date", "Due Date"),
        ("status", "Status"),
        ("technician_display", "Technician"),
        ("labour_hours", "Hours"),
        ("actual_cost", "Actual Cost"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PreventiveMaintenanceDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()
        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.load_assets()
        self.configure_widgets()
        self.connect_signals()

        TableHelper.setup(
            self.ui.tblHistory,
            self.HISTORY_COLUMNS
        )

        self.ui.tblHistory.setEnabled(False)

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

        self.ui.tblHistory.itemDoubleClicked.connect(
            self.open_history_work_order
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

        self.ui.groupHistory.setEnabled(True)
        self.ui.tblHistory.setEnabled(True)
        self.load_history()

    def load_history(self):
        if self.record_id is None:
            return

        records = WorkOrderService.get_by_pm_id(self.record_id)

        TableHelper.populate(
            self.ui.tblHistory,
            records,
            self.HISTORY_COLUMNS
        )

        self.format_history_values()

        self.apply_history_highlighting()
        self.ui.tblHistory.clearSelection()

    def format_history_values(self):
        from app.helpers.format_helper import FormatHelper
        cost_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "actual_cost"
            ),
            None
        )

        hours_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "labour_hours"
            ),
            None
        )

        for row in range(self.ui.tblHistory.rowCount()):
            if cost_column is not None:
                item = self.ui.tblHistory.item(
                    row,
                    cost_column
                )

                if item is not None:
                    try:
                        item.setText(
                            FormatHelper.currency(
                                float(item.text() or 0)
                            )
                        )
                    except ValueError:
                        pass

            if hours_column is not None:
                item = self.ui.tblHistory.item(
                    row,
                    hours_column
                )
                if item is not None:
                    try:
                        item.setText(
                            FormatHelper.quantity(
                                float(item.text() or 0)
                            )
                        )
                    except ValueError:
                        pass

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
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["task"],
                "Task"
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["frequency_type"],
                "Frequency Type"
            )
        ):
            return False

        if data["frequency_value"] <= 0:
            self.warning(
                "Validation",
                "Frequency Value must be greater than zero."
            )
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["priority"],
                "Priority"
            )
        ):
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

    def open_history_work_order(self, item):
        row = item.row()

        if row < 0:
            return

        self.ui.tblHistory.selectRow(row)

        id_item = self.ui.tblHistory.item(row, 0)

        if id_item is None:
            return

        work_order_id = id_item.data(Qt.ItemDataRole.UserRole)

        if work_order_id is None:
            return

        from app.dialogs.work_order_dialog import (
            WorkOrderDialog
        )

        dialog = WorkOrderDialog(self)
        dialog.edit_record(work_order_id)

        if dialog.exec():
            self.load_history()

    def apply_history_highlighting(self):
        status_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "status"
            ),
            None
        )

        if status_column is None:
            return

        for row in range(self.ui.tblHistory.rowCount()):
            status_item = self.ui.tblHistory.item(
                row,
                status_column
            )

            if status_item is None:
                continue

            status = status_item.text().strip()

            if status in {"Completed", "Closed"}:
                background = QColor(220, 245, 225)
                tooltip = "Maintenance work completed."

            elif status == "In Progress":
                background = QColor(220, 235, 255)
                tooltip = "Maintenance work is in progress."

            elif status == "On Hold":
                background = QColor(255, 240, 205)
                tooltip = "Maintenance work is currently on hold."

            elif status == "Cancelled":
                background = QColor(235, 235, 235)
                tooltip = "This work order was cancelled."

            else:
                continue

            for column in range(
                self.ui.tblHistory.columnCount()
            ):
                item = self.ui.tblHistory.item(row, column)

                if item is not None:
                    item.setBackground(background)
                    item.setToolTip(tooltip)

        for column in range(
            self.ui.tblHistory.columnCount()
        ):
            item = self.ui.tblHistory.item(row, column)

            if item is not None:
                item.setBackground(background)
                item.setToolTip(tooltip)