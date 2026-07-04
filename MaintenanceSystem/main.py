import sys

from PySide6.QtWidgets import QApplication

from database import Database
from app.controllers.login_controller import LoginController


def main():

    Database.initialize()

    app = QApplication(sys.argv)

    window = LoginController()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()