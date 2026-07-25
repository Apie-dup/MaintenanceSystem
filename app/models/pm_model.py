from app.database.connection import Database


class PMModel:

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                pm.id,
                pm.pm_number,
                a.asset_number,
                a.asset_name,
                pm.task,
                pm.description,
                pm.frequency_type,
                pm.frequency_value,
                pm.last_service_date,
                pm.next_due_date,
                pm.estimated_hours,
                pm.estimated_cost,
                pm.priority,
                pm.active,
                pm.notes
            FROM preventive_maintenance pm
            LEFT JOIN assets a
            ON pm.asset_id = a.id
            ORDER BY pm.next_due_date
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM preventive_maintenance
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
            INSERT INTO preventive_maintenance
            (
                pm_number,
                asset_id,
                task,
                description,
                frequency_type,
                frequency_value,
                last_service_date,
                next_due_date,
                estimated_hours,
                estimated_cost,
                priority,
                active,
                notes
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, record)

        conn.commit()
        conn.close()

    @staticmethod
    def update(record):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE preventive_maintenance
            SET
                asset_id = ?,
                task = ?,
                description = ?,
                frequency_type = ?,
                frequency_value = ?,
                last_service_date = ?,
                next_due_date = ?,
                estimated_hours = ?,
                estimated_cost = ?,
                priority = ?,
                active = ?,
                notes = ?
            WHERE id = ?
        """, record)

        conn.commit()
        conn.close()

    @staticmethod
    def delete(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM preventive_maintenance
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search(text):
        
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                pm.id,
                pm.pm_number,
                a.asset_number,
                a.asset_name,
                pm.task,
                pm.frequency_type,
                pm.next_due_date,
                pm.priority,
                pm.active
            FROM preventive_maintenance pm
            LEFT JOIN assets a
                ON pm.asset_id = a.id
            WHERE
                pm.pm_number LIKE ?
                OR a.asset_number LIKE ?
                OR a.asset_name LIKE ?
                OR pm.task LIKE ?
            ORDER BY pm.pm_number
        """, (
            f"%{text}%",
            f"%{text}%",
            f"%{text}%",
            f"%{text}%"
        ))

        rows = cursor.fetchall()
        
        conn.close()
        
        return rows

    @staticmethod
    def get_next_pm_number():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT pm_number
            FROM preventive_maintenance
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return "PM-000001"

        number = int(row[0].split("-")[1]) + 1
        return f"PM-{number:06d}"