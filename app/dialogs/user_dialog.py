from app.base.base_dialog import BaseDialog
from app.services.user_service import UserService
from app.ui.generated.ui_user_dialog import Ui_UserDialog


class UserDialog(BaseDialog):

    ENTITY_NAME = "User"

    def __init__(
        self,
        record_id=None,
        parent=None
    ):
        super().__init__(
            record_id,
            parent
        )

        self.ui = Ui_UserDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()

        self.setup_dialog()

    # -------------------------------------------------
    # Setup
    # -------------------------------------------------

    def setup_dialog(self):

        self.ui.cmbRole.clear()
        self.ui.cmbRole.addItems(
            UserService.ROLES
        )

        self.ui.cmbStatus.clear()
        self.ui.cmbStatus.addItems([
            "Active",
            "Inactive",
        ])

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # -------------------------------------------------
    # Clear fields
    # -------------------------------------------------

    def clear_fields(self):

        self.ui.txtUsername.clear()
        self.ui.txtFullName.clear()

        self.ui.cmbRole.setCurrentText(
            "Viewer"
        )

        self.ui.cmbStatus.setCurrentText(
            "Active"
        )

        self.ui.txtPassword.clear()
        self.ui.txtConfirmPassword.clear()

        self.ui.lblPasswordHint.setText(
            "Password is required when creating a user."
        )

        self.set_focus(
            self.ui.txtUsername
        )

    # -------------------------------------------------
    # Form data
    # -------------------------------------------------

    def get_form_data(self):

        return {
            "username":
                self.ui.txtUsername.text().strip(),

            "fullname":
                self.ui.txtFullName.text().strip(),

            "role":
                self.ui.cmbRole.currentText().strip(),

            "active":
                self.ui.cmbStatus.currentText()
                == "Active",

            "password":
                self.ui.txtPassword.text(),

            "confirm_password":
                self.ui.txtConfirmPassword.text(),
        }

    def set_form_data(self, data):

        self.ui.txtUsername.setText(
            data["username"] or ""
        )

        self.ui.txtFullName.setText(
            data["fullname"] or ""
        )

        self.ui.cmbRole.setCurrentText(
            data["role"] or "Viewer"
        )

        self.ui.cmbStatus.setCurrentText(
            "Active"
            if data["active"]
            else "Inactive"
        )

        # Never show the stored password hash.
        self.ui.txtPassword.clear()
        self.ui.txtConfirmPassword.clear()

    # -------------------------------------------------
    # Load
    # -------------------------------------------------

    def load_record(self, record_id):

        record = UserService.get_by_id(
            record_id
        )

        if record is None:
            raise ValueError(
                "User could not be found."
            )

        self.set_form_data(
            record
        )

        self.ui.lblPasswordHint.setText(
            "Leave password blank to keep "
            "the existing password."
        )

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def validate(self):

        data = self.get_form_data()

        if not data["username"]:
            self.warning(
                "Validation",
                "Username is required."
            )
            self.ui.txtUsername.setFocus()
            return False

        if not data["fullname"]:
            self.warning(
                "Validation",
                "Full Name is required."
            )
            self.ui.txtFullName.setFocus()
            return False

        if (
            data["role"]
            not in UserService.ROLES
        ):
            self.warning(
                "Validation",
                "Please select a valid role."
            )
            return False

        # New users must have a password.
        if (
            self.is_add
            and not data["password"]
        ):
            self.warning(
                "Validation",
                "Password is required."
            )
            self.ui.txtPassword.setFocus()
            return False

        # If a password is supplied,
        # confirmation must match.
        if data["password"]:

            if (
                data["password"]
                != data["confirm_password"]
            ):
                self.warning(
                    "Validation",
                    "Passwords do not match."
                )
                self.ui.txtConfirmPassword.setFocus()
                return False

        return True

    # -------------------------------------------------
    # Save
    # -------------------------------------------------

    def save(self):

        data = self.get_form_data()

        if self.is_add:

            self.record_id = (
                UserService.create(
                    data
                )
            )

        else:

            UserService.update(
                self.record_id,
                data
            )