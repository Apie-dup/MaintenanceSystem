from app.base.base_dialog import BaseDialog
from app.services.asset_service import AssetService
from app.services.vehicle_sop_service import (
    VehicleSopService
)
from app.ui.generated.ui_vehicle_sop_dialog import (
    Ui_VehicleSopDialog
)


class VehicleSopDialog(BaseDialog):

    ENTITY_NAME = "Vehicle SOP"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_VehicleSopDialog()
        self.ui.setupUi(self)

        self.record_id = None

        self.configure_widgets()
        self.load_assets()
        self.load_frequencies()
        self.connect_signals()

    def configure_widgets(self):

        self.ui.txtSopNumber.setReadOnly(
            True
        )

    def connect_signals(self):

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    def load_assets(self):

        self.ui.cmbAsset.clear()

        self.ui.cmbAsset.addItem(
            "Select Vehicle / Asset",
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

    def load_frequencies(self):

        self.ui.cmbFrequency.clear()

        for frequency in (
            VehicleSopService.get_frequencies()
        ):
            self.ui.cmbFrequency.addItem(
                frequency
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

        self.ui.txtSopNumber.setText(
            VehicleSopService.get_next_sop_number()
        )

        self.ui.cmbAsset.setCurrentIndex(0)

        self.ui.txtSopName.clear()

        if self.ui.cmbFrequency.count() > 0:
            self.ui.cmbFrequency.setCurrentIndex(0)

        self.ui.chkActive.setChecked(
            True
        )

        self.ui.txtDescription.clear()
        self.ui.txtNotes.clear()

    def get_form_data(self):

        return {
            "sop_number":
                self.ui.txtSopNumber.text().strip(),

            "asset_id":
                self.ui.cmbAsset.currentData(),

            "sop_name":
                self.ui.txtSopName.text().strip(),

            "frequency":
                self.ui.cmbFrequency.currentText(),

            "description":
                self.ui.txtDescription
                .toPlainText()
                .strip(),

            "active":
                self.ui.chkActive.isChecked(),

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
                "Please select a Vehicle / Asset."
            )
            return

        if not data["sop_name"]:
            self.warning(
                "Validation",
                "SOP Name is required."
            )
            return

        try:

            if self.record_id is None:

                VehicleSopService.create(
                    data
                )

            else:

                data["id"] = self.record_id

                VehicleSopService.update(
                    data
                )

            self.accept()

        except ValueError as error:

            self.warning(
                "Validation",
                str(error)
            )

        except Exception as error:

            self.warning(
                "Vehicle SOP",
                (
                    "Unable to save Vehicle SOP."
                    f"\n\n{error}"
                )
            )

    def load_record(self):

        record = VehicleSopService.get_by_id(
            self.record_id
        )

        if not record:
            return

        self.ui.txtSopNumber.setText(
            record["sop_number"] or ""
        )

        index = self.ui.cmbAsset.findData(
            record["asset_id"]
        )

        if index >= 0:
            self.ui.cmbAsset.setCurrentIndex(
                index
            )

        self.ui.txtSopName.setText(
            record["sop_name"] or ""
        )

        index = self.ui.cmbFrequency.findText(
            record["frequency"] or ""
        )

        if index >= 0:
            self.ui.cmbFrequency.setCurrentIndex(
                index
            )

        self.ui.txtDescription.setPlainText(
            record["description"] or ""
        )

        self.ui.chkActive.setChecked(
            bool(record["active"])
        )

        self.ui.txtNotes.setPlainText(
            record["notes"] or ""
        )