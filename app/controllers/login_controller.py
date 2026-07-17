from PySide6.QtWidgets import QMainWindow, QMessageBox

from app.ui.generated.ui_login import Ui_LoginWindow
from app.services.auth_service import AuthService
from app.controllers.main_controller import MainController


class LoginController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnExit.clicked.connect(self.close)

    def login(self):

        username = self.ui.txtUsername.text().strip()
        password = self.ui.txtPassword.text()

        if not username or not password:

            QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter a username and password."
            )
            return

        user = AuthService.login(username, password)

        if user:

            self.main_window = MainController(user)

            self.main_window.show()

            self.close()

        else:

            QMessageBox.critical(
                self,
                "Login Failed",
                "Invalid username or password."
            )