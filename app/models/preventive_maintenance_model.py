from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class PreventiveMaintenanceModel:

    # ---------------------------------------------------------
    # Get all PM plans
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                preventive_maintenance.asset_id,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.description,
                preventive_maintenance.frequency_type,
                preventive_maintenance.frequency_value,
                preventive_maintenance.last_service_date,
                preventive_maintenance.next_due_date,
                
                CASE
                    WHEN preventive_maintenance.active = 0
                        THEN 'Inactive'

                    WHEN DATE(preventive_maintenance.next_due_date) < DATE('now')
                        THEN 'Overdue'

                    WHEN DATE(preventive_maintenance.next_due_date) = DATE('now')
                        THEN 'Due Today'

                    WHEN DATE(preventive_maintenance.next_due_date) <= DATE(
                        'now',
                        '+7 days'
                    )
                        THEN 'Due Soon'

                    ELSE 'Scheduled'
                END AS due_status,
                
                preventive_maintenance.estimated_hours,
                preventive_maintenance.estimated_cost,
                preventive_maintenance.priority,

                CASE
                    WHEN preventive_maintenance.active = 1 THEN 'Yes'
                    ELSE 'No'
                END AS active_display,
                
                preventive_maintenance.active,
                preventive_maintenance.notes,
                preventive_maintenance.created_at
            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id
            ORDER BY
                preventive_maintenance.next_due_date,
                preventive_maintenance.pm_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get PM plan by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                preventive_maintenance.asset_id,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.description,
                preventive_maintenance.frequency_type,
                preventive_maintenance.frequency_value,
                preventive_maintenance.last_service_date,
                preventive_maintenance.next_due_date,
                preventive_maintenance.estimated_hours,
                preventive_maintenance.estimated_cost,
                preventive_maintenance.priority,
                preventive_maintenance.active,
                preventive_maintenance.notes,
                preventive_maintenance.created_at
            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id
            WHERE preventive_maintenance.id = ?
        """, (record_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------------------------------------------------
    # Search PM plans
    # ---------------------------------------------------------

    @staticmethod
    def search(search_text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                preventive_maintenance.asset_id,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.description,
                preventive_maintenance.frequency_type,
                preventive_maintenance.frequency_value,
                preventive_maintenance.last_service_date,
                preventive_maintenance.next_due_date,

                CASE
                    WHEN preventive_maintenance.active = 0
                        THEN 'Inactive'
                
                    WHEN preventive_maintenance.next_due_date < DATE('now')
                        THEN 'Overdue'
                
                    WHEN preventive_maintenance.next_due_date = DATE('now')
                        THEN 'Due Today'
                
                    WHEN preventive_maintenance.next_due_date <= DATE(
                        'now',
                        '+7 days'
                    )
                    THEN 'Due Soon'
                
                    ELSE 'Scheduled'
                    END AS due_status,
                
                preventive_maintenance.estimated_hours,
                preventive_maintenance.estimated_cost,
                preventive_maintenance.priority,

                CASE
                    WHEN preventive_maintenance.active = 1 THEN 'Yes'
                    ELSE 'No'
                END AS active_display,
                
                preventive_maintenance.active,
                preventive_maintenance.notes,
                preventive_maintenance.created_at
            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id
            WHERE
                preventive_maintenance.pm_number LIKE ?
                OR assets.asset_number LIKE ?
                OR assets.asset_name LIKE ?
                OR preventive_maintenance.task LIKE ?
                OR preventive_maintenance.description LIKE ?
                OR preventive_maintenance.frequency_type LIKE ?
                OR preventive_maintenance.priority LIKE ?
            ORDER BY
                preventive_maintenance.next_due_date,
                preventive_maintenance.pm_number
        """, (
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
    # Insert PM plan
    # ---------------------------------------------------------

    @staticmethod
    def insert(data):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["pm_number"],
            data["asset_id"],
            data["task"],
            data["description"],
            data["frequency_type"],
            data["frequency_value"],
            data["last_service_date"],
            data["next_due_date"],
            data["estimated_hours"],
            data["estimated_cost"],
            data["priority"],
            data["active"],
            data["notes"],
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
    # Update PM plan
    # ---------------------------------------------------------

    @staticmethod
    def update(record_id, data):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            UPDATE preventive_maintenance
            SET
                pm_number = ?,
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
        """, (
            data["pm_number"],
            data["asset_id"],
            data["task"],
            data["description"],
            data["frequency_type"],
            data["frequency_value"],
            data["last_service_date"],
            data["next_due_date"],
            data["estimated_hours"],
            data["estimated_cost"],
            data["priority"],
            data["active"],
            data["notes"],
            record_id,
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
    # Delete PM plan
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM preventive_maintenance
                WHERE id = ?
            """, (record_id,))

            record_id = cursor.lastrowid

            conn.commit()

            return record_id

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Check duplicate PM number
    # ---------------------------------------------------------

    @staticmethod
    def number_exists(pm_number, exclude_id=None):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM preventive_maintenance
                WHERE pm_number = ?
                LIMIT 1
            """, (pm_number,))
        else:
            cursor.execute("""
                SELECT 1
                FROM preventive_maintenance
                WHERE pm_number = ?
                  AND id <> ?
                LIMIT 1
            """, (
                pm_number,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    # ---------------------------------------------------------
    # Next PM number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_pm_number():
        return CodeGenerator.next_code(
            table_name="preventive_maintenance",
            field_name="pm_number",
            prefix="PM",
            digits=6,
        )

    # ---------------------------------------------------------
    # Dashboard queries
    # ---------------------------------------------------------

    @staticmethod
    def get_overdue():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.next_due_date,
                preventive_maintenance.priority
            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id
                        WHERE preventive_maintenance.active = 1
                            AND DATE(preventive_maintenance.next_due_date) < DATE('now')
            ORDER BY preventive_maintenance.next_due_date
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_due_today():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.next_due_date,
                preventive_maintenance.priority
            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id
                        WHERE preventive_maintenance.active = 1
                            AND DATE(preventive_maintenance.next_due_date) = DATE('now')
            ORDER BY preventive_maintenance.pm_number
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_due_this_week():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                assets.asset_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.next_due_date,
                preventive_maintenance.priority
            FROM preventive_maintenance
            LEFT JOIN assets
            ON preventive_maintenance.asset_id = assets.id
            WHERE preventive_maintenance.active = 1
            AND DATE(preventive_maintenance.next_due_date) > DATE('now')
            AND DATE(preventive_maintenance.next_due_date) <= DATE(
                'now',
                '+7 days'
            )
            ORDER BY preventive_maintenance.next_due_date
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_due_list(limit=10):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id,
                preventive_maintenance.pm_number,
                assets.asset_name,
                preventive_maintenance.task,
                preventive_maintenance.next_due_date,

                CASE
                    WHEN DATE(preventive_maintenance.next_due_date) < DATE('now')
                        THEN 'Overdue'

                    WHEN DATE(preventive_maintenance.next_due_date) = DATE('now')
                        THEN 'Due Today'

                    WHEN DATE(preventive_maintenance.next_due_date) <= DATE(
                        'now',
                        '+7 days'
                    )
                        THEN 'Due Soon'

                    ELSE 'Upcoming'
                END AS due_status

            FROM preventive_maintenance
            LEFT JOIN assets
                ON preventive_maintenance.asset_id = assets.id

            WHERE preventive_maintenance.active = 1

            ORDER BY preventive_maintenance.next_due_date

            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def update_service_dates(
        pm_id,
        last_service_date,
        next_due_date
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE preventive_maintenance
            SET
                last_service_date = ?,
                next_due_date = ?
            WHERE id = ?
        """, (
            last_service_date,
            next_due_date,
            pm_id,
        ))

        conn.commit()
        conn.close()