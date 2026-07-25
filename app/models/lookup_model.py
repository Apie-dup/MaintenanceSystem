from app.database.connection import Database

class LookupModel:



    @staticmethod
    def get_all(lookup_type):


        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                lookup_value
            FROM lookup_values
            WHERE lookup_type = ?
                AND active  = 1
            ORDER BY
                sort_order,
                lookup_value
            """, (lookup_type,))
        
        rows = cursor.fetchall()
        conn.close()

        return rows
    
    @staticmethod
    def get(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                lokup_type,
                lookup_value,
                sort_order,
                active
            FROM lookup_values
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()
        conn.close()

        return row
    
    @staticmethod
    def insert(record):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO looup_values
            (
                lookup_type,
                lookup_value,
                sort_order,
                active
            )
            VALUES (?,?,?,?)
        """, record)

        conn.commit()
        conn.close()

    @staticmethod
    def update(record):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE lookup_values
            SET
                lookup_type = ?,
                lookup_value = ?,
                sort_order = ?,
                active = ?
            WHERE id = ?
        """, record)

        conn.commit()
        conn.close()

    @staticmethod
    def delete(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM lookup_values
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search(lookup_type, text):

        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{text}%"

        cursor.execute("""
            SELECT
                id,
                lookup_value
            FROM lookup_values
            WHERE lookup_type = ?
                AND lookup_value LIKE ?
            ORDER BY
                sort_order,
                lookup_value
        """, (lookup_type, search))

        rows = cursor.fetchall()
        conn.close()

        return rows
        