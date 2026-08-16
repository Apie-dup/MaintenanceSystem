import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor, QPalette

from app.database.setup import DatabaseSetup
from app.controllers.login_controller import LoginController
from app.core.logger import logger
from app.core.theme import AppTheme


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

        AppTheme.apply_system_theme(app)


        def apply_light_palette(app):
            palette = QPalette()

            palette.setColor(
                QPalette.ColorRole.Window,
                QColor("#f7f7f7")
            )

            palette.setColor(
                QPalette.ColorRole.WindowText,
                QColor("#1f1f1f")
            )

            palette.setColor(
                QPalette.ColorRole.Base,
                QColor("#ffffff")
            )

            palette.setColor(
                QPalette.ColorRole.AlternateBase,
                QColor("#fafafa")
            )

            palette.setColor(
                QPalette.ColorRole.Text,
                QColor("#1f1f1f")
            )

            palette.setColor(
                QPalette.ColorRole.Button,
                QColor("#ffffff")
            )

            palette.setColor(
                QPalette.ColorRole.ButtonText,
                QColor("#1f1f1f")
            )

            palette.setColor(
                QPalette.ColorRole.Highlight,
                QColor("#cfe8ff")
            )

            palette.setColor(
                QPalette.ColorRole.HighlightedText,
                QColor("#1f1f1f")
            )
            app.setPalette(palette)

        # Start in light mode
        AppTheme.apply(app, AppTheme.MODE_DARK)

        app.setStyle("Fusion")

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