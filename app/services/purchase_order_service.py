from app.database.connection import Database
from app.models.purchase_order_model import PurchaseOrderModel
from app.models.purchase_order_item_model import PurchaseOrderItemModel
from app.models.supplier_model import SupplierModel
from app.models.inventory_model import InventoryModel
from app.services.inventory_transaction_service import (
    InventoryTransactionService,
)


class PurchaseOrderService:

    # ---------------------------------------------------------
    # Statuses
    # ---------------------------------------------------------

    DRAFT = "Draft"
    ORDERED = "Ordered"
    PARTIALLY_RECEIVED = "Partially Received"
    RECEIVED = "Received"
    CANCELLED = "Cancelled"

    STATUSES = (
        DRAFT,
        ORDERED,
        PARTIALLY_RECEIVED,
        RECEIVED,
        CANCELLED,
    )

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        records = PurchaseOrderModel.get_all()

        return PurchaseOrderService.prepare_records(
            records
        )

    @staticmethod
    def get_by_id(purchase_order_id):
        return PurchaseOrderModel.get_by_id(
            purchase_order_id
        )

    @staticmethod
    def search(search_text):
        records = PurchaseOrderModel.search(
            search_text
        )

        return PurchaseOrderService.prepare_records(
            records
        )

    @staticmethod
    def prepare_records(records):
        prepared = []

        for record in records:
            purchase_order = dict(record)

            purchase_order["total"] = (
                PurchaseOrderItemModel.get_total(
                    purchase_order["id"]
                )
            )

            prepared.append(
                purchase_order
            )

        return prepared

    @staticmethod
    def get_items(purchase_order_id):
        return (
            PurchaseOrderItemModel
            .get_by_purchase_order(
                purchase_order_id
            )
        )

    @staticmethod
    def get_total(purchase_order_id):
        return PurchaseOrderItemModel.get_total(
            purchase_order_id
        )

    @staticmethod
    def get_next_purchase_order_number():
        return (
            PurchaseOrderModel
            .get_next_purchase_order_number()
        )

    @staticmethod
    def get_item(item_id):
        return PurchaseOrderItemModel.get_by_id(
            item_id
        )

    # ---------------------------------------------------------
    # Create PO
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        supplier_id = data.get("supplier_id")

        if supplier_id is None:
            raise ValueError(
                "Supplier is required."
            )

        supplier = SupplierModel.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Supplier not found."
            )

        order_date = (
            data.get("order_date")
            or ""
        ).strip()

        if not order_date:
            raise ValueError(
                "Order Date is required."
            )

        purchase_order_number = (
            data.get("purchase_order_number")
            or PurchaseOrderModel
            .get_next_purchase_order_number()
        )

        po_data = {
            "purchase_order_number":
                purchase_order_number,

            "supplier_id":
                supplier_id,

            "order_date":
                order_date,

            "expected_date":
                data.get("expected_date"),

            "status":
                PurchaseOrderService.DRAFT,

            "reference":
                data.get("reference"),

            "notes":
                data.get("notes"),

            "user_id": (
                data.get("user_id")
            ),

            "username": (
                data.get("username")
            ),
        }

        return PurchaseOrderModel.insert(
            po_data
        )

    # ---------------------------------------------------------
    # Update PO
    # ---------------------------------------------------------

    @staticmethod
    def update(
        purchase_order_id,
        data,
    ):

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                purchase_order_id
            )
        )

        if purchase_order is None:
            raise ValueError(
                "Purchase Order not found."
            )

        if (
            purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Only Draft Purchase Orders "
                "can be edited."
            )

        supplier_id = data.get(
            "supplier_id"
        )

        if supplier_id is None:
            raise ValueError(
                "Supplier is required."
            )

        supplier = SupplierModel.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Supplier not found."
            )

        order_date = (
            data.get("order_date")
            or ""
        ).strip()

        if not order_date:
            raise ValueError(
                "Order Date is required."
            )

        update_data = {
            "supplier_id":
                supplier_id,

            "order_date":
                order_date,

            "expected_date":
                data.get("expected_date"),

            "status":
                PurchaseOrderService.DRAFT,

            "reference":
                data.get("reference"),

            "notes":
                data.get("notes"),
        }

        PurchaseOrderModel.update(
            purchase_order_id,
            update_data,
        )

    # ---------------------------------------------------------
    # Add item
    # ---------------------------------------------------------

    @staticmethod
    def add_item(
        purchase_order_id,
        data,
    ):

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                purchase_order_id
            )
        )

        if purchase_order is None:
            raise ValueError(
                "Purchase Order not found."
            )

        if (
            purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Items can only be added to "
                "a Draft Purchase Order."
            )

        inventory_id = data.get(
            "inventory_id"
        )

        if inventory_id is None:
            raise ValueError(
                "Inventory item is required."
            )

        inventory = InventoryModel.get_by_id(
            inventory_id
        )

        if inventory is None:
            raise ValueError(
                "Inventory item not found."
            )

        quantity = float(
            data.get(
                "quantity_ordered",
                0,
            )
            or 0
        )

        if quantity <= 0:
            raise ValueError(
                "Quantity Ordered must be "
                "greater than zero."
            )

        unit_cost = float(
            data.get(
                "unit_cost",
                0,
            )
            or 0
        )

        if unit_cost < 0:
            raise ValueError(
                "Unit Cost cannot be negative."
            )

        item_data = {
            "purchase_order_id":
                purchase_order_id,

            "inventory_id":
                inventory_id,

            "quantity_ordered":
                quantity,

            "quantity_received":
                0,

            "unit_cost":
                unit_cost,

            "notes":
                data.get("notes"),
        }

        return PurchaseOrderItemModel.insert(
            item_data
        )

    # ---------------------------------------------------------
    # Update item
    # ---------------------------------------------------------

    @staticmethod
    def update_item(
        item_id,
        data,
    ):

        item = PurchaseOrderItemModel.get_by_id(
            item_id
        )

        if item is None:
            raise ValueError(
                "Purchase Order item not found."
            )

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                item["purchase_order_id"]
            )
        )

        if (
            purchase_order is None
            or purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Only items on a Draft Purchase "
                "Order can be edited."
            )

        inventory_id = data.get(
            "inventory_id"
        )

        if inventory_id is None:
            raise ValueError(
                "Inventory item is required."
            )

        inventory = InventoryModel.get_by_id(
            inventory_id
        )

        if inventory is None:
            raise ValueError(
                "Inventory item not found."
            )

        quantity = float(
            data.get(
                "quantity_ordered",
                0,
            )
            or 0
        )

        if quantity <= 0:
            raise ValueError(
                "Quantity Ordered must be "
                "greater than zero."
            )

        unit_cost = float(
            data.get(
                "unit_cost",
                0,
            )
            or 0
        )

        if unit_cost < 0:
            raise ValueError(
                "Unit Cost cannot be negative."
            )

        PurchaseOrderItemModel.update(
            item_id,
            {
                "inventory_id":
                    inventory_id,

                "quantity_ordered":
                    quantity,

                "unit_cost":
                    unit_cost,

                "notes":
                    data.get("notes"),
            },
        )

    # ---------------------------------------------------------
    # Delete item
    # ---------------------------------------------------------

    @staticmethod
    def delete_item(item_id):

        item = PurchaseOrderItemModel.get_by_id(
            item_id
        )

        if item is None:
            raise ValueError(
                "Purchase Order item not found."
            )

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                item["purchase_order_id"]
            )
        )

        if (
            purchase_order is None
            or purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Only items on a Draft Purchase "
                "Order can be removed."
            )

        PurchaseOrderItemModel.delete(
            item_id
        )

    @staticmethod
    def delete(purchase_order_id):
        purchase_order = (
            PurchaseOrderModel.get_by_id(
                purchase_order_id
            )
        )

        if purchase_order is None:
            raise ValueError(
                "Purchase Order not found."
            )

        if (
            purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Only Draft Purchase Orders can be deleted."
            )

        PurchaseOrderModel.delete(
            purchase_order_id
        )

    # ---------------------------------------------------------
    # Mark as ordered
    # ---------------------------------------------------------

    @staticmethod
    def mark_ordered(
        purchase_order_id,
    ):

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                purchase_order_id
            )
        )

        if purchase_order is None:
            raise ValueError(
                "Purchase Order not found."
            )

        if (
            purchase_order["status"]
            != PurchaseOrderService.DRAFT
        ):
            raise ValueError(
                "Only a Draft Purchase Order "
                "can be marked as Ordered."
            )

        items = (
            PurchaseOrderItemModel
            .get_by_purchase_order(
                purchase_order_id
            )
        )

        if not items:
            raise ValueError(
                "The Purchase Order must contain "
                "at least one item before it can "
                "be marked as Ordered."
            )

        PurchaseOrderModel.update_status(
            purchase_order_id,
            PurchaseOrderService.ORDERED,
        )

    @staticmethod
    def cancel(
        purchase_order_id,
    ):

        purchase_order = (
            PurchaseOrderModel.get_by_id(
                purchase_order_id
            )
        )

        if purchase_order is None:
            raise ValueError(
                "Purchase Order not found."
            )

        status = purchase_order["status"]

        if status == PurchaseOrderService.CANCELLED:
            raise ValueError(
                "This Purchase Order is already "
                "Cancelled."
            )

        if status == PurchaseOrderService.RECEIVED:
            raise ValueError(
                "A Received Purchase Order "
                "cannot be cancelled."
            )

        if (
            status
            == PurchaseOrderService.PARTIALLY_RECEIVED
        ):
            raise ValueError(
                "A Partially Received Purchase Order "
                "cannot be cancelled."
            )

        if status not in (
            PurchaseOrderService.DRAFT,
            PurchaseOrderService.ORDERED,
        ):
            raise ValueError(
                "This Purchase Order cannot "
                "be cancelled."
            )

        items = (
            PurchaseOrderItemModel
            .get_by_purchase_order(
                purchase_order_id
            )
        )

        for item in items:
            if float(
                item["quantity_received"] or 0
            ) > 0:
                raise ValueError(
                    "This Purchase Order cannot be "
                    "cancelled because stock has "
                    "already been received."
                )

        PurchaseOrderModel.update_status(
            purchase_order_id,
            PurchaseOrderService.CANCELLED,
        )

    # ---------------------------------------------------------
    # Receive item
    # ---------------------------------------------------------

    @staticmethod
    def receive_item(
        item_id,
        quantity,
        user=None,
        notes=None,
    ):
        quantity = float(
            quantity or 0
        )

        if quantity <= 0:
            raise ValueError(
                "Received Quantity must be greater than zero."
            )

        conn = Database.connect()

        try:
            # -------------------------------------------------
            # Get PO item
            # -------------------------------------------------
            item = PurchaseOrderItemModel.get_by_id(
                item_id,
                connection=conn,
            )

            if item is None:
                raise ValueError(
                    "Purchase Order item not found."
                )

            # -------------------------------------------------
            # Get PO
            # -------------------------------------------------

            purchase_order = PurchaseOrderModel.get_by_id(
                item["purchase_order_id"],
                connection=conn,
            )

            if purchase_order is None:
                raise ValueError(
                    "Purchase Order not found."
                )

            if purchase_order["status"] not in {
                PurchaseOrderService.ORDERED,
                PurchaseOrderService.PARTIALLY_RECEIVED,
            }:
                raise ValueError(
                    "Stock can only be received against "
                    "an Ordered or Partially Received "
                    "Purchase Order."
                )

            # -------------------------------------------------
            # Validate outstanding quantity
            # -------------------------------------------------

            quantity_ordered = float(
                item["quantity_ordered"] or 0
            )

            quantity_received = float(
                item["quantity_received"] or 0
            )

            quantity_outstanding = (
                quantity_ordered
                - quantity_received
            )

            if quantity > quantity_outstanding:
                raise ValueError(
                    "Received Quantity cannot exceed "
                    "the outstanding quantity."
                )

            # -------------------------------------------------
            # Get inventory
            # -------------------------------------------------

            inventory = InventoryModel.get_by_id(
                item["inventory_id"],
                connection=conn,
            )

            if inventory is None:
                raise ValueError(
                    "Inventory item not found."
                )

            previous_quantity = float(
                inventory["quantity"] or 0
            )

            new_quantity = (
                previous_quantity
                + quantity
            )

            # -------------------------------------------------
            # Update inventory
            # -------------------------------------------------

            InventoryModel.update_quantity(
                item["inventory_id"],
                new_quantity,
                connection=conn,
            )

            # -------------------------------------------------
            # Update PO item
            # -------------------------------------------------

            new_quantity_received = (
                quantity_received
                + quantity
            )

            PurchaseOrderItemModel.update_quantity_received(
                item_id,
                new_quantity_received,
                connection=conn,
            )

            # -------------------------------------------------
            # Inventory transaction
            # -------------------------------------------------

            InventoryTransactionService.record(
                inventory_id=item["inventory_id"],
                transaction_type=(
                    InventoryTransactionService.STOCK_RECEIVED
                ),
                quantity_change=quantity,
                previous_quantity=previous_quantity,
                new_quantity=new_quantity,
                unit_cost=float(
                    item["unit_cost"] or 0
                ),
                reference=(
                    purchase_order[
                        "purchase_order_number"
                    ]
                ),
                notes=notes,
                user=user,
                connection=conn,
            )

            # -------------------------------------------------
            # Recalculate PO status
            # -------------------------------------------------

            items = (
                PurchaseOrderItemModel
                .get_by_purchase_order(
                    item["purchase_order_id"],
                    connection=conn,
                )
            )

            all_received = all(
                float(
                    row["quantity_received"] or 0
                )
                >= float(
                    row["quantity_ordered"] or 0
                )
                for row in items
            )

            if all_received:
                new_status = (
                    PurchaseOrderService.RECEIVED
                )
            else:
                new_status = (
                    PurchaseOrderService
                    .PARTIALLY_RECEIVED
                )

            PurchaseOrderModel.update_status(
                item["purchase_order_id"],
                new_status,
                connection=conn,
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def get_open_order_for_inventory(
        inventory_id
    ):
        return (
            PurchaseOrderItemModel
            .get_open_order_for_inventory(
                inventory_id
            )
        )