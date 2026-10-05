from app.base.crud_page import CrudPage
from app.services.vehicle_sop_service import (
    VehicleSopService
)
from app.ui.generated.ui_vehicle_sop_page import (
    Ui_VehicleSopPage
)
from app.dialogs.vehicle_sop_dialog import (
    VehicleSopDialog
)
from app.dialogs.vehicle_sop_checklist_dialog import (
    VehicleSopChecklistDialog
)
from app.helpers.table_helper import TableHelper


class VehicleSopPage(CrudPage):

    PAGE_TITLE = "Vehicle SOPs"

    ENTITY_NAME = "Vehicle SOP"

    RECORD_NAME = "vehicle SOPs"

    TABLE_COLUMNS = [
        ("sop_number", "SOP Number"),
        ("asset_number", "Asset No."),
        ("asset_name", "Vehicle / Asset"),
        ("sop_name", "SOP Name"),
        ("frequency", "Frequency"),
        ("active", "Active"),
    ]

    SEARCH_FIELDS = [
        "sop_number",
        "asset_number",
        "asset_name",
        "sop_name",
        "frequency",
    ]

    def __init__(
        self,
        user=None,
        parent=None,
    ):
        super().__init__(parent)

        self.user = user

        self.ui = Ui_VehicleSopPage()
        self.ui.setupUi(self)

        self.service = VehicleSopService

        self.dialog_class = VehicleSopDialog

        self.table = self.ui.tblVehicleSops
        self.search_widget = self.ui.txtSearch

        self.entity_name = "Vehicle SOP"
        self.record_name = "vehicle SOPs"

        self.setup_page()

    def setup_page(self):

        self.setup_table()

        self.connect_signals()

        self.load_data()

    def connect_signals(self):

        self.ui.txtSearch.textChanged.connect(
            self.search
        )

        self.ui.btnAdd.clicked.connect(
            self.add_record
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_record
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.tblVehicleSops.itemDoubleClicked.connect(
            self.edit_record
        )

        self.ui.btnChecklist.clicked.connect(
            self.open_checklist
        )

    def open_checklist(self):

        record_id = self.require_selection()

        if record_id is None:
            return

        dialog = VehicleSopChecklistDialog(
            record_id,
            self
        )

        dialog.exec()

        self.load_data()

    def populate_table(self, records):

        display_records = []

        for record in records:

            item = dict(record)

            item["active"] = (
                "Yes"
                if item["active"]
                else "No"
            )

            display_records.append(item)

        TableHelper.populate(
            self.table,
            display_records,
            self.TABLE_COLUMNS
        )