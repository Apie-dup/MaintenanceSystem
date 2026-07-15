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

from app.database.seed import (
    seed_default_admin,
    seed_app_settings,
    seed_lookup_tables,
    seed_preventive_maintenance
)


if __name__ == "__main__":
    main()