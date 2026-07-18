from app.database.connection import Database


class InventoryModel:

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                part_number,
                part_name,
                category,
                quantity,
                minimum_quantity,
                location,
                status,
                unit_cost
            FROM inventory
            ORDER BY part_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

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

    @staticmethod
    def insert(part):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inventory (
                part_number,
                part_name,
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
                ?
            )
        """, part)

        conn.commit()
        conn.close()

    @staticmethod
    def update(part):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE inventory
            SET
                part_number = ?,
                part_name = ?,
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
        """, part)

        conn.commit()
        conn.close()

    @staticmethod
    def get(part_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                part_number,
                part_name,
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
            FROM inventory
            WHERE id = ?
        """, (part_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def delete(part_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM inventory
            WHERE id = ?
        """, (part_id,))

        conn.commit()
        conn.close()

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
                category,
                quantity,
                minimum_quantity,
                location,
                status,
                unit_cost
            FROM inventory
            WHERE
                part_number LIKE ?
                OR part_name LIKE ?
                OR category LIKE ?
                OR location LIKE ?
                OR status LIKE ?
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

    @staticmethod
    def get_low_stock():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                part_number,
                part_name,
                quantity,
                minimum_quantity
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
                SUM(quantity * unit_cost)
            FROM inventory
        """)

        value = cursor.fetchone()[0]

        conn.close()

        return value or 0