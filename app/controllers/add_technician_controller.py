from app.ui.generated.ui_add_technician import Ui_AddTechnicianDialog
from app.services.technician_service import TechnicianService
from app.core.lookup_manager import LookupManager
from app.base.base_dialog import CrudDialog
from app.utils.validators import Validator


class AddTechnicianController(CrudDialog):

    def __init__(self, record_id=None):
        super().__init__(record_id)

        self.ui = Ui_AddTechnicianDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):
        self.load_lookup_values()

        if self.is_add:
            self.ui.txtEmployeeNumber.setText(
                TechnicianService.get_next_employee_number()
            )
        
        else:
            
            technician = TechnicianService.get(self.record_id)

        
            if not technician:
                self.warning("Error", "Technician not found.")
                self.reject()
                return

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
            self.set_entity_name("Technician")

        self.ui.buttonBox.accepted.connect(self.save)
        self.ui.buttonBox.rejected.connect(self.reject)

    def load_lookup_values(self):

        LookupManager.load(self.ui.cmbTrade, "Trades")
        LookupManager.load(self.ui.cmbDepartment, "Departments")
        LookupManager.load(self.ui.cmbStatus, "Statuses")

    def save(self):

        employee_number = self.ui.txtEmployeeNumber.text().strip()
        first_name = self.ui.txtFirstName.text().strip()
        last_name = self.ui.txtLastName.text().strip()
        phone = self.ui.txtPhone.text().strip()
        email = self.ui.txtEmail.text().strip()
        trade = self.ui.cmbTrade.currentText()
        department = self.ui.cmbDepartment.currentText()
        hourly_rate = self.ui.dsbHourlyRate.value()
        status = self.ui.cmbStatus.currentText()

        # -------------------------
        # VALIDATION
        # -------------------------
        if not Validator.required(self, employee_number, "Employee Number"):
            return

        if not Validator.required(self, first_name, "First Name"):
            return

        if not Validator.required(self, last_name, "Last Name"):
            return

        # -------------------------
        # ADD MODE
        # -------------------------
        if self.is_add:

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

            TechnicianService.add(technician)

            self.information("Success", "Technician added successfully.")

        # -------------------------
        # UPDATE MODE
        # -------------------------
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
                self.record_id
            )

            TechnicianService.update(technician)

            self.information("Success", "Technician updated successfully.")

        self.accept()

