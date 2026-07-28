from app.base.base_dialog import BaseDialog
from app.services.supplier_service import SupplierService
from app.services.message_service import MessageService
from app.services.validation_service import ValidationService

from app.ui.generated.ui_supplier_dialog import Ui_SupplierDialog


class SupplierDialog(BaseDialog):

    ENTITY_NAME = "Supplier"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SupplierDialog()
        self.ui.setupUi(self)

        self.connect_signals()

    def setup_dialog(self):

        self.setup_combos()

        self.setup_signals()

    def setup_combos(self):

        self.ui.cmbStatus.addItems([
            "Active",
            "Inactive"
        ])

    def conect_signals(self):

        self.ui.btnSave.clicked.connect(
            self.save_and_close
        )

        self.ui.btnCancel.clicked.connect(
            self.reject
        )

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
                self.ui.txtNotes.toPlainText().strip()
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
            supplier["status"]
    )

        self.ui.txtNotes.setPlainText(
            supplier["notes"] or ""
    )
        

    def clear_fields(self):

        self.ui.txtSupplierCode.setText(
            SupplierService.get_next_supplier_code()
        )

        self.ui.txtSupplierName.setFocus()

        self.ui.txtSupplierName.clear()

        self.ui.txtContacPerson.clear()

        self.ui.txtPhone.clear()

        self.ui.txtEmail.clear()

        self.ui.txtAddress.clear()

        self.ui.cmbStatus.setCurrentIndex("Active")

        self.ui.txtNotes.clear()

    def load_record(self, supplier_id):

        supplier = SupplierService.get_by_id(supplier_id)

        if supplier is None:

            self.error(
                "Supplier",
                "Supplier not found."
            )

            self.reject()

            return

            self.set_form_data(supplier)

    def validate(self):

        valid, message = ValidationService.required(
            self.ui.txtSupplierCode.text(),
            "Supplier Code"
        )

        if not valid:
            MessageService.warning(self, "Validation", message)
            return False

        valid, message = ValidationService.required(
            self.ui.txtSupplierName.text(),
            "Supplier Name"
        )

        if not valid:
            MessageService.warning(self, "Validation", message)
            return False

        valid, message = ValidationService.email(
            self.ui.txtEmail.text()
        )

        if not valid:
            MessageService.warning(self, "Validation", message)
            return False

        return True

    def save(self):

        data = self.get_form_data()

        if self.is_add:

            SupplierService.create(data)

        else:

            SupplierService.update(
                self.record_id,
                data
        )

