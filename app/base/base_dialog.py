from PySide6.QtWidgets import QDialog, QWidget

from app.services.message_service import MessageService
from app.core.logger import logger


class BaseDialog(QDialog):

    # ---------------------------------------------------------
    # Dialog Configuration
    # ---------------------------------------------------------

    ENTITY_NAME = ""

    def __init__(self, record_id=None, parent=None):
        if parent is None and record_id is not None and isinstance(record_id, QWidget):
            parent = record_id
            record_id = None

        super().__init__(parent)

        self.record_id = record_id

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def is_add(self):
        return self.record_id is None

    @property
    def is_edit(self):
        return self.record_id is not None

    def set_entity_name(self, entity_name):
        self.ENTITY_NAME = entity_name

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def new_record(self):
        """
        Prepare dialog for adding a new record.
        """
        self.record_id = None

        self.setWindowTitle(f"Add {self.ENTITY_NAME}")

        self.clear_fields()

    def edit_record(self, record_id):
        """
        Prepare dialog for editing an existing record.
        """
        self.record_id = record_id

        self.setWindowTitle(f"Edit {self.ENTITY_NAME}")

        self.load_record(record_id)

    # ---------------------------------------------------------
    # Methods child dialogs must implement
    # ---------------------------------------------------------

    def clear_fields(self):
        raise NotImplementedError(
            "clear_fields() must be implemented."
        )

    def load_record(self, record_id):
        raise NotImplementedError(
            "load_record() must be implemented."
        )

    def validate(self):
        raise NotImplementedError(
            "validate() must be implemented."
        )

    def save(self):
        raise NotImplementedError(
            "save() must be implemented."
        )

    # ---------------------------------------------------------
    # Message Helpers
    # ---------------------------------------------------------

    def information(self, title, message):
        MessageService.information(self, title, message)

    def warning(self, title, message):
        MessageService.warning(self, title, message)

    def error(self, title, message):
        MessageService.error(self, title, message)

    def confirm(self, title, message):
        return MessageService.confirm(self, title, message)

    # ---------------------------------------------------------
    # Data Mapping
    # ---------------------------------------------------------

    def get_from_data(self):

        """
        Return a dictionary containing all form data.
        """
        raise NotImplementedError(
            "get_form_data() must be implemented."
        )

    def set_form_data(self, data):

        """
        Populate the form field from a dictionary.
        """

        raise NotImplementedError(
            "set_form_data() must be implemented"
        )

    def save_and_close(self):

        if not self.validate():
            return

        try:
            self.save()

            logger.info(
                "%s saved successfully. Record ID: %s",
                self.ENTITY_NAME,
                self.record_id
            )

            self.accept()

        except ValueError as error:
            logger.warning(
                "Validation or business-rule error while saving %s: %s",
                self.ENTITY_NAME,
                error
            )

            self.warning(
                self.ENTITY_NAME,
                str(error)
            )

        except Exception as error:
            logger.exception(
                "Unexpected error while saving %s.",
                self.ENTITY_NAME
            )

            self.error(
                self.ENTITY_NAME,
                f"Unexpected error:\n\n{error}"
            )

    def set_read_only(self, *widgets):

        for widget in widgets:
            widget.setReadOnly(True)

    def set_focus(self, widget):
        widget.setFocus()

        if hasattr(widget, "selectAll"):
            widget.selectAll()