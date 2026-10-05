from PySide6.QtWidgets import QDialog

from app.services.vehicle_sop_inspection_service import (
    VehicleSopInspectionService
)
from app.ui.generated.ui_vehicle_sop_inspection_result_dialog import (
    Ui_VehicleSopInspectionResultDialog
)


class VehicleSopInspectionResultDialog(QDialog):

    def __init__(
        self,
        check_description,
        result=None,
        comments=None,
        parent=None
    ):
        super().__init__(parent)

        self.ui = Ui_VehicleSopInspectionResultDialog()
        self.ui.setupUi(self)

        self.check_description = (
            check_description or ""
        )

        self.load_results()
        self.load_data(
            result,
            comments
        )

        self.ui.buttonBox.accepted.connect(
            self.accept
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Results
    # ---------------------------------------------------------

    def load_results(self):

        self.ui.cmbResult.clear()

        self.ui.cmbResult.addItem(
            "Select Result",
            None
        )

        for result in (
            VehicleSopInspectionService
            .get_results()
        ):
            self.ui.cmbResult.addItem(
                result,
                result
            )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_data(
        self,
        result,
        comments
    ):

        self.ui.lblCheckDescription.setText(
            self.check_description
        )

        if result:

            index = (
                self.ui.cmbResult
                .findData(result)
            )

            if index >= 0:
                self.ui.cmbResult.setCurrentIndex(
                    index
                )

        self.ui.txtComments.setPlainText(
            comments or ""
        )

    # ---------------------------------------------------------
    # Values
    # ---------------------------------------------------------

    def get_data(self):

        return {
            "result":
                self.ui.cmbResult.currentData(),

            "comments":
                self.ui.txtComments
                .toPlainText()
                .strip(),
        }

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def accept(self):

        if (
            self.ui.cmbResult.currentData()
            is None
        ):
            return

        super().accept()