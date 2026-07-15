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
                a.asset_number || ' - ' || a.asset_name AS asset,
                pm.task,
                pm.frequency_type,
                pm.next_due_date,
                pm.priority,
                CASE
                    WHEN pm.active = 1 THEN 'Active'
                    ELSE 'Inactive'
                END
            FROM preventive_maintenance pm

            LEFT JOIN assets a
                ON pm.asset_id = a.id

            ORDER BY pm.pm_number
        """)

        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(pm_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
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
            FROM preventive_maintenance
            WHERE id = ?
        """, (pm_id,))

        row = cursor.fetchone()
        conn.close()
        return row

    @staticmethod
    def insert(pm):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO preventive_maintenance (
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
            VALUES (
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?
            )
        """, pm)

        conn.commit()
        conn.close()

    @staticmethod
    def update(pm):
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
        """, pm)

        conn.commit()
        conn.close()

    @staticmethod
    def delete(pm_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM preventive_maintenance
            WHERE id = ?
        """, (pm_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search(search_text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute("""
            SELECT
                pm.id,
                pm.pm_number,
                a.asset_number || ' - ' || a.asset_name AS asset,
                pm.task,
                pm.frequency_type,
                pm.next_due_date,
                pm.priority,
                CASE
                    WHEN pm.active = 1 THEN 'Active'
                    ELSE 'Inactive'
                END
            FROM preventive_maintenance pm

            LEFT JOIN assets a
                ON pm.asset_id = a.id

            WHERE
                pm.pm_number LIKE ?
                OR pm.task LIKE ?
                OR pm.frequency_type LIKE ?
                OR pm.priority LIKE ?
                OR a.asset_name LIKE ?
                OR a.asset_number LIKE ?

            ORDER BY pm.pm_number
        """, (
            search,
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