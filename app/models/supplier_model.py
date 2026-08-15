from genericpath import exists

from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class SupplierModel:

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes,
                created_at
            FROM suppliers
            ORDER BY supplier_code
            """
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_by_id(supplier_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes,
                created_at
            FROM suppliers
            WHERE id = ?
            """,
            (supplier_id,),
        )

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def get_by_code(supplier_code):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes,
                created_at
            FROM suppliers
            WHERE supplier_code = ?
            """,
            (supplier_code,),
        )

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def search(search_text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute(
            """
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes,
                created_at
            FROM suppliers
            WHERE
                supplier_code LIKE ?
                OR supplier_name LIKE ?
                OR contact_person LIKE ?
                OR phone LIKE ?
                OR email LIKE ?
                OR status LIKE ?
            ORDER BY supplier_code
            """,
            (search, search, search, search, search, search),
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def insert(data):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO suppliers
            (
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["supplier_code"],
                data["supplier_name"],
                data["contact_person"],
                data["phone"],
                data["email"],
                data["address"],
                data["status"],
                data["notes"],
            )
        )

        conn.commit()

        supplier_id = cursor.lastrowid

        conn.close()

        return supplier_id

    @staticmethod
    def update(supplier_id, data):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE suppliers
            SET
                supplier_code = ?,
                supplier_name = ?,
                contact_person = ?,
                phone = ?,
                email = ?,
                address = ?,
                status = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                data["supplier_code"],
                data["supplier_name"],
                data["contact_person"],
                data["phone"],
                data["email"],
                data["address"],
                data["status"],
                data["notes"],
                supplier_id,
            )
        )

        conn.commit()

        conn.close()

    @staticmethod
    def delete(supplier_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM suppliers
            WHERE id = ?
            """,
            (supplier_id,),
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_next_supplier_code():
        return CodeGenerator.next_code(
            table_name="suppliers",
            field_name="supplier_code",
            prefix="SUP",
            digits=6
        )

    @staticmethod
    def get_active_suppliers():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                supplier_code,
                supplier_name
            FROM suppliers
            WHERE status = 'Active'
            ORDER BY supplier_name
            """
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def code_exists(
        supplier_code,
        exclude_id=None
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM suppliers
                WHERE supplier_code = ?
                LIMIT 1
            """, (
                supplier_code,
            ))
        else:
            cursor.execute("""
                SELECT 1
                FROM suppliers
                WHERE supplier_code = ?
                AND id <> ?
                LIMIT 1
            """, (
                supplier_code,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists
