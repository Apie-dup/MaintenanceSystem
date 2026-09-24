from app.base.base_dialog import BaseDialog
from app.services.inventory_service import InventoryService
from app.services.purchase_order_service import PurchaseOrderService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_purchase_order_item_dialog import (
    Ui_PurchaseOrderItemDialog,
)


class PurchaseOrderItemDialog(BaseDialog):

    ENTITY_NAME = "Purchase Order Item"

    def __init__(
        self,
        purchase_order_id,
        parent=None,
    ):
        super().__init__(parent)

        self.purchase_order_id = purchase_order_id

        self.ui = Ui_PurchaseOrderItemDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_inventory()
        self.configure_widgets()
        self.connect_signals()

    def configure_widgets(self):
        self.ui.dsbQuantityOrdered.setMinimum(
            0.01
        )
        self.ui.dsbQuantityOrdered.setMaximum(
            999999.99
        )
        self.ui.dsbQuantityOrdered.setDecimals(2)

        self.ui.dsbUnitCost.setMinimum(
            0.00
        )
        self.ui.dsbUnitCost.setMaximum(
            999999999.99
        )
        self.ui.dsbUnitCost.setDecimals(2)

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.cmbInventory.currentIndexChanged.connect(
            self.inventory_changed
        )

    # ---------------------------------------------------------
    # Inventory
    # ---------------------------------------------------------

    def load_inventory(self):
        self.ui.cmbInventory.clear()

        records = InventoryService.get_all()

        for inventory in records:
            display_text = (
                f'{inventory["part_number"]} - '
                f'{inventory["part_name"]}'
            )

            self.ui.cmbInventory.addItem(
                display_text,
                inventory["id"],
            )

    def inventory_changed(self, *_args):
        inventory_id = (
            self.ui.cmbInventory.currentData()
        )

        if inventory_id is None:
            return

        inventory = InventoryService.get_by_id(
            inventory_id
        )

        if inventory is None:
            return

        self.ui.dsbUnitCost.setValue(
            float(
                inventory["unit_cost"]
                or 0
            )
        )

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------

    def clear_fields(self):
        if self.ui.cmbInventory.count() > 0:
            self.ui.cmbInventory.setCurrentIndex(0)

        self.ui.dsbQuantityOrdered.setValue(
            1.00
        )

        self.ui.txtNotes.clear()

        self.inventory_changed()

        self.set_focus(
            self.ui.dsbQuantityOrdered
        )

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        return {
            "inventory_id":
                self.ui.cmbInventory.currentData(),

            "quantity_ordered":
                self.ui.dsbQuantityOrdered.value(),

            "unit_cost":
                self.ui.dsbUnitCost.value(),

            "notes":
                self.ui.txtNotes.toPlainText().strip(),
        }

    def set_form_data(self, item):
        inventory_index = (
            self.ui.cmbInventory.findData(
                item["inventory_id"]
            )
        )

        if inventory_index >= 0:
            self.ui.cmbInventory.setCurrentIndex(
                inventory_index
            )

        self.ui.dsbQuantityOrdered.setValue(
            float(
                item["quantity_ordered"]
                or 0
            )
        )

        self.ui.dsbUnitCost.setValue(
            float(
                item["unit_cost"]
                or 0
            )
        )

        self.ui.txtNotes.setPlainText(
            item["notes"] or ""
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):
        item = PurchaseOrderService.get_item(
            record_id
        )

        if item is None:
            self.error(
                "Purchase Order Item",
                "Purchase Order item not found.",
            )
            self.reject()
            return

        self.set_form_data(item)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["inventory_id"],
                "Inventory Item",
            ),
        ):
            return False

        if data["quantity_ordered"] <= 0:
            self.warning(
                "Purchase Order Item",
                (
                    "Quantity Ordered must be "
                    "greater than zero."
                ),
            )
            return False

        if data["unit_cost"] < 0:
            self.warning(
                "Purchase Order Item",
                (
                    "Unit Cost cannot be "
                    "negative."
                ),
            )
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.is_add:
            self.record_id = (
                PurchaseOrderService.add_item(
                    self.purchase_order_id,
                    data,
                )
            )
        else:
            PurchaseOrderService.update_item(
                self.record_id,
                data,
            )