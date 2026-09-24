from app.database.connection import Database


class PurchaseOrderItemModel:

    # ---------------------------------------------------------
    # Get items by purchase order
    # ---------------------------------------------------------

    @staticmethod
    def get_by_purchase_order(
        purchase_order_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    purchase_order_items.id,
                    purchase_order_items.purchase_order_id,
                    purchase_order_items.inventory_id,

                    inventory.part_number,
                    inventory.part_name,
                    inventory.unit,

                    purchase_order_items.quantity_ordered,
                    purchase_order_items.quantity_received,
                    purchase_order_items.unit_cost,

                    (
                        purchase_order_items.quantity_ordered
                        * purchase_order_items.unit_cost
                    ) AS line_total,

                    (
                        purchase_order_items.quantity_ordered
                        - purchase_order_items.quantity_received
                    ) AS quantity_outstanding,

                    purchase_order_items.notes

                FROM purchase_order_items

                INNER JOIN inventory
                    ON purchase_order_items.inventory_id
                    = inventory.id

                WHERE
                    purchase_order_items.purchase_order_id = ?

                ORDER BY
                    purchase_order_items.id
            """, (
                purchase_order_id,
            ))

            return cursor.fetchall()

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Get by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(
        item_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    purchase_order_items.id,
                    purchase_order_items.purchase_order_id,
                    purchase_order_items.inventory_id,

                    inventory.part_number,
                    inventory.part_name,
                    inventory.unit,

                    purchase_order_items.quantity_ordered,
                    purchase_order_items.quantity_received,
                    purchase_order_items.unit_cost,

                    (
                        purchase_order_items.quantity_ordered
                        * purchase_order_items.unit_cost
                    ) AS line_total,

                    (
                        purchase_order_items.quantity_ordered
                        - purchase_order_items.quantity_received
                    ) AS quantity_outstanding,

                    purchase_order_items.notes

                FROM purchase_order_items

                INNER JOIN inventory
                    ON purchase_order_items.inventory_id
                    = inventory.id

                WHERE
                    purchase_order_items.id = ?
            """, (
                item_id,
            ))

            return cursor.fetchone()

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Insert
    # ---------------------------------------------------------

    @staticmethod
    def insert(
        data,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO purchase_order_items
                (
                    purchase_order_id,
                    inventory_id,
                    quantity_ordered,
                    quantity_received,
                    unit_cost,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data["purchase_order_id"],
                data["inventory_id"],
                data["quantity_ordered"],
                data.get(
                    "quantity_received",
                    0,
                ),
                data.get(
                    "unit_cost",
                    0,
                ),
                data.get("notes"),
            ))

            item_id = cursor.lastrowid

            if owns_connection:
                conn.commit()

            return item_id

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(
        item_id,
        data,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            conn.execute("""
                UPDATE purchase_order_items
                SET
                    inventory_id = ?,
                    quantity_ordered = ?,
                    unit_cost = ?,
                    notes = ?
                WHERE id = ?
            """, (
                data["inventory_id"],
                data["quantity_ordered"],
                data.get(
                    "unit_cost",
                    0,
                ),
                data.get("notes"),
                item_id,
            ))

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Update quantity received
    # ---------------------------------------------------------

    @staticmethod
    def update_quantity_received(
        item_id,
        quantity_received,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            conn.execute("""
                UPDATE purchase_order_items
                SET quantity_received = ?
                WHERE id = ?
            """, (
                quantity_received,
                item_id,
            ))

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(
        item_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            conn.execute("""
                DELETE FROM purchase_order_items
                WHERE id = ?
            """, (
                item_id,
            ))

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    @staticmethod
    def get_open_order_for_inventory(
        inventory_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    purchase_order_items.id,
                    purchase_order_items.purchase_order_id,
                    purchase_order_items.inventory_id,
                    purchase_order_items.quantity_ordered,
                    purchase_order_items.quantity_received,

                    (
                        purchase_order_items.quantity_ordered
                        - purchase_order_items.quantity_received
                    ) AS quantity_outstanding,

                    purchase_orders.purchase_order_number,
                    purchase_orders.status

                FROM purchase_order_items

                INNER JOIN purchase_orders
                    ON purchase_order_items.purchase_order_id
                    = purchase_orders.id

                WHERE
                    purchase_order_items.inventory_id = ?

                    AND purchase_orders.status IN (
                        'Draft',
                        'Ordered',
                        'Partially Received'
                    )

                    AND purchase_order_items.quantity_received
                        < purchase_order_items.quantity_ordered

                ORDER BY
                    purchase_orders.id DESC

                LIMIT 1
            """, (
                inventory_id,
            ))

            return cursor.fetchone()

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Purchase order total
    # ---------------------------------------------------------

    @staticmethod
    def get_total(
        purchase_order_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(
                            quantity_ordered
                            * unit_cost
                        ),
                        0
                    ) AS total

                FROM purchase_order_items

                WHERE purchase_order_id = ?
            """, (
                purchase_order_id,
            ))

            row = cursor.fetchone()

            return float(
                row["total"] or 0
            )

        finally:
            if owns_connection:
                conn.close()