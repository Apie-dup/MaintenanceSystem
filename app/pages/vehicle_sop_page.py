from pathlib import Path

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
from PySide6.QtWidgets import QFileDialog

from app.services.vehicle_sop_item_service import (
    VehicleSopItemService
)
from app.helpers.pdf_report_export_helper import (
    PdfReportExportHelper
)
from app.services.message_service import MessageService


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

        self.ui.btnPrintInspectionForm.clicked.connect(
            self.print_inspection_form
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

    def print_inspection_form(self):

        record_id = self.require_selection()

        if record_id is None:
            return

        # ---------------------------------------------
        # Load SOP
        # ---------------------------------------------

        sop = VehicleSopService.get_by_id(
            record_id
        )

        if not sop:
            MessageService.warning(
                self,
                "Print Inspection Form",
                "The selected Vehicle SOP could not be found."
            )
            return

        # ---------------------------------------------
        # Load checklist
        # ---------------------------------------------

        items = VehicleSopItemService.get_by_sop_id(
            record_id
        )

        if not items:
            MessageService.warning(
                self,
                "Print Inspection Form",
                (
                    "This Vehicle SOP does not have any "
                    "checklist items."
                )
            )
            return

        # ---------------------------------------------
        # Suggested filename
        # ---------------------------------------------

        sop_number = (
            sop["sop_number"]
            or "SOP"
        )

        sop_name = (
            sop["sop_name"]
            or "Inspection"
        )

        safe_name = "".join(
            character
            if character.isalnum()
            or character in (" ", "-", "_")
            else "_"
            for character in sop_name
        ).strip()

        safe_name = safe_name.replace(
            " ",
            "_"
        )

        suggested_filename = (
            f"{sop_number}_"
            f"{safe_name}_Form.pdf"
        )

        # ---------------------------------------------
        # Select PDF location
        # ---------------------------------------------

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Inspection Form",
            suggested_filename,
            "PDF Files (*.pdf)"
        )

        if not file_path:
            return

        if not file_path.lower().endswith(
            ".pdf"
        ):
            file_path += ".pdf"

        # ---------------------------------------------
        # Generate PDF
        # ---------------------------------------------

        try:

            PdfReportExportHelper\
                .export_sop_inspection_form_to_pdf(
                    sop,
                    items,
                    file_path
                )

        except Exception as error:

            MessageService.error(
                self,
                "Print Inspection Form",
                (
                    "The inspection form could not be "
                    f"created.\n\n{error}"
                )
            )
            return

        # ---------------------------------------------
        # Success
        # ---------------------------------------------

        MessageService.information(
            self,
            "Inspection Form Created",
            (
                "The blank inspection form was created "
                "successfully.\n\n"
                f"{Path(file_path).name}"
            )
        )

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