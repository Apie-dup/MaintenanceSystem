from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QFormLayout, QSizePolicy,QDialogButtonBox

from app.base.base_dialog import BaseDialog
from app.core.lookup_manager import LookupManager
from app.helpers.form_helper import FormHelper
from app.services.validation_service import ValidationService
from app.services.work_order_service import WorkOrderService
from app.ui.generated.ui_add_work_order import Ui_AddWorkOrderDialog
from app.services.work_order_parts_service import WorkOrderPartService
from app.helpers.table_helper import TableHelper
from app.dialogs.issue_part_dialog import IssuePartDialog
from app.helpers.format_helper import FormatHelper
from app.services.work_order_history_service import WorkOrderHistoryService
from app.helpers.form_helper import FormHelper



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

    HISTORY_COLUMNS = [
        ("created_at", "Date / Time"),
        ("action", "Action"),
        ("field_name", "Field"),
        ("old_value", "Previous"),
        ("new_value", "New"),
        ("notes", "Notes"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddWorkOrderDialog()
        self.ui.setupUi(self)

        FormHelper.apply(self)

        FormHelper.apply_large_dialog(
            self
        )

        self.apply_form_standards()
        self.setup_dialog()

        # Add mode has no persisted work order yet, so material actions
        # are enabled only after opening an existing record.
        self.ui.groupMaterials.setEnabled(False)

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.setWindowFlag(
            Qt.WindowType.WindowMaximizeButtonHint,
            True,
        )
        

        self.load_lookup_values()
        self.restrict_status_options()
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

        for layout_name in (
            "formGeneralInfo",
            "formAssignment",
        ):
            form_layout = getattr(self.ui, layout_name, None)
            if form_layout is not None:
                form_layout.setRowWrapPolicy(
                    QFormLayout.RowWrapPolicy.WrapLongRows)
                form_layout.setVerticalSpacing(12)

        if hasattr(self.ui, "gridDatesCosts"):
            self.ui.gridDatesCosts.setColumnStretch(1, 1)
            self.ui.gridDatesCosts.setColumnStretch(3, 1)

        TableHelper.setup(
            self.ui.tblParts,
            self.PART_COLUMNS
        )

        TableHelper.setup(
            self.ui.tblHistory,
            self.HISTORY_COLUMNS
        )

        self.ui.tblHistory.setEnabled(False)
        

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

        self.ui.btnComplete.clicked.connect(
            self.complete_work_order
        )

        self.ui.btnCloseWorkOrder.clicked.connect(
            self.close_work_order
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

        if dialog.exec():
            self.load_record(
                self.record_id
            )

        self.load_parts()
        self.load_history()

        work_order = WorkOrderService.get_by_id(
            self.record_id
        )

        if work_order is not None:
            self.ui.dsbActualCost.setValue(
                float(work_order["actual_cost"] or 0)
            )

        self.load_history()

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

        self.load_history()

    # ---------------------------------------------------------
    # Lookup values
    # ---------------------------------------------------------

    def load_lookup_values(self):
        LookupManager.load(
            self.ui.cmbPriority,
            "Priorities",
            [
                "Low",
                "Medium",
                "High",
                "Critical"
            ]
        )

        LookupManager.load(
            self.ui.cmbStatus,
            "Work Order Statuses",
            [
                "Open",
                "Assigned",
                "In Progress",
                "On Hold",
                "Completed",
                "Closed",
                "Cancelled"
            ]
        )

    def restrict_status_options(
            self,
            current_status=None,
        ):

            """
            Completed and Closed are controlled by
            """
            protected_statuses = {
                "Completed",
                "Closed",
            }

            for status in protected_statuses:

                # Keep the current status visible when
                # viewing an existing work order

                if status == current_status:
                    continue

                index = self.ui.cmbStatus.findText(
                    status
                )

                if index >= 0:
                    self.ui.cmbStatus.removeItem(
                        index
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

        TableHelper.populate(
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

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):

        self.ui.groupMaterials.setEnabled(False)
        self.ui.cmbAsset.setEnabled(True)

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

        self.restrict_status_options()

        self.ui.cmbStatus.setCurrentText("Open")

        today = QDate.currentDate()

        self.ui.dtDateCreated.setDate(today)
        self.ui.dtDueDate.setDate(
            today.addDays(7)
        )

        self.ui.dsbEstimatedCost.setValue(0.00)
        self.ui.dsbActualCost.setValue(0.00)
        self.ui.dsbLabourHours.setValue(0.00)

        self.ui.btnComplete.setEnabled(False)
        self.ui.btnCloseWorkOrder.setEnabled(False)

        self.set_focus(
            self.ui.txtTitle
        )

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

        # Work orders generated from PM should keep their asset fixed.
        self.ui.cmbAsset.setEnabled(
            not bool(work_order["pm_id"])
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
    # Read-only state
    # ---------------------------------------------------------

    def set_work_order_read_only(self, read_only):

        # General information
        self.ui.txtTitle.setReadOnly(
            read_only
        )

        self.ui.teDescription.setReadOnly(
            read_only
        )

        self.ui.cmbPriority.setEnabled(
            not read_only
        )

        self.ui.cmbStatus.setEnabled(
            not read_only
        )

        # Assignment
        self.ui.cmbAsset.setEnabled(
            not read_only
        )

        self.ui.cmbTechnician.setEnabled(
            not read_only
        )

        self.ui.txtRequestedBy.setReadOnly(
            read_only
        )

        # Dates and costs
        self.ui.dtDateCreated.setEnabled(
            not read_only
        )

        self.ui.dtDueDate.setEnabled(
            not read_only
        )

        self.ui.dsbEstimatedCost.setReadOnly(
            read_only
        )

        # Actual Cost should always be system controlled
        self.ui.dsbActualCost.setReadOnly(
            True
        )

        self.ui.dsbLabourHours.setReadOnly(
            read_only
        )

        # Notes
        self.ui.teNotes.setReadOnly(
            read_only
        )

        # Materials
        self.ui.groupMaterials.setEnabled(
            not read_only
        )

        # Save button
        save_button = self.ui.buttonBox.button(
            self.ui.buttonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setEnabled(
                not read_only
            )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):

        self.ui.tabWorkOrder.setTabEnabled(
            1,
            False
        )

        self.ui.tabWorkOrder.setTabEnabled(
            2,
            False
        )

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

        self.restrict_status_options(
            work_order["status"]
        )

        self.set_form_data(
            work_order
        )

        self.ui.groupMaterials.setEnabled(True)
        self.ui.groupHistory.setEnabled(True)

        self.load_parts()
        self.load_history()

        status = work_order["status"]

        self.ui.btnComplete.setEnabled(
            status not in {
                "Completed",
                "Closed",
                "Cancelled",
            }
        )

        self.ui.btnCloseWorkOrder.setEnabled(
            status == "Completed"
        )

        if status == "Completed":
            self.ui.cmbStatus.setEnabled(False)

        self.set_work_order_read_only(
            status == "Closed"
        )

        self.ui.tabWorkOrder.setTabEnabled(
            1,
            True
        )

        self.ui.tabWorkOrder.setTabEnabled(
            2,
            True
        )

    def load_history(self):

        if self.record_id is None:
            return

        records = WorkOrderHistoryService.get_history(
            self.record_id
        )

        TableHelper.populate(
            self.ui.tblHistory,
            records,
            self.HISTORY_COLUMNS
        )

        self.format_history_values()

        self.ui.tblHistory.clearSelection()

    def format_history_values(self):

        field_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "field_name"
            ),
            None
        )

        old_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "old_value"
            ),
            None
        )

        new_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.HISTORY_COLUMNS)
                if field == "new_value"
            ),
            None
        )

        if (
            field_column is None
            or old_column is None
            or new_column is None
        ):
            return

        for row in range(
            self.ui.tblHistory.rowCount()
        ):

            field_item = self.ui.tblHistory.item(
                row,
                field_column
            )

            if field_item is None:
                continue

            field_name = field_item.text().strip()

            old_item = self.ui.tblHistory.item(
                row,
                old_column
            )

            new_item = self.ui.tblHistory.item(
                row,
                new_column
            )

            if field_name in {
                "Estimated Cost",
                "Actual Cost",
            }:

                for item in (
                    old_item,
                    new_item,
                ):
                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text() or 0
                        )

                        item.setText(
                            FormatHelper.currency(
                                value
                            )
                        )

                    except ValueError:
                        pass

            elif field_name == "Labour Hours":

                for item in (
                    old_item,
                    new_item,
                ):
                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text() or 0
                        )

                        item.setText(
                            FormatHelper.quantity(
                                value
                            )
                        )
                    except ValueError:
                        pass
                

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
            self.record_id = WorkOrderService.create(data)
            self.ui.groupMaterials.setEnabled(True)

        else:
            WorkOrderService.update(
                self.record_id,
                data
            )

    def selected_part_id(self):

        return TableHelper.selected_id(
            self.ui.tblParts
        )

    def complete_work_order(self):

        if self.record_id is None:
            self.warning(
                "Complete Work Order",
                "Please save the Work Order first."
            )
            return

        if not self.confirm(
            "Complete Work Order",
            (
                "Mark this Work Order as completed?\n\n"
                "If this Work Order was generated from "
                "Preventive Maintenance, the PM schedule "
                "will also be advanced."
            )
        ):
            return

        try:
            WorkOrderService.complete_work_order(
                self.record_id
            )

        except ValueError as error:
            self.warning(
                "Complete Work Order",
                str(error)
            )
            return

        except Exception as error:
            self.error(
                "Complete Work Order",
                f"Could not complete the Work Order.\n\n{error}"
            )
            return

        self.information(
            "Complete Work Order",
            "Work Order completed successfully."
        )

        self.load_record(
            self.record_id
        )


    def close_work_order(self):

        if self.record_id is None:
            return

        if not self.confirm(
            "Close Work Order",
            (
                "Close this Work Order?\n\n"
                "A closed Work Order should no longer be edited."
            )
        ):
            return

        try:
            WorkOrderService.close_work_order(
                self.record_id
            )

        except ValueError as error:
            self.warning(
                "Close Work Order",
                str(error)
            )
            return

        except Exception as error:
            self.error(
                "Close Work Order",
                f"Could not close the Work Order.\n\n{error}"
            )
            return

        self.information(
            "Close Work Order",
            "Work Order closed successfully."
        )

        self.load_record(
            self.record_id
        )   