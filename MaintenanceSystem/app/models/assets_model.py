from database import Database


class AssetModel:

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                asset_number,
                asset_name,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                status,
                warranty_expiry
            FROM assets
            ORDER BY asset_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows