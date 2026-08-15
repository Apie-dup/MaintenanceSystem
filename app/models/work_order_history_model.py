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
    ):
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
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                work_order_id,
                action,
                field_name,
                old_value,
                new_value,
                notes,
            ))

            record_id = cursor.lastrowid

            conn.commit()

            return record_id

        except Exception:
            conn.rollback()
            raise

        finally:
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