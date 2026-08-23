from app.base.base_dialog import BaseDialog
from app.constants import ASSET_LOCATIONS
from app.helpers.lookup_helper import LookupHelper
from app.services.inventory_service import InventoryService
from app.services.supplier_service import SupplierService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_add_inventory import Ui_AddInventoryItemDialog
from app.helpers.form_helper import FormHelper


class InventoryDialog(BaseDialog):

    ENTITY_NAME = "Inventory Item"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AddInventoryItemDialog()
        self.ui.setupUi(self)

        self.resize(700, 700)

        self.setMinimumSize(
            700,
            700,    
        )

        self.setMaximumWidth(
            900
        )

        self.apply_form_standards()

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.setup_combos()
        self.connect_signals()

        self.ui.spnQuantity.setMaximum(999999)
        self.ui.spnMinimumQuantity.setMaximum(999999)
        self.ui.spnReorderQuantity.setMaximum(999999)

        self.ui.txtPartNumber.setReadOnly(True)

    def setup_combos(self):
        LookupHelper.fill_combo(
            self.ui.cmbCategory,
            [
                "Electrical",
                "Mechanical",
                "Plumbing",
                "Safety",
                "Tools",
                "Consumables",
                "Other",
            ]
        )

        LookupHelper.fill_combo(
            self.ui.cmbUnit,
            [
                "Each",
                "Box",
                "Bag",
                "Bottle",
                "Litre",
                "Metre",
                "Kilogram",
                "Set",
            ]
        )

        LookupHelper.fill_combo(
            self.ui.cmbStatus,
            [
                "Active",
                "Inactive",
            ]
        )

        LookupHelper.fill_combo(
            self.ui.cmbLocation,
            ASSET_LOCATIONS
        )

        self.setup_suppliers()

    def setup_suppliers(self):
        self.ui.cmbSupplier.clear()
        self.ui.cmbSupplier.addItem(
            "No Supplier",
            None
        )

        suppliers = SupplierService.get_active_suppliers()

        for supplier in suppliers:
            display_text = (
                f'{supplier["supplier_code"]} - '
                f'{supplier["supplier_name"]}'
            )

            self.ui.cmbSupplier.addItem(
                display_text,
                supplier["id"]
            )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Clear fields
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtPartNumber.setText(
            InventoryService.get_next_part_number()
        )

        self.ui.txtPartName.clear()
        self.ui.txtDescription.clear()
        self.ui.cmbLocation.setCurrentIndex(0)
        self.ui.txtBarcode.clear()
        self.ui.teNotes.clear()

        self.ui.cmbCategory.setCurrentIndex(0)
        self.ui.cmbSupplier.setCurrentIndex(0)
        self.ui.cmbUnit.setCurrentIndex(0)
        self.ui.cmbStatus.setCurrentText("Active")

        self.ui.spnQuantity.setValue(0)
        self.ui.spnMinimumQuantity.setValue(0)
        self.ui.spnReorderQuantity.setValue(0)
        self.ui.dsbUnitCost.setValue(0.00)

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "part_number":
                self.ui.txtPartNumber.text().strip(),

            "part_name":
                self.ui.txtPartName.text().strip(),

            "description":
                self.ui.txtDescription.text().strip(),

            "category":
                self.ui.cmbCategory.currentText(),

            "supplier_id":
                self.ui.cmbSupplier.currentData(),

            "unit":
                self.ui.cmbUnit.currentText(),

            "quantity":
                self.ui.spnQuantity.value(),

            "minimum_quantity":
                self.ui.spnMinimumQuantity.value(),

            "reorder_quantity":
                self.ui.spnReorderQuantity.value(),

            "unit_cost":
                self.ui.dsbUnitCost.value(),

            "location":
                self.ui.cmbLocation.currentText(),

            "barcode":
                self.ui.txtBarcode.text().strip(),

            "status":
                self.ui.cmbStatus.currentText(),

            "notes":
                self.ui.teNotes.toPlainText().strip(),
        }

    def set_form_data(self, inventory):
        self.ui.txtPartNumber.setText(
            inventory["part_number"]
        )

        self.ui.txtPartName.setText(
            inventory["part_name"]
        )

        self.ui.txtDescription.setText(
            inventory["description"] or ""
        )

        self.ui.cmbCategory.setCurrentText(
            inventory["category"] or ""
        )

        supplier_index = self.ui.cmbSupplier.findData(
            inventory["supplier_id"]
        )

        if supplier_index >= 0:
            self.ui.cmbSupplier.setCurrentIndex(
                supplier_index
            )
        else:
            self.ui.cmbSupplier.setCurrentIndex(0)

        self.ui.cmbUnit.setCurrentText(
            inventory["unit"] or ""
        )

        self.ui.spnQuantity.setValue(
            inventory["quantity"] or 0
        )

        self.ui.spnMinimumQuantity.setValue(
            inventory["minimum_quantity"] or 0
        )

        self.ui.spnReorderQuantity.setValue(
            inventory["reorder_quantity"] or 0
        )

        self.ui.dsbUnitCost.setValue(
            inventory["unit_cost"] or 0.00
        )

        self.ui.cmbLocation.setCurrentText(
            inventory["location"] or ""
        )

        self.ui.txtBarcode.setText(
            inventory["barcode"] or ""
        )

        self.ui.cmbStatus.setCurrentText(
            inventory["status"] or "Active"
        )

        self.ui.teNotes.setPlainText(
            inventory["notes"] or ""
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):
        inventory = InventoryService.get_by_id(
            record_id
        )

        if inventory is None:
            self.error(
                "Inventory",
                "Inventory item not found."
            )
            self.reject()
            return

        self.set_form_data(inventory)

    def set_inventory_read_only(
        self,
        read_only=True
    ):

        # ---------------------------------------------------------
        # Text fields
        # ---------------------------------------------------------

        self.ui.txtPartNumber.setReadOnly(
            True
        )

        self.ui.txtPartName.setReadOnly(
            read_only
        )

        self.ui.txtDescription.setReadOnly(
            read_only
        )

        self.ui.txtBarcode.setReadOnly(
            read_only
        )

        self.ui.teNotes.setReadOnly(
            read_only
        )

        # ---------------------------------------------------------
        # Combo boxes
        # ---------------------------------------------------------

        self.ui.cmbCategory.setEnabled(
            not read_only
        )

        self.ui.cmbSupplier.setEnabled(
            not read_only
        )

        self.ui.cmbUnit.setEnabled(
            not read_only
        )

        self.ui.cmbLocation.setEnabled(
            not read_only
        )

        self.ui.cmbStatus.setEnabled(
            not read_only
        )

        # ---------------------------------------------------------
        # Quantities / cost
        # ---------------------------------------------------------

        self.ui.spnQuantity.setReadOnly(
            read_only
        )

        self.ui.spnMinimumQuantity.setReadOnly(
            read_only
        )

        self.ui.spnReorderQuantity.setReadOnly(
            read_only
        )

        self.ui.dsbUnitCost.setReadOnly(
            read_only
        )

        # ---------------------------------------------------------
        # Save button
        # ---------------------------------------------------------

        save_button = self.ui.buttonBox.button(
            self.ui.buttonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setVisible(
                not read_only
            )

        # ---------------------------------------------------------
        # Dialog title
        # ---------------------------------------------------------

        if read_only:
            self.setWindowTitle(
                "View Inventory Item"
            )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["part_name"],
                "Part Name"
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["category"],
                "Category"
            )
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["unit"],
                "Unit"
            )
        ):
            return False

        if data["minimum_quantity"] > data["quantity"]:
            # This may be valid in your system, so this is only a warning,
            # not a validation failure.
            pass

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            InventoryService.create(data)
        else:
            InventoryService.update(
                self.record_id,
                data
            )