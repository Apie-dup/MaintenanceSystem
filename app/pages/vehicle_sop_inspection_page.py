from app.base.crud_page import CrudPage
from app.services.vehicle_sop_inspection_service import (
    VehicleSopInspectionService
)
from app.ui.generated.ui_vehicle_sop_inspection_page import (
    Ui_VehicleSopInspectionPage
)
from app.helpers.table_helper import TableHelper
from app.dialogs.vehicle_sop_inspection_dialog import (
    VehicleSopInspectionDialog
)
from app.services.message_service import MessageService


class VehicleSopInspectionPage(CrudPage):

    PAGE_TITLE = "SOP Inspections"
    
    ENTITY_NAME = "SOP Inspection"

    RECORD_NAME = "sop inspection"

    TABLE_COLUMNS = [
        ("inspection_number", "Inspection No."),
        ("inspection_date", "Date"),
        ("asset_number", "Asset No."),
        ("asset_name", "Vehicle / Asset"),
        ("sop_name", "SOP"),
        ("frequency", "Frequency"),
        ("operator_name", "Operator"),
        ("status", "Status"),
    ]

    SEARCH_FIELDS = [
        "inspection_number",
        "inspection_date",
        "asset_number",
        "asset_name",
        "sop_number",
        "sop_name",
        "frequency",
        "operator_name",
        "status",
    ]

    def __init__(
        self,
        user=None,
        parent=None
    ):
        super().__init__(
            parent=parent
        )

        self.user = user

        self.ui = Ui_VehicleSopInspectionPage()
        self.ui.setupUi(self)

        self.service = (
            VehicleSopInspectionService
        )

        self.table = self.ui.tblInspections
        self.search_widget = self.ui.txtSearch

        self.entity_name = "SOP Inspection"
        self.record_name = "SOP inspections"

        self.setup_page()
        self.connect_signals()
        self.load_data()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_page(self):

        TableHelper.setup(
            self.table,
            self.TABLE_COLUMNS
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):

        self.ui.txtSearch.textChanged.connect(
            self.search
        )

        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.btnNew.clicked.connect(
            self.new_inspection
        )

        self.ui.btnOpen.clicked.connect(
            self.open_inspection
        )

        self.ui.tblInspections.itemDoubleClicked.connect(
            self.open_inspection
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_inspection
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_data(self):

        records = self.service.get_all()

        TableHelper.populate(
            self.table,
            records,
            self.TABLE_COLUMNS
        )

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(self, text=None):

        if text is None:
            text = (
                self.ui.txtSearch
                .text()
                .strip()
            )

        records = self.service.search(text)

        TableHelper.populate(
            self.table,
            records,
            self.TABLE_COLUMNS
        )

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self):

        self.ui.txtSearch.clear()
        self.load_data()

    # ---------------------------------------------------------
    # New inspection
    # ---------------------------------------------------------

    def new_inspection(self):

        dialog = VehicleSopInspectionDialog(
            user=self.user,
            parent=self
        )

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Open / View
    # ---------------------------------------------------------

    def open_inspection(self):

        inspection_id = TableHelper.selected_id(
            self.ui.tblInspections
        )

        if not inspection_id:
            return

        dialog = VehicleSopInspectionDialog(
            inspection_id=inspection_id,
            user=self.user,
            parent=self
        )

        if dialog.exec():
            self.load_data()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete_inspection(self):

        inspection_id = TableHelper.selected_id(
            self.ui.tblInspections
        )

        if not inspection_id:
            return

        inspection = (
            VehicleSopInspectionService.get_by_id(
                inspection_id
            )
        )

        if not inspection:
            return

        confirmed = MessageService.confirm(
            self,
            "Delete Inspection",
            (
                f'Delete inspection '
                f'{inspection["inspection_number"]}?'
            )
        )

        if not confirmed:
            return

        try:

            VehicleSopInspectionService.delete(
                inspection_id
            )

        except ValueError as error:

            MessageService.warning(
                self,
                "Cannot Delete Inspection",
                str(error)
            )

            return

        MessageService.information(
            self,
            "Inspection Deleted",
            "The inspection was deleted successfully."
        )

        self.load_data()