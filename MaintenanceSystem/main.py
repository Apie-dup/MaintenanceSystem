import sys

from PySide6.QtWidgets import QApplication

from app.controllers.login_controller import LoginController
from app.database.setup import setup_database


def main():
    setup_database()

    app = QApplication(sys.argv)

    window = LoginController()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()