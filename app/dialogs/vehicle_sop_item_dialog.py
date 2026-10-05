from app.base.base_dialog import BaseDialog
from app.services.vehicle_sop_item_service import (
    VehicleSopItemService
)
from app.ui.generated.ui_vehicle_sop_item_dialog import (
    Ui_VehicleSopItemDialog
)


class VehicleSopItemDialog(BaseDialog):

    ENTITY_NAME = "SOP Checklist Item"

    def __init__(
        self,
        sop_id,
        parent=None,
    ):
        super().__init__(parent)

        self.ui = Ui_VehicleSopItemDialog()
        self.ui.setupUi(self)

        self.sop_id = sop_id
        self.record_id = None

        self.connect_signals()

    def connect_signals(self):

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
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

        sequence = (
            VehicleSopItemService
            .get_next_sequence(
                self.sop_id
            )
        )

        self.ui.spnSequence.setValue(
            sequence
        )

        self.ui.txtCheckDescription.clear()

        self.ui.chkRequired.setChecked(
            True
        )

    def get_form_data(self):

        return {
            "sop_id":
                self.sop_id,

            "sequence":
                self.ui.spnSequence.value(),

            "check_description":
                self.ui.txtCheckDescription
                .toPlainText()
                .strip(),

            "required":
                self.ui.chkRequired.isChecked(),
        }

    def save_and_close(self):

        data = self.get_form_data()

        if not data["check_description"]:
            self.warning(
                "Validation",
                "Check Description is required."
            )
            return

        try:

            if self.record_id is None:

                VehicleSopItemService.create(
                    data
                )

            else:

                data["id"] = self.record_id

                VehicleSopItemService.update(
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
                "Vehicle SOP Checklist",
                (
                    "Unable to save checklist item."
                    f"\n\n{error}"
                )
            )

    def load_record(self):

        record = (
            VehicleSopItemService.get_by_id(
                self.record_id
            )
        )

        if not record:
            return

        self.ui.spnSequence.setValue(
            int(record["sequence"] or 1)
        )

        self.ui.txtCheckDescription.setPlainText(
            record["check_description"] or ""
        )

        self.ui.chkRequired.setChecked(
            bool(record["required"])
        )