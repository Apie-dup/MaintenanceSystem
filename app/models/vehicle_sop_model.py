from app.database.connection import Database


class VehicleSopModel:
    """
    Database operations for vehicle SOP definitions.
    """

    @staticmethod
    def get_all():
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    vehicle_sops.*,
                    assets.asset_number,
                    assets.asset_name
                FROM vehicle_sops
                INNER JOIN assets
                    ON vehicle_sops.asset_id = assets.id
                ORDER BY
                    assets.asset_name,
                    CASE vehicle_sops.frequency
                        WHEN 'Daily' THEN 1
                        WHEN 'Weekly' THEN 2
                        WHEN 'Monthly' THEN 3
                        ELSE 4
                    END,
                    vehicle_sops.sop_number
            """)

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_by_id(sop_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    vehicle_sops.*,
                    assets.asset_number,
                    assets.asset_name
                FROM vehicle_sops
                INNER JOIN assets
                    ON vehicle_sops.asset_id = assets.id
                WHERE vehicle_sops.id = ?
            """, (sop_id,))

            return cursor.fetchone()

        finally:
            conn.close()

    @staticmethod
    def search(text):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            search_text = f"%{text.strip()}%"

            cursor.execute("""
                SELECT
                    vehicle_sops.*,
                    assets.asset_number,
                    assets.asset_name
                FROM vehicle_sops
                INNER JOIN assets
                    ON vehicle_sops.asset_id = assets.id
                WHERE
                    vehicle_sops.sop_number LIKE ?
                    OR vehicle_sops.sop_name LIKE ?
                    OR vehicle_sops.frequency LIKE ?
                    OR assets.asset_number LIKE ?
                    OR assets.asset_name LIKE ?
                ORDER BY
                    assets.asset_name,
                    vehicle_sops.sop_number
            """, (search_text,) * 5)

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_next_sop_number():
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT MAX(
                    CAST(SUBSTR(sop_number, 5) AS INTEGER)
                )
                FROM vehicle_sops
                WHERE sop_number GLOB 'SOP-[0-9]*'
            """)

            row = cursor.fetchone()
            next_number = (row[0] or 0) + 1

            return f"SOP-{next_number:04d}"

        finally:
            conn.close()

    @staticmethod
    def create(data):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO vehicle_sops
                (
                    sop_number,
                    asset_id,
                    sop_name,
                    frequency,
                    description,
                    active,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                data["sop_number"],
                data["asset_id"],
                data["sop_name"],
                data["frequency"],
                data.get("description"),
                data.get("active", 1),
                data.get("notes"),
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
                UPDATE vehicle_sops
                SET
                    sop_number = ?,
                    asset_id = ?,
                    sop_name = ?,
                    frequency = ?,
                    description = ?,
                    active = ?,
                    notes = ?
                WHERE id = ?
            """, (
                data["sop_number"],
                data["asset_id"],
                data["sop_name"],
                data["frequency"],
                data.get("description"),
                data.get("active", 1),
                data.get("notes"),
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
    def delete(sop_id):
        conn = Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM vehicle_sops
                WHERE id = ?
            """, (sop_id,))

            conn.commit()

            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()