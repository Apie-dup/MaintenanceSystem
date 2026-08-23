from app.database.connection import Database


class SettingsModel:

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                key,
                value,
                description,
                updated_at
            FROM app_settings
            ORDER BY key
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_value(key, default=None):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT value
            FROM app_settings
            WHERE key = ?
            LIMIT 1
        """, (key,))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return default

        return row["value"]

    @staticmethod
    def set_value(key, value):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE app_settings
            SET
                value = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE key = ?
        """, (
            value,
            key,
        ))

        conn.commit()
        conn.close()