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
from app.dialogs.work_order_dialog import (
            WorkOrderDialog
)
from app.helpers.format_helper import FormatHelper
from app.core.permissions import Permissions
from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)


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

        self.resize(700, 700)

        self.setMinimumSize(
            700,
            700,
        )

        self.setMaximumWidth(
            900
        )

        self.apply_form_standards()
        self._loading_record = False
        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.load_assets()
        self.configure_widgets()
        self.connect_signals()
        self.update_frequency_mode()

        TableHelper.setup(
            self.ui.tblHistory,
            self.HISTORY_COLUMNS
        )

        self.ui.tblHistory.setEnabled(False)

    def configure_widgets(self):

        self.set_read_only(
            self.ui.txtPMNumber
        )

        self.ui.dtLastService.setCalendarPopup(True)
        self.ui.dtNextDue.setCalendarPopup(True)

        # Next Due is calculated by the application.
        self.ui.dtNextDue.setReadOnly(True)

        self.ui.spnFrequencyValue.setMinimum(1)
        self.ui.spnFrequencyValue.setMaximum(999999)

        self.ui.dsbEstimatedHours.setDecimals(2)
        self.ui.dsbEstimatedHours.setMinimum(0.00)
        self.ui.dsbEstimatedHours.setMaximum(999999.99)

        self.ui.dsbEstimatedCost.setDecimals(2)
        self.ui.dsbEstimatedCost.setMinimum(0.00)
        self.ui.dsbEstimatedCost.setMaximum(999999999.99)

        # Calculated by the application.
        self.ui.dsbNextDueMeter.setReadOnly(True)

        blank_date = QDate(2000, 1, 1)

        self.ui.dtLastService.setMinimumDate(
            blank_date
        )

        self.ui.dtNextDue.setMinimumDate(
            blank_date
        )

        self.ui.dtLastService.setSpecialValueText(
            ""
        )

        self.ui.dtNextDue.setSpecialValueText(
            ""
        )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.cmbFrequencyType.currentTextChanged.connect(
            self.update_frequency_mode
        )

        self.ui.spnFrequencyValue.valueChanged.connect(
            self.calculate_next_due_meter
        )

        self.ui.dsbLastServiceMeter.valueChanged.connect(
            self.calculate_next_due_meter
        )

        self.ui.dtLastService.dateChanged.connect(
            self.calculate_next_due
        )

        self.ui.tblHistory.itemDoubleClicked.connect(
            self.open_history_work_order
        )

        self.ui.cmbAsset.currentIndexChanged.connect(
            self.load_latest_asset_meter
        )

        self.ui.cmbFrequencyType.currentIndexChanged.connect(
            self.load_latest_asset_meter
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

        self.ui.cmbMeterType.setCurrentIndex(-1)
        self.ui.dsbLastServiceMeter.setValue(0.00)
        self.ui.dsbLastServiceMeter.setReadOnly(False)
        self.ui.dsbNextDueMeter.setValue(0.00)
        self.ui.dsbNextDueMeter.setReadOnly(False)

        self.ui.dsbEstimatedHours.setValue(0.00)
        self.ui.dsbEstimatedCost.setValue(0.00)

        self.ui.cmbPriority.setCurrentText(
            "Medium"
        )

        self.ui.chkActive.setChecked(True)

        self.update_frequency_mode()

        self.calculate_next_due()

        self.set_focus(
            self.ui.txtTask
        )

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.tabWidget.setTabEnabled(
            1,
            False
        )

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):

        frequency_type = (
            self.ui.cmbFrequencyType.currentText().strip()
        )

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        is_meter_based = (
            frequency_type in meter_types
        )

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
                frequency_type,

            "frequency_value":
                self.ui.spnFrequencyValue.value(),

            #---------------------------------------------------------
            # Calendar-based scheduling
            #---------------------------------------------------------

            "last_service_date":
                (
                    None
                    if is_meter_based
                    else self.ui.dtLastService.date().toString(
                        "yyyy-MM-dd"
                    )
                ),

            "next_due_date":
                (
                    None
                    if is_meter_based
                    else self.ui.dtNextDue.date().toString(
                        "yyyy-MM-dd"
                    )
                ),

            #---------------------------------------------------------
            # Meter-based scheduling
            #---------------------------------------------------------

            "meter_type":
                (
                    frequency_type
                    if is_meter_based
                    else None
                ),

            "last_service_meter":
                (
                    self.ui.dsbLastServiceMeter.value()
                    if is_meter_based
                    else None
                ),

            "next_due_meter":
                (
                    self.ui.dsbNextDueMeter.value()
                    if is_meter_based
                    else None
                ),

            #---------------------------------------------------------
            # Estimates
            #---------------------------------------------------------

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

        self._loading_record = True

        try:
            self.ui.txtPMNumber.setText(
                pm["pm_number"]
            )

            # Set asset early
            asset_index = self.ui.cmbAsset.findData(
                pm["asset_id"]
            )

            if asset_index >= 0:
                self.ui.cmbAsset.setCurrentIndex(
                    asset_index
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

            meter_type = (
                pm["meter_type"]
                or pm["frequency_type"]
                or ""
            )

            self.ui.cmbMeterType.setCurrentText(
                meter_type
            )

            self.ui.dsbLastServiceMeter.setValue(
                float(
                    pm["last_service_meter"] 
                    or 0
                )
            )

            self.ui.dsbNextDueMeter.setValue(
                float(
                    pm["next_due_meter"]
                    or 0
                )
            )

            # Existing PM service milestone must not be
            # changed manually

            self.ui.dsbLastServiceMeter.setReadOnly(
                True
            )

            self.ui.dsbNextDueMeter.setReadOnly(
                True
            )

            self.ui.dsbEstimatedHours.setValue(
                float(
                    pm["estimated_hours"]
                    or 0
                )
            )

            self.ui.dsbEstimatedCost.setValue(
                float(
                    pm["estimated_cost"]
                    or 0
                )
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

            self.update_frequency_mode()

        finally:
            self._loading_record = False

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

        self.ui.tabWidget.setTabEnabled(
            1,
            True
        )

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.groupHistory.setEnabled(True)
        self.ui.tblHistory.setEnabled(True)
        self.load_history()

        self.update_frequency_mode()

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

        if (
            frequency_type
            not in PreventiveMaintenanceService.METER_FREQUENCY_TYPES
        ):

            return

        frequency_value = (
            self.ui.spnFrequencyValue.value()
        )

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

    def set_pm_read_only(
        self,
        read_only=True
    ):
        # ---------------------------------------------------------
        # Text fields
        # ---------------------------------------------------------

        self.ui.txtPMNumber.setReadOnly(
            True
        )

        self.ui.txtTask.setReadOnly(
            read_only
        )

        self.ui.teDescription.setReadOnly(
            read_only
        )

        self.ui.teNotes.setReadOnly(
            read_only
        )

        # ---------------------------------------------------------
        # Combo boxes
        # ---------------------------------------------------------

        self.ui.cmbAsset.setEnabled(
            not read_only
        )

        self.ui.cmbFrequencyType.setEnabled(
            not read_only
        )

        self.ui.cmbPriority.setEnabled(
            not read_only
        )

        # ---------------------------------------------------------
        # Frequency
        # ---------------------------------------------------------

        self.ui.spnFrequencyValue.setReadOnly(
            read_only
        )

        # ---------------------------------------------------------
        # Dates
        # ---------------------------------------------------------

        self.ui.dtLastService.setEnabled(
            not read_only
        )

        # Next Due is always calculated/read-only.
        self.ui.dtNextDue.setReadOnly(
            True
        )

        self.ui.cmbMeterType.setEnabled(
            not read_only
        )

        self.ui.dsbLastServiceMeter.setReadOnly(
            read_only
        )

        self.ui.dsbNextDueMeter.setReadOnly(
            True
        )

        # ---------------------------------------------------------
        # Estimated values
        # ---------------------------------------------------------

        self.ui.dsbEstimatedHours.setReadOnly(
            read_only
        )

        self.ui.dsbEstimatedCost.setReadOnly(
            read_only
        )

        # ---------------------------------------------------------
        # Active
        # ---------------------------------------------------------

        self.ui.chkActive.setEnabled(
            not read_only
        )

        # ---------------------------------------------------------
        # Save button
        # ---------------------------------------------------------

        save_button = self.ui.buttonBox.button(
            self.ui.buttonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setVisible(
                not read_only
            )

        #----------------------------------------------------------
        # Dialog title
        # ---------------------------------------------------------

        if read_only:
            self.setWindowTitle(
                "View Preventive Maintenance"
            )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):

        data = self.get_form_data()

        try:
            PreventiveMaintenanceService.validate(
                data
            )

        except ValueError as error:
            self.warning(
                "Preventive Maintenance",
                str(error)
            )
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            self.record_id = (
                PreventiveMaintenanceService.create(data)
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

        self.ui.tblHistory.selectRow(
            row
        )

        id_item = self.ui.tblHistory.item(
            row,
            0
        )

        if id_item is None:
            return

        work_order_id = id_item.data(
            Qt.ItemDataRole.UserRole
        )

        if work_order_id is None:
            return

        main_window = self.window()

        user = getattr(
            main_window,
            "user",
            {}
        )

        role = user.get(
            "role",
            ""
        )

        dialog = WorkOrderDialog(
            self
        )

        dialog.edit_record(
            work_order_id
        )

        # Read-only when the user cannot edit Work Orders.
        if not Permissions.has_permission(
            role,
            "work_orders.edit"
        ):
            dialog.set_work_order_read_only(
                True
            )

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

    def update_frequency_mode(self):

        frequency_type = (
            self.ui.cmbFrequencyType.currentText().strip()
        )

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        is_meter_based = (
            frequency_type in meter_types
        )

        # -------------------------------------------------
        # Calendar fields
        # -------------------------------------------------

        self.ui.dtLastService.setEnabled(
            not is_meter_based
        )

        self.ui.dtNextDue.setEnabled(
            not is_meter_based
        )

        # -------------------------------------------------
        # Meter fields
        # -------------------------------------------------

        self.ui.cmbMeterType.setEnabled(
            is_meter_based
        )

        self.ui.dsbLastServiceMeter.setEnabled(
            is_meter_based
        )

        self.ui.dsbNextDueMeter.setEnabled(
            is_meter_based
        )

        # -------------------------------------------------
        # Meter-based PM
        # -------------------------------------------------

        if is_meter_based:
            index = self.ui.cmbMeterType.findText(
                frequency_type
            )

            if index >= 0:
                self.ui.cmbMeterType.setCurrentIndex(
                    index
                )

            if not self._loading_record:
                self.calculate_next_due_meter()

            else:

                self.ui.cmbMeterType.setCurrentIndex(
                    -1
                )

            if not self._loading_record:
                self.calculate_next_due()

        # -------------------------------------------------
        # Calendar-based PM
        # -------------------------------------------------

        else:

            self.ui.cmbMeterType.setCurrentIndex(
                -1
            )

            self.calculate_next_due()

    def calculate_next_due_meter(self, *_args):

        frequency_type = (
            self.ui.cmbFrequencyType.currentText().strip()
        )

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        if frequency_type not in meter_types:
            return

        frequency_value = (
            self.ui.spnFrequencyValue.value()
        )

        last_service_meter = (
            self.ui.dsbLastServiceMeter.value()
        )

        next_due_meter = (
            last_service_meter
            + frequency_value
        )

        self.ui.dsbNextDueMeter.setValue(
            next_due_meter
        )

    def load_latest_asset_meter(self):

        if self._loading_record:
            return

        # Do not overwrite stored values when editing
        # an existing PM schedule.
        if self.record_id is not None:
            return

        frequency_type = (
            self.ui.cmbFrequencyType
            .currentText()
            .strip()
        )

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        if frequency_type not in meter_types:
            return

        asset_id = self.ui.cmbAsset.currentData()

        if asset_id is None:
            return

        latest_meter = (
            AssetMeterReadingService.get_latest_reading_value(
                asset_id,
                frequency_type
            )
        )

        # ---------------------------------------------
        # No meter history
        # ---------------------------------------------

        if latest_meter is None:

            self.ui.dsbLastServiceMeter.setReadOnly(
                False
            )

            self.ui.dsbLastServiceMeter.setValue(
                0.00
            )

            self.calculate_next_due_meter()

            return

        # ---------------------------------------------
        # Existing meter history
        # ---------------------------------------------

        self.ui.dsbLastServiceMeter.setValue(
            latest_meter
        )

        self.ui.dsbLastServiceMeter.setReadOnly(
            True
        )

        self.calculate_next_due_meter()