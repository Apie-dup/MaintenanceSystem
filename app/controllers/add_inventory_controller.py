from PySide6.QtWidgets import QDialog, QMessageBox

from app.ui.generated.ui_add_inventory import Ui_AddInventoryDialog
from app.services.inventory_service import InventoryService
from app.utils.validators import Validator
from app.core.lookup_manager import LookupManager


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
            item = InventoryService.get(self.item_id)

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
                description,
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
                notes,
                created_at,
            ) = item

            self.ui.txtPartNumber.setText(part_number or "")
            self.ui.txtPartName.setText(part_name or "")
            self.ui.cmbCategory.setCurrentText(category or "")
            self.ui.cmbSupplier.setCurrentIndex(0)
            self.ui.cmbUnit.setCurrentText(unit or "")
            self.ui.spnQuantity.setValue(quantity or 0)
            self.ui.spnMinimumQuantity.setValue(minimum_quantity or 0)
            self.ui.spnReorderQuantity.setValue(reorder_quantity or 0)
            self.ui.dsbUnitCost.setValue(unit_cost or 0)
            self.ui.cmbLocation.setCurrentText(location or "")
            self.ui.txtBarcode.setText(barcode or "")
            self.ui.cmbStatus.setCurrentText(status or "")
            self.ui.textEdit.setPlainText(notes or "")

        self.ui.buttonBox.accepted.connect(self.save_item)
        self.ui.buttonBox.rejected.connect(self.reject)

    def load_lookup_values(self):

        LookupManager.load(
            self.ui.cmbCategory,
            "Inventory Categories"
        )

        LookupManager.load(
            self.ui.cmbSupplier,
            "Suppliers"
        )

        LookupManager.load(
            self.ui.cmbLocation,
            "Inventory Locations"
        )

        LookupManager.load(
            self.ui.cmbUnit,
            "Units"
        )

        LookupManager.load(
            self.ui.cmbStatus,
            "Statuses"
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
            "",
            self.ui.cmbCategory.currentText(),
            self.ui.cmbSupplier.currentData(),
            self.ui.cmbUnit.currentText(),
            self.ui.spnQuantity.value(),
            self.ui.spnMinimumQuantity.value(),
            self.ui.spnReorderQuantity.value(),
            self.ui.dsbUnitCost.value(),
            self.ui.cmbLocation.currentText(),
            self.ui.txtBarcode.text().strip(),
            self.ui.cmbStatus.currentText(),
            self.ui.textEdit.toPlainText().strip(),
        )

        if self.item_id is None:

            InventoryService.add(item)

            QMessageBox.information(
                self,
                "Success",
                "Inventory item added successfully."
            )

        else:

            update_item = item + (self.item_id,)

            InventoryService.update(update_item)

            QMessageBox.information(
                self,
                "Success"
                "Inventory item updated successfully"
            )

            self.accept()
    
