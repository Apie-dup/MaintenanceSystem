from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidgetItem,
)

from app.base.base_dialog import BaseDialog
from app.services.inventory_service import (
    InventoryService
)
from app.services.inventory_transaction_service import (
    InventoryTransactionService
)
from app.ui.generated.ui_inventory_transactions_dialog import (
    Ui_InventoryTransactionsDialog
)


class InventoryTransactionsDialog(BaseDialog):

    def __init__(
        self,
        inventory_id,
        parent=None
    ):
        super().__init__(parent)

        self.inventory_id = inventory_id

        self.ui = Ui_InventoryTransactionsDialog()
        self.ui.setupUi(self)

        self.inventory = None

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):

        self.setWindowTitle(
            "Inventory Transactions"
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

        self.setup_table()
        self.load_inventory()
        self.load_transactions()

    # ---------------------------------------------------------
    # Table
    # ---------------------------------------------------------

    def setup_table(self):

        table = self.ui.tblTransactions

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table.verticalHeader().setVisible(
            False
        )

        header = table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            9,
            QHeaderView.ResizeMode.Stretch
        )

    # ---------------------------------------------------------
    # Inventory heading
    # ---------------------------------------------------------

    def load_inventory(self):

        self.ui.lblPartNumber.setText(
            self.inventory["part_number"]
        )

        self.ui.lblPartName.setText(
            self.inventory["part_name"]
        )

    # ---------------------------------------------------------
    # Transactions
    # ---------------------------------------------------------

    def load_transactions(self):

        records = (
            InventoryTransactionService
            .get_by_inventory(
                self.inventory_id
            )
        )

        table = self.ui.tblTransactions

        table.setRowCount(
            len(records)
        )

        for row_index, record in enumerate(
            records
        ):

            quantity_change = float(
                record["quantity_change"] or 0
            )

            previous_quantity = float(
                record["previous_quantity"] or 0
            )

            new_quantity = float(
                record["new_quantity"] or 0
            )

            unit_cost = float(
                record["unit_cost"] or 0
            )

            # Signed stock change
            if quantity_change > 0:
                change_text = (
                    f"+{quantity_change:g}"
                )
            else:
                change_text = (
                    f"{quantity_change:g}"
                )

            values = [
                record["created_at"] or "",
                record["transaction_type"] or "",
                change_text,
                f"{previous_quantity:g}",
                f"{new_quantity:g}",
                f"N$ {unit_cost:,.2f}",
                record["work_order_number"] or "",
                record["reference"] or "",
                record["username"] or "",
                record["notes"] or "",
            ]

            for column_index, value in enumerate(
                values
            ):

                item = QTableWidgetItem(
                    str(value)
                )

                if column_index in {
                    2,
                    3,
                    4,
                    5,
                }:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignRight
                        | Qt.AlignmentFlag.AlignVCenter
                    )

                table.setItem(
                    row_index,
                    column_index,
                    item
                )