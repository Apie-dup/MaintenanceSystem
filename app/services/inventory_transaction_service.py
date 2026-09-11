from app.models.inventory_transaction_model import(
    InventoryTransactionModel,
)
from app.database.connection import Database
from app.models.inventory_model import InventoryModel



class InventoryTransactionService:

    # --------------------------------------------------------------
    # Transaction types
    # --------------------------------------------------------------

    OPENING_STOCK = "Opening Stock"
    STOCK_RECEIVED = "Stock Received"
    ADJUSTMENT_INCREASE = "Adjustment Increase"
    ADJUSTMENT_DECREASE = "Adjustment Decrease"
    ISSUED_TO_WORK_ORDER = "Issued to Work Order"
    RETURNED_FROM_WORK_ORDER = "Returned from Work Order"

    # --------------------------------------------------------------
    # Read
    # --------------------------------------------------------------

    @staticmethod
    def get_by_inventory(
        inventory_id
    ):

        return (
            InventoryTransactionModel
            .get_by_inventory(
                inventory_id
            )
        )

    @staticmethod
    def get_by_id(
        record_id
    ):

        return (
            InventoryTransactionModel
            .get_by_id(
                record_id
            )
        )

    # ------------------------------------------------------------------
    # Record transaction
    # ------------------------------------------------------------------

    @staticmethod
    def record(
        inventory_id,
        transaction_type,
        quantity_change,
        previous_quantity,
        new_quantity,
        unit_cost=0,
        work_order_id=None,
        reference=None,
        notes=None,
        user=None,
        connection=None
    ):

        if inventory_id is None:
            raise ValueError(
                "Inventory item is required."
            )

        if not (
            transaction_type or ""
        ).strip():
            raise ValueError(
                "Transaction type is required."
            )

        quantity_change = float(
            quantity_change or 0
        )

        previous_quantity = float(
            previous_quantity or 0
        )

        new_quantity = float(
            new_quantity or 0
        )

        unit_cost = float(
            unit_cost or 0
        )

        if previous_quantity < 0:
            raise ValueError(
                "Previous quantity cannot be negative."
            )

        if new_quantity < 0:
            raise ValueError(
                "New quantity cannot be negative."
            )

        data = {
            "inventory_id":
                inventory_id,

            "transaction_type":
                transaction_type,

            "quantity_change":
                quantity_change,

            "previous_quantity":
                previous_quantity,

            "new_quantity":
                new_quantity,

            "unit_cost":
                unit_cost,

            "work_order_id":
                work_order_id,

            "reference":
                reference,

            "notes":
                notes,

            "user_id": (
                user.get("id")
                if user
                else None
            ),

            "username": (
                user.get("username")
                if user
                else None
            ),
        }

        return (
            InventoryTransactionModel
            .insert(
                data,
                connection=connection
            )
        )

    @staticmethod
    def receive_stock(
        inventory_id,
        quantity,
        unit_cost=None,
        reference=None,
        notes=None,
        user=None
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

            inventory = InventoryModel.get_by_id(
                inventory_id
            )

            if inventory is None:
                raise ValueError(
                    "Inventory item not found."
                )

            previous_quantity = float(
                inventory["quantity"] or 0
            )

            current_unit_cost = float(
                inventory["unit_cost"] or 0
            )

            if unit_cost is None:
                unit_cost = current_unit_cost
            else:
                unit_cost = float(
                    unit_cost or 0
                )

            if unit_cost < 0:
                raise ValueError(
                    "Unit Cost cannot be negative."
                )

            new_quantity = (
                previous_quantity
                + quantity
            )

            InventoryModel.update_quantity(
                inventory_id,
                new_quantity,
                connection=conn
            )

            InventoryTransactionService.record(
                inventory_id=inventory_id,
                transaction_type=(
                    InventoryTransactionService
                    .STOCK_RECEIVED
                ),
                quantity_change=quantity,
                previous_quantity=previous_quantity,
                new_quantity=new_quantity,
                unit_cost=unit_cost,
                reference=reference,
                notes=notes,
                user=user,
                connection=conn,
            )

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()

    @staticmethod
    def adjust_stock(
        inventory_id,
        adjustment_type,
        quantity,
        reference=None,
        notes=None,
        user=None
    ):

        quantity = float(
            quantity or 0
        )

        if quantity <= 0:
            raise ValueError(
                "Adjustment Quantity must be greater than zero."
            )

        adjustment_type = (
            adjustment_type or ""
        ).strip()

        if adjustment_type not in {
            "Increase",
            "Decrease",
        }:
            raise ValueError(
                "Adjustment Type must be Increase or Decrease."
            )

        conn = Database.connect()

        try:

            inventory = InventoryModel.get_by_id(
                inventory_id
            )

            if inventory is None:
                raise ValueError(
                    "Inventory item not found."
                )

            previous_quantity = float(
                inventory["quantity"] or 0
            )

            unit_cost = float(
                inventory["unit_cost"] or 0
            )

            if adjustment_type == "Increase":

                quantity_change = quantity

                transaction_type = (
                    InventoryTransactionService
                    .ADJUSTMENT_INCREASE
                )

            else:

                quantity_change = -quantity

                transaction_type = (
                    InventoryTransactionService
                    .ADJUSTMENT_DECREASE
                )

            new_quantity = (
                previous_quantity
                + quantity_change
            )

            if new_quantity < 0:
                raise ValueError(
                    "Adjustment would reduce stock below zero."
                )

            InventoryModel.update_quantity(
                inventory_id,
                new_quantity,
                connection=conn
            )

            InventoryTransactionService.record(
                inventory_id=inventory_id,
                transaction_type=transaction_type,
                quantity_change=quantity_change,
                previous_quantity=previous_quantity,
                new_quantity=new_quantity,
                unit_cost=unit_cost,
                reference=reference,
                notes=notes,
                user=user,
                connection=conn,
            )

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:

            conn.close()