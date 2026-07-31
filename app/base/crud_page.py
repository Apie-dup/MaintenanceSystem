from PySide6.QtCore import Qt

from app.base.base_page import BasePage
from app.helpers.table_helper import TableHelper


class CrudPage(BasePage):

    PAGE_TITLE = ""

    # Example:
    # [
    #     ("supplier_code", "Code"),
    #     ("supplier_name", "Supplier Name"),
    # ]
    TABLE_COLUMNS = []

    SEARCH_FIELDS = []

    def __init__(self, parent=None):
        super().__init__(parent)

        self.service = None
        self.dialog_class = None
        self.dialog = None
        self.table = None
        self.search_widget = None
        self.status_label = None

        # Use singular and plural names separately.
        self.entity_name = "Record"
        self.record_name = "records"

    # -------------------------------------------------
    # Validate page configuration
    # -------------------------------------------------

    def validate_configuration(self):

        if self.service is None:
            raise RuntimeError(
                f"{self.__class__.__name__}: service is not configured."
            )

        if self.dialog_class is None and self.dialog is None:
            raise RuntimeError(
                f"{self.__class__.__name__}: dialog class is not configured."
            )

        if self.table is None:
            raise RuntimeError(
                f"{self.__class__.__name__}: table is not configured."
            )
    # ---------------------------------------------------------
    # Table setup
    # ---------------------------------------------------------

    def setup_table(self):

        TableHelper.setup(
            self.table,
            self.TABLE_COLUMNS
        )

    # ---------------------------------------------------------
    # Load data
    # ---------------------------------------------------------

    def load_data(self):

        records = self.service.get_all()

        self.populate_table(records)

    def populate_table(self, records):

        TableHelper.populate_table(
            self.table,
            records,
            self.TABLE_COLUMNS
        )

        if self.status_label is not None:

            count = len(records)

            if count == 1:
                text = f"1 {self.entity_name.lower()}"
            else:
                text = f"{count} {self.record_name}"

            self.status_label.setText(text)
            

    # ---------------------------------------------------------
    # Status label
    # ---------------------------------------------------------

    def update_status_label(self, record_count):
        if self.status_label is None:
            return

        label = self.record_name

        if record_count == 1:
            label = self.entity_name.lower()

        self.status_label.setText(
            f"{record_count} {label}"
        )

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self):
        if self.search_widget is not None:

            if self.search_widget.text().strip():

               self.search_widget.clear()

            else:
               self.load_data()

        else:

            self.load_data()

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(self, text=None):

        if text is None:

            if self.search_widget is not None:
                text = self.search_widget.text()

            else:
                text = ""

        text = text.strip()

        if text:
            records = self.service.search(text)
        else:
            records = self.service.get_all()

        self.populate_table(records)

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def selected_id(self):

        return TableHelper.selected_id(self.table)

    def selected_row(self):

        return TableHelper.selected_row(self.table)

    def require_selection(self):
        record_id = self.selected_id()

        if record_id is None:
            self.warning(
                self.PAGE_TITLE or self.entity_name,
                f"Please select a {self.entity_name.lower()}."
            )
            return None

        return record_id

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    def add_record(self):
        dialog_cls = self.dialog_class or self.dialog

        dialog = dialog_cls(self)

        dialog.new_record()

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Edit
    # ---------------------------------------------------------

    def edit_record(self):

        record_id = self.selected_id()

        if record_id is None:

            self.warning(
                "Edit",
                f"Please select a {self.entity_name.lower()}."
            )
            return

        dialog_cls = self.dialog_class or self.dialog

        dialog = dialog_cls(self)

        dialog.edit_record(record_id)

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete_record(self):

        record_id = self.require_selection()

        if record_id is None:

            self.warning(
                "Delete",
                f"Please select a {self.entity_name.lower()}."
            )

            return

        if not self.confirm_delete(
            "Delete",
            f"Delete selected {self.entity_name.lower()}?"
        ):
            return

        self.service.delete(record_id)

        self.information(
            "Delete",
            f"{self.entity_name} deleted successfully."
        )

        self.load_data()