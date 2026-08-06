from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QDialog, QWidget

from app.core.logger import logger
from app.helpers.form_helper import FormHelper
from app.services.message_service import MessageService


class BaseDialog(QDialog):
    """
    Base class for all Add/Edit dialogs.

    Provides:
    - Add and Edit modes
    - Standard dialog titles
    - Shared save workflow
    - Message helpers
    - Form standards
    - Ctrl+S and Escape shortcuts
    """

    ENTITY_NAME = "Record"

    def __init__(self, record_id=None, parent=None):

        # Supports:
        # Dialog(parent)
        # Dialog(record_id, parent)
        if (
            parent is None
            and isinstance(record_id, QWidget)
        ):
            parent = record_id
            record_id = None

        super().__init__(parent)

        self.record_id = record_id

        self.setModal(True)

        self._setup_shortcuts()

    # ---------------------------------------------------------
    # Mode
    # ---------------------------------------------------------

    @property
    def is_add(self):
        return self.record_id is None

    @property
    def is_edit(self):
        return self.record_id is not None

    # ---------------------------------------------------------
    # Entity
    # ---------------------------------------------------------

    def set_entity_name(self, entity_name):
        self.ENTITY_NAME = entity_name

    # ---------------------------------------------------------
    # Public workflow
    # ---------------------------------------------------------

    def new_record(self):
        """
        Prepare the dialog for creating a new record.
        """
        self.record_id = None

        self.setWindowTitle(
            f"Add {self.ENTITY_NAME}"
        )

        self.clear_fields()

    def edit_record(self, record_id):
        """
        Prepare the dialog for editing an existing record.
        """
        self.record_id = record_id

        self.setWindowTitle(
            f"Edit {self.ENTITY_NAME}"
        )

        self.load_record(record_id)

    # ---------------------------------------------------------
    # Save workflow
    # ---------------------------------------------------------

    def save_and_close(self):

        if not self.validate():
            return

        try:
            self.save()

            logger.info(
                "%s saved successfully. Record ID: %s",
                self.ENTITY_NAME,
                self.record_id,
            )

            self.accept()

        except ValueError as error:
            logger.warning(
                "Business-rule error while saving %s: %s",
                self.ENTITY_NAME,
                error,
            )

            self.warning(
                self.ENTITY_NAME,
                str(error),
            )

        except Exception as error:
            logger.exception(
                "Unexpected error while saving %s.",
                self.ENTITY_NAME,
            )

            self.error(
                self.ENTITY_NAME,
                f"Unexpected error:\n\n{error}",
            )

    # ---------------------------------------------------------
    # Required child methods
    # ---------------------------------------------------------

    def clear_fields(self):
        raise NotImplementedError(
            "clear_fields() must be implemented."
        )

    def get_form_data(self):
        raise NotImplementedError(
            "get_form_data() must be implemented."
        )

    def set_form_data(self, data):
        raise NotImplementedError(
            "set_form_data() must be implemented."
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
    # Message helpers
    # ---------------------------------------------------------

    def information(self, title, message):
        MessageService.information(
            self,
            title,
            message,
        )

    def warning(self, title, message):
        MessageService.warning(
            self,
            title,
            message,
        )

    def error(self, title, message):
        MessageService.error(
            self,
            title,
            message,
        )

    def confirm(self, title, message):
        return MessageService.confirm(
            self,
            title,
            message,
        )

    # ---------------------------------------------------------
    # Form helpers
    # ---------------------------------------------------------

    def apply_form_standards(self):
        FormHelper.apply(self)

    @staticmethod
    def set_read_only(*widgets):
        for widget in widgets:
            widget.setReadOnly(True)

    @staticmethod
    def set_focus(widget):

        if hasattr(widget, "selectAll"):
            widget.selectAll()

    # ---------------------------------------------------------
    # Keyboard shortcuts
    # ---------------------------------------------------------

    def _setup_shortcuts(self):

        self.save_shortcut = QShortcut(
            QKeySequence.StandardKey.Save,
            self,
        )

        self.save_shortcut.activated.connect(
            self.save_and_close
        )

        self.close_shortcut = QShortcut(
            QKeySequence.StandardKey.Cancel,
            self,
        )

        self.close_shortcut.activated.connect(
            self.reject
        )