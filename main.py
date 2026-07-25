import sys

from PySide6.QtWidgets import QApplication

from app.database.setup import DatabaseSetup
from app.controllers.login_controller import LoginController


def main():
    # Initialize the database
    DatabaseSetup.initialize()

    # Start Qt
    app = QApplication(sys.argv)

    window = LoginController()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()