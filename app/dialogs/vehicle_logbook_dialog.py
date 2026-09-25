from PySide6.QtCore import QDate

from app.base.base_dialog import BaseDialog
from app.services.asset_service import AssetService
from app.services.vehicle_logbook_service import (
    VehicleLogbookService
)
from app.ui.generated.ui_vehicle_logbook_dialog import (
    Ui_VehicleLogbookDialog
)
from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)


class VehicleLogbookDialog(BaseDialog):

    ENTITY_NAME = "Vehicle Logbook Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_VehicleLogbookDialog()
        self.ui.setupUi(self)

        self.record_id = None
        self.user = None

        if parent is not None:
            self.user = getattr(
                parent,
                "user",
                None
            )

        self.configure_widgets()
        self.load_assets()
        self.connect_signals()

    def configure_widgets(self):

        self.ui.dtLogDate.setDate(
            QDate.currentDate()
        )

        self.ui.dsbDistance.setReadOnly(
            True
        )

        self.ui.dsbHoursUsed.setReadOnly(
            True
        )

    def connect_signals(self):

        self.ui.cmbAsset.currentIndexChanged.connect(
            self.load_latest_meter
        )

        self.ui.dsbStartMeter.valueChanged.connect(
            self.calculate_distance
        )

        self.ui.dsbEndMeter.valueChanged.connect(
            self.calculate_distance
        )

        self.ui.dsbStartHours.valueChanged.connect(
            self.calculate_hours
        )

        self.ui.dsbEndHours.valueChanged.connect(
            self.calculate_hours
        )

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    def load_latest_meter(self):

        asset_id = (
            self.ui.cmbAsset.currentData()
        )

        if asset_id is None:
            self.ui.dsbStartMeter.setValue(0)
            self.ui.dsbEndMeter.setValue(0)
            self.ui.dsbDistance.setValue(0)

            self.ui.dsbStartHours.setValue(0)
            self.ui.dsbEndHours.setValue(0)
            self.ui.dsbHoursUsed.setValue(0)

            return

        # -------------------------------------------------
        # Kilometers
        # -------------------------------------------------

        latest_kilometers = (
            AssetMeterReadingService
            .get_latest_reading_value(
                asset_id,
                "Kilometers"
            )
        )

        if latest_kilometers is None:
            latest_kilometers = 0

        self.ui.dsbStartMeter.setValue(
            latest_kilometers
        )

        self.ui.dsbEndMeter.setValue(
            latest_kilometers
        )

        self.calculate_distance()

        # -------------------------------------------------
        # Running Hours
        # -------------------------------------------------

        latest_hours = (
            AssetMeterReadingService
            .get_latest_reading_value(
                asset_id,
                "Running Hours"
            )
        )

        if latest_hours is None:
            latest_hours = 0

        self.ui.dsbStartHours.setValue(
            latest_hours
        )

        self.ui.dsbEndHours.setValue(
            latest_hours
        )

        self.calculate_hours()

    def load_assets(self):

        self.ui.cmbAsset.clear()

        self.ui.cmbAsset.addItem(
            "Select Vehicle",
            None
        )

        assets = AssetService.get_all()

        for asset in assets:

            label = (
                f"{asset['asset_number']} - "
                f"{asset['asset_name']}"
            )

            self.ui.cmbAsset.addItem(
                label,
                asset["id"]
            )

    def new_record(self):

        self.record_id = None

        self.setWindowTitle(
            f"Add {self.ENTITY_NAME}"
        )

        self.clear_fields()

    def edit_record(self, record_id):

        self.record_id = record_id

        self.setWindowTitle(
            f"Edit {self.ENTITY_NAME}"
        )

        self.load_record()

    def clear_fields(self):

        self.ui.cmbAsset.setCurrentIndex(0)

        self.ui.dtLogDate.setDate(
            QDate.currentDate()
        )

        self.ui.txtDriver.clear()
        self.ui.txtFrom.clear()
        self.ui.txtTo.clear()
        self.ui.txtPurpose.clear()
        self.ui.teDefectReported.clear()

        self.ui.dsbStartMeter.setValue(0)
        self.ui.dsbEndMeter.setValue(0)
        self.ui.dsbDistance.setValue(0)

        self.ui.dsbStartHours.setValue(0)
        self.ui.dsbEndHours.setValue(0)
        self.ui.dsbHoursUsed.setValue(0)

        self.ui.dsbFuelQuantity.setValue(0)
        self.ui.dsbFuelCost.setValue(0)

        self.ui.txtNotes.clear()

    def calculate_distance(self):

        start_meter = (
            self.ui.dsbStartMeter.value()
        )

        end_meter = (
            self.ui.dsbEndMeter.value()
        )

        distance = max(
            0,
            end_meter - start_meter
        )

        self.ui.dsbDistance.setValue(
            distance
        )

    def calculate_hours(self):

        start_hours = (
            self.ui.dsbStartHours.value()
        )

        end_hours = (
            self.ui.dsbEndHours.value()
        )

        hours_used = max(
            0,
            end_hours - start_hours
        )

        self.ui.dsbHoursUsed.setValue(
            hours_used
        )

    def get_form_data(self):

        return {
            "asset_id":
                self.ui.cmbAsset.currentData(),

            "log_date":
                self.ui.dtLogDate.date()
                .toString("yyyy-MM-dd"),

            "driver_name":
                self.ui.txtDriver.text().strip(),

            "start_meter":
                self.ui.dsbStartMeter.value(),

            "end_meter":
                self.ui.dsbEndMeter.value(),

            "start_hours": (
                self.ui.dsbStartHours.value()
                if (
                        self.ui.dsbStartHours.value() > 0
                        or self.ui.dsbEndHours.value() > 0
                    )
                    else None
            ),

            "end_hours": (
                self.ui.dsbEndHours.value()
                if (
                    self.ui.dsbStartHours.value() > 0
                    or self.ui.dsbEndHours.value() > 0
                )
                else None
            ),

            "origin":
                self.ui.txtFrom.text().strip(),

            "destination":
                self.ui.txtTo.text().strip(),

            "purpose":
                self.ui.txtPurpose.text().strip(),

            "defect_reported":
                self.ui.teDefectReported.toPlainText().strip(),

            "fuel_quantity":
                self.ui.dsbFuelQuantity.value(),

            "fuel_cost":
                self.ui.dsbFuelCost.value(),

            "notes":
                self.ui.txtNotes
                .toPlainText()
                .strip(),
        }

    def save_and_close(self):

        data = self.get_form_data()

        if data["asset_id"] is None:
            self.warning(
                "Validation",
                "Please select a vehicle."
            )
            return

        if (
            data["end_meter"]
            < data["start_meter"]
        ):
            self.warning(
                "Validation",
                "End km cannot be less than Start km."
            )
            return

        if (
            data["end_hours"]
            < data["start_hours"]
        ):
            self.warning(
                "Validation",
                "End Hours cannot be less than Start Hours."
            )
            return

        try:

            if self.record_id is None:

                VehicleLogbookService.create(
                    data,
                    user=self.user,
                )

            else:

                VehicleLogbookService.update(
                    self.record_id,
                    data,
                )

            self.accept()

        except ValueError as error:

            self.warning(
                "Validation",
                str(error)
            )

        except Exception as error:

            self.warning(
                "Vehicle Logbook",
                (
                    "Unable to save logbook entry."
                    f"\n\n{error}"
                )
            )

    def load_record(self):

        record = (
            VehicleLogbookService.get_by_id(
                self.record_id
            )
        )

        if not record:
            return

        index = self.ui.cmbAsset.findData(
            record["asset_id"]
        )

        if index >= 0:
            self.ui.cmbAsset.setCurrentIndex(
                index
            )

        self.ui.dtLogDate.setDate(
            QDate.fromString(
                record["log_date"],
                "yyyy-MM-dd"
            )
        )

        self.ui.txtDriver.setText(
            record["driver_name"] or ""
        )

        self.ui.txtFrom.setText(
            record["origin"] or ""
        )

        self.ui.txtTo.setText(
            record["destination"] or ""
        )

        self.ui.txtPurpose.setText(
            record["purpose"] or ""
        )

        self.ui.teDefectReported.setPlainText(
            record["defect_reported"] or ""
        )

        self.ui.dsbStartMeter.setValue(
            float(record["start_meter"] or 0)
        )

        self.ui.dsbEndMeter.setValue(
            float(record["end_meter"] or 0)
        )

        self.ui.dsbStartHours.setValue(
            float(record["start_hours"] or 0)
        )

        self.ui.dsbEndHours.setValue(
            float(record["end_hours"] or 0)
        )

        self.ui.dsbFuelQuantity.setValue(
            float(record["fuel_quantity"] or 0)
        )

        self.ui.dsbFuelCost.setValue(
            float(record["fuel_cost"] or 0)
        )

        self.ui.txtNotes.setPlainText(
            record["notes"] or ""
        )

        self.calculate_distance()
        self.calculate_hours()