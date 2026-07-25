from app.database.connection import Database


class InventoryModel:

    # -------------------------------------------------
    # Get all inventory
    # -------------------------------------------------

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                part_number,
                part_name,
                description,
                category,
                supplier_id,
                unit,
                quantity,
                minimum_quantity,
                reorder_quantity,
                unit_cost,
                location,
                barcode,
                status,
                notes,
                created_at
            FROM inventory
            ORDER BY part_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows
    
    # -------------------------------------------------
    # Get single item
    # -------------------------------------------------
    
    @staticmethod
    def get(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM inventory
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()

        conn.close()

        return row
    
    # -------------------------------------------------
    # Insert
    # -------------------------------------------------

    @staticmethod
    def insert(record):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inventory (
                part_number,
                part_name,
                description,
                category,
                supplier_id,
                unit,
                quantity,
                minimum_quantity,
                reorder_quantity,
                unit_cost,
                location,
                barcode,
                status,
                notes
            )
            VALUES (
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?
            )
        """, record)

        conn.commit()
        conn.close()

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    @staticmethod
    def update(record):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE inventory
            SET
                part_name = ?,
                description = ?,
                category = ?,
                supplier_id = ?,
                unit = ?,
                quantity = ?,
                minimum_quantity = ?,
                reorder_quantity = ?,
                unit_cost = ?,
                location = ?,
                barcode = ?,
                status = ?,
                notes = ?
            WHERE id = ?
        """, record)

        conn.commit()
        conn.close()

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    @staticmethod
    def delete(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM inventory
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    @staticmethod
    def search(search_text):

        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute("""
            SELECT
                id,
                part_number,
                part_name,
                description,
                category,
                quantity,
                unit_cost,
                location,
                status
            FROM inventory
            WHERE
                part_number LIKE ?
                OR part_name LIKE ?
                OR description LIKE ?
                OR category LIKE ?
                OR location LIKE ?
            ORDER BY part_number
        """, (
            search,
            search,
            search,
            search,
            search
        ))

        rows = cursor.fetchall()
        conn.close()

        return rows
    
    # -------------------------------------------------
    # Next Part Number
    # -------------------------------------------------

    @staticmethod
    def get_next_part_number():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT part_number
            FROM inventory
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return "PRT-000001"

        number = int(row[0].split("-")[1]) + 1
        return f"PRT-{number:06d}"

    # -------------------------------------------------
    # Dashboard
    # -------------------------------------------------

    @staticmethod
    def get_low_stock():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM inventory
            WHERE quantity <= minimum_quantity
            ORDER BY part_name
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_total_stock_value():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALSCE(
                    SUM(quantity * unit_cost)),
                    0
                )
            FROM inventory
        """)

        value = cursor.fetchone()[0]

        conn.close()

        return value
