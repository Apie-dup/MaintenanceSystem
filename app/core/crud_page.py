from app.core.base_page import BasePage


class CrudPage(BasePage):

    def __init__(self):
        super().__init__()

        self.service = None
        self.table = None
        self.status_label = None
        self.record_name = "records"

    # -------------------------------------------------
    # Load data
    # -------------------------------------------------

    def load_data(self):

        if self.service is None:
            return

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