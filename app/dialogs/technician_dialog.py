from app.base.base_dialog import BaseDialog
from app.core.lookup_manager import LookupManager
from app.services.technician_service import TechnicianService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_add_technician import Ui_AddTechnicianDialog


class TechnicianDialog(BaseDialog):

    ENTITY_NAME = "Technician"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddTechnicianDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()
        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.connect_signals()

        self.set_read_only(
            self.ui.txtEmployeeNumber
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Lookup values
    # ---------------------------------------------------------

    def load_lookup_values(self):
        LookupManager.load(
            self.ui.cmbTrade,
            "Trades"
        )

        LookupManager.load(
            self.ui.cmbDepartment,
            "Departments"
        )

        LookupManager.load(
            self.ui.cmbStatus,
            "Statuses"
        )

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtEmployeeNumber.setText(
            TechnicianService.get_next_employee_number()
        )

        self.ui.txtFirstName.clear()
        self.ui.txtLastName.clear()
        self.ui.txtPhone.clear()
        self.ui.txtEmail.clear()

        if self.ui.cmbTrade.count() > 0:
            self.ui.cmbTrade.setCurrentIndex(0)

        if self.ui.cmbDepartment.count() > 0:
            self.ui.cmbDepartment.setCurrentIndex(0)

        self.ui.cmbStatus.setCurrentText(
            "Active"
        )

        self.ui.dsbHourlyRate.setValue(0.00)

        self.set_focus(
            self.ui.txtFirstName
        )

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "employee_number":
                self.ui.txtEmployeeNumber.text().strip(),

            "first_name":
                self.ui.txtFirstName.text().strip(),

            "last_name":
                self.ui.txtLastName.text().strip(),

            "phone":
                self.ui.txtPhone.text().strip(),

            "email":
                self.ui.txtEmail.text().strip(),

            "trade":
                self.ui.cmbTrade.currentText().strip(),

            "department":
                self.ui.cmbDepartment.currentText().strip(),

            "hourly_rate":
                self.ui.dsbHourlyRate.value(),

            "status":
                self.ui.cmbStatus.currentText().strip(),
        }

    def set_form_data(self, technician):
        self.ui.txtEmployeeNumber.setText(
            technician["employee_number"] or ""
        )

        self.ui.txtFirstName.setText(
            technician["first_name"] or ""
        )

        self.ui.txtLastName.setText(
            technician["last_name"] or ""
        )

        self.ui.txtPhone.setText(
            technician["phone"] or ""
        )

        self.ui.txtEmail.setText(
            technician["email"] or ""
        )

        self.ui.cmbTrade.setCurrentText(
            technician["trade"] or ""
        )

        self.ui.cmbDepartment.setCurrentText(
            technician["department"] or ""
        )

        self.ui.dsbHourlyRate.setValue(
            float(technician["hourly_rate"] or 0)
        )

        self.ui.cmbStatus.setCurrentText(
            technician["status"] or "Active"
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):
        technician = TechnicianService.get_by_id(
            record_id
        )

        if technician is None:
            self.error(
                "Technician",
                "Technician not found."
            )
            self.reject()
            return

        self.set_form_data(technician)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["employee_number"],
                "Employee Number"
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["first_name"],
                "First Name"
            )
        ):
            self.set_focus(
                self.ui.txtFirstName
            )
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["last_name"],
                "Last Name"
            )
        ):
            self.set_focus(
                self.ui.txtLastName
            )
            return False

        if not ValidationService.check(
            self,
            ValidationService.email(
                data["email"]
            )
        ):
            self.set_focus(
                self.ui.txtEmail
            )
            return False

        if not ValidationService.check(
            self,
            ValidationService.phone(
                data["phone"]
            )
        ):
            self.set_focus(
                self.ui.txtPhone
            )
            return False

        if not ValidationService.check(
            self,
            ValidationService.positive_number(
                data["hourly_rate"],
                "Hourly Rate"
            )
        ):
            self.ui.dsbHourlyRate.setFocus()
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            self.record_id = TechnicianService.create(
                data
            )
        else:
            TechnicianService.update(
                self.record_id,
                data
            )