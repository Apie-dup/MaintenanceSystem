from app.database.connection import Database


class AssetModel:

# --------------------------------------------------
# READ
# --------------------------------------------------

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                asset_number,
                asset_name,
                description,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                purchase_date,
                warranty_expiry,
                status
            FROM assets
            ORDER BY asset_number
     """)

        rows = cursor.fetchall()
        conn.close()

        return rows
    
    @staticmethod
    def get_by_id(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                asset_number,
                asset_name,
                description,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                purchase_date,
                warranty_expiry,
                status
            FROM assets
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()

        conn.close()

        return row
    
    @staticmethod
    def search(text):

        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{text}%"

        cursor.execute("""
            SELECT
                id,
                asset_number,
                asset_name,
                description,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                warranty_expiry,
                status
            FROM assets
            WHERE
                asset_number LIKE ?
                OR asset_name LIKE ?
                OR category LIKE ?
                OR location LIKE ?
                OR manufacturer LIKE ?
                OR model LIKE ?
                OR serial_number LIKE ?
                OR status LIKE ?
        """, (

            search,
            search,
            search,
            search,
            search,
            search,
            search,
            search
        ))

        rows = cursor.fetchall()

        conn.close()

        return rows
    
# --------------------------------------------------
# CREATE
# --------------------------------------------------

    @staticmethod
    def insert(asset):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO assets (
                asset_number,
                asset_name,
                description,
                category,
                location,
                manufacturer,
                model,
                serial_number,
                purchase_date,
                warranty_expiry,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, asset)

        conn.commit()
        conn.close()

# --------------------------------------------------
# UPDATE
# --------------------------------------------------

    @staticmethod
    def update(asset):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE assets
            SER
                asset_number = ?,
                asset_name = ?,
                description = ?,
                location = ?,
                manufacturer = ?,
                model = ?,
                serial_number = ?,
                purchase_date = ?,
                warrenty_expiry = ?,
                status = ?
            WHERE id = ?
        """, asset)

        conn.commit()
        conn.close()

# --------------------------------------------------
# DELETE
# --------------------------------------------------

    @staticmethod
    def delete(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM assets
            WHERE id = ?
        """, (record_id))

        conn.commit()
        conn.close()

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

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
    
    