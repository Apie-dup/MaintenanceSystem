from app.database.connection import Database


class AssetMeterReadingModel:

    @staticmethod
    def add(
        asset_id,
        meter_type,
        reading,
        reading_date,
        notes=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO asset_meter_readings
                (
                    asset_id,
                    meter_type,
                    reading,
                    reading_date,
                    notes
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                asset_id,
                meter_type,
                reading,
                reading_date,
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

    @staticmethod
    def get_latest_reading(
        asset_id,
        meter_type,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                asset_id,
                meter_type,
                reading,
                reading_date,
                notes,
                created_at
            FROM asset_meter_readings
            WHERE asset_id = ?
              AND meter_type = ?
            ORDER BY
                reading_date DESC,
                id DESC
            LIMIT 1
        """, (
            asset_id,
            meter_type,
        ))

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def get_history(
        asset_id,
        meter_type=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        if meter_type:
            cursor.execute("""
                SELECT
                    id,
                    asset_id,
                    meter_type,
                    reading,
                    reading_date,
                    notes,
                    created_at
                FROM asset_meter_readings
                WHERE asset_id = ?
                  AND meter_type = ?
                ORDER BY
                    reading_date DESC,
                    id DESC
            """, (
                asset_id,
                meter_type,
            ))

        else:
            cursor.execute("""
                SELECT
                    id,
                    asset_id,
                    meter_type,
                    reading,
                    reading_date,
                    notes,
                    created_at
                FROM asset_meter_readings
                WHERE asset_id = ?
                ORDER BY
                    reading_date DESC,
                    id DESC
            """, (
                asset_id,
            ))

        rows = cursor.fetchall()
        conn.close()

        return rows