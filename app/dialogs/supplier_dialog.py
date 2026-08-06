from app.base.base_dialog import BaseDialog
from app.services.supplier_service import SupplierService
from app.services.validation_service import ValidationService
from app.helpers.lookup_helper import LookupHelper
from app.ui.generated.ui_supplier_dialog import Ui_SupplierDialog
from app.helpers.form_helper import FormHelper


class SupplierDialog(BaseDialog):

    ENTITY_NAME = "Supplier"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SupplierDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()
        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.setup_combos()
        self.connect_signals()

        self.ui.txtSupplierCode.setReadOnly(True)
        
    def setup_combos(self):
        LookupHelper.fill_combo(
            self.ui.cmbStatus,
            [
                "Active",
                "Inactive",
            ]
        )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtSupplierCode.setText(
            SupplierService.get_next_supplier_code()
        )

        self.ui.txtSupplierName.clear()
        self.ui.txtContactPerson.clear()
        self.ui.txtPhone.clear()
        self.ui.txtEmail.clear()
        self.ui.txtAddress.clear()
        self.ui.txtNotes.clear()

        self.ui.cmbStatus.setCurrentText("Active")

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "supplier_code":
                self.ui.txtSupplierCode.text().strip(),

            "supplier_name":
                self.ui.txtSupplierName.text().strip(),

            "contact_person":
                self.ui.txtContactPerson.text().strip(),

            "phone":
                self.ui.txtPhone.text().strip(),

            "email":
                self.ui.txtEmail.text().strip(),

            "address":
                self.ui.txtAddress.toPlainText().strip(),

            "status":
                self.ui.cmbStatus.currentText(),

            "notes":
                self.ui.txtNotes.toPlainText().strip(),
        }

    def set_form_data(self, supplier):
        self.ui.txtSupplierCode.setText(
            supplier["supplier_code"]
        )

        self.ui.txtSupplierName.setText(
            supplier["supplier_name"]
        )

        self.ui.txtContactPerson.setText(
            supplier["contact_person"] or ""
        )

        self.ui.txtPhone.setText(
            supplier["phone"] or ""
        )

        self.ui.txtEmail.setText(
            supplier["email"] or ""
        )

        self.ui.txtAddress.setPlainText(
            supplier["address"] or ""
        )

        self.ui.cmbStatus.setCurrentText(
            supplier["status"] or "Active"
        )

        self.ui.txtNotes.setPlainText(
            supplier["notes"] or ""
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, supplier_id):
        supplier = SupplierService.get_by_id(
            supplier_id
        )

        if supplier is None:
            self.error(
                "Supplier",
                "Supplier not found."
            )
            self.reject()
            return

        self.set_form_data(supplier)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["supplier_name"],
                "Supplier Name"
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.email(
                data["email"]
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.phone(
                data["phone"]
            )
        ):
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            SupplierService.create(data)
        else:
            SupplierService.update(
                self.record_id,
                data
            )