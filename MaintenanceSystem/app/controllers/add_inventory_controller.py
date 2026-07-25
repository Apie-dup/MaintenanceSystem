from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt

from app.ui.generated.ui_add_inventory import Ui_AddInventoryDialog
from app.services.inventory_service import InventoryService
from app.services.lookup_service import LookupService
from app.services.supplier_service import SupplierService
from app.utils.validator import Validator


class AddInventoryController(QDialog):

    def __init__(self, part_id=None):
        super().__init__()

        self.part_id = part_id

        self.ui = Ui_AddInventoryDialog()
        self.ui.setupUi(self)

        self.initialize_dialog()

    def initialize_dialog(self):

        self.load_categories()
        self.load_suppliers()
        self.load_units()
        self.load_status()

        self.ui.dsbUnitCost.setDecimals(2)

        if self.part_id is None:

            self.ui.txtPartNumber.setText(
                InventoryService.get_next_part_number()
            )

            self.ui.txtPartNumber.setReadOnly(True)

        else:

            self.load_inventory()

        self.ui.buttonBox.accepted.connect(
            self.save_inventory
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        def load_categories(self):

            self.ui.cmbCategory.clear()

            categories = LookupService.get_lookup_values(
                "Inventory Category"
        )

            self.ui.cmbCategory.addItems(categories)

        def load_suppliers(self):

            self.ui.cmbSupplier.clear()

            self.ui.cmbSupplier.addItem(
                "None",
                None
        )

            suppliers = SupplierService.get_suppliers()

            for supplier in suppliers:

                supplier_id = supplier[0]
                supplier_name = supplier[2]

                self.ui.cmbSupplier.addItem(
                    supplier_name,
                    supplier_id
                )

        def load_units(self):

            self.ui.cmbUnit.clear()

            self.ui.cmbUnit.addItems([

                "Each",

                "Box",

                "Pack",

                "Kg",

                "Litre",

                "Meter"

            ])

        def load_status(self):

            self.ui.cmbStatus.clear()

            self.ui.cmbStatus.addItems([

                "Active",

                "Inactive",

                "Obsolete"

            ])

        def save_inventory(self):

            part_name = self.ui.txtPartName.text().strip()

            if not Validator.required(
                    self,
                    part_name,
                    "Part Name"
            ):
                return

            supplier_id = self.ui.cmbSupplier.currentData()

            part = (

                self.ui.txtPartNumber.text(),

                part_name,

                self.ui.cmbCategory.currentText(),

                supplier_id,

                self.ui.cmbUnit.currentText(),

                self.ui.spnQuantity.value(),

                self.ui.spnMinimum.value(),

                self.ui.spnReorder.value(),

                self.ui.dsbUnitCost.value(),

                self.ui.txtLocation.text().strip(),

                self.ui.txtBarcode.text().strip(),

                self.ui.cmbStatus.currentText(),

                self.ui.teNotes.toPlainText().strip()

            )

            if self.part_id is None:

                InventoryService.add_inventory(part)

                QMessageBox.information(
                    self,
                    "Success",
                    "Inventory item added successfully."
                )

            else:

                update_part = part + (self.part_id,)

                InventoryService.update_inventory(
                    update_part
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Inventory item updated successfully."
                )

            self.accept()

        def load_inventory(self):

            part = InventoryService.get_item(
                self.part_id
            )

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
            ) = part

            self.ui.txtPartNumber.setText(part_number)
            self.ui.txtPartName.setText(part_name)

            self.ui.cmbCategory.setCurrentText(category)

            index = self.ui.cmbSupplier.findData(
                 supplier_id
            )

            if index >= 0:
                self.ui.cmbSupplier.setCurrentIndex(index)

            self.ui.cmbUnit.setCurrentText(unit)

            self.ui.spnQuantity.setValue(quantity)

            self.ui.spnMinimum.setValue(minimum_quantity)

            self.ui.spnReorder.setValue(reorder_quantity)

            self.ui.dsbUnitCost.setValue(unit_cost)

            self.ui.txtLocation.setText(location or "")

            self.ui.txtBarcode.setText(barcode or "")

            self.ui.cmbStatus.setCurrentText(status)

            self.ui.teNotes.setPlainText(notes or "")