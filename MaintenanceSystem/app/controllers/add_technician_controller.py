from PySide6.QtWidgets import QDialog, QMessageBox

from app.ui.generated.ui_add_technician import Ui_AddTechnicianDialog
from app.services.technician_service import TechnicianService
from app.services.lookup_service import LookupService


class AddTechnicianController(QDialog):

    def __init__(self, technician_id=None):
        super().__init__()

        self.technician_id = technician_id

        self.ui = Ui_AddTechnicianDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):
        # Trades
        self.ui.cmbTrade.clear()
        LookupService.load_trades(self.ui.cmbTrade)

        # Departments (kept as a combo for convenience)
        self.ui.cmbDepartment.clear()
        LookupService.load_departments(self.ui.cmbDepartment)

        # Status
        self.ui.cmbStatus.clear()
        LookupService.load_statuses(self.ui.cmbStatus)

        if self.technician_id is None:
            self.ui.txtEmployeeNumber.setText(
                TechnicianService.get_next_employee_number()
            )
            self.setWindowTitle("Add Technician")
        else:
            technician = TechnicianService.get_technician(
                self.technician_id
            )

            (
                _,
                employee_number,
                first_name,
                last_name,
                phone,
                email,
                trade,
                department,
                status,
                hourly_rate,
                created_at
            ) = technician

            self.ui.txtEmployeeNumber.setText(employee_number)
            self.ui.txtEmployeeNumber.setReadOnly(True)
            self.ui.txtFirstName.setText(first_name)
            self.ui.txtLastName.setText(last_name)
            self.ui.txtPhone.setText(phone)
            self.ui.txtEmail.setText(email)
            self.ui.cmbTrade.setCurrentText(trade)
            self.ui.cmbDepartment.setCurrentText(department)
            self.ui.dsbHourlyRate.setValue(hourly_rate or 0)
            self.ui.cmbStatus.setCurrentText(status)
            self.setWindowTitle("Edit Technician")

        try:
            self.ui.buttonBox.accepted.disconnect()
            self.ui.buttonBox.rejected.disconnect()
        except Exception:
            pass

        self.ui.buttonBox.accepted.connect(self.save_technician)
        self.ui.buttonBox.rejected.connect(self.reject)

    def save_technician(self):

       employee_number = self.ui.txtEmployeeNumber.text().strip()
       first_name = self.ui.txtFirstName.text().strip()
       last_name = self.ui.txtLastName.text().strip()
       phone = self.ui.txtPhone.text().strip()
       email = self.ui.txtEmail.text().strip()
       trade = self.ui.cmbTrade.currentText()
       department = self.ui.cmbDepartment.currentText()
       hourly_rate = self.ui.dsbHourlyRate.value()
       status = self.ui.cmbStatus.currentText()

       if not employee_number:
         QMessageBox.warning(self, "Validation", "Employee Number is required.")
         return

       if not first_name:
         QMessageBox.warning(self, "Validation", "First Name is required.")
         return

       if not last_name:
         QMessageBox.warning(self, "Validation", "Last Name is required.")
         return

       if self.technician_id is None:

        technician = (
            employee_number,
            first_name,
            last_name,
            phone,
            email,
            trade,
            department,
            hourly_rate,
            status
        )

        TechnicianService.add_technician(technician)

        QMessageBox.information(
            self,
            "Success",
            "Technician added successfully."
        )

       else:

        technician = (
            first_name,
            last_name,
            phone,
            email,
            trade,
            department,
            hourly_rate,
            status,
            self.technician_id
        )

        TechnicianService.update_technician(technician)

        QMessageBox.information(
            self,
            "Success",
            "Technician updated successfully."
        )

       self.accept()
