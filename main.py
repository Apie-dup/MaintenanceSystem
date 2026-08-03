import sys

from PySide6.QtWidgets import QApplication

from app.database.setup import DatabaseSetup
from app.controllers.login_controller import LoginController
from app.core.logger import logger


def main():

    try:
        logger.info("Starting Maintenance System application.")

        # Initialize or rebuild the database
        REBUILD_DATABASE = False

        if REBUILD_DATABASE:
            DatabaseSetup.rebuild()
        else:
            DatabaseSetup.initialize()

        # Start Qt
        app = QApplication(sys.argv)

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
            "Unhandled error occurred during application startup."
        )

        raise

if __name__ == "__main__":
    main()