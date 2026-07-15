from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from app.ui.generated.ui_add_work_order import Ui_AddWorkOrderDialog
from app.services.work_order_service import WorkOrderService
from app.services.asset_service import AssetService
from app.services.technician_service import TechnicianService
from app.services.lookup_service import LookupService

class AddWorkOrderController(QDialog):
    
    def __init__(self, work_order_id=None):
        super().__init__()

        self.work_order_id = work_order_id

        self.ui = Ui_AddWorkOrderDialog()
        self.ui.setupUi(self)
        self.ui.cmbAsset.currentIndexChanged.connect(
        self.load_asset_details
    )

        self.initialize_dialog()

    def initialize_dialog(self):

        self.load_priorities()
        self.load_status()
        self.load_assets()
        self.load_technicians()

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

        assets = AssetService.get_assets()

        for asset in assets:

            asset_id = asset[0]
            asset_number = asset[1]
            asset_name = asset[2]

            self.ui.cmbAsset.addItem(
                f"{asset_number} - {asset_name}",
                asset_id
            )

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
        technician_id = self.ui.cmbTechnician.currentData()

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

            self.ui.teNotes.toPlainText().strip()
        

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

        work_order = WorkOrderService.get_work_order(self.work_order_id)

        if not work_order:
            QMessageBox.warning(
                self,
                "Error",
                "Work order not found."
            )
            self.reject()
            return

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

        self.ui.txtWorkOrderNumber.setText(work_order_number)
        self.ui.txtWorkOrderNumber.setReadOnly(True)

        self.ui.txtTitle.setText(title or "")
        self.ui.teDescription.setPlainText(description or "")

        self.ui.cmbPriority.setCurrentText(priority or "Low")
        self.ui.cmbStatus.setCurrentText(status or "Open")

        self.ui.txtRequestedBy.setText(requested_by or "")

        if date_created:
            self.ui.dtDateCreated.setDate(QDate.fromString(date_created, "yyyy-MM-dd"))

        if due_date:
            self.ui.dtDueDate.setDate(QDate.fromString(due_date, "yyyy-MM-dd"))

        self.ui.dsbEstimatedCost.setValue(estimated_cost or 0)
        self.ui.dsbActualCost.setValue(actual_cost or 0)
        self.ui.dsbLabourHours.setValue(labour_hours or 0)

        self.ui.teNotes.setPlainText(notes or "")

        index = self.ui.cmbAsset.findData(asset_id)
        if index >= 0:
            self.ui.cmbAsset.setCurrentIndex(index)

        index = self.ui.cmbTechnician.findData(technician_id)
        if index >= 0:
            self.ui.cmbTechnician.setCurrentIndex(index)

    def load_technicians(self):

        self.ui.cmbTechnician.clear()
        self.ui.cmbTechnician.addItem("Unassigned", None)

        technicians = TechnicianService.get_technicians()

        for technician in technicians:

            technician_id = technician[0]
            employee_number = technician[1]
            first_name = technician[2]
            last_name = technician[3]

            self.ui.cmbTechnician.addItem(
                f"{employee_number} - {first_name} {last_name}",
                technician_id
            )

    def load_asset_details(self):

        asset_id = self.ui.cmbAsset.currentData()

        if asset_id is None:
            return

        asset = AssetService.get_asset(asset_id)

        if not asset:
            return

        category = asset[3] if len(asset) > 3 else ""
        location = asset[4] if len(asset) > 4 else ""

        category_widget = getattr(self.ui, "cmbCategory", None)
        if category_widget is not None and hasattr(category_widget, "setCurrentText"):
            category_widget.setCurrentText(category)

        location_widget = getattr(self.ui, "cmbLocation", None)
        if location_widget is not None and hasattr(location_widget, "setCurrentText"):
            location_widget.setCurrentText(location)