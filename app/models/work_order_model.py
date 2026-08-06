from genericpath import exists

from app.database.connection import Database
from app.helpers.code_generator import CodeGenerator


class WorkOrderModel:

    # ---------------------------------------------------------
    # Get all work orders
    # ---------------------------------------------------------

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_orders.id,
                work_orders.work_order_number,
                work_orders.asset_id,
                assets.asset_number,
                assets.asset_name,
                work_orders.title,
                work_orders.description,
                work_orders.priority,
                work_orders.status,
                work_orders.technician_id,

                CASE
                    WHEN technicians.id IS NULL THEN 'Unassigned'
                    ELSE technicians.employee_number
                        || ' - '
                        || technicians.first_name
                        || ' '
                        || technicians.last_name
                END AS technician_display,
                
                work_orders.requested_by,
                work_orders.date_created,
                work_orders.due_date,
                work_orders.estimated_cost,
                work_orders.actual_cost,
                work_orders.labour_hours,
                work_orders.notes,
                work_orders.pm_id
            FROM work_orders
            LEFT JOIN assets
                ON work_orders.asset_id = assets.id
            LEFT JOIN technicians
                ON work_orders.technician_id = technicians.id
            ORDER BY work_orders.id DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get work order by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_orders.id,
                work_orders.work_order_number,
                work_orders.asset_id,
                assets.asset_number,
                assets.asset_name,
                work_orders.title,
                work_orders.description,
                work_orders.priority,
                work_orders.status,
                work_orders.technician_id,
                technicians.employee_number,
                technicians.first_name,
                technicians.last_name,
                work_orders.requested_by,
                work_orders.date_created,
                work_orders.due_date,
                work_orders.estimated_cost,
                work_orders.actual_cost,
                work_orders.labour_hours,
                work_orders.notes,
                work_orders.pm_id
            FROM work_orders
            LEFT JOIN assets
                ON work_orders.asset_id = assets.id
            LEFT JOIN technicians
                ON work_orders.technician_id = technicians.id
            WHERE work_orders.id = ?
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
                work_orders.id,
                work_orders.work_order_number,
                work_orders.asset_id,
                assets.asset_number,
                assets.asset_name,
                work_orders.title,
                work_orders.description,
                work_orders.priority,
                work_orders.status,
                work_orders.technician_id,

                CASE
                    WHEN technicians.id IS NULL THEN 'Unassigned'
                    ELSE technicians.employee_number
                        || ' - '
                        || technicians.first_name
                        || ' '
                        || technicians.last_name
                    END AS technician_display,
                
                work_orders.requested_by,
                work_orders.date_created,
                work_orders.due_date,
                work_orders.estimated_cost,
                work_orders.actual_cost,
                work_orders.labour_hours,
                work_orders.notes,
                work_orders.pm_id
            FROM work_orders
            LEFT JOIN assets
                ON work_orders.asset_id = assets.id
            LEFT JOIN technicians
                ON work_orders.technician_id = technicians.id
            WHERE
                work_orders.work_order_number LIKE ?
                OR work_orders.title LIKE ?
                OR work_orders.description LIKE ?
                OR work_orders.priority LIKE ?
                OR work_orders.status LIKE ?
                OR work_orders.requested_by LIKE ?
                OR assets.asset_number LIKE ?
                OR assets.asset_name LIKE ?
                OR technicians.employee_number LIKE ?
                OR technicians.first_name LIKE ?
                OR technicians.last_name LIKE ?
            ORDER BY work_orders.id DESC
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

        cursor.execute("""
            INSERT INTO work_orders
            (
                work_order_number,
                asset_id,
                title,
                description,
                priority,
                status,
                technician_id,
                requested_by,
                date_created,
                due_date,
                estimated_cost,
                actual_cost,
                labour_hours,
                notes,
                pm_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["work_order_number"],
            data["asset_id"],
            data["title"],
            data["description"],
            data["priority"],
            data["status"],
            data["technician_id"],
            data["requested_by"],
            data["date_created"],
            data["due_date"],
            data["estimated_cost"],
            data["actual_cost"],
            data["labour_hours"],
            data["notes"],
            data["pm_id"],
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
            UPDATE work_orders
            SET
                work_order_number = ?,
                asset_id = ?,
                title = ?,
                description = ?,
                priority = ?,
                status = ?,
                technician_id = ?,
                requested_by = ?,
                date_created = ?,
                due_date = ?,
                estimated_cost = ?,
                actual_cost = ?,
                labour_hours = ?,
                notes = ?,
                pm_id = ?
            WHERE id = ?
        """, (
            data["work_order_number"],
            data["asset_id"],
            data["title"],
            data["description"],
            data["priority"],
            data["status"],
            data["technician_id"],
            data["requested_by"],
            data["date_created"],
            data["due_date"],
            data["estimated_cost"],
            data["actual_cost"],
            data["labour_hours"],
            data["notes"],
            data["pm_id"],
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
            DELETE FROM work_orders
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Duplicate number check
    # ---------------------------------------------------------

    @staticmethod
    def number_exists(work_order_number, exclude_id=None):
        conn = Database.connect()
        cursor = conn.cursor()

        if exclude_id is None:
            cursor.execute("""
                SELECT 1
                FROM work_orders
                WHERE work_order_number = ?
                LIMIT 1
            """, (work_order_number,))
        else:
            cursor.execute("""
                SELECT 1
                FROM work_orders
                WHERE work_order_number = ?
                  AND id <> ?
                LIMIT 1
            """, (
                work_order_number,
                exclude_id,
            ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    # ---------------------------------------------------------
    # Next work order number
    # ---------------------------------------------------------

    @staticmethod
    def get_next_work_order_number():
        return CodeGenerator.next_code(
            table_name="work_orders",
            field_name="work_order_number",
            prefix="WO",
            digits=6,
        )

    @staticmethod
    def update_actual_cost(
        work_order_id,
        actual_cost,
        connection=None
    ):
        owns_connection = connection is None

        conn = connection or Database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE work_orders
            SET actual_cost = ?
            WHERE id = ?
        """, (
            actual_cost,
            work_order_id
        ))

        if owns_connection:
            conn.commit()
            conn.close()

    @staticmethod
    def get_open_count():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM work_orders
            WHERE status NOT IN ('Completed', 'Closed', 'Cancelled')
        """)

        row = cursor.fetchone()
        conn.close()

        return int(row["total"] or 0)

    @staticmethod
    def get_urgent(limit=10):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_orders.id,
                work_orders.work_order_number,
                assets.asset_name,
                work_orders.priority,
                work_orders.status,
                work_orders.due_date
            FROM work_orders
            LEFT JOIN assets
                ON work_orders.asset_id = assets.id
            WHERE work_orders.status NOT IN (
                'Completed',
                'Closed',
                'Cancelled'
            )
            ORDER BY
                CASE work_orders.priority
                    WHEN 'Emergency' THEN 1
                    WHEN 'High' THEN 2
                    WHEN 'Medium' THEN 3
                    WHEN 'Low' THEN 4
                    ELSE 5
                END,
                work_orders.due_date
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def open_pm_work_order_exists(pm_number):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1
            FROM work_orders
            WHERE requested_by = ?
            AND status NOT IN (
                'Completed',
                'Closed',
                'Cancelled'
            )
            LIMIT 1
        """, (
            f"PM Schedule {pm_number}",
        ))

        exists = cursor.fetchone() is not None

        conn.close()

        return exists

    @staticmethod
    def get_pm_history(pm_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_orders.id,
                work_orders.work_order_number,
                work_orders.date_created,
                work_orders.due_date,
                work_orders.status,
                work_orders.technician_id,
                CASE
                WHEN technicians.id IS NULL
                    THEN 'Unassigned'
                ELSE technicians.employee_number
                     || ' - '
                     || technicians.first_name
                     || ' '
                     || technicians.last_name
                END AS technician_display,

                work_orders.labour_hours,
                work_orders.actual_cost,
                work_orders.notes

            FROM work_orders

            LEFT JOIN technicians
                ON work_orders.technician_id = technicians.id

            WHERE work_orders.pm_id = ?

            ORDER BY
                work_orders.date_created DESC,
                work_orders.id DESC
        """, (pm_id,))

        rows = cursor.fetchall()
        conn.close()

        return rows