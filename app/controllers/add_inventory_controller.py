from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate

from app.ui.generated.ui_add_inventory import Ui_AddInventoryDialog
from app.services.inventory_service import InventoryService
from app.services.lookup_service import LookupService
from app.utils.validators import Validator


class AddInventoryController(QDialog):

    def __init__(self, item_id=None):
        super().__init__()

        self.item_id = item_id

        self.ui = Ui_AddInventoryDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):

        self.load_lookup_values()

        if self.item_id is None:
            self.setWindowTitle("Add Inventory Item")

        else:
            
            self.setWindowTitle("Edit Inventory")
            item = InventoryService.get_item(self.item_id)

        if not item:
            QMessageBox.warning(
                self,
                "Inventory",
                "Inventory item not found."
            )

            self.reject()
            return
        
        (

            _,
            part_number,
            part_name,
            category,
            supplier_id,
            unit,
            quantity,
            minimum_quantity,
            reorder_quantity,
            unit_cost,
            location,
            barcode,
            status,
            notes
            ) = item

        self.ui.txtPartNumber.setText(part_number)
        self.ui.txtPartName.setText(part_name)
        self.ui.cmbCategory.setCurrentText(category)
        self.ui.cmbUnit.setCurrentText(unit)
        self.ui.spnQuantity.setValue(quantity)
        self.ui.spnMinimumQuantity.setValue(minimum_quantity)
        self.ui.spnReorderQuantity.setValue(reorder_quantity)
        self.ui.dsbUnitCost.setValue(unit_cost)
        self.ui.cmbLocation.setCurrentText(location)
        self.ui.txtBarcode.setText(barcode)
        self.ui.cmbStatus.setCurrentText(status)
        self.ui.teNotes.setPlainText(notes)

        self.ui.buttonBox.accepted.connect(self.save_item)
        self.ui.buttonBox.rejected.connect(self.reject)

    def load_lookup_values(self):

        self.ui.cmbCategory.clear()
        self.ui.cmbLocation.clear()
        self.ui.cmbSupplier.clear()

        self.ui.cmbCategory.addItems(
            LookupService.get_categories()
        )

        self.ui.cmbLocation.addItems(
            LookupService.get_location()
        )

        self.ui.cmbSupplier.addItems(
            LookupService.get_suppliers()
        )

    def save_item(self):

        part_name = self.ui.txtPartName.text().strip()

        if not Validator.required(
            self,
            part_name,
            "Part Name"
        ):
            return
        
        item = (
            self.ui.txtPartNumber.text().strip(),
            part_name,
            self.ui.cmbCategory.currentText(),
            self.ui.cmbSupplier.currentData(),      # supplier_id
            self.ui.cmbUnit.currentText(),
            self.ui.spnQuantity.value(),
            self.ui.spnMinimumQuantity.value(),
            self.ui.spnReorderQuantity.value(),
            self.ui.dsbUnitCost.value(),
            self.ui.cmbLocation.currentText(),
            self.ui.txtBarcode.text().strip(),
            self.ui.cmbStatus.currentText(),
            self.ui.teNotes.toPlainText().strip(),
        )
        

        if self.item_id is None:

            InventoryService.add_item(item)

            QMessageBox.information(
                self,
                "Success",
                "Inventory item added successfully."
            )

        else:

            update_item = item + (self.item_id,)

            InventoryService.update_item(update_item)

            QMessageBox.information(
                self,
                "Success"
                "Inventory item updated successfully"
            )

            self.accept()
    
