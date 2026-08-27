from app.database.connection import Database


class WorkOrderHistoryModel:

    # ---------------------------------------------------------
    # Add history entry
    # ---------------------------------------------------------

    @staticmethod
    def add(
        work_order_id,
        action,
        field_name=None,
        old_value=None,
        new_value=None,
        notes=None,
        user_id=None,
        username=None,
        conn=None,
    ):
        owns_connection = (
            conn is None
        )

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO work_order_history
                (
                    work_order_id,
                    action,
                    field_name,
                    old_value,
                    new_value,
                    notes,
                    user_id,
                    username
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                work_order_id,
                action,
                field_name,
                old_value,
                new_value,
                notes,
                user_id,
                username,
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

    # ---------------------------------------------------------
    # Get Work Order history
    # ---------------------------------------------------------

    @staticmethod
    def get_history(work_order_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                work_order_id,
                action,
                field_name,
                old_value,
                new_value,
                notes,
                user_id,
                username,
                created_at
            FROM work_order_history
            WHERE work_order_id = ?
            ORDER BY
                created_at DESC,
                id DESC
        """, (
            work_order_id,
        ))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def log_created(
        work_order_id,
        user_id=None,
        username=None
    ):
        return WorkOrderHistoryModel.add(
            work_order_id,
            action="Created",
            notes="Work Order created.",
            user_id=user_id,
            username=username,
        )

    