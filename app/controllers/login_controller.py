from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox
)

from app.ui.generated.ui_login import (
    Ui_LoginWindow
)

from app.services.auth_service import (
    AuthService
)

from app.controllers.main_controller import (
    MainController
)


class LoginController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.settings = QSettings(
            "MaintenanceSystem",
            "MaintenanceSystem"
        )

        self.load_remembered_username()

        self.ui.btnLogin.clicked.connect(
            self.login
        )

        self.ui.btnExit.clicked.connect(
            self.close
        )

        self.ui.txtUsername.returnPressed.connect(
            self.login
        )

        self.ui.txtPassword.returnPressed.connect(
            self.login
        )

    def load_remembered_username(self):

        remember_me = self.settings.value(
            "login/remember_me",
            False,
            type=bool
        )

        username = self.settings.value(
            "login/username",
            "",
            type=str
        )

        self.ui.chkRememberMe.setChecked(
            remember_me
        )

        if remember_me and username:

            self.ui.txtUsername.setText(
                username
            )

            self.ui.txtPassword.setFocus()

        else:

            self.ui.txtUsername.setFocus()

    def login(self):

        username = (
            self.ui.txtUsername.text().strip()
        )

        password = (
            self.ui.txtPassword.text()
        )

        if not username or not password:

            QMessageBox.warning(
                self,
                "Missing Information",
                (
                    "Please enter a username "
                    "and password."
                )
            )
            return

        user = AuthService.login(
            username,
            password
        )

        if user:

            if (
                self.ui.chkRememberMe
                .isChecked()
            ):

                self.settings.setValue(
                    "login/remember_me",
                    True
                )

                self.settings.setValue(
                    "login/username",
                    username
                )

            else:

                self.settings.setValue(
                    "login/remember_me",
                    False
                )

                self.settings.remove(
                    "login/username"
                )

            self.main_window = (
                MainController(user)
            )

            self.main_window.show()

            self.close()

        else:

            QMessageBox.critical(
                self,
                "Login Failed",
                (
                    "Invalid username "
                    "or password."
                )
            )


