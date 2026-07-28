from PySide6.QtWidgets import QMessageBox


class MessageService:

    """
    Central application message handler
    """

    @staticmethod
    def information(parent, title, message):

        QMessageBox.information(
            parent,
            title,
            message
        )

    @staticmethod
    def warning(parent, title, message):

        QMessageBox.warning(
            parent,
            title,
            message
        )

    @staticmethod
    def error(parent, title, message):

        QMessageBox.critical(
            parent,
            title,
            message
        )

    @staticmethod
    def confirm(parent, title, message):

        result = QMessageBox.question(
            parent,
            title,
            message,
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        return result == QMessageBox.StandardButton.Yes