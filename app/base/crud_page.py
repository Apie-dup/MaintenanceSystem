from app.base.base_page import BasePage


class CrudPage(BasePage):

    PAGE_TITLE = []

    # Table configuration
    TABLE_COLUMNS = []

    # Search configuration
    SEARCH_FIELDS = []


    def __init__(self, parent=None):
        super().__init__(parent)

        self.selected_id = None

        self.service = None
        self.dialog = None
        self.table = None
        self.status_label = None
        self.record_name = "records"

    # -------------------------------------------------
    # Load data
    # -------------------------------------------------

    def load_data(self):

        records = self.service.get_all()

        self.populate_table(
            self.table,
            records,
            self.status_label,
            self.record_name
        )

    # -------------------------------------------------
    # Refresh
    # -------------------------------------------------

    def refresh(self):
        self.load_data()

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(self, text):

        text = text.strip()

        if text:
            records = self.service.search(text)
        else:
            records = self.service.get_all()

        self.populate_table(
            self.table,
            records,
            self.status_label,
            self.record_name
        )

    # -------------------------------------------------
    # Add
    # -------------------------------------------------


    def add_record(self):

        dialog = self.dialog()

        if dialog.exec():
            self.load_data()

    # -------------------------------------------------
    # Edit
    # -------------------------------------------------
    
    def edit_record(self):

        record_id = self.selected_(self.table)

        if record_id is None:

            self.warning(
                "Ëdit",
                f"Please select a {self.record_name[:-1]}."
            )

            return
        
        dialog = self.dialog(record_id)

        if dialog.exec():
            self.load_data()

    def delete_record(self):

        row = self.selected_row(self.table)

        if row is None:

            self.warning(
                "Delete",
                f"Please select a {self.record_name[:-1]}."
            )

            return
        
        record_id = int(row[0])

        if not self.confirm_delete(
            "Delete",
            "Delete selected record?"
        ):
            return
        
        self.service.delete(record_id)

        self.information(
            "Delete",
            "Record deleted successfully."
        )

        self.load_data()