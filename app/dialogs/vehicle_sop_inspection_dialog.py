from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHeaderView
)

from app.services.vehicle_sop_inspection_service import (
    VehicleSopInspectionService
)
from app.services.vehicle_sop_service import (
    VehicleSopService
)
from app.ui.generated.ui_vehicle_sop_inspection_dialog import (
    Ui_VehicleSopInspectionDialog
)
from app.models.vehicle_sop_item_model import (
    VehicleSopItemModel
)
from app.helpers.table_helper import TableHelper
from app.dialogs.vehicle_sop_inspection_result_dialog import (
    VehicleSopInspectionResultDialog
)
from app.services.message_service import MessageService
from app.services.work_order_service import WorkOrderService


class VehicleSopInspectionDialog(QDialog):

    METER_TYPES = [
        "Kilometers",
        "Running Hours",
        "Cycles",
    ]

    def __init__(
        self,
        inspection_id=None,
        user=None,
        parent=None
    ):
        super().__init__(parent)

        self.ui = Ui_VehicleSopInspectionDialog()
        self.ui.setupUi(self)

        self.inspection_id = inspection_id
        self.user = user
        self.sops = {}

        self.setup_dialog()
        self.connect_signals()

        if self.inspection_id is None:
            self.setup_new_inspection()
        else:
             self.load_inspection()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):

        self.ui.cmbSop.clear()
        self.ui.cmbSop.addItem(
            "Select SOP",
            None
        )

        for sop in VehicleSopService.get_active():

            self.sops[sop["id"]] = sop

            display_text = (
                f'{sop["sop_number"]} - '
                f'{sop["sop_name"]}'
            )

            self.ui.cmbSop.addItem(
                display_text,
                sop["id"]
            )

        self.ui.cmbMeterType.clear()
        self.ui.cmbMeterType.addItem(
            "No Meter Reading",
            None
        )

        for meter_type in self.METER_TYPES:
            self.ui.cmbMeterType.addItem(
                meter_type,
                meter_type
            )

        TableHelper.setup(
            self.ui.tblChecklist,
            [
                ("sequence", "Seq."),   
                ("check_description", "Check Description"),
                ("required_display", "Required"),
                ("result_display", "Result"),
                ("work_order_number", "Work Order"),
            ]
        )

        header = self.ui.tblChecklist.horizontalHeader()

        header.setStretchLastSection(False)

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.Stretch
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeMode.ResizeToContents
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):

        self.ui.cmbSop.currentIndexChanged.connect(
            self.sop_changed
        )

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.btnSetResult.clicked.connect(
            self.set_result
        )

        self.ui.tblChecklist.itemDoubleClicked.connect(
            self.set_result
        )

        self.ui.btnComplete.clicked.connect(
            self.complete_inspection
        )

        self.ui.btnCreateWorkOrder.clicked.connect(
            self.create_work_order
        )

    # ---------------------------------------------------------
    # New inspection
    # ---------------------------------------------------------

    def setup_new_inspection(self):

        self.setWindowTitle(
            "New SOP Inspection"
        )

        self.ui.txtInspectionNumber.setText(
            VehicleSopInspectionService
            .get_next_inspection_number()
        )

        self.ui.dtInspectionDate.setDate(
            QDate.currentDate()
        )

        self.ui.txtAsset.clear()
        self.ui.txtFrequency.clear()

        self.ui.tblChecklist.setRowCount(0)

        self.ui.btnSetResult.setEnabled(False)
        self.ui.btnComplete.setEnabled(False)
        self.ui.btnCreateWorkOrder.setEnabled(False)

    # ---------------------------------------------------------
    # SOP selection
    # ---------------------------------------------------------

    def sop_changed(self):

        sop_id = self.ui.cmbSop.currentData()

        if not sop_id:

            self.ui.txtAsset.clear()
            self.ui.txtFrequency.clear()
            self.ui.tblChecklist.setRowCount(0)

            return

        sop = self.sops.get(sop_id)

        if not sop:
            return

        asset_text = (
            f'{sop["asset_number"]} - '
            f'{sop["asset_name"]}'
        )

        self.ui.txtAsset.setText(
            asset_text
        )

        self.ui.txtFrequency.setText(
            sop["frequency"]
        )

        sop_items = (
            VehicleSopItemModel.get_by_sop_id(
                sop_id
            )
        )

        preview_items = []

        for item in sop_items:
            preview_items.append({
                "id": item["id"],
                "sequence": item["sequence"],
                "check_description": item["check_description"],
                "required_display": (
                    "Yes" if item["required"] else "No"
                ),
                "result_display": "",
                "work_order_number": "",
            })

        TableHelper.populate(
            self.ui.tblChecklist,
            preview_items,
            [
                ("sequence", "Seq."),
                ("check_description", "Check Description"),
                ("required_display", "Required"),
                ("result_display", "Result"),
                ("work_order_number", "Work Order"),
            ]
        )

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save_and_close(self):

        meter_type = (
            self.ui.cmbMeterType.currentData()
        )

        meter_reading = None

        if meter_type:
            meter_reading = (
                self.ui.spnMeterReading.value()
            )

        inspection_date = (
            self.ui.dtInspectionDate
            .date()
            .toString("yyyy-MM-dd")
        )

        operator_name = (
            self.ui.txtOperator
            .text()
            .strip()
        )

        comments = (
            self.ui.txtComments
            .toPlainText()
            .strip()
        )

        try:

            # ---------------------------------------------
            # New inspection
            # ---------------------------------------------

            if self.inspection_id is None:

                sop_id = (
                    self.ui.cmbSop.currentData()
                )

                if not sop_id:
                    return

                self.inspection_id = (
                    VehicleSopInspectionService.create({
                        "sop_id":
                            sop_id,

                        "inspection_date":
                            inspection_date,

                        "operator_name":
                            operator_name,

                        "meter_type":
                            meter_type,

                        "meter_reading":
                            meter_reading,

                        "comments":
                            comments,
                    })
                )

            # ---------------------------------------------
            # Existing inspection
            # ---------------------------------------------

            else:

                inspection = (
                    VehicleSopInspectionService
                    .get_by_id(
                        self.inspection_id
                    )
                )

                if not inspection:
                    return

                if (
                    inspection["status"]
                    == "Completed"
                ):
                    return

                VehicleSopInspectionService.update({
                    "id":
                        self.inspection_id,

                    "inspection_date":
                        inspection_date,

                    "operator_name":
                        operator_name,

                    "meter_type":
                        meter_type,

                    "meter_reading":
                        meter_reading,

                    "status":
                        inspection["status"],

                    "comments":
                        comments,
                })

        except ValueError:
            return

        self.accept()

    # ---------------------------------------------------------
    # Load existing inspection
    # ---------------------------------------------------------

    def load_inspection(self):

        inspection = (
            VehicleSopInspectionService.get_by_id(
                self.inspection_id
            )
        )

        if not inspection:
            raise ValueError(
                "SOP inspection was not found."
            )

        self.setWindowTitle(
            f'Inspection {inspection["inspection_number"]}'
        )

        self.ui.txtInspectionNumber.setText(
            inspection["inspection_number"]
        )

        # Existing inspections use their historical
        # snapshot rather than the current SOP definition.
        self.ui.cmbSop.clear()
        self.ui.cmbSop.addItem(
            (
                f'{inspection["sop_number"]} - '
                f'{inspection["sop_name"]}'
            ),
            inspection["sop_id"]
        )

        self.ui.txtAsset.setText(
            (
                f'{inspection["asset_number"]} - '
                f'{inspection["asset_name"]}'
            )
        )

        self.ui.txtFrequency.setText(
            inspection["frequency"]
        )

        date = QDate.fromString(
            inspection["inspection_date"],
            "yyyy-MM-dd"
        )

        if date.isValid():
            self.ui.dtInspectionDate.setDate(
                date
            )

        self.ui.txtOperator.setText(
            inspection["operator_name"] or ""
        )

        meter_type = inspection["meter_type"]

        if meter_type:

            index = (
                self.ui.cmbMeterType
                .findData(meter_type)
            )

            if index >= 0:
                self.ui.cmbMeterType.setCurrentIndex(
                    index
                )

        if inspection["meter_reading"] is not None:
            self.ui.spnMeterReading.setValue(
                float(inspection["meter_reading"])
            )

        self.ui.txtComments.setPlainText(
            inspection["comments"] or ""
        )

        self.load_inspection_items()

        completed = (
            inspection["status"] == "Completed"
        )

        self.ui.cmbSop.setEnabled(False)

        self.ui.btnSetResult.setEnabled(
            not completed
        )

        self.ui.btnComplete.setEnabled(
            not completed
        )

        self.ui.btnCreateWorkOrder.setEnabled(
            completed
        )

        if completed:
            self.ui.dtInspectionDate.setEnabled(False)
            self.ui.txtOperator.setReadOnly(True)

            self.ui.cmbMeterType.setEnabled(False)
            self.ui.spnMeterReading.setReadOnly(True)

            self.ui.txtComments.setReadOnly(True)

            save_button = self.ui.buttonBox.button(
                QDialogButtonBox.StandardButton.Save
            )

            if save_button:
                save_button.setEnabled(False)

            self.ui.tblChecklist.setEnabled(True)

    # ---------------------------------------------------------
    # Load inspection checklist
    # ---------------------------------------------------------

    def load_inspection_items(self):

        items = (
            VehicleSopInspectionService.get_items(
                self.inspection_id
            )
        )

        display_items = []

        for item in items:

            display_items.append({
                "id":
                    item["id"],

                "sequence":
                    item["sequence"],

                "check_description":
                    item["check_description"],

                "required_display":
                    "Yes"
                    if item["required"]
                    else "No",

                "result_display":
                    item["result"] or "",

                "work_order_number":
                    item["work_order_number"] or "",
            })

        TableHelper.populate(
            self.ui.tblChecklist,
            display_items,
            [
                ("sequence", "Seq."),
                (
                    "check_description",
                    "Check Description"
                ),
                (
                    "required_display",
                    "Required"
                ),
                (
                    "result_display",
                    "Result"
                ),
                (
                    "work_order_number",
                    "Work Order"
                ),
            ]
        )

    # ---------------------------------------------------------
    # Set checklist result
    # ---------------------------------------------------------

    def set_result(self):

        if self.inspection_id is None:
            return

        item_id = TableHelper.selected_id(
            self.ui.tblChecklist
        )

        if not item_id:
            return

        items = (
            VehicleSopInspectionService.get_items(
                self.inspection_id
            )
        )

        item = next(
            (
                row
                for row in items
                if row["id"] == item_id
            ),
            None
        )

        if not item:
            return

        dialog = VehicleSopInspectionResultDialog(
            check_description=item[
                "check_description"
            ],
            result=item["result"],
            comments=item["comments"],
            parent=self
        )

        if not dialog.exec():
            return

        data = dialog.get_data()

        try:

            VehicleSopInspectionService.update_item_result(
                item_id,
                data["result"],
                data["comments"]
            )

        except ValueError:
            return

        self.load_inspection_items()

    # ---------------------------------------------------------
    # Create Work Order from failed checklist item
    # ---------------------------------------------------------

    def create_work_order(self):

        if self.inspection_id is None:
            return

        item_id = TableHelper.selected_id(
            self.ui.tblChecklist
        )

        if not item_id:
            MessageService.warning(
                self,
                "Create Work Order",
                "Select a failed checklist item first."
            )
            return

        items = (
            VehicleSopInspectionService.get_items(
                self.inspection_id
            )
        )

        item = next(
            (
                row
                for row in items
                if row["id"] == item_id
            ),
            None
        )

        if not item:
            return

        if item["result"] != "Fail":
            MessageService.warning(
                self,
                "Create Work Order",
                "A Work Order can only be created "
                "from a failed checklist item."
            )
            return

        confirmed = MessageService.confirm(
            self,
            "Create Work Order",
            (
                "Create a Work Order for this "
                "failed checklist item?\n\n"
                f'{item["check_description"]}'
            )
        )

        if not confirmed:
            return

        try:

            work_order_id = (
                VehicleSopInspectionService
                .create_work_order_for_failed_item(
                    self.inspection_id,
                    item_id,
                    user=self.user
                )
            )

            work_order = (
                WorkOrderService.get_by_id(
                    work_order_id
                )
            )

            self.load_inspection_items()

        except ValueError as error:

            MessageService.warning(
                self,
                "Cannot Create Work Order",
                str(error)
            )

            return

        MessageService.information(
            self,
            "Work Order Created",
            (
                "The Work Order was created "
                "successfully.\n\n"
                f"Work Order ID: {work_order["work_order_number"]}"
            )
        )

    # ---------------------------------------------------------
    # Complete inspection
    # ---------------------------------------------------------

    def complete_inspection(self):

        if self.inspection_id is None:
            return

        confirmed = MessageService.confirm(
            self,
            "Complete Inspection",
            (
                "Complete this inspection?\n\n"
                "Once completed, the inspection "
                "and checklist results can no "
                "longer be modified."
            )
        )

        if not confirmed:
            return

        try:

            VehicleSopInspectionService.complete(
                self.inspection_id
            )

        except ValueError as error:

            MessageService.warning(
                self,
                "Cannot Complete Inspection",
                str(error)
            )

            return

        MessageService.information(
            self,
            "Inspection Completed",
            "The inspection was completed successfully."
        )

        self.accept()