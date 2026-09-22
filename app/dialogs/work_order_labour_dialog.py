from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)

from app.ui.generated.ui_work_order_labour_dialog import (
    Ui_WorkOrderLabourDialog
)

from app.services.technician_service import (
    TechnicianService
)

from app.services.work_order_labour_service import (
    WorkOrderLabourService
)


class WorkOrderLabourDialog(QDialog):

    def __init__(
        self,
        work_order_id,
        user=None,
        parent=None
    ):
        super().__init__(parent)

        self.ui = Ui_WorkOrderLabourDialog()
        self.ui.setupUi(self)

        self.work_order_id = work_order_id
        self.user = user

        self.setup_dialog()
        self.load_technicians()
        self.connect_signals()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.ui.dtWorkDate.setDate(
            QDate.currentDate()
        )

        self.ui.txtLabourCost.setReadOnly(
            True
        )

        self.update_labour_cost()

    # ---------------------------------------------------------
    # Technicians
    # ---------------------------------------------------------

    def load_technicians(self):
        self.ui.cmbTechnician.clear()

        self.ui.cmbTechnician.addItem(
            "Select Technician",
            None
        )

        technicians = (
            TechnicianService.get_active_technicians()
        )

        for technician in technicians:

            name = (
                f"{technician['employee_number']} - "
                f"{technician['first_name']} "
                f"{technician['last_name']}"
            )

            self.ui.cmbTechnician.addItem(
                name,
                technician["id"]
            )

    def technician_changed(self):
        technician_id = (
            self.ui.cmbTechnician.currentData()
        )

        if technician_id is None:
            self.ui.dsbHourlyRate.setValue(
                0.00
            )
            return

        technician = (
            TechnicianService.get_by_id(
                technician_id
            )
        )

        if technician is None:
            self.ui.dsbHourlyRate.setValue(
                0.00
            )
            return

        self.ui.dsbHourlyRate.setValue(
            float(
                technician["hourly_rate"]
                or 0
            )
        )

    # ---------------------------------------------------------
    # Labour Cost
    # ---------------------------------------------------------

    def update_labour_cost(self):
        hours = (
            self.ui.dsbHours.value()
        )

        hourly_rate = (
            self.ui.dsbHourlyRate.value()
        )

        labour_cost = (
            hours * hourly_rate
        )

        self.ui.txtLabourCost.setText(
            f"N$ {labour_cost:,.2f}"
        )

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save_labour(self):
        technician_id = (
            self.ui.cmbTechnician.currentData()
        )

        if technician_id is None:
            QMessageBox.warning(
                self,
                "Validation",
                "Please select a technician."
            )
            return

        hours = (
            self.ui.dsbHours.value()
        )

        if hours <= 0:
            QMessageBox.warning(
                self,
                "Validation",
                "Labour Hours must be greater than zero."
            )
            return

        hourly_rate = (
            self.ui.dsbHourlyRate.value()
        )

        data = {
            "work_order_id":
                self.work_order_id,

            "technician_id":
                technician_id,

            "work_date":
                self.ui.dtWorkDate.date()
                .toString("yyyy-MM-dd"),

            "hours":
                hours,

            "hourly_rate":
                hourly_rate,

            "description":
                self.ui.txtDescription
                .text()
                .strip(),

            "notes":
                self.ui.txtNotes
                .toPlainText()
                .strip(),

            "user_id":
                self.get_user_id(),

            "username":
                self.get_username(),
        }

        try:
            WorkOrderLabourService.add_labour(
                data
            )

            self.accept()

        except ValueError as error:
            QMessageBox.warning(
                self,
                "Labour",
                str(error)
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Labour",
                f"Unable to add labour.\n\n{error}"
            )

    # ---------------------------------------------------------
    # User Audit
    # ---------------------------------------------------------

    def get_user_id(self):
        if self.user is None:
            return None

        if isinstance(self.user, dict):
            return self.user.get("id")

        try:
            return self.user["id"]
        except (KeyError, TypeError):
            return getattr(
                self.user,
                "id",
                None
            )

    def get_username(self):
        if self.user is None:
            return None

        if isinstance(self.user, dict):
            return self.user.get(
                "username"
            )

        try:
            return self.user["username"]
        except (KeyError, TypeError):
            return getattr(
                self.user,
                "username",
                None
            )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.cmbTechnician.currentIndexChanged.connect(
            self.technician_changed
        )

        self.ui.dsbHours.valueChanged.connect(
            self.update_labour_cost
        )

        self.ui.dsbHourlyRate.valueChanged.connect(
            self.update_labour_cost
        )

        # Qt Designer originally connects accepted
        # directly to accept(). Disconnect that so
        # validation/service saving happens first.
        try:
            self.ui.buttonBox.accepted.disconnect()
        except RuntimeError:
            pass

        self.ui.buttonBox.accepted.connect(
            self.save_labour
        )