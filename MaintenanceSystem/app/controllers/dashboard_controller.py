from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_dashboard import Ui_DashboardWindow


class DashboardController(QMainWindow):

    def __init__(self, user):

        super().__init__()

        self.ui = Ui_DashboardWindow()

        self.ui.setupUi(self)

        self.user = user

        self.setWindowTitle(
            f"Maintenance Management System - {user['fullname']}"
        )