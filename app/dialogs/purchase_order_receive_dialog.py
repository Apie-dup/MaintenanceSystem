from app.base.base_dialog import BaseDialog
from app.services.purchase_order_service import (
    PurchaseOrderService,
)
from app.ui.generated.ui_purchase_order_receive_dialog import (
    Ui_PurchaseOrderReceiveDialog,
)


class PurchaseOrderReceiveDialog(BaseDialog):

    ENTITY_NAME = "Receive Stock"

    def __init__(
        self,
        item_id,
        user=None,
        parent=None,
    ):
        super().__init__(parent)

        self.item_id = item_id
        self.user = user or {}

        self.ui = Ui_PurchaseOrderReceiveDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.configure_widgets()
        self.connect_signals()
        self.load_item()

    def configure_widgets(self):
        self.ui.txtInventoryItem.setReadOnly(
            True
        )

        for widget in (
            self.ui.dsbQuantityOrdered,
            self.ui.dsbQuantityReceived,
            self.ui.dsbOutstanding,
        ):
            widget.setReadOnly(True)
            widget.setButtonSymbols(
                widget.ButtonSymbols.NoButtons
            )

        self.ui.dsbReceiveQuantity.setMinimum(
            0.01
        )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Load item
    # ---------------------------------------------------------

    def load_item(self):
        item = PurchaseOrderService.get_item(
            self.item_id
        )

        if item is None:
            self.error(
                "Receive Stock",
                "Purchase Order item not found.",
            )
            self.reject()
            return

        quantity_ordered = float(
            item["quantity_ordered"] or 0
        )

        quantity_received = float(
            item["quantity_received"] or 0
        )

        outstanding = (
            quantity_ordered
            - quantity_received
        )

        inventory_text = (
            f'{item["part_number"]} - '
            f'{item["part_name"]}'
        )

        self.ui.txtInventoryItem.setText(
            inventory_text
        )

        self.ui.dsbQuantityOrdered.setValue(
            quantity_ordered
        )

        self.ui.dsbQuantityReceived.setValue(
            quantity_received
        )

        self.ui.dsbOutstanding.setValue(
            outstanding
        )

        # The user may receive less than outstanding,
        # but never more.
        self.ui.dsbReceiveQuantity.setMaximum(
            outstanding
        )

        # Default to receiving the full outstanding
        # quantity.
        self.ui.dsbReceiveQuantity.setValue(
            outstanding
        )

        self.set_focus(
            self.ui.dsbReceiveQuantity
        )

    # ---------------------------------------------------------
    # BaseDialog requirements
    # ---------------------------------------------------------

    def clear_fields(self):
        pass

    def get_form_data(self):
        return {
            "quantity":
                self.ui.dsbReceiveQuantity.value(),

            "notes":
                self.ui.txtNotes
                .toPlainText()
                .strip(),
        }

    def set_form_data(self, data):
        pass

    def load_record(self, record_id):
        pass

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        quantity = (
            self.ui.dsbReceiveQuantity.value()
        )

        outstanding = (
            self.ui.dsbOutstanding.value()
        )

        if quantity <= 0:
            self.warning(
                "Receive Stock",
                (
                    "Receive Quantity must be "
                    "greater than zero."
                ),
            )
            return False

        if quantity > outstanding:
            self.warning(
                "Receive Stock",
                (
                    "Receive Quantity cannot exceed "
                    "the outstanding quantity."
                ),
            )
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        PurchaseOrderService.receive_item(
            item_id=self.item_id,
            quantity=data["quantity"],
            user=self.user,
            notes=data["notes"],
        )