from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QSizePolicy,
    QInputDialog,
)

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
from app.services.settings_service import SettingsService
from app.core.permissions import Permissions
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)



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
        ("username", "User"),
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

        self.user = getattr(
            parent, 
            "user", 
            {}
        )

        if not self.user and parent is None:
            main_window = parent.window()

            self.user = getattr(
                main_window,
                "user",
                {}
            )

        self.role = self.user.get(
            "role",
            ""
        )

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
        self.apply_permissions()

        self.ui.txtWorkOrderNumber.setReadOnly(True)

        self.ui.dtDateCreated.setCalendarPopup(True)
        self.ui.dtDueDate.setCalendarPopup(True)

        self.ui.dsbEstimatedCost.setDecimals(2)
        self.ui.dsbActualCost.setDecimals(2)
        self.ui.dsbLabourHours.setDecimals(2)

        currency_symbol = SettingsService.currency_symbol()

        self.ui.dsbEstimatedCost.setPrefix(
            f"{currency_symbol} "
        )

        self.ui.dsbActualCost.setPrefix(
            f"{currency_symbol} "
        )

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

        self.ui.btnReopen.clicked.connect(
            self.reopen_work_order
        )

    def issue_part(self):

        if not Permissions.has_permission(
            self.role,
            "work_orders.issue_parts"
        ):
            self.warning(
                "Issue Part",
                "You do not have permission "
                "to issue parts."
            )
            return

        if self.record_id is None:
            self.warning(
                "Issue Part",
                "Please save the work order before issuing parts."
            )
            return

        dialog = IssuePartDialog(
            self.record_id,
            user=self.user,
            parent=self
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

        if work_order["status"] == "Closed":
            self.set_closed_mode()

    def remove_part(self):

        if not Permissions.has_permission(
            self.role,
            "work_orders.remove_parts"
        ):
            self.warning(
                "Remove Part",
                "You do not have permission "
                "to remove issued parts."
            )
            return
    
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
                issued_part_id,
                user=self.user
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
        Populate the status combo with satatuses that may be
        selected manually.

        Completed and Closed are controlled by their
        dedicated workflow actions, but the current status
        must remain visible when viewing an existing record.
        """

        allowed_statuses = [
            "Open",
            "Assigned",
            "In Progress",
            "On Hold",
            "Cancelled",
        ]

        # Complete and Close cannot be selected
        # manually, but must be visible for an existing
        # work order that already has that status.
        if current_status in {
            "Completed",
            "Closed",
        }:
            allowed_statuses.append(
                current_status
            )

        self.ui.cmbStatus.clear()

        for status in allowed_statuses:
            self.ui.cmbStatus.addItem(
                status
            )

        if current_status:
            self.ui.cmbStatus.setCurrentText(
                current_status
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
        self.ui.dsbEstimatedHours.setValue(0.00)
        self.ui.dsbLabourHours.setValue(0.00)

        self.ui.dsbMeterReading.setValue(0.00)
        self.ui.dsbMeterReading.setVisible(False)
        self.ui.lblMeterReading.setVisible(False)

        self.ui.btnComplete.setEnabled(False)
        self.ui.btnCloseWorkOrder.setEnabled(False)

        self.set_focus(
            self.ui.txtTitle
        )

    def new_from_logbook(self, logbook):

        # Start with the normal new Work Order setup.
        self.new_record()

        # ---------------------------------------------------------
        # Vehicle
        # ---------------------------------------------------------

        asset_index = self.ui.cmbAsset.findData(
            logbook["asset_id"]
        )

        if asset_index >= 0:
            self.ui.cmbAsset.setCurrentIndex(
                asset_index
            )

        # Keep the vehicle fixed because this Work Order
        # originates from this vehicle's logbook entry.
        self.ui.cmbAsset.setEnabled(False)

        # ---------------------------------------------------------
        # Requested by
        # ---------------------------------------------------------

        self.ui.txtRequestedBy.setText(
            logbook["driver_name"] or ""
        )

        # ---------------------------------------------------------
        # Description
        # ---------------------------------------------------------

        description_parts = []

        if logbook["defect_reported"]:
            description_parts.append(
                (
                    "DEFECT / FAULT REPORTED:\n"
                    f"{logbook["defect_reported"]}"
                )
            )

        if logbook["log_date"]:
            description_parts.append(
                f'Logbook Date: {logbook["log_date"]}'
            )

        if logbook["origin"] or logbook["destination"]:
            description_parts.append(
                (
                    f'Journey: {logbook["origin"] or ""}'
                    f' to {logbook["destination"] or ""}'
                )
            )

        if logbook["purpose"]:
            description_parts.append(
                f'Purpose: {logbook["purpose"]}'
            )

        if logbook["end_meter"] is not None:
            description_parts.append(
                f'Odometer: {logbook["end_meter"]:,.1f} km'
            )

        if logbook["notes"]:
            description_parts.append(
                f'Logbook Notes: {logbook["notes"]}'
            )

        description_text = "\n".join(
            description_parts
        )

        self.ui.teDescription.setPlainText(
            description_text
        )

        # The user must enter the actual fault / job title.
        self.ui.txtTitle.clear()
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

            "estimated_hours":
                self.ui.dsbEstimatedHours.value(),

            "meter_reading":
                (
                    self.ui.dsbMeterReading.value()
                    if self.ui.dsbMeterReading.isVisible()
                    else None
                ),

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

        self.ui.dsbEstimatedHours.setValue(
            float(work_order["estimated_hours"] or 0)
        )

        self.ui.dsbMeterReading.setValue(
            float(
                work_order["meter_reading"] or 0
            )
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

        self.update_meter_mode()

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

        if read_only:

            self.ui.btnComplete.setVisible(
                False
            )

            self.ui.btnCloseWorkOrder.setVisible(
                False
            )

            self.ui.btnIssuePart.setVisible(
                False
            )

            self.ui.btnRemovePart.setVisible(
                False
            )

    def set_technician_mode(
        self,
        enabled=True
    ):

        if not enabled:
            return

        # ---------------------------------------------------------
        # General information
        # ---------------------------------------------------------

        self.ui.txtWorkOrderNumber.setReadOnly(
            True
        )

        self.ui.txtTitle.setReadOnly(
            True
        )

        self.ui.teDescription.setReadOnly(
            True
        )

        self.ui.cmbPriority.setEnabled(
            False
        )

        current_status = (
            self.ui.cmbStatus.currentText()
        )

        self.restrict_technician_status_options(
            current_status
        )

        self.ui.cmbStatus.setEnabled(
            True
        )

        # Estimated Labour is planning information

        self.ui.dsbEstimatedHours.setReadOnly(
            True
        )

        # Technician records actual labour

        self.ui.dsbLabourHours.setReadOnly(
            False
        )

        # ---------------------------------------------------------
        # Assignment
        # ---------------------------------------------------------

        self.ui.cmbAsset.setEnabled(
            False
        )

        self.ui.cmbTechnician.setEnabled(
            False
        )

        self.ui.txtRequestedBy.setReadOnly(
            True
        )

        # ---------------------------------------------------------
        # Dates / costs
        # ---------------------------------------------------------

        self.ui.dtDateCreated.setEnabled(
            False
        )

        self.ui.dtDueDate.setEnabled(
            False
        )

        self.ui.dsbEstimatedCost.setReadOnly(
            True
        )

        self.ui.dsbActualCost.setReadOnly(
            True
        )

        self.ui.dsbLabourHours.setReadOnly(
            False
        )

        # ---------------------------------------------------------
        # Notes
        # ---------------------------------------------------------

        self.ui.teNotes.setReadOnly(
            False
        )

        # ---------------------------------------------------------
        # Materials
        # ---------------------------------------------------------

        self.ui.groupMaterials.setEnabled(
            True
        )

        self.ui.btnIssuePart.setVisible(
            Permissions.has_permission(
                self.role,
                "work_orders.issue_parts"
            )
        )

        self.ui.btnRemovePart.setVisible(
            Permissions.has_permission(
                self.role,
                "work_orders.remove_parts"
            )
        )

        # ---------------------------------------------------------
        # Work Order actions
        # ---------------------------------------------------------

        self.ui.btnComplete.setVisible(
            Permissions.has_permission(
                self.role,
                "work_orders.complete"
            )
        )

        self.ui.btnCloseWorkOrder.setVisible(
            Permissions.has_permission(
                self.role,
                "work_orders.close"
            )
        )

        # ---------------------------------------------------------
        # Save
        # ---------------------------------------------------------

        save_button = self.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setVisible(
                True
            )

        self.setWindowTitle(
            "Update Work Order"
        )

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

        self.ui.btnReopen.setEnabled(
            status == "Completed"
        )

        if status == "Completed":
            self.ui.cmbStatus.setEnabled(False)

        self.set_work_order_read_only(
            status == "Closed"
        )

        if status == "Closed":
            self.set_closed_mode()

        self.ui.tabWorkOrder.setTabEnabled(
            1,
            True
        )

        self.ui.tabWorkOrder.setTabEnabled(
            2,
            True
        )

        self.update_workflow_buttons()

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

        #---------------------------------------------------------
        # Terminal statuses must use dedicated workflow buttons
        #---------------------------------------------------------

        if not self.is_add:

            existing = WorkOrderService.get_by_id(
                self.record_id
            )

            if existing is None:
                raise ValueError(
                    "Work Order not found."
                )

            old_status = existing["status"]
            new_status = data["status"]

            # Do not allow ordinary Save to complete a Work Order.
            if (
                old_status != "Completed"
                and new_status == "Completed"
            ):
                raise ValueError(
                    "Use the complete Work Order button "
                    "to complete this Work Order."
                )

        #---------------------------------------------------------
        # Add
        #---------------------------------------------------------

        if self.is_add:

            if data["status"] in {
                "Completed",
                "Closed",
            }:
                raise ValueError(
                    "A new work Order cannot be created "
                    "as Completed or Closed."
                )

            self.record_id = WorkOrderService.create(
                data,
                user=self.user
            )

            self.ui.groupMaterials.setEnabled(
                True
            )

        #---------------------------------------------------------
        # Update
        #---------------------------------------------------------

        else:
            
            WorkOrderService.update(
                self.record_id,
                data,
                user=self.user
            )

    def selected_part_id(self):

        return TableHelper.selected_id(
            self.ui.tblParts
        )

    def complete_work_order(self):

        # -------------------------------------------------
        # Permission
        # -------------------------------------------------
        if not Permissions.has_permission(
            self.role,
            "work_orders.complete"
        ):
            self.warning(
                "Complete Work Order",
                "You do not have permission "
                "to complete work orders."
            )
            return

        # -------------------------------------------------
        # Record must exist
        # -------------------------------------------------
        if self.record_id is None:
            self.warning(
                "Complete Work Order",
                "Please save the Work Order first."
            )
            return

        work_order = WorkOrderService.get_by_id(
            self.record_id
        )

        if work_order is None:
            self.warning(
                "Complete Work Order",
                "Work Order not found."
            )
            return

        # -------------------------------------------------
        # Meter reading
        # -------------------------------------------------

        meter_reading = None

        if work_order["pm_id"] is not None:

            pm = PreventiveMaintenanceService.get_by_id(
                work_order["pm_id"]
            )

            if pm is None:
                self.warning(
                    "Complete Work Order",
                    "The linked PM schedule could not be found."
                )
                return

            meter_reading = None

            if work_order["pm_id"] is not None:

                pm = PreventiveMaintenanceService.get_by_id(
                    work_order["pm_id"]
                )

                if pm is None:
                    self.warning(
                        "Complete Work Order",
                        "The linked PM schedule could not be found."
                    )
                    return

            meter_types = {
                "Running Hours",
                "Kilometers",
                "Cycles",
            }

            if pm["frequency_type"] in meter_types:

                meter_reading = (
                    self.ui.dsbMeterReading.value()
                )

                if meter_reading <= 0:
                    self.warning(
                        "Complete Work Order",
                        "Please enter a valid Meter Reading "
                        "before completing this Work Order."
                    )
                    self.ui.dsbMeterReading.setFocus()
                    return

        # -------------------------------------------------
        # Confirmation
        # -------------------------------------------------

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

        # -------------------------------------------------
        # Complete
        # -------------------------------------------------

        try:
            WorkOrderService.complete_work_order(
                self.record_id,
                user=self.user,
                meter_reading=meter_reading,
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
                (
                    "Could not complete the Work Order."
                    f"\n\n{error}"
                )
            )
            return

        # -------------------------------------------------
        # Refresh dialog
        # -------------------------------------------------

        self.load_record(
            self.record_id
        )

        self.load_history()

        self.update_workflow_buttons()

        self.information(
            "Complete Work Order",
            "Work Order completed successfully."
        )

    def close_work_order(self):

        if not Permissions.has_permission(
            self.role,
            "work_orders.close"
        ):
            self.warning(
                "Close Work Order",
                "You do not have permission "
                "to close work orders."
            )
            return

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
                self.record_id,
                user=self.user
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

        self.load_record(
            self.record_id
        )

        self.update_workflow_buttons()

        self.information(
            "Close Work Order",
            "Work Order closed successfully."
        )

    def apply_permissions(self):

        can_complete = Permissions.has_permission(
        self.role,
        "work_orders.complete"
        )

        can_close = Permissions.has_permission(
            self.role,
            "work_orders.close"
        )

        can_reopen = Permissions.has_permission(
            self.role,
            "work_orders.reopen"
        )

        can_issue_parts = Permissions.has_permission(
            self.role,
            "work_orders.issue_parts"
        )

        can_remove_parts = Permissions.has_permission(
            self.role,
            "work_orders.remove_parts"
        )

        self.ui.btnComplete.setVisible(
            can_complete
        )

        self.ui.btnCloseWorkOrder.setVisible(
            can_close
        )

        self.ui.btnReopen.setVisible(
            can_reopen
        )

        self.ui.btnIssuePart.setVisible(
            can_issue_parts
        )

        self.ui.btnRemovePart.setVisible(
            can_remove_parts
        )

    def restrict_technician_status_options(
        self,
        current_status=None
    ):

        allowed_statuses = {
            "Assigned",
            "In Progress",
            "On Hold",
        }

        if current_status:
            allowed_statuses.add(
                current_status
            )

        for index in reversed(
            range(self.ui.cmbStatus.count())
        ):
            status = self.ui.cmbStatus.itemText(
                index
            )

            if status not in allowed_statuses:
                self.ui.cmbStatus.removeItem(
                    index
                )

    def set_closed_mode(self):

    # ---------------------------------------------------------
    # General
    # ---------------------------------------------------------

        self.ui.txtWorkOrderNumber.setReadOnly(True)
        self.ui.txtTitle.setReadOnly(True)
        self.ui.teDescription.setReadOnly(True)

        self.ui.cmbPriority.setEnabled(False)
        self.ui.cmbStatus.setEnabled(False)

    # ---------------------------------------------------------
    # Assignment
    # ---------------------------------------------------------

        self.ui.cmbAsset.setEnabled(False)
        self.ui.cmbTechnician.setEnabled(False)
        self.ui.txtRequestedBy.setReadOnly(True)

    # ---------------------------------------------------------
    # Dates / Costs
    # ---------------------------------------------------------

        self.ui.dtDateCreated.setEnabled(False)
        self.ui.dtDueDate.setEnabled(False)

        self.ui.dsbEstimatedCost.setReadOnly(True)
        self.ui.dsbActualCost.setReadOnly(True)
        self.ui.dsbLabourHours.setReadOnly(True)

    # ---------------------------------------------------------
    # Notes
    # ---------------------------------------------------------

        self.ui.teNotes.setReadOnly(True)

    # ---------------------------------------------------------
    # Materials
    # ---------------------------------------------------------

        self.ui.groupMaterials.setEnabled(False)

        self.ui.btnIssuePart.setVisible(False)
        self.ui.btnRemovePart.setVisible(False)

    # ---------------------------------------------------------
    # Work Order actions
    # ---------------------------------------------------------

        self.ui.btnComplete.setVisible(False)
        self.ui.btnCloseWorkOrder.setVisible(False)
        self.ui.btnReopen.setVisible(False)

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

        save_button = self.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setVisible(
                False
            )

        cancel_button = self.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Cancel
        )

        if cancel_button is not None:
            cancel_button.setText(
                "Close"
            )

        self.setWindowTitle(
            "View Closed Work Order"
        )

    def reopen_work_order(self):

        if not Permissions.has_permission(
            self.role,
            "work_orders.reopen"
        ):
            self.warning(
                "Reopen Work Order",
                "You do not have permission "
                "to reopen Work Orders."
            )
            return

        if self.record_id is None:
            return

        reason, accepted = QInputDialog.getMultiLineText(
            self,
            "Reopen Work Order",
            "Reason for reopening:"
        )

        if not accepted:
            return

        reason = reason.strip()

        if not reason:
            self.warning(
                "Reopen Work Order",
                "A reason is required."
            )
            return

        if not self.confirm(
            "Reopen Work Order",
            (
                "Reopen this completed Work Order?\n\n"
                "The status will change to In Progress."
            )
        ):
            return

        try:
            WorkOrderService.reopen_work_order(
                self.record_id,
                reason,
                user=self.user,
            )

        except ValueError as error:
            self.warning(
                "Reopen Work Order",
                str(error)
            )
            return

        except Exception as error:
            self.error(
                "Reopen Work Order",
                (
                    "Could not reopen the Work Order."
                    f"\n\n{error}"
                )
            )
            return

        self.load_record(
            self.record_id
        )

        self.update_workflow_buttons()

        self.information(
        "Reopen Work Order",
        "Work Order reopened successfully."
        )

    def update_workflow_buttons(self):

        if self.record_id is None:
            self.ui.btnComplete.setVisible(False)
            self.ui.btnCloseWorkOrder.setVisible(False)
            self.ui.btnReopen.setVisible(False)
            return

        work_order = WorkOrderService.get_by_id(
            self.record_id
        )

        if work_order is None:
            self.ui.btnComplete.setVisible(False)
            self.ui.btnCloseWorkOrder.setVisible(False)
            self.ui.btnReopen.setVisible(False)
            return

        status = work_order["status"]
        pm_id = work_order["pm_id"]

        can_complete = Permissions.has_permission(
            self.role,
            "work_orders.complete"
        )

        can_close = Permissions.has_permission(
            self.role,
            "work_orders.close"
        )

        can_reopen = Permissions.has_permission(
            self.role,
            "work_orders.reopen"
        )

        self.ui.btnComplete.setVisible(
            can_complete
            and status in {
                "Open",
                "Assigned",
                "In Progress",
                "On Hold",
            }
        )

        self.ui.btnCloseWorkOrder.setVisible(
            can_close
            and status == "Completed"
        )

        self.ui.btnReopen.setVisible(
            can_reopen
            and status == "Completed"
            and pm_id is None
        )

    def update_meter_mode(self):

        show_meter = False

        if self.record_id is not None:

            work_order = WorkOrderService.get_by_id(
                self.record_id
            )

            if (
                work_order is not None
                and work_order["pm_id"] is not None
            ):

                from app.services.preventive_maintenance_service import (
                    PreventiveMaintenanceService
                )

                pm = PreventiveMaintenanceService.get_by_id(
                    work_order["pm_id"]
                )

                if pm is not None:

                    meter_types = {
                        "Running Hours",
                        "Kilometers",
                        "Cycles",
                    }

                    show_meter = (
                        pm["frequency_type"]
                        in meter_types
                    )

        self.ui.lblMeterReading.setVisible(
            show_meter
        )

        self.ui.dsbMeterReading.setVisible(
            show_meter
        )