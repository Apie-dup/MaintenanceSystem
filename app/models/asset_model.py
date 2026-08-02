from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class AssetModel:

    # ---------------------------------------------------------
    # Get all assets
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Get asset by ID
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

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
            WHERE
                asset_number LIKE ?
                OR asset_name LIKE ?
                OR description LIKE ?
                OR category LIKE ?
                OR location LIKE ?
                OR manufacturer LIKE ?
                OR model LIKE ?
                OR serial_number LIKE ?
                OR status LIKE ?
            ORDER BY asset_number
        """, (
            search,
            search,
            search,
            search,
            search,
            search,
            search,
            search,
            search,
        ))

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Insert
    # ---------------------------------------------------------

    @staticmethod
    def insert(data):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO assets
            (
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
        """, (
            data["asset_number"],
            data["asset_name"],
            data["description"],
            data["category"],
            data["location"],
            data["manufacturer"],
            data["model"],
            data["serial_number"],
            data["purchase_date"],
            data["warranty_expiry"],
            data["status"],
        ))

        conn.commit()

        record_id = cursor.lastrowid

        conn.close()

        return record_id

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE assets
            SET
                asset_number = ?,
                asset_name = ?,
                description = ?,
                category = ?,
                location = ?,
                manufacturer = ?,
                model = ?,
                serial_number = ?,
                purchase_date = ?,
                warranty_expiry = ?,
                status = ?
            WHERE id = ?
        """, (
            data["asset_number"],
            data["asset_name"],
            data["description"],
            data["category"],
            data["location"],
            data["manufacturer"],
            data["model"],
            data["serial_number"],
            data["purchase_date"],
            data["warranty_expiry"],
            data["status"],
            record_id,
        ))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM assets
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Next asset number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_asset_number():
        return CodeGenerator.next_code(
            table_name="assets",
            field_name="asset_number",
            prefix="AST",
            digits=4
        )

    @staticmethod
    def get_by_number(asset_number):

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
            WHERE asset_number = ?
        """, (asset_number,))

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def number_exists(asset_number, exclude_id=None):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM assets
                WHERE asset_number = ?
                LIMIT 1
            """, (asset_number,))
        else:
            cursor.execute("""
                SELECT 1
                FROM assets
                WHERE asset_number = ?
                  AND id <> ?
                LIMIT 1
            """, (
                asset_number,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None
        conn.close()

        return exists

    @staticmethod
    def get_active_assets():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                asset_number,
                asset_name
            FROM assets
            WHERE status = 'Active'
            ORDER BY asset_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows
    