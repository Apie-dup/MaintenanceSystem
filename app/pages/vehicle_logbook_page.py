from PySide6.QtWidgets import QFileDialog
from app.base.crud_page import CrudPage
from app.services.vehicle_logbook_service import (
    VehicleLogbookService
)
from app.ui.generated.ui_vehicle_logbook_page import (
    Ui_VehicleLogbookPage
)
from app.dialogs.vehicle_logbook_dialog import (
    VehicleLogbookDialog
)
from app.helpers.pdf_report_export_helper import (
    PdfReportExportHelper
)
from app.services.message_service import (
    MessageService
)
from app.dialogs.print_vehicle_logbook_dialog import(
    PrintVehicleLogbookDialog
)
from app.dialogs.work_order_dialog import (
    WorkOrderDialog
)

class VehicleLogbookPage(CrudPage):

    PAGE_TITLE = "Vehicle Logbook"

    ENTITY_NAME = "Vehicle Logbook Entry"

    RECORD_NAME = "vehicle logbook entries"

    TABLE_COLUMNS = [
        ("log_date", "Date"),
        ("asset_number", "Asset No."),
        ("asset_name", "Vehicle"),
        ("driver_name", "Driver"),
        ("origin", "From"),
        ("destination", "To"),
        ("start_meter", "Start km"),
        ("end_meter", "End km"),
        ("distance", "Distance"),
        ("purpose", "Purpose"),
        ("fuel_quantity", "Fuel"),
        ("work_order_number", "Work Order"),
        ("defect_status", "Defect / Fault"),
    ]

    SEARCH_FIELDS = [
        "asset_number",
        "asset_name",
        "driver_name",
        "origin",
        "destination",
        "purpose",
        "defect_reported",
    ]

    def __init__(
        self,
        user=None,
        parent=None,
    ):
        super().__init__(
            parent
        )

        self.user = user

        self.ui = Ui_VehicleLogbookPage()
        self.ui.setupUi(self)

        self.service = (
            VehicleLogbookService
        )

        # We will add this in the next step.
        self.dialog_class = VehicleLogbookDialog

        self.table = self.ui.tblLogbook
        self.search_widget = (
            self.ui.txtSearch
        )

        self.entity_name = (
            "Vehicle Logbook Entry"
        )

        self.record_name = (
            "vehicle logbook entries"
        )

        self.setup_page()

    def setup_page(self):

        self.setup_table()

        self.connect_signals()

        self.load_data()

        self.update_work_order_buttons()

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

        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.btnCreateWorkOrder.clicked.connect(
            self.create_work_order
        )

        self.ui.btnOpenWorkOrder.clicked.connect(
            self.open_work_order
        )

        self.ui.tblLogbook.itemSelectionChanged.connect(
            self.update_work_order_buttons
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.ui.tblLogbook.itemDoubleClicked.connect(
            self.edit_record
        )

        self.ui.btnPrint.clicked.connect(
            self.print_logbook
        )

    def print_logbook(self):

        # -------------------------------------------------
        # Select vehicle and period
        # -------------------------------------------------

        dialog = PrintVehicleLogbookDialog(
            self
        )

        if not dialog.exec():
            return

        asset_id = dialog.asset_id()
        asset_text = dialog.asset_text()
        from_date = dialog.from_date()
        to_date = dialog.to_date()

        # -------------------------------------------------
        # Get filtered logbook records
        # -------------------------------------------------

        records = (
            VehicleLogbookService
            .get_by_asset_and_date_range(
                asset_id,
                from_date,
                to_date
            )
        )

        if not records:
            MessageService.warning(
                self,
                "Vehicle Logbook",
                (
                    "No logbook entries were found "
                    "for the selected vehicle and period."
                )
            )
            return

        # -------------------------------------------------
        # Save file
        # -------------------------------------------------

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Vehicle Logbook",
            "Vehicle_Logbook.pdf",
            "PDF Files (*.pdf)"
        )

        if not file_path:
            return

        if not file_path.lower().endswith(
            ".pdf"
        ):
            file_path += ".pdf"

        # -------------------------------------------------
        # Create PDF
        # -------------------------------------------------

        try:

            PdfReportExportHelper.export_vehicle_logbook_to_pdf(
                records=records,
                file_path=file_path,
                asset_text=asset_text,
                from_date=from_date,
                to_date=to_date,
            )

            MessageService.information(
                self,
                "Vehicle Logbook",
                "Vehicle Logbook exported successfully."
            )

        except Exception as error:

            MessageService.error(
                self,
                "Vehicle Logbook",
                (
                    "Unable to export "
                    "Vehicle Logbook.\n\n"
                    f"{error}"
                )
            )

    def create_work_order(self):

        record_id = self.require_selection()

        if record_id is None:
            return

        logbook = VehicleLogbookService.get_by_id(
            record_id
        )

        if logbook is None:
            MessageService.error(
                self,
                "Vehicle Logbook",
                "Unable to load the selected logbook entry."
            )
            return

        # ---------------------------------------------------------
        # Prevent duplicate Work Order
        # ---------------------------------------------------------

        if logbook["work_order_id"] is not None:
            MessageService.warning(
                self,
                "Vehicle Logbook",
                (
                    "A Work Order has already been created "
                    "from this logbook entry."
                )
            )
            return

        # ---------------------------------------------------------
        # Open Work Order dialog
        # ---------------------------------------------------------

        dialog = WorkOrderDialog(self)

        dialog.new_from_logbook(
            logbook
        )

        if dialog.exec():

            VehicleLogbookService.link_work_order(
                record_id,
                dialog.record_id
            )

            MessageService.information(
                self,
                "Vehicle Logbook",
            (
                    "Work Order created and linked "
                    "successfully."
            )
        )

        self.load_data()

    def open_work_order(self):

        record_id = self.require_selection()

        if record_id is None:
            return

        logbook = VehicleLogbookService.get_by_id(
            record_id
        )

        if logbook is None:
            MessageService.error(
                self,
                "Vehicle Logbook",
                "Unable to load the selected logbook entry."
            )
            return

        work_order_id = logbook["work_order_id"]

        if work_order_id is None:
            MessageService.warning(
                self,
                "Vehicle Logbook",
                (
                    "This logbook entry does not have "
                    "a linked Work Order."
                )
            )
            return

        dialog = WorkOrderDialog(self)

        dialog.edit_record(
            work_order_id
        )

        if dialog.exec():
            self.load_data()

    def update_work_order_buttons(self):

        record_id = self.selected_id()

        # Nothing selected
        if record_id is None:
            self.ui.btnCreateWorkOrder.setEnabled(False)
            self.ui.btnOpenWorkOrder.setEnabled(False)
            return

        logbook = VehicleLogbookService.get_by_id(
            record_id
        )

        if logbook is None:
            self.ui.btnCreateWorkOrder.setEnabled(False)
            self.ui.btnOpenWorkOrder.setEnabled(False)
            return

        has_work_order = (
            logbook["work_order_id"] is not None
        )

        self.ui.btnCreateWorkOrder.setEnabled(
            not has_work_order
        )

        self.ui.btnOpenWorkOrder.setEnabled(
            has_work_order
        )

    def show_unresolved_defects(self):

        records = (
            VehicleLogbookService
            .get_unresolved_defects()
        )

        self.populate_table(records)

        self.update_work_order_buttons()

    def show_all(self):

        if self.search_widget is not None:
            self.search_widget.clear()

        self.load_data()

        self.update_work_order_buttons()