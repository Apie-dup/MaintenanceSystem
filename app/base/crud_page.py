from app.base.base_page import BasePage
from app.helpers.table_helper import TableHelper


class CrudPage(BasePage):
    """
    Generic page for standard CRUD modules.
    """

    PAGE_TITLE = ""
    TABLE_COLUMNS = []
    SEARCH_FIELDS = []

    def __init__(self, parent=None):
        super().__init__(parent)

        self.service = None
        self.dialog_class = None
        self.table = None
        self.search_widget = None
        self.status_label = None

        self.entity_name = getattr(
            self,
            "ENTITY_NAME",
        ) or "Record"

        self.record_name = getattr(
            self,
            "RECORD_NAME",
        ) or "records"

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    def validate_configuration(self):
        if self.service is None:
            raise ValueError(
                f"{self.__class__.__name__}: service is not configured."
            )

        if self.dialog_class is None:
            raise ValueError(
                f"{self.__class__.__name__}: dialog_class is not configured."
            )

        if self.table is None:
            raise ValueError(
                f"{self.__class__.__name__}: table is not configured."
            )

        if not self.TABLE_COLUMNS:
            raise ValueError(
                f"{self.__class__.__name__}: TABLE_COLUMNS is empty."
            )

    # ---------------------------------------------------------
    # Table
    # ---------------------------------------------------------

    def setup_table(self):
        TableHelper.setup(
            self.table,
            self.TABLE_COLUMNS
        )

    def populate_table(self, records):
        TableHelper.populate(
            self.table,
            records,
            self.TABLE_COLUMNS
        )

        self.update_status_label(
            len(records)
        )

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    def update_status_label(self, count):
        if self.status_label is None:
            return

        if count == 1:
            text = self.entity_name.lower()
        else:
            text = self.record_name.lower()

        self.status_label.setText(
            f"{count} {text}"
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_data(self):
        records = self.service.get_all()
        self.populate_table(records)

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(self, text):
        text = text.strip()

        if text:
            records = self.service.search(text)
        else:
            records = self.service.get_all()

        self.populate_table(records)

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self):
        if self.search_widget is not None:
            self.search_widget.clear()

        self.load_data()

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def selected_id(self):
        return TableHelper.selected_id(
            self.table
        )

    def require_selection(self):
        record_id = self.selected_id()

        if record_id is not None:
            return record_id

        self.warning(
            self.entity_name,
            (
                f"Please select a "
                f"{self.entity_name.lower()}."
            )
        )

        return None

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    def add_record(self):
        dialog = self.dialog_class(self)
        dialog.new_record()

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Edit
    # ---------------------------------------------------------

    def edit_record(self):
        record_id = self.require_selection()

        if record_id is None:
            return

        dialog = self.dialog_class(self)
        dialog.edit_record(record_id)

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete_record(self):
        record_id = self.require_selection()

        if record_id is None:
            return

        if not self.confirm(
            f"Delete {self.entity_name}",
            (
                f"Are you sure you want to delete this "
                f"{self.entity_name.lower()}?"
            )
        ):
            return

        try:
            self.service.delete(record_id)

        except Exception as error:
            self.error(
                f"Delete {self.entity_name}",
                (
                    f"Could not delete the "
                    f"{self.entity_name.lower()}.\n\n"
                    f"{error}"
                )
            )
            return

        self.information(
            f"Delete {self.entity_name}",
            (
                f"{self.entity_name} deleted "
                "successfully."
            )
        )

        self.load_data()