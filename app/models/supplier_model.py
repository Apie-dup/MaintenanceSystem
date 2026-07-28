from app.database.connection import Database

class SupplierModel:

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
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
                created _at
            FROM supliers
            ORDER BY supplier_name
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_by_id(supplier_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
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
        """, (supplier_id,))

        row = cursor.fetchone

        conn.close()

        return row

    @staticmethod
    def get_by_code(supplier_code):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.excute("""
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_persn,
                phone,
                email,
                address,
                status,
                notes,
                created_at 
            FROM suppliers
            WHERE supplier_code = ?
        """, (supplier_code,))

        row = cursor.fetchone()

        conn.close()

        return row

    @staticmethod
    def search(search_text):

        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute("""
            SELECT
                id,
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                notes,
                created_at
            FROM suppliers
            WHERE
                supplier_code LIKE ?
                OR supplier_name LIKE ?
                OR contact_person LIKE ?
                OR phone LIKE ?
                OR email LIKE ?
            ORDER BY supplier_name
        """,(
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
    def insert(data):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
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
        """, data)

        conn.commit()
        conn.close()

    @staticmethod
    def update(data):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE suppliers
            SET
                supplier_code =?
                supplier_name = ?
                contact_person = ?
                phone = ?
                email = ?
                address = ?
                status = ?
                notes = ?
            WHERE id = ?
        """, data)

        conn.commit()
        conn.close()

    @staticmethod
    def delete(supplier_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM suppliers
            WHERE id = ?
        """, (supplier_id,))

    @staticmethod
    def get_next_supplier_code():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT supplier_code
            FROM suppliers
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return "SUP-000001"

        last_number = int(row[0].split("-")[1])

        return f"SUP-{last_number + 1:06d}"

    @staticmethod
    def get_active_suppliers():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                supplier_code,
                supplier_name
            FROM suppliers
            WHERE status = 'Active'
            ORDER BY supplier_name
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows