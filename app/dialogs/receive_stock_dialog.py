from app.base.base_dialog import BaseDialog
from app.services.inventory_service import (
    InventoryService
)
from app.services.inventory_transaction_service import (
    InventoryTransactionService
)
from app.ui.generated.ui_receive_stock_dialog import (
    Ui_ReceiveStockDialog
)


class ReceiveStockDialog(BaseDialog):

    def __init__(
        self,
        inventory_id,
        user=None,
        parent=None
    ):
        super().__init__(parent)

        self.inventory_id = inventory_id
        self.user = user

        self.ui = Ui_ReceiveStockDialog()
        self.ui.setupUi(self)

        self.inventory = None

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):

        self.setWindowTitle(
            "Receive Stock"
        )

        self.inventory = (
            InventoryService.get_by_id(
                self.inventory_id
            )
        )

        if self.inventory is None:
            raise ValueError(
                "Inventory item not found."
            )

        self.load_inventory()

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_inventory(self):

        part_text = (
            f'{self.inventory["part_number"]} - '
            f'{self.inventory["part_name"]}'
        )

        self.ui.lblPartValue.setText(
            part_text
        )

        self.ui.lblCurrentQuantityValue.setText(
            f'{float(self.inventory["quantity"] or 0):g}'
        )

        self.ui.dsbQuantity.setValue(
            1.00
        )

        self.ui.dsbUnitCost.setValue(
            float(
                self.inventory["unit_cost"] or 0
            )
        )

        self.ui.txtReference.clear()
        self.ui.txtNotes.clear()

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):

        InventoryTransactionService.receive_stock(
            inventory_id=self.inventory_id,
            quantity=self.ui.dsbQuantity.value(),
            unit_cost=self.ui.dsbUnitCost.value(),
            reference=(
                self.ui.txtReference
                .text()
                .strip()
            ),
            notes=(
                self.ui.txtNotes
                .toPlainText()
                .strip()
            ),
            user=self.user,
        )

    # ---------------------------------------------------------
    # Save and close
    # ---------------------------------------------------------

    def save_and_close(self):

        try:

            self.save()

            self.accept()

        except ValueError as error:

            self.warning(
                "Receive Stock",
                str(error)
            )

        except Exception as error:

            self.warning(
                "Receive Stock",
                f"Unexpected error:\n{error}"
            )