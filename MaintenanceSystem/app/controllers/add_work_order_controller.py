from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from app.ui.generated.ui_add_work_order import Ui_AddWorkOrderDialog
from app.services.work_order_service import WorkOrderService
from app.services.asset_service import AssetService

class AddWorkOrderConttoller(QDialog):
    
    def __init__(self, work_order_id=None):
        super().__init__()

        self.work_order_id = work_order_id

        self.ui = Ui_AddWorkOrderDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):

        self.load_prorities()
        self.load_status()
        self.load_assets()

        self.ui.dtDateCreated.setCalendarPopup(True)
        self.ui.dtDueDate.setCalendarPopup(True)

        self.ui.dsbEstimatedCost.setDecimals(2)
        self.ui.dsbActualCost.setDecimals(2)
        self.ui.dsbLabourHours.setDecimals(2)

        if self.work_order_id is None:

           self.ui.txtWorkOrderNumber.setText(
               WorkOrderService.get_next_work_order_number()
           )

           self.ui.txtWorkOrderNumber.setReadOnly(True)

           self.ui.dtDateCreated.setDate(QDate.currentDate())

        else:

            self.load_work_order()

        self.ui.buttonBox.accepted.connect(self.save_work_order)
        self.ui.buttonBox.rejected.connect(self.reject)

    def load_priorities(self):

        self.ui.cmbPriority.clear()

        self.ui.cmbPriority.addItems([
            "Low",
            "Medium",
            "High",
            "Critical"
        ])

    def load_status(self):

        self.ui.cmbStatus.clear()

        self.ui.cmbStatus.addItems([
            "Open",
            "Assigned",
            "In Progress",
            "Waiting Parts",
            "Completed",
            "Cancelled"
        ])

    def load_assets(self):

        self.ui.cmbAsset.clear()

        assets = AssetService.get_asset()

        for asset in assets:

            asset_id = asset[0]
            asset_number = asset[1]
            asset_name = asset[2]

            self.ui.cmbAsset.addItem(
                f"{asset_number} - {asset_name}",
                asset_id
            )

        self.ui.cmbThechnician.addItem("Unassigned", None)

    def save_work_order(self):

        title = self.ui.txtTitle.text().strip()

        if not title:
            QMessageBox.warning(
                self,
                "Validation",
                "Title is required."
            )
            return
        
        asset_id = self.ui.cmbAsset.currentData()
        technician_id = self.ui.cmbThechnician.currentData()

        work_order = (

            self.ui.txtWorkOrderNumber.text(),

            asset_id,

            title,

            self.ui.teDescription.toPlainText().strip(),

            self.ui.cmbPriority.currentText(),

            self.ui.cmbStatus.currentText(),

            technician_id,

            self.ui.txtRequestedBy.text().strip(),

            self.ui.dtDateCreated.date().toString("yyyy-MM-dd"),

            self.ui.dtDueDate.date().toString("yyyy-MM-dd"),

            self.ui.dsbEstimatedCost.value(),

            self.ui.dsbActualCost.value(),

            self.ui.dsbLabourHours.value(),

            self.ui.teNotes.toPlaintText().strip()
        

        )

        if self.work_order_id is None:

            WorkOrderService.add_work_order(work_order)

            QMessageBox.information(
                self,
                "Success",
                "Work Order created successfuly."
            )
        
        else:

            update_work_order = (

                asset_id,

                title,

                self.ui.teDescription.toPlainText().strip(),

                self.ui.cmbPriority.currentText(),

                self.ui.cmbStatus.currentText(),

                technician_id,

                self.ui.txtRequestedBy.text().strip(),

                self.ui.dtDateCreated.date().toString("yyyy-MM-dd"),

                self.ui.dtDueDate.date().toString("yyyy-MM-dd"),

                self.ui.dsbEstimatedCost.value(),

                self.ui.dsbActualCost.value(),

                self.ui.dsbLabourHours.value(),

                self.ui.teNotes.toPlainText().strip(),

                self.work_order_id

            )

            WorkOrderService.update_work_order(update_work_order)

            QMessageBox.information(
                self,
                "Success",
                "Work Order updated successfully."
            )
        
        self.accept()

    def load_work_order(self):

        work_order = WorkOrderService.get_work_order(
            self.work_order_id
        )

        (
            _,
            work_order_number,
            asset_id,
            title,
            description,
            priority,
            status,
            technician_id,
            requested_by,
            date_created,
            due_date,
            estimated_cost,
            actual_cost,
            labour_hours,
            notes
        ) = work_order