from PySide6.QtCore import QDate

from app.base.base_dialog import BaseDialog
from app.core.lookup_manager import LookupManager
from app.services.validation_service import ValidationService
from app.services.work_order_service import WorkOrderService
from app.ui.generated.ui_add_work_order import Ui_AddWorkOrderDialog
from app.services.work_order_parts_service import WorkOrderPartService
from app.helpers.table_helper import TableHelper
from app.dialogs.issue_part_dialog import IssuePartDialog
from app.helpers.format_helper import FormatHelper


class WorkOrderDialog(BaseDialog):

    ENTITY_NAME = "Work Order"

    PART_COLUMNS = [
        ("part_number", "Part Number"),
        ("part_name", "Part Name"),
        ("quantity", "Qty"),
        ("unit", "Unit"),
        ("unit_cost", "Unit Cost"),
        ("total_cost", "Total"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddWorkOrderDialog()
        self.ui.setupUi(self)

        self.setup_dialog()

        # Add mode has no persisted work order yet, so material actions
        # are enabled only after opening an existing record.
        self.ui.groupMaterials.setEnabled(False)

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_lookup_values()
        self.load_assets()
        self.load_technicians()
        self.connect_signals()

        self.ui.txtWorkOrderNumber.setReadOnly(True)

        self.ui.dtDateCreated.setCalendarPopup(True)
        self.ui.dtDueDate.setCalendarPopup(True)

        self.ui.dsbEstimatedCost.setDecimals(2)
        self.ui.dsbActualCost.setDecimals(2)
        self.ui.dsbLabourHours.setDecimals(2)

        self.ui.dsbEstimatedCost.setMinimum(0)
        self.ui.dsbActualCost.setMinimum(0)
        self.ui.dsbLabourHours.setMinimum(0)

        TableHelper.setup(
            self.ui.tblParts,
            self.PART_COLUMNS
        )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.btnIssuePart.clicked.connect(
            self.issue_part
        )

        self.ui.btnRemovePart.clicked.connect(
            self.remove_part
        )

    def issue_part(self):

        if self.record_id is None:
            self.warning(
                "Issue Part",
                "Please save the work order before issuing parts."
            )
            return

        dialog = IssuePartDialog(
            self.record_id,
            self
        )

        if not dialog.exec():
            return

        self.load_parts()

        work_order = WorkOrderService.get_by_id(
            self.record_id
        )

        if work_order is not None:
            self.ui.dsbActualCost.setValue(
                float(work_order["actual_cost"] or 0)
            )
    def remove_part(self):
        issued_part_id = self.selected_part_id()

        if issued_part_id is None:
            self.warning(
                "Remove Part",
                "Please select an issued part."
            )
            return

        if not self.confirm(
            "Remove Part",
            (
                "Remove the selected part from this work order?\n\n"
                "The issued quantity will be returned to inventory."
            )
        ):
            return

        try:
            WorkOrderPartService.remove_part(
                issued_part_id
            )

        except ValueError as error:
            self.warning(
                "Remove Part",
                str(error)
            )
            return

        except Exception as error:
            self.error(
                "Remove Part",
                f"Could not remove the part.\n\n{error}"
            )
            return

        self.load_parts()

        # Refresh the displayed actual cost.
        work_order = WorkOrderService.get_by_id(
            self.record_id
        )

        if work_order is not None:
            self.ui.dsbActualCost.setValue(
                float(work_order["actual_cost"] or 0)
            )

        self.information(
            "Remove Part",
            "Part removed and inventory restored successfully."
        )

    # ---------------------------------------------------------
    # Lookup values
    # ---------------------------------------------------------

    def load_lookup_values(self):
        LookupManager.load(
            self.ui.cmbPriority,
            "Priorities"
        )

        LookupManager.load(
            self.ui.cmbStatus,
            "Statuses"
        )

    def load_assets(self):
        self.ui.cmbAsset.clear()

        assets = WorkOrderService.asset_lookup()

        for asset in assets:
            self.ui.cmbAsset.addItem(
                (
                    f'{asset["asset_number"]} - '
                    f'{asset["asset_name"]}'
                ),
                asset["id"]
            )

    def load_technicians(self):
        self.ui.cmbTechnician.clear()
        self.ui.cmbTechnician.addItem(
            "Unassigned",
            None
        )

        technicians = WorkOrderService.technician_lookup()

        for technician in technicians:
            self.ui.cmbTechnician.addItem(
                (
                    f'{technician["employee_number"]} - '
                    f'{technician["first_name"]} '
                    f'{technician["last_name"]}'
                ),
                technician["id"]
            )

    def load_parts(self):
        row = WorkOrderPartService.get_by_work_order(
            self.record_id
        )

        TableHelper.populate_table(
            self.ui.tblParts,
            row,
            self.PART_COLUMNS
        )

        total = WorkOrderPartService.get_total_cost(
            self.record_id
        )

        self.ui.lblMaterialTotal.setText(
            FormatHelper.currency(total)
        )

        unit_cost = WorkOrderPartService.get_total_unit_cost(
            self.record_id
        )

        self.ui.lblMaterialUnitCost.setText(
            FormatHelper.currency(unit_cost)
        )

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):

        self.ui.groupMaterials.setEnabled(False)

        self.ui.txtWorkOrderNumber.setText(
            WorkOrderService.get_next_work_order_number()
        )

        self.ui.txtTitle.clear()
        self.ui.teDescription.clear()
        self.ui.txtRequestedBy.clear()
        self.ui.teNotes.clear()

        if self.ui.cmbAsset.count() > 0:
            self.ui.cmbAsset.setCurrentIndex(0)

        self.ui.cmbTechnician.setCurrentIndex(0)

        self.ui.cmbPriority.setCurrentText("Low")
        self.ui.cmbStatus.setCurrentText("Open")

        today = QDate.currentDate()

        self.ui.dtDateCreated.setDate(today)
        self.ui.dtDueDate.setDate(
            today.addDays(7)
        )

        self.ui.dsbEstimatedCost.setValue(0.00)
        self.ui.dsbActualCost.setValue(0.00)
        self.ui.dsbLabourHours.setValue(0.00)

        self.ui.txtTitle.setFocus()

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "work_order_number":
                self.ui.txtWorkOrderNumber.text().strip(),

            "asset_id":
                self.ui.cmbAsset.currentData(),

            "title":
                self.ui.txtTitle.text().strip(),

            "description":
                self.ui.teDescription.toPlainText().strip(),

            "priority":
                self.ui.cmbPriority.currentText().strip(),

            "status":
                self.ui.cmbStatus.currentText().strip(),

            "technician_id":
                self.ui.cmbTechnician.currentData(),

            "requested_by":
                self.ui.txtRequestedBy.text().strip(),

            "date_created":
                self.ui.dtDateCreated.date().toString(
                    "yyyy-MM-dd"
                ),

            "due_date":
                self.ui.dtDueDate.date().toString(
                    "yyyy-MM-dd"
                ),

            "estimated_cost":
                self.ui.dsbEstimatedCost.value(),

            "actual_cost":
                self.ui.dsbActualCost.value(),

            "labour_hours":
                self.ui.dsbLabourHours.value(),

            "notes":
                self.ui.teNotes.toPlainText().strip(),
        }

    def set_form_data(self, work_order):
        self.ui.txtWorkOrderNumber.setText(
            work_order["work_order_number"]
        )

        self.ui.txtTitle.setText(
            work_order["title"] or ""
        )

        self.ui.teDescription.setPlainText(
            work_order["description"] or ""
        )

        self.ui.cmbPriority.setCurrentText(
            work_order["priority"] or "Low"
        )

        self.ui.cmbStatus.setCurrentText(
            work_order["status"] or "Open"
        )

        self.ui.txtRequestedBy.setText(
            work_order["requested_by"] or ""
        )

        self.set_date_value(
            self.ui.dtDateCreated,
            work_order["date_created"]
        )

        self.set_date_value(
            self.ui.dtDueDate,
            work_order["due_date"]
        )

        self.ui.dsbEstimatedCost.setValue(
            float(work_order["estimated_cost"] or 0)
        )

        self.ui.dsbActualCost.setValue(
            float(work_order["actual_cost"] or 0)
        )

        self.ui.dsbLabourHours.setValue(
            float(work_order["labour_hours"] or 0)
        )

        self.ui.teNotes.setPlainText(
            work_order["notes"] or ""
        )

        asset_index = self.ui.cmbAsset.findData(
            work_order["asset_id"]
        )

        if asset_index >= 0:
            self.ui.cmbAsset.setCurrentIndex(
                asset_index
            )

        technician_index = (
            self.ui.cmbTechnician.findData(
                work_order["technician_id"]
            )
        )

        if technician_index >= 0:
            self.ui.cmbTechnician.setCurrentIndex(
                technician_index
            )
        else:
            self.ui.cmbTechnician.setCurrentIndex(0)

    @staticmethod
    def set_date_value(date_widget, value):
        if not value:
            return

        date_value = QDate.fromString(
            value,
            "yyyy-MM-dd"
        )

        if date_value.isValid():
            date_widget.setDate(date_value)

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):

        self.ui.groupMaterials.setEnabled(True)

        work_order = WorkOrderService.get_by_id(
            record_id
        )

        if work_order is None:
            self.error(
                "Work Order",
                "Work order not found."
            )
            self.reject()
            return

        self.set_form_data(work_order)

        self.load_parts()

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if data["asset_id"] is None:
            self.warning(
                "Validation",
                "Asset is required."
            )
            self.ui.cmbAsset.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["title"],
                "Title"
            )
        ):
            self.ui.txtTitle.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["priority"],
                "Priority"
            )
        ):
            self.ui.cmbPriority.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["status"],
                "Status"
            )
        ):
            self.ui.cmbStatus.setFocus()
            return False

        if (
            self.ui.dtDueDate.date()
            < self.ui.dtDateCreated.date()
        ):
            self.warning(
                "Validation",
                "Due Date cannot be earlier than "
                "Date Created."
            )
            self.ui.dtDueDate.setFocus()
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            WorkOrderService.create(data)
        else:
            WorkOrderService.update(
                self.record_id,
                data
            )

    def selected_part_id(self):

        return TableHelper.selected_id(
            self.ui.tblParts
        )