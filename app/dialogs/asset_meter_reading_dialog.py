from PySide6.QtCore import QDate, Signal

from app.services.asset_service import AssetService
from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)
from app.ui.generated.ui_asset_meter_reading_dialog import (
    Ui_AssetMeterReadingDialog
)

from app.core.permissions import Permissions

from PySide6.QtWidgets import (
    QDialog,
    QTableWidgetItem,
)


class AssetMeterReadingDialog(QDialog):

    reading_recorded = Signal(int)

    def __init__(
        self,
        asset_id,
        user=None,
        parent=None,
    ):
        super().__init__(parent)

        self.ui = Ui_AssetMeterReadingDialog()
        self.ui.setupUi(self)

        self.asset_id = asset_id
        self.user = user or {}
        self.role = self.user.get(
            "role",
            ""
        )

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):

        self.setWindowTitle(
            "Asset Meter Readings"
        )

        self.ui.dtReadingDate.setDate(
            QDate.currentDate()
        )

        self.apply_permissions()

        self.setup_history_table()

        self.connect_signals()

        self.load_initial_data()

    def load_initial_data(self):  

        self.load_asset()

        self.load_history()

        self.load_latest_meter()

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):

        self.ui.btnRecordReading.clicked.connect(
            self.record_reading
        )

        self.ui.btnClose.clicked.connect(
            self.accept
        )

        self.ui.cmbMeterType.currentTextChanged.connect(
            self.load_latest_meter
        )

    # ---------------------------------------------------------
    # Table
    # ---------------------------------------------------------

    def setup_history_table(self):

        self.ui.tblHistory.setColumnCount(5)

        self.ui.tblHistory.setHorizontalHeaderLabels(
            [
                "Reading Date",
                "Meter Type",
                "Reading",
                "Source",
                "Notes",
            ]
        )

        self.ui.tblHistory.setSelectionBehavior(
            self.ui.tblHistory.SelectionBehavior.SelectRows
        )

        self.ui.tblHistory.setEditTriggers(
            self.ui.tblHistory.EditTrigger.NoEditTriggers
        )

    # ---------------------------------------------------------
    # Asset
    # ---------------------------------------------------------

    def load_asset(self):

        asset = AssetService.get_by_id(
            self.asset_id
        )

        if asset is None:
            self.ui.lblAsset.setText(
                "Asset not found"
            )
            return

        self.ui.lblAsset.setText(
            f'{asset["asset_number"]} - '
            f'{asset["asset_name"]}'
        )

    # ---------------------------------------------------------
    # History
    # ---------------------------------------------------------

    def load_history(self):

        records = (
            AssetMeterReadingService
            .get_history(
                self.asset_id
            )
        )

        self.ui.tblHistory.setRowCount(
            len(records)
        )

        for row, record in enumerate(records):

            reading = float(
                record["reading"] or 0
            )

            source_type = (
                record["source_type"]
                or "Manual"
            )

            work_order_number = (
                record["work_order_number"]
                or ""
            )

            if (
                source_type == "Work Order"
                and work_order_number
            ):

                source_display = work_order_number

            else:
                source_display = source_type

            self.ui.tblHistory.setItem(
                row,
                0,
                QTableWidgetItem(
                    record["reading_date"] or ""
                )
            )

            self.ui.tblHistory.setItem(
                row,
                1,
                QTableWidgetItem(
                    record["meter_type"] or ""
                )
            )

            self.ui.tblHistory.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"{reading:,.2f}"
                )
            )

            self.ui.tblHistory.setItem(
                row,
                3,
                QTableWidgetItem(
                    source_display
                )
            )

            self.ui.tblHistory.setItem(
                row,
                4,
                QTableWidgetItem(
                    record["notes"] or ""
                )
            )

        self.ui.tblHistory.resizeColumnsToContents()

    # ---------------------------------------------------------
    # Latest reading
    # ---------------------------------------------------------

    def load_latest_meter(self, *_args):

        meter_type = (
            self.ui.cmbMeterType
            .currentText()
            .strip()
        )

        if not meter_type:
            return

        latest = (
            AssetMeterReadingService
            .get_latest_reading_value(
                self.asset_id,
                meter_type
            )
        )

        if latest is None:
            self.ui.dsbReading.setValue(
                0.00
            )
            return

        self.ui.dsbReading.setValue(
            float(latest)
        )

    # ---------------------------------------------------------
    # Record reading
    # ---------------------------------------------------------

    def record_reading(self):

        meter_type = (
            self.ui.cmbMeterType
            .currentText()
            .strip()
        )

        reading = (
            self.ui.dsbReading.value()
        )

        reading_date = (
            self.ui.dtReadingDate
            .date()
            .toString(
                "yyyy-MM-dd"
            )
        )

        notes = (
            self.ui.teNotes
            .toPlainText()
            .strip()
        )

        if not meter_type:
            self.warning(
                "Meter Reading",
                "Please select a Meter Type."
            )
            return

        latest = (
            AssetMeterReadingService
            .get_latest_reading_value(
                self.asset_id,
                meter_type
            )
        )

        if (
            latest is not None
            and reading <= latest
        ):
            self.warning(
                "Meter Reading",
                (
                    "The new meter reading must be greater "
                    "than the current reading.\n\n"
                    f"Current reading: {latest:,.2f}"
                )
            )
            return
        
        try:
            AssetMeterReadingService.add_reading(
                asset_id=self.asset_id,
                meter_type=meter_type,
                reading=reading,
                reading_date=reading_date,
                notes=notes or None,
            )

            self.reading_recorded.emit(
                self.asset_id
            )

        except ValueError as error:
            self.warning(
                "Meter Reading",
                str(error)
            )
            return

        except Exception as error:
            self.warning(
                "Meter Reading",
                (
                    "Could not record the meter reading."
                    f"\n\n{error}"
                )
            )
            return

        self.ui.teNotes.clear()

        self.load_history()

        self.load_latest_meter()

        self.information(
            "Meter Reading",
            "Meter reading recorded successfully."
        )

        

    # ---------------------------------------------------------
    # Messages
    # ---------------------------------------------------------

    def warning(
        self,
        title,
        message,
    ):
        from PySide6.QtWidgets import QMessageBox

        QMessageBox.warning(
            self,
            title,
            message,
        )

    def information(
        self,
        title,
        message,
    ):
        from PySide6.QtWidgets import QMessageBox

        QMessageBox.information(
            self,
            title,
            message,
        )

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "asset_meter_readings.create"
        )

        for widget in (
            self.ui.cmbMeterType,
            self.ui.dsbReading,
            self.ui.dtReadingDate,
            self.ui.teNotes,
            self.ui.btnRecordReading,
        ):
            widget.setEnabled(
                can_create
            )
        

    def record_reading(self):

        if not Permissions.has_permission(
            self.role,
            "asset_meter_readings.create"
        ):
            self.warning(
                "Meter Reading",
                "You do not have permission "
                "to record meter readings."
            )
            return