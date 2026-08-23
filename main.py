import sys

from PySide6.QtWidgets import QApplication

from app.database.setup import DatabaseSetup
from app.controllers.login_controller import LoginController
from app.core.logger import logger
from app.core.theme import AppTheme
from app.services.settings_service import SettingsService


def main():

    try:
        logger.info(
            "Starting Maintenance System application."
        )

        #---------------------------------------------
        # Database
        #---------------------------------------------

        REBUILD_DATABASE = False

        if REBUILD_DATABASE:
            DatabaseSetup.rebuild()
        else:
            DatabaseSetup.initialize()

        #--------------------------------------------
        # Start Qt
        #--------------------------------------------

        app = QApplication(sys.argv)

        app.setStyle("Fusion")

        #--------------------------------------------
        # Load saved theme
        #--------------------------------------------

        theme_mode = (
            SettingsService.theme_mode()
        )

        AppTheme.apply(
            app,
            theme_mode
        )

        #-------------------------------------------
        # Login
        #-------------------------------------------

        login_window = LoginController()
        login_window.show()

        exit_code = app.exec()

        logger.info(
            "Application exited with code: %s",
            exit_code
        )

        sys.exit(exit_code)

    except Exception:

        logger.exception(
            "Unhandled error occured during"
            "application startup."
        )

        raise

if __name__ == "__main__":
    main()