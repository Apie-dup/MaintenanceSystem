from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class PurchaseOrderModel:

    # ---------------------------------------------------------
    # Get all
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    purchase_orders.id,
                    purchase_orders.purchase_order_number,
                    purchase_orders.supplier_id,

                    suppliers.supplier_code,
                    suppliers.supplier_name,

                    purchase_orders.order_date,
                    purchase_orders.expected_date,
                    purchase_orders.status,
                    purchase_orders.reference,
                    purchase_orders.notes,
                    purchase_orders.user_id,
                    purchase_orders.username,
                    purchase_orders.created_at

                FROM purchase_orders

                LEFT JOIN suppliers
                    ON purchase_orders.supplier_id
                    = suppliers.id

                ORDER BY
                    purchase_orders.id DESC
            """)

            return cursor.fetchall()

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Get by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(
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
                    purchase_orders.id,
                    purchase_orders.purchase_order_number,
                    purchase_orders.supplier_id,

                    suppliers.supplier_code,
                    suppliers.supplier_name,

                    purchase_orders.order_date,
                    purchase_orders.expected_date,
                    purchase_orders.status,
                    purchase_orders.reference,
                    purchase_orders.notes,
                    purchase_orders.user_id,
                    purchase_orders.username,
                    purchase_orders.created_at

                FROM purchase_orders

                LEFT JOIN suppliers
                    ON purchase_orders.supplier_id
                    = suppliers.id

                WHERE purchase_orders.id = ?
            """, (
                purchase_order_id,
            ))

            return cursor.fetchone()

        finally:
            if owns_connection:
                conn.close()

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            search = (
                f"%{search_text or ''}%"
            )

            cursor.execute("""
                SELECT
                    purchase_orders.id,
                    purchase_orders.purchase_order_number,
                    purchase_orders.supplier_id,

                    suppliers.supplier_code,
                    suppliers.supplier_name,

                    purchase_orders.order_date,
                    purchase_orders.expected_date,
                    purchase_orders.status,
                    purchase_orders.reference,
                    purchase_orders.notes,
                    purchase_orders.user_id,
                    purchase_orders.username,
                    purchase_orders.created_at

                FROM purchase_orders

                LEFT JOIN suppliers
                    ON purchase_orders.supplier_id
                    = suppliers.id

                WHERE
                    purchase_orders.purchase_order_number LIKE ?
                    OR suppliers.supplier_code LIKE ?
                    OR suppliers.supplier_name LIKE ?
                    OR purchase_orders.status LIKE ?
                    OR purchase_orders.reference LIKE ?

                ORDER BY
                    purchase_orders.id DESC
            """, (
                search,
                search,
                search,
                search,
                search,
            ))

            return cursor.fetchall()

        finally:
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
                INSERT INTO purchase_orders
                (
                    purchase_order_number,
                    supplier_id,
                    order_date,
                    expected_date,
                    status,
                    reference,
                    notes,
                    user_id,
                    username
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["purchase_order_number"],
                data["supplier_id"],
                data["order_date"],
                data.get("expected_date"),
                data.get("status", "Draft"),
                data.get("reference"),
                data.get("notes"),
                data.get("user_id"),
                data.get("username"),
            ))

            purchase_order_id = (
                cursor.lastrowid
            )

            if owns_connection:
                conn.commit()

            return purchase_order_id

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
        purchase_order_id,
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
                UPDATE purchase_orders
                SET
                    supplier_id = ?,
                    order_date = ?,
                    expected_date = ?,
                    status = ?,
                    reference = ?,
                    notes = ?
                WHERE id = ?
            """, (
                data["supplier_id"],
                data["order_date"],
                data.get("expected_date"),
                data["status"],
                data.get("reference"),
                data.get("notes"),
                purchase_order_id,
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
    # Update status
    # ---------------------------------------------------------

    @staticmethod
    def update_status(
        purchase_order_id,
        status,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            conn.execute("""
                UPDATE purchase_orders
                SET status = ?
                WHERE id = ?
            """, (
                status,
                purchase_order_id,
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
        purchase_order_id,
        connection=None,
    ):
        owns_connection = connection is None

        conn = (
            connection
            or Database.connect()
        )

        try:
            conn.execute("""
                DELETE FROM purchase_orders
                WHERE id = ?
            """, (
                purchase_order_id,
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
    # Next purchase order number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_purchase_order_number():
        return CodeGenerator.next_code(
            table_name="purchase_orders",
            field_name="purchase_order_number",
            prefix="PO",
            digits=6,
        )