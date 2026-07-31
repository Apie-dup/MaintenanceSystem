from PySide6.QtWidgets import QDialog, QWidget

from app.services.message_service import MessageService


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
            self.accept()

        except ValueError as error:
            self.warning(
                self.ENTITY_NAME,
                str(error)
        )

        except Exception as error:
            self.error(
                self.ENTITY_NAME,
                f"Unexpected error:\n\n{error}"
        )