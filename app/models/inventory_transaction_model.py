from app.database.connection import Database



class InventoryTransactionModel:

    # -----------------------------------------------------------
    # Insert transaction
    # -----------------------------------------------------------

    @staticmethod
    def insert(
        data,
        connection=None
    ):

        owns_connection = (
            connection is None
        )

        conn = (
            connection
            or Database.connect()
        )

        try:

            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO inventory_transactions
                (
                    inventory_id,
                    transaction_type,
                    quantity_change,
                    previous_quantity,
                    new_quantity,
                    unit_cost,
                    work_order_id,
                    reference,
                    notes,
                    user_id,
                    username
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["inventory_id"],
                data["transaction_type"],
                data["quantity_change"],
                data["previous_quantity"],
                data["new_quantity"],
                data.get("unit_cost", 0),
                data.get("work_order_id"),
                data.get("reference"),
                data.get("notes"),
                data.get("user_id"),
                data.get("username"),
            ))

            record_id = cursor.lastrowid

            if owns_connection:
                conn.commit()

            return record_id

        except Exception:

            if owns_connection:
                conn.rollback()

            raise

        finally:

            if owns_connection:
                conn.close()

    # -----------------------------------------------------------
    # Get transactions for inventory item
    # -----------------------------------------------------------

    @staticmethod
    def get_by_inventory(
        inventory_id
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory_transactions.id,
                inventory_transactions.inventory_id,
                inventory_transactions.transaction_type,
                inventory_transactions.quantity_change,
                inventory_transactions.previous_quantity,
                inventory_transactions.new_quantity,
                inventory_transactions.unit_cost,
                inventory_transactions.work_order_id,

                work_orders.work_order_number,

                inventory_transactions.reference,
                inventory_transactions.notes,
                inventory_transactions.user_id,
                inventory_transactions.username,
                inventory_transactions.created_at
            
            FROM inventory_transactions

            LEFT JOIN work_orders
                ON inventory_transactions.work_order_id
                = work_orders.id

            WHERE inventory_transactions.inventory_id = ?

            ORDER BY
                inventory_transactions.created_at DESC,
                inventory_transactions.id DESC

        """, (
            inventory_id,
        ))

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_by_id(
        record_id
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory_transactions.id,
                inventory_transactions.inventory_id,
                inventory_transactions.transaction_type,
                inventory_transactions.quantity_change,
                inventory_transactions.previous_quantity,
                inventory_transactions.new_quantity,
                inventory_transactions.unit_cost,
                inventory_transactions.work_order_id,
                
                work_orders.work_order_number,
                
                inventory_transactions.reference,
                inventory_transactions.notes,
                inventory_transactions.user_id,
                inventory_transactions.username,
                inventory_transactions.created_at
                
            FROM inventory_transactions
            
            LEFT JOIN work_orders
                ON inventory_transactions.work_order_id
                = work_orders.id
                
            WHERE inventory_transactions.id = ?
        """, (
            record_id,
        ))

        row = cursor.fetchone()

        conn.close()

        return row
