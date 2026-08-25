from multiprocessing import connection

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
                work_orders.pm_id,
                work_orders.created_at,
                work_orders.completed_date,
                work_orders.closed_date
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
                work_orders.estimated_hours,
                work_orders.actual_cost,
                work_orders.labour_hours,
                work_orders.meter_reading,
                work_orders.notes,
                work_orders.pm_id,
                work_orders.created_at,
                work_orders.completed_date,
                work_orders.closed_date
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
                work_orders.pm_id,
                work_orders.created_at,
                work_orders.completed_date,
                work_orders.closed_date
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
            ORDER BY work_orders.created_at DESC,
                     work_orders.id DESC
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

        try:
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
                    estimated_hours,
                    actual_cost,
                    labour_hours,
                    meter_reading,
                    notes,
                    pm_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                data.get("estimated_hours", 0),
                data["actual_cost"],
                data["labour_hours"],
                data.get("meter_reading"),
                data["notes"],
                data.get("pm_id"),
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
                    estimated_hours = ?,
                    actual_cost = ?,
                    labour_hours = ?,
                    meter_reading = ?,
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
                data.get("estimated_hours", 0),
                data["actual_cost"],
                data["labour_hours"],
                data.get("meter_reading"),
                data["notes"],
                data.get("pm_id"),
                record_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Work Order not found."
                )

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
                DELETE FROM work_orders
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
                    WHEN 'Critical' THEN 1
                    WHEN 'Emergency' THEN 2
                    WHEN 'High' THEN 3
                    WHEN 'Medium' THEN 4
                    WHEN 'Low' THEN 5
                    ELSE 6
                END,
                work_orders.due_date
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def open_pm_work_order_exists(pm_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1
            FROM work_orders
            WHERE pm_id = ?
            AND status NOT IN (
                'Completed',
                'Closed',
                'Cancelled'
            )
            LIMIT 1
        """, (pm_id,))

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

    @staticmethod
    def complete(
        record_id,
        completed_date,
        meter_reading=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE work_orders
                SET
                    status = 'Completed',
                    completed_date = ?,
                    meter_reading = ?
                WHERE id = ?
            """, (
                completed_date,
                meter_reading,
                record_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Work Order not found."
                )
            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def close(record_id, closed_date):

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE work_orders
                SET
                    status = 'Closed',
                    closed_date = ?
                WHERE id = ?
            """, (
                closed_date,
                record_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Work Order not found."
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def calculate_actual_cost(
        work_order_id,
        connection=None
    ):

        owns_connection = (
            connection is None
        )

        conn = (
            connection
            or Database.connect()
        )

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_orders.labour_hours,
                technicians.hourly_rate
            FROM work_orders

            LEFT JOIN technicians
                ON work_orders.technician_id
                = technicians.id

            WHERE work_orders.id = ?
        """, (
            work_order_id,
        ))

        work_order = cursor.fetchone()

        if work_order is None:
            if owns_connection:
                conn.close()

                return 0.00

            labour_cost = (
                float(
                    work_order["labour_hours"] or 0
                )
                *
                float(
                    work_order["hourly_rate"] or 0
                )
            )

            cursor.execute("""
                SELECT COALESCE(
                    SUM(total_cost),
                    0
                ) AS material_cost
                FROM work_order_parts
                WHERE work_order_id = ?
            """, (
                work_order_id,
            ))

            material_row = cursor.fetchone()

            material_cost = float(
                material_row["material_cost"] or 0
            )

            total = (
                labour_cost
                + material_cost
            )

            if owns_connection:
                conn.close()

            return total

    @staticmethod
    def set_status(
        work_order_id,
        status,
        connection=None
    ):
        owns_connection = (
        connection is None
    )

        conn = (
            connection
            or Database.connect()
        )

        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE work_orders
                SET status = ?
                WHERE id = ?
            """, (
                status,
                work_order_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Work Order not found."
                )

            if owns_connection:
                conn.commit()

        except Exception:
            if owns_connection:
                conn.rollback()

            raise

        finally:
            if owns_connection:
                conn.close()

    @staticmethod
    def reopen(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE work_orders
                SET
                    status = "In Progress",
                    completed_date = NULL,
                    closed_date = NULL
                WHERE id = ?
                  AND status = 'Completed'
            """, (
                record_id,
            ))

            if cursor.rowcount == 0:
                raise ValueError(
                    "Only completed Work Orders "
                    "can be reopened."
                )

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()