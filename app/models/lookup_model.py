from app.database.connection import Database


class LookupModel:

    @staticmethod
    def get_all(lookup_type):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                value AS lookup_value
            FROM lookups
            WHERE lookup_type = ?
                AND active = 1
            ORDER BY
                sort_order,
                value
            """,
            (lookup_type,),
        )

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                lookup_type,
                value AS lookup_value,
                sort_order,
                active
            FROM lookups
            WHERE id = ?
            """,
            (record_id,),
        )

        row = cursor.fetchone()
        conn.close()

        return row

    @staticmethod
    def insert(record):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO lookups
            (
                lookup_type,
                value,
                sort_order,
                active
            )
            VALUES (?, ?, ?, ?)
            """,
            record,
        )

        record_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return record_id

    @staticmethod
    def update(record):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE lookups
            SET
                lookup_type = ?,
                value = ?,
                sort_order = ?,
                active = ?
            WHERE id = ?
            """,
            record,
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM lookups
            WHERE id = ?
            """,
            (record_id,),
        )

        conn.commit()
        conn.close()

    @staticmethod
    def search(lookup_type, text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{text}%"

        cursor.execute(
            """
            SELECT
                id,
                value AS lookup_value
            FROM lookups
            WHERE lookup_type = ?
                AND value LIKE ?
                AND active = 1
            ORDER BY
                sort_order,
                value
            """,
            (lookup_type, search),
        )

        rows = cursor.fetchall()
        conn.close()

        return rows
        