from app.database.connection import Database

class TechnicianModel:
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
                trade,
                department,
                phone,
                status
            FROM technicians
            ORDER BY employee_number
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def insert(technician):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO technicians (
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
        """, technician)
        conn.commit()
        conn.close()

    @staticmethod
    def get_next_employee_number():
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT employee_number
            FROM technicians
            ORDER BY id DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return "EMP-0001"
        number = int(row[0].split("-")[1]) + 1
        return f"EMP-{number:04d}"

    @staticmethod
    def get_by_id(technician_id):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM technicians
            WHERE id = ?
        """, (technician_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(technician):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE technicians
            SET
                first_name = ?,
                last_name = ?,
                phone = ?,
                email = ?,
                trade = ?,
                department = ?,
                hourly_rate = ?,
                status = ?
            WHERE id = ?
        """, technician)
        conn.commit()
        conn.close()

    @staticmethod
    def delete(technician_id):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE
            FROM technicians
            WHERE id = ?
        """, (technician_id,))
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
                employee_number,
                first_name,
                last_name,
                trade,
                department,
                phone,
                status
            FROM technicians
            WHERE
                employee_number LIKE ?
                OR first_name LIKE ?
                OR last_name LIKE ?
                OR trade LIKE ?
                OR department LIKE ?
            ORDER BY employee_number
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