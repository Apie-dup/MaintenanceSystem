from PySide6.QtWidgets import QDialog, QMessageBox


class CrudDialog(QDialog):

    def __init__(self, record_id=None):
        super().__init__()

        self.record_id = record_id

    # ------------------------------------------
    # Mode
    # ------------------------------------------

    @property
    def is_add(self):
        return self.record_id is None

    @property
    def is_edit(self):
        return self.record_id is not None

    # ------------------------------------------
    # Dialog title
    # ------------------------------------------

    def set_entity(self, entity):

        if self.is_add:
            self.setWindowTitle(f"Add {entity}")
        else:
            self.setWindowTitle(f"Edit {entity}")

    # ------------------------------------------
    # Message helpers
    # ------------------------------------------

    def information(self, title, message):

        QMessageBox.information(
            self,
            title,
            message
        )

    def warning(self, title, message):

        QMessageBox.warning(
            self,
            title,
            message
        )

    def question(self, title, message):

        return QMessageBox.question(
            self,
            title,
            message,
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )