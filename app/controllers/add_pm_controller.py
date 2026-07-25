from PySide6.QtCore import QDate


from app.ui.generated.ui_add_pm import Ui_AddPMDialog
from app.core.crud_dialog import CrudDialog
from app.core.lookup_manager import LookupManager
from app.services.pm_service import PMService
from app.services.asset_service import AssetService
from app.utils.validators import Validator


class AddPMController(CrudDialog):

    def __init__(self, record_id=None):
        super().__init__(record_id)

        self.ui = Ui_AddPMDialog()
        self.ui.setupUi(self)

        self.initalize_dialog()

    def initalize_dialog(self):

        self.load_lookup_values()
        self.load_assets()

        self.ui.dtLastService.setCalendarPopup(True)
        self.ui.dtNextDue.setCalendarPopup(True)

        self.ui.spnFrequencyValue.setMinimum(1)

        self.ui.dsbEstimatedHours.setDecimals(2)
        self.ui.dsbEstimatedCost.setDecimals(2)

        self.ui.chkActive.setChecked(True)

        if self.is_add:

            self.ui.txtPMNumber.setText(
                PMService.get_next_pm_number()
            )

            self.ui.txtPMNumber.setReadOnly(True)

            today = QDate.currentDate()

            self.ui.dtLastService.setDate(today)
            self.ui.dtNextDue.setDate(today)

        else:

            self.load_pm()

            self.ui.buttonBox.accepted.connect(self.save)
            self.ui.buttonBox.rejected.connect(self.reject)

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

        assets = AssetService.get_all()

        for asset in assets:

            self.ui.cmbAsset.addItem(
                f"{asset[1]} - {asset[2]}",
                asset[0]
            )

    def save(self):

        task = self.ui.txtTask.text().strip()

        if not Validator.required(
            self,
            task,
            "Task"
        ):

            return

        if self.ui.cmbAsset.currentData() is None:

            self.warning(
                "Validation",
                "Please select an asset."
            )



            return

        pm = (

            self.ui.txtPMNumber.text(),

            self.ui.cmbAsset.currentData(),

            task,

            self.ui.teDescription.toPlainText().strip(),

            self.ui.cmbFrequencyType.currentText(),

            self.ui.spnFrequencyValue.value(),

            self.ui.dtLastService.date().toString("yyyy-MM-dd"),

            self.ui.dtNextDue.date().toString("yyyy-MM-dd"),

            self.ui.dsbEstimatedHours.value(),

            self.ui.dsbEstimatedCost.value(),

            self.ui.cmbPriority.currentText(),

            1 if self.ui.chkActive.isChecked() else 0,

            self.ui.teNotes.toPlainText().strip()
        )

        if self.is_add:

            PMService.add(pm)

            self.information(
                "Success",
                "Preventive Maintenance scheduel created successfully."
            )

        else:

            update_pm = (

                self.ui.cmbAsset.currentData(),

                task,

                self.ui.teDescription.toPlainText().strip(),

                self.ui.cmbFrequencyType.currentText(),

                self.ui.spnFrequencyValue.value(),

                self.ui.dtLastService.date().toString("yyyy-MM-dd"),

                self.ui.dtNextDue.date().toString("yyyy-MM-dd"),

                self.ui.dsbEstimatedHours.value(),

                self.ui.dsbEstimatedCost.value(),

                self.ui.cmbPriority.currentText(),

                1 if self.ui.chkActive.isChecked() else 0,

                self.ui.teNotes.toPlainText().strip(),

                self.record_id

            )

            PMService.update(update_pm)

            self.information(
                "Success",
                "Preventive Maintenance updated successfully."
            )


        self.accept()

    def load_pm(self):

        pm = PMService.get(self.record_id)

        if not pm:

            self.warning(
                "Error",
                "Preventive Maintenence record not foun."
            )

            self.reject()


            return


        (

            _,
            pm_number,
            asset_id,
            task,
            description,
            frequenct_type,
            frequenct_value,
            last_service,
            next_due,
            estimated_hours,
            estimated_cost,
            priority,
            active,
            notes,
            created_at

        ) = pm

        self.ui.txtPMNumber.setText(pm_number)
        self.ui.txtPMNumber.setReadOnly(True)

        self.ui.txtTask.setTask(task or "")
        self.ui.teDescription.setPlainText(description or "")

        self.ui.cmbFrequencyType.setCurrentText(frequenct_type or "")
        self.ui.spnFrequencyValue.setValue(frequenct_value or "")

        if last_service:
            self.ui.dtLastService.setDate(
                QDate.fromString(last_service, "yyyy-MM-dd")
            )

        if next_due:
            self.ui.dtNextDue.setDate(
                QDate.fromString(next_due, "yyyy-MM-dd")
            )


        self.ui.dsbEstimatedHours.setValue(
            estimated_hours or 0
        )

        self.ui.dsbEstimatedCost.setValue(
            estimated_cost or 0
        )

        self.ui.cmbPriority.setCurrentText(priority or "")

        self.ui.chkActive.setChecked(bool(active))

        self.ui.teNotes.setPlainText(notes or "")

        index = self.ui.cmbAsset.findData(asset_id)

        if index >= 0:
            self.ui.cmbAsset.setCurrentIndex(index)