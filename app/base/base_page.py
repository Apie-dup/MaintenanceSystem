from PySide6.QtWidgets import QWidget

from app.services.message_service import MessageService
from app.core.logger import logger


class BasePage(QWidget):
    """
    Base class for all application pages.
    """

    PAGE_TITLE = ""

    def __init__(self, parent=None):
        super().__init__(parent)

    # ---------------------------------------------------------
    # Page Life Cycle
    # ---------------------------------------------------------

    def setup_page(self):
        """
        Override in child pages.
        """
        pass

    def load_data(self):
        """
        Override in child pages.
        """
        pass

    def refresh(self):
        """
        Default refresh simply reloads data.
        """
        self.load_data()

    # ---------------------------------------------------------
    # Messages
    # ---------------------------------------------------------

    def information(self, title, message):
        MessageService.information(
            self,
            title,
            message
        )

    def warning(self, title, message):
        MessageService.warning(
            self,
            title,
            message
        )

    def error(self, title, message):
        MessageService.error(
            self,
            title,
            message
        )

    def confirm(self, title, message):
        return MessageService.confirm(
            self,
            title,
            message
        )

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    def log_info(self, message):
        logger.info(
            "%s: %s",
            self.__class__.__name__,
            message
        )

    def log_warning(self, message):
        logger.warning(
            "%s: %s",
            self.__class__.__name__,
            message
        )

    def log_error(self, message):
        logger.error(
            "%s: %s",
            self.__class__.__name__,
            message
        )