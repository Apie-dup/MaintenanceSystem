from app.base.base_page import BasePage


class ModulePage(BasePage):

    def __init__(self):
        super().__init__()

        self.table = None
        self.status_label = None
        self.record_name = "records"

    def setup_module(
        self,
        table,
        status_label=None,
        record_name="records"
    ):

        self.table = table
        self.status_label = status_label
        self.record_name = record_name

        self.setup_table(table)

    def show_records(self, records):

        self.populate_table(
            self.table,
            records,
            self.status_label,
            self.record_name
        )

    def select_record(self):

        return self.selected_id(self.table)

    def refresh(self):
        """
        Override in child classes.
        """
        pass