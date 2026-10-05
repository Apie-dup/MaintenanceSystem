from app.database.connection import Database


class VehicleSopItemModel:
    """
    Database operations for Vehicle SOP checklist items.
    """

    @staticmethod
    def get_by_sop_id(sop_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    id,
                    sop_id,
                    sequence,
                    check_description,
                    required,
                    created_at
                FROM vehicle_sop_items
                WHERE sop_id = ?
                ORDER BY
                    sequence,
                    id
            """, (sop_id,))

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_by_id(item_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    id,
                    sop_id,
                    sequence,
                    check_description,
                    required,
                    created_at
                FROM vehicle_sop_items
                WHERE id = ?
            """, (item_id,))

            return cursor.fetchone()

        finally:
            conn.close()

    @staticmethod
    def get_next_sequence(sop_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT MAX(sequence)
                FROM vehicle_sop_items
                WHERE sop_id = ?
            """, (sop_id,))

            row = cursor.fetchone()

            return (row[0] or 0) + 1

        finally:
            conn.close()

    @staticmethod
    def create(data):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO vehicle_sop_items
                (
                    sop_id,
                    sequence,
                    check_description,
                    required
                )
                VALUES (?, ?, ?, ?)
            """, (
                data["sop_id"],
                data["sequence"],
                data["check_description"],
                data.get("required", 1),
            ))

            conn.commit()

            return cursor.lastrowid

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def update(data):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE vehicle_sop_items
                SET
                    sequence = ?,
                    check_description = ?,
                    required = ?
                WHERE id = ?
            """, (
                data["sequence"],
                data["check_description"],
                data.get("required", 1),
                data["id"],
            ))

            conn.commit()

            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def delete(item_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM vehicle_sop_items
                WHERE id = ?
            """, (item_id,))

            conn.commit()

            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()