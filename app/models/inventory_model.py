from app.database import connection
from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class InventoryModel:

    # ---------------------------------------------------------
    # Get all inventory
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.description,
                inventory.category,
                inventory.supplier_id,
                suppliers.supplier_code,
                suppliers.supplier_name,
                inventory.unit,
                inventory.quantity,
                inventory.minimum_quantity,
                inventory.reorder_quantity,
                inventory.unit_cost,
                inventory.location,
                inventory.barcode,
                inventory.status,
                inventory.notes,
                inventory.created_at
            FROM inventory
            LEFT JOIN suppliers
                ON inventory.supplier_id = suppliers.id
            ORDER BY inventory.part_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get inventory item by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.description,
                inventory.category,
                inventory.supplier_id,
                suppliers.supplier_code,
                suppliers.supplier_name,
                inventory.unit,
                inventory.quantity,
                inventory.minimum_quantity,
                inventory.reorder_quantity,
                inventory.unit_cost,
                inventory.location,
                inventory.barcode,
                inventory.status,
                inventory.notes,
                inventory.created_at
            FROM inventory
            LEFT JOIN suppliers
                ON inventory.supplier_id = suppliers.id
            WHERE inventory.id = ?
        """, (record_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------------------------------------------------
    # Insert
    # ---------------------------------------------------------

    @staticmethod
    def insert(data):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inventory
            (
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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["part_number"],
            data["part_name"],
            data["description"],
            data["category"],
            data["supplier_id"],
            data["unit"],
            data["quantity"],
            data["minimum_quantity"],
            data["reorder_quantity"],
            data["unit_cost"],
            data["location"],
            data["barcode"],
            data["status"],
            data["notes"],
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
            UPDATE inventory
            SET
                part_number = ?,
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
        """, (
            data["part_number"],
            data["part_name"],
            data["description"],
            data["category"],
            data["supplier_id"],
            data["unit"],
            data["quantity"],
            data["minimum_quantity"],
            data["reorder_quantity"],
            data["unit_cost"],
            data["location"],
            data["barcode"],
            data["status"],
            data["notes"],
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
            DELETE FROM inventory
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

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
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.description,
                inventory.category,
                inventory.supplier_id,
                suppliers.supplier_code,
                suppliers.supplier_name,
                inventory.unit,
                inventory.quantity,
                inventory.minimum_quantity,
                inventory.reorder_quantity,
                inventory.unit_cost,
                inventory.location,
                inventory.barcode,
                inventory.status,
                inventory.notes,
                inventory.created_at
            FROM inventory
            LEFT JOIN suppliers
                ON inventory.supplier_id = suppliers.id
            WHERE
                inventory.part_number LIKE ?
                OR inventory.part_name LIKE ?
                OR inventory.description LIKE ?
                OR inventory.category LIKE ?
                OR inventory.location LIKE ?
                OR inventory.barcode LIKE ?
                OR suppliers.supplier_code LIKE ?
                OR suppliers.supplier_name LIKE ?
                OR inventory.status LIKE ?
            ORDER BY inventory.part_number
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
    # Next Part Number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_part_number():
        return CodeGenerator.next_code(
            table_name="inventory",
            field_name="part_number",
            prefix="PRT",
            digits=6
        )

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    @staticmethod
    def get_low_stock():
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.quantity,
                inventory.minimum_quantity,
                inventory.unit,
                inventory.location,
                inventory.status
            FROM inventory
            WHERE inventory.quantity <= inventory.minimum_quantity
              AND inventory.status = 'Active'
            ORDER BY inventory.part_name
        """)
        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_total_stock_value():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COALESCE(
                SUM(quantity * unit_cost),
                0
            ) AS total_stock_value
            FROM inventory
        """)

        row = cursor.fetchone()
        conn.close()

        return row["total_stock_value"]

    @staticmethod
    def update_quantity(
        inventory_id,
        quantity,
        connection=None
    ):
        owns_connection = connection is None
        conn = connection or Database.connect()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE inventory
                SET quantity = ?
                WHERE id = ?
            """, (
                quantity,
                inventory_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Inventory item not found."
                )

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    @staticmethod
    def part_number_exists(
        part_number,
        exclude_id=None
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM inventory
                WHERE part_number = ?
                LIMIT 1
            """, (
                part_number,
            ))
        else:
            cursor.execute("""
                SELECT 1
                FROM inventory
                WHERE part_number = ?
                AND id <> ?
                LIMIT 1
            """, (
                part_number,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    @staticmethod
    def get_low_stock():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                inventory.id,
                inventory.part_number,
                inventory.part_name,
                inventory.description,
                inventory.category,
                
                inventory.supplier_id,
                suppliers.supplier_code,
                suppliers.supplier_name,
                
                inventory.unit,
                inventory.quantity,
                inventory.minimum_quantity,
                inventory.reorder_quantity,
                inventory.unit_cost,
                inventory.location,
                inventory.barcode,
                inventory.status,
                inventory.notes
            
            FROM inventory
            
            LEFT JOIN suppliers
                ON inventory.supplier_id = suppliers.id
                
            WHERE
                inventory.quantity
                    <= inventory.minimum_quantity
                    
                AND inventory.status = 'Active'
                
            ORDER BY
                inventory.quantity ASC,
                inventory.part_number
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows