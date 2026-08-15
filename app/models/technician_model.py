from genericpath import exists

from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class TechnicianModel:

    # ---------------------------------------------------------
    # Get all technicians
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                employee_number,
                first_name,
                last_name,
                phone,
                email,
                trade,
                department,
                hourly_rate,
                status,
                created_at
            FROM technicians
            ORDER BY employee_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get technician by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                employee_number,
                first_name,
                last_name,
                phone,
                email,
                trade,
                department,
                hourly_rate,
                status,
                created_at
            FROM technicians
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
                employee_number,
                first_name,
                last_name,
                phone,
                email,
                trade,
                department,
                hourly_rate,
                status,
                created_at
            FROM technicians
            WHERE
                employee_number LIKE ?
                OR first_name LIKE ?
                OR last_name LIKE ?
                OR phone LIKE ?
                OR email LIKE ?
                OR trade LIKE ?
                OR department LIKE ?
                OR status LIKE ?
            ORDER BY employee_number
        """, (
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

        try:
            cursor.execute("""
                INSERT INTO technicians
                (
                    employee_number,
                    first_name,
                    last_name,
                    phone,
                    email,
                    trade,
                    department,
                    hourly_rate,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["employee_number"],
                data["first_name"],
                data["last_name"],
                data["phone"],
                data["email"],
                data["trade"],
                data["department"],
                data["hourly_rate"],
                data["status"],
            ))

            record_id = cursor.lastrowid

            conn.commit()

            return record_id

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE technicians
                SET
                    employee_number = ?,
                    first_name = ?,
                    last_name = ?,
                    phone = ?,
                    email = ?,
                    trade = ?,
                    department = ?,
                    hourly_rate = ?,
                    status = ?
                WHERE id = ?
            """, (
                data["employee_number"],
                data["first_name"],
                data["last_name"],
                data["phone"],
                data["email"],
                data["trade"],
                data["department"],
                data["hourly_rate"],
                data["status"],
                record_id,
            ))

            record_id = cursor.lastrowid

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM technicians
                WHERE id = ?
            """, (record_id,))

            record_id = cursor.lastrowid

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Duplicate employee-number check
    # ---------------------------------------------------------

    @staticmethod
    def employee_number_exists(
        employee_number,
        exclude_id=None
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM technicians
                WHERE employee_number = ?
                LIMIT 1
            """, (employee_number,))
        else:
            cursor.execute("""
                SELECT 1
                FROM technicians
                WHERE employee_number = ?
                  AND id <> ?
                LIMIT 1
            """, (
                employee_number,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    # ---------------------------------------------------------
    # Next employee number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_employee_number():
        return CodeGenerator.next_code(
            table_name="technicians",
            field_name="employee_number",
            prefix="EMP",
            digits=6,
        )

    @staticmethod
    def get_active_technicians():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                employee_number,
                first_name,
                last_name
            FROM technicians
            WHERE status = 'Active'
            ORDER BY first_name, last_name
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def is_used_in_work_orders(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1
            FROM work_orders
            WHERE technician_id = ?
            LIMIT 1
        """, (record_id,))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists