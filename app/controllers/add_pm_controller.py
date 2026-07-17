from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from app.ui.generated.ui_add_pm import Ui_AddPMDialog
from app.services.pm_service import PMService
from app.services.asset_service import AssetService


class AddPMController(QDialog):

    def __init__(self, pm_id=None):
        super().__init__()

        self.pm_id = pm_id

        self.ui = Ui_AddPMDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):

        self.load_assets()
        self.load_frequencies()
        self.load_priorities()

        self.ui.dtLastService.setCalendarPopup(True)
        self.ui.dtNextDue.setCalendarPopup(True)

        self.ui.dsbEstimatedHours.setDecimals(2)
        self.ui.dsbEstimatedCost.setDecimals(2)

        if self.pm_id is None:

            self.ui.txtPMNumber.setText(
                PMService.get_next_pm_number()
            )

            self.ui.txtPMNumber.setReadOnly(True)

            self.ui.chkActive.setChecked(True)

            self.ui.dtLastService.setDate(
                QDate.currentDate()
            )

            self.ui.dtNextDue.setDate(
                QDate.currentDate()
            )

        else:

            self.load_pm()

        self.ui.buttonBox.accepted.connect(
            self.save_pm
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )


    def load_assets(self):

        self.ui.cmbAsset.clear()

        assets = AssetService.get_assets()

        for asset in assets:

            self.ui.cmbAsset.addItem(
                f"{asset[1]} - {asset[2]}",
                asset[0]
            )


    def load_frequencies(self):

        self.ui.cmbFrequency.clear()

        self.ui.cmbFrequency.addItems([
            "Daily",
            "Weekly",
            "Monthly",
            "Quarterly",
            "Yearly"
        ])


    def load_priorities(self):

        self.ui.cmbPriority.clear()

        self.ui.cmbPriority.addItems([
            "Low",
            "Medium",
            "High",
            "Critical"
        ])


    def save_pm(self):

        if not self.ui.txtTask.text().strip():

            QMessageBox.warning(
                self,
                "Validation",
                "Task is required."
            )
            return


        pm = (

            self.ui.txtPMNumber.text(),

            self.ui.cmbAsset.currentData(),

            self.ui.txtTask.text().strip(),

            self.ui.teDescription.toPlainText().strip(),

            self.ui.cmbFrequency.currentText(),

            self.ui.spnFrequencyValue.value(),

            self.ui.dtLastService.date().toString(
                "yyyy-MM-dd"
            ),

            self.ui.dtNextDue.date().toString(
                "yyyy-MM-dd"
            ),

            self.ui.dsbEstimatedHours.value(),

            self.ui.dsbEstimatedCost.value(),

            self.ui.cmbPriority.currentText(),

            1 if self.ui.chkActive.isChecked() else 0,

            self.ui.teNotes.toPlainText().strip()
        )


        if self.pm_id is None:

            PMService.add_pm(pm)

            QMessageBox.information(
                self,
                "Success",
                "Preventive Maintenance added successfully."
            )

        else:

            update_pm = pm[1:] + (
                self.pm_id,
            )

            PMService.update_pm(update_pm)

            QMessageBox.information(
                self,
                "Success",
                "Preventive Maintenance updated successfully."
            )


        self.accept()


    def load_pm(self):

        pm = PMService.get_pm(
            self.pm_id
        )

        if not pm:
            return


        (
            _,
            pm_number,
            asset_id,
            task,
            description,
            frequency,
            frequency_value,
            last_service,
            next_due,
            estimated_hours,
            estimated_cost,
            priority,
            active,
            notes
        ) = pm


        self.ui.txtPMNumber.setText(pm_number)
        self.ui.txtPMNumber.setReadOnly(True)

        self.ui.txtTask.setText(task)

        self.ui.teDescription.setPlainText(
            description or ""
        )

        self.ui.cmbAsset.setCurrentIndex(
            self.ui.cmbAsset.findData(asset_id)
        )

        self.ui.cmbFrequency.setCurrentText(
            frequency
        )

        self.ui.spnFrequencyValue.setValue(
            frequency_value
        )

        self.ui.dtLastService.setDate(
            QDate.fromString(
                last_service,
                "yyyy-MM-dd"
            )
        )

        self.ui.dtNextDue.setDate(
            QDate.fromString(
                next_due,
                "yyyy-MM-dd"
            )
        )

        self.ui.dsbEstimatedHours.setValue(
            estimated_hours or 0
        )

        self.ui.dsbEstimatedCost.setValue(
            estimated_cost or 0
        )

        self.ui.cmbPriority.setCurrentText(
            priority
        )

        self.ui.chkActive.setChecked(
            bool(active)
        )

        self.ui.teNotes.setPlainText(
            notes or ""
        )