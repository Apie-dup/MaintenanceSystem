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

    @staticmethod
    def insert(asset):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO assets (
                asset_number,
                asset_name,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                purchase_date,
                warranty_expiry,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, asset)

        conn.commit()
        conn.close()

    @staticmethod
    def get_next_asset_number():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT asset_number
            FROM assets
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return "AST-0001"
        
        number = int(row[0].split('-')[1]) + 1
        return f"AST-{number:04d}"

        