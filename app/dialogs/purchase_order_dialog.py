from PySide6.QtCore import QDate

from app.base.base_dialog import BaseDialog
from app.dialogs.purchase_order_item_dialog import (
    PurchaseOrderItemDialog,
)
from app.helpers.format_helper import FormatHelper
from app.helpers.table_helper import TableHelper
from app.services.purchase_order_service import (
    PurchaseOrderService,
)
from app.services.supplier_service import SupplierService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_purchase_order_dialog import (
    Ui_PurchaseOrderDialog,
)
from app.dialogs.purchase_order_receive_dialog import (
    PurchaseOrderReceiveDialog,
)


class PurchaseOrderDialog(BaseDialog):

    ENTITY_NAME = "Purchase Order"

    ITEM_COLUMNS = [
        ("part_number", "Part Number"),
        ("part_name", "Part Name"),
        ("unit", "Unit"),
        ("quantity_ordered", "Qty Ordered"),
        ("quantity_received", "Qty Received"),
        ("unit_cost", "Unit Cost"),
        ("line_total", "Total"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pending_inventory_item = None

        self.user = getattr(
            parent,
            "user",
            {},
        )

        self.ui = Ui_PurchaseOrderDialog()
        self.ui.setupUi(self)

        self.apply_form_standards()

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.setup_suppliers()
        self.configure_widgets()
        self.connect_signals()

        TableHelper.setup(
            self.ui.tblItems,
            self.ITEM_COLUMNS,
        )

    def setup_suppliers(self):
        self.ui.cmbSupplier.clear()

        suppliers = (
            SupplierService.get_active_suppliers()
        )

        for supplier in suppliers:
            display_text = (
                f'{supplier["supplier_code"]} - '
                f'{supplier["supplier_name"]}'
            )

            self.ui.cmbSupplier.addItem(
                display_text,
                supplier["id"],
            )

    def configure_widgets(self):
        self.set_read_only(
            self.ui.txtPurchaseOrderNumber,
            self.ui.txtStatus,
        )

        self.ui.dtOrderDate.setCalendarPopup(True)
        self.ui.dtExpectedDate.setCalendarPopup(True)

        blank_date = QDate(2000, 1, 1)

        self.ui.dtExpectedDate.setMinimumDate(
            blank_date
        )

        self.ui.dtExpectedDate.setSpecialValueText(
            " "
        )

        self.ui.dtExpectedDate.setDate(
            blank_date
        )

    def connect_signals(self):
        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.btnAddItem.clicked.connect(
            self.add_item
        )

        self.ui.btnEditItem.clicked.connect(
            self.edit_item
        )

        self.ui.btnDeleteItem.clicked.connect(
            self.delete_item
        )

        self.ui.tblItems.itemDoubleClicked.connect(
            self.edit_item
        )

        self.ui.btnMarkOrdered.clicked.connect(
            self.mark_ordered
        )

        self.ui.btnCancelOrder.clicked.connect(
            self.cancel_order
        )

        self.ui.btnReceiveStock.clicked.connect(
            self.receive_stock
        )

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.txtPurchaseOrderNumber.setText(
            PurchaseOrderService
            .get_next_purchase_order_number()
        )

        if self.ui.cmbSupplier.count() > 0:
            self.ui.cmbSupplier.setCurrentIndex(0)

        today = QDate.currentDate()

        self.ui.dtOrderDate.setDate(
            today
        )

        self.ui.dtExpectedDate.setDate(
            self.ui.dtExpectedDate.minimumDate()
        )

        self.ui.txtStatus.setText(
            PurchaseOrderService.DRAFT
        )

        self.ui.txtReference.clear()
        self.ui.txtNotes.clear()

        self.ui.tblItems.setRowCount(0)

        self.update_total()

        # A new PO has no database ID yet.
        self.set_item_controls_enabled(False)

        self.ui.btnMarkOrdered.setEnabled(False)

        self.ui.btnCancelOrder.setEnabled(False)

        self.ui.btnReceiveStock.setEnabled(False)

    def prefill_from_inventory(self, inventory):
        if not inventory:
            return

        self.pending_inventory_item = dict(
            inventory
        )

        supplier_id = inventory["supplier_id"]

        if supplier_id is not None:
            supplier_index = (
                self.ui.cmbSupplier.findData(
                    supplier_id
                )
            )

            if supplier_index >= 0:
                self.ui.cmbSupplier.setCurrentIndex(
                    supplier_index
                )

        part_number = (
            inventory["part_number"] or ""
        )

        self.ui.txtReference.setText(
            f"REORDER-{part_number}"
        )

    # ---------------------------------------------------------
    # Form data
    # ---------------------------------------------------------

    def get_form_data(self):
        expected_date = None

        if (
            self.ui.dtExpectedDate.date()
            != self.ui.dtExpectedDate.minimumDate()
        ):
            expected_date = (
                self.ui.dtExpectedDate
                .date()
                .toString("yyyy-MM-dd")
            )

        return {
            "purchase_order_number":
                self.ui.txtPurchaseOrderNumber
                .text()
                .strip(),

            "supplier_id":
                self.ui.cmbSupplier.currentData(),

            "order_date":
                self.ui.dtOrderDate
                .date()
                .toString("yyyy-MM-dd"),

            "expected_date":
                expected_date,

            "reference":
                self.ui.txtReference.text().strip(),

            "notes":
                self.ui.txtNotes.toPlainText().strip(),

            "user_id":
                self.user.get("id"),

            "username":
                self.user.get("username"),
        }

    def set_form_data(self, purchase_order):
        self.ui.txtPurchaseOrderNumber.setText(
            purchase_order[
                "purchase_order_number"
            ]
        )

        supplier_index = (
            self.ui.cmbSupplier.findData(
                purchase_order["supplier_id"]
            )
        )

        if supplier_index >= 0:
            self.ui.cmbSupplier.setCurrentIndex(
                supplier_index
            )

        self.set_date_value(
            self.ui.dtOrderDate,
            purchase_order["order_date"],
        )

        expected_date = purchase_order[
            "expected_date"
        ]

        if expected_date:
            self.set_date_value(
                self.ui.dtExpectedDate,
                expected_date,
            )
        else:
            self.ui.dtExpectedDate.setDate(
                self.ui.dtExpectedDate.minimumDate()
            )

        self.ui.txtStatus.setText(
            purchase_order["status"] or ""
        )

        self.ui.txtReference.setText(
            purchase_order["reference"] or ""
        )

        self.ui.txtNotes.setPlainText(
            purchase_order["notes"] or ""
        )

    @staticmethod
    def set_date_value(date_widget, value):
        if not value:
            return

        parsed_date = QDate.fromString(
            value,
            "yyyy-MM-dd",
        )

        if parsed_date.isValid():
            date_widget.setDate(
                parsed_date
            )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load_record(self, record_id):
        purchase_order = (
            PurchaseOrderService.get_by_id(
                record_id
            )
        )

        if purchase_order is None:
            self.error(
                "Purchase Order",
                "Purchase Order not found.",
            )
            self.reject()
            return

        self.set_form_data(
            purchase_order
        )

        self.load_items()

        status = purchase_order["status"]

        is_draft = (
            status
            == PurchaseOrderService.DRAFT
        )

        can_receive = status in {
            PurchaseOrderService.ORDERED,
            PurchaseOrderService.PARTIALLY_RECEIVED,
        }

        can_cancel = status in {
            PurchaseOrderService.DRAFT,
            PurchaseOrderService.ORDERED,
        }

        self.set_header_read_only(
            not is_draft
        )

        self.set_item_controls_enabled(
            is_draft
        )

        self.ui.btnMarkOrdered.setEnabled(
            is_draft
        )

        self.ui.btnCancelOrder.setEnabled(
            can_cancel
        )

        self.ui.btnReceiveStock.setEnabled(
            can_receive
        )

    # ---------------------------------------------------------
    # Items
    # ---------------------------------------------------------

    def load_items(self):
        if self.record_id is None:
            self.ui.tblItems.setRowCount(0)
            self.update_total()
            return

        items = PurchaseOrderService.get_items(
            self.record_id
        )

        TableHelper.populate(
            self.ui.tblItems,
            items,
            self.ITEM_COLUMNS,
        )

        self.format_item_values()
        self.update_total()

    def add_item(self):
        if self.record_id is None:
            return

        dialog = PurchaseOrderItemDialog(
            self.record_id,
            self,
        )

        dialog.new_record()

        if dialog.exec():
            self.load_items()

    def edit_item(self, *_args):
        if self.record_id is None:
            return

        item_id = TableHelper.selected_id(
            self.ui.tblItems
        )

        if item_id is None:
            self.warning(
                "Purchase Order Item",
                "Please select a Purchase Order item.",
            )
            return

        dialog = PurchaseOrderItemDialog(
            self.record_id,
            self,
        )

        dialog.edit_record(
            item_id
        )

        if dialog.exec():
            self.load_items()

    def receive_stock(self):
        if self.record_id is None:
            return

        item_id = TableHelper.selected_id(
            self.ui.tblItems
        )

        if item_id is None:
            self.warning(
                "Receive Stock",
                "Please select an item to receive.",
            )
            return

        item = PurchaseOrderService.get_item(
            item_id
        )

        if item is None:
            self.warning(
                "Receive Stock",
                "Purchase Order item not found.",
            )
            return

        quantity_ordered = float(
            item["quantity_ordered"] or 0
        )

        quantity_received = float(
            item["quantity_received"] or 0
        )

        if quantity_received >= quantity_ordered:
            self.information(
                "Receive Stock",
                "This item has already been fully received.",
            )
            return

        dialog = PurchaseOrderReceiveDialog(
            item_id=item_id,
            user=self.user,
            parent=self,
        )

        if dialog.exec():
            # Reload the entire PO because receiving can
            # change both quantities and PO status.
            self.load_record(
                self.record_id
            )

    def delete_item(self):
        if self.record_id is None:
            return

        item_id = TableHelper.selected_id(
            self.ui.tblItems
        )

        if item_id is None:
            self.warning(
                "Purchase Order Item",
                "Please select a Purchase Order item.",
            )
            return

        if not self.confirm(
            "Delete Purchase Order Item",
            (
                "Are you sure you want to delete "
                "this Purchase Order item?"
            ),
        ):
            return

        try:
            PurchaseOrderService.delete_item(
                item_id
            )

        except ValueError as error:
            self.warning(
                "Purchase Order Item",
                str(error),
            )
            return

        except Exception as error:
            self.error(
                "Purchase Order Item",
                (
                    "Could not delete the Purchase "
                    f"Order item.\n\n{error}"
                ),
            )
            return

        self.load_items()

    def mark_ordered(self):
        if self.record_id is None:
            self.warning(
                "Purchase Order",
                "Save the Purchase Order before marking it as Ordered.",
            )
            return

        if not self.confirm(
            "Mark Purchase Order as Ordered",
            (
                "Mark this Purchase Order as Ordered?\n\n"
                "Once ordered, the Purchase Order header "
                "and items can no longer be edited."
            ),
        ):
            return

        try:
            PurchaseOrderService.mark_ordered(
                self.record_id
            )

        except ValueError as error:
            self.warning(
                "Purchase Order",
                str(error),
            )
            return

        except Exception as error:
            self.error(
                "Purchase Order",
                (
                    "Could not mark the Purchase Order "
                    f"as Ordered.\n\n{error}"
                ),
            )
            return

        # Reload the record so status and controls
        # immediately reflect the Ordered state.
        self.load_record(
            self.record_id
        )

        self.information(
            "Purchase Order",
            "Purchase Order marked as Ordered.",
        )

    def cancel_order(self):
        if self.record_id is None:
            self.warning(
                "Purchase Order",
                "Save the Purchase Order before cancelling it.",
            )
            return

        if not self.confirm(
            "Cancel Purchase Order",
            (
                "Are you sure you want to cancel this "
                "Purchase Order?\n\n"
                "A cancelled Purchase Order can no longer "
                "be edited or received."
            ),
        ):
            return

        try:
            PurchaseOrderService.cancel(
                self.record_id
            )

        except ValueError as error:
            self.warning(
                "Purchase Order",
                str(error),
            )
            return

        except Exception as error:
            self.error(
                "Purchase Order",
                (
                    "Could not cancel the Purchase Order."
                    f"\n\n{error}"
                ),
            )
            return

        # Reload so the status and controls immediately
        # reflect the Cancelled state.
        self.load_record(
            self.record_id
        )

        self.information(
            "Purchase Order",
            "Purchase Order cancelled.",
        )

    # ---------------------------------------------------------
    # Item formatting
    # ---------------------------------------------------------

    def format_item_values(self):
        unit_cost_column = 5
        total_column = 6

        for row in range(
            self.ui.tblItems.rowCount()
        ):
            unit_cost_item = (
                self.ui.tblItems.item(
                    row,
                    unit_cost_column,
                )
            )

            if unit_cost_item is not None:
                try:
                    unit_cost_item.setText(
                        FormatHelper.currency(
                            float(
                                unit_cost_item.text()
                                or 0
                            )
                        )
                    )
                except ValueError:
                    pass

            total_item = (
                self.ui.tblItems.item(
                    row,
                    total_column,
                )
            )

            if total_item is not None:
                try:
                    total_item.setText(
                        FormatHelper.currency(
                            float(
                                total_item.text()
                                or 0
                            )
                        )
                    )
                except ValueError:
                    pass

    def update_total(self):
        total = 0.00

        if self.record_id is not None:
            total = (
                PurchaseOrderService.get_total(
                    self.record_id
                )
            )

        self.ui.lblTotal.setText(
            f"Total: {FormatHelper.currency(total)}"
        )

    # ---------------------------------------------------------
    # Read-only / status control
    # ---------------------------------------------------------

    def set_item_controls_enabled(
        self,
        enabled,
    ):
        self.ui.btnAddItem.setEnabled(
            enabled
        )

        self.ui.btnEditItem.setEnabled(
            enabled
        )

        self.ui.btnDeleteItem.setEnabled(
            enabled
        )

        self.ui.tblItems.setEnabled(
            self.record_id is not None
        )

    def set_header_read_only(
        self,
        read_only=True,
    ):
        self.ui.cmbSupplier.setEnabled(
            not read_only
        )

        self.ui.dtOrderDate.setEnabled(
            not read_only
        )

        self.ui.dtExpectedDate.setEnabled(
            not read_only
        )

        self.ui.txtReference.setReadOnly(
            read_only
        )

        self.ui.txtNotes.setReadOnly(
            read_only
        )

        save_button = self.ui.buttonBox.button(
            self.ui.buttonBox.StandardButton.Save
        )

        if save_button is not None:
            save_button.setVisible(
                not read_only
            )

        if read_only:
            self.setWindowTitle(
                "View Purchase Order"
            )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["supplier_id"],
                "Supplier",
            ),
        ):
            return False

        if not ValidationService.check(
            self,
            ValidationService.required(
                data["order_date"],
                "Order Date",
            ),
        ):
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        data = self.get_form_data()

        if self.record_id is None:
            purchase_order_id = (
                PurchaseOrderService.create(
                    data
                )
            )

            try:
                if self.pending_inventory_item:
                    reorder_quantity = float(
                        self.pending_inventory_item[
                            "reorder_quantity"
                        ] or 0
                    )

                    if reorder_quantity <= 0:
                        raise ValueError(
                            "Reorder Quantity must be "
                            "greater than zero."
                        )

                    PurchaseOrderService.add_item(
                        purchase_order_id,
                        {
                            "inventory_id":
                                self.pending_inventory_item[
                                    "id"
                                ],

                            "quantity_ordered":
                                reorder_quantity,

                            "unit_cost":
                                float(
                                    self.pending_inventory_item[
                                        "unit_cost"
                                    ] or 0
                                ),

                            "notes":
                                "Created from low stock reorder.",
                        },
                    )

            except Exception:
                # Do not leave an empty Draft PO behind
                # if the automatic reorder item fails.
                PurchaseOrderService.delete(
                    purchase_order_id
                )
                raise

            self.record_id = purchase_order_id

        else:
            PurchaseOrderService.update(
                self.record_id,
                data,
            )