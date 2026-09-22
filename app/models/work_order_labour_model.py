from app.database.connection import Database


class WorkOrderLabourModel:

    @staticmethod
    def get_by_work_order(work_order_id):
        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    work_order_labour.id,
                    work_order_labour.work_order_id,
                    work_order_labour.technician_id,

                    technicians.employee_number,

                    (
                        technicians.first_name
                        || ' '
                        || technicians.last_name
                    ) AS technician_name,

                    work_order_labour.work_date,
                    work_order_labour.hours,
                    work_order_labour.hourly_rate,
                    work_order_labour.labour_cost,
                    work_order_labour.description,
                    work_order_labour.notes,
                    work_order_labour.user_id,
                    work_order_labour.username,
                    work_order_labour.created_at

                FROM work_order_labour

                INNER JOIN technicians
                    ON work_order_labour.technician_id =
                       technicians.id

                WHERE work_order_labour.work_order_id = ?

                ORDER BY
                    work_order_labour.work_date DESC,
                    work_order_labour.id DESC
            """, (work_order_id,))

            return cursor.fetchall()

        finally:
            conn.close()

    @staticmethod
    def get_by_id(
        labour_id,
        connection=None
    ):
        own_connection = (
            connection is None
        )

        conn = (
            connection
            if connection is not None
            else Database.connect()
        )

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT *
                FROM work_order_labour
                WHERE id = ?
            """, (
                labour_id,
            ))

            return cursor.fetchone()

        finally:
            if own_connection:
                conn.close()

    @staticmethod
    def insert(data, connection=None):
        own_connection = connection is None

        conn = (
            connection
            if connection is not None
            else Database.connect()
        )

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO work_order_labour
                (
                    work_order_id,
                    technician_id,
                    work_date,
                    hours,
                    hourly_rate,
                    labour_cost,
                    description,
                    notes,
                    user_id,
                    username
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["work_order_id"],
                data["technician_id"],
                data["work_date"],
                data["hours"],
                data["hourly_rate"],
                data["labour_cost"],
                data.get("description"),
                data.get("notes"),
                data.get("user_id"),
                data.get("username"),
            ))

            labour_id = cursor.lastrowid

            if own_connection:
                conn.commit()

            return labour_id

        except Exception:
            if own_connection:
                conn.rollback()
            raise

        finally:
            if own_connection:
                conn.close()

    @staticmethod
    def delete(labour_id, connection=None):
        own_connection = connection is None

        conn = (
            connection
            if connection is not None
            else Database.connect()
        )

        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM work_order_labour
                WHERE id = ?
            """, (labour_id,))

            if own_connection:
                conn.commit()

        except Exception:
            if own_connection:
                conn.rollback()
            raise

        finally:
            if own_connection:
                conn.close()

    @staticmethod
    def get_total_hours(work_order_id, connection=None):
        own_connection = connection is None

        conn = (
            connection
            if connection is not None
            else Database.connect()
        )

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(hours),
                        0
                    )
                FROM work_order_labour
                WHERE work_order_id = ?
            """, (work_order_id,))

            row = cursor.fetchone()

            return float(row[0] or 0)

        finally:
            if own_connection:
                conn.close()

    @staticmethod
    def get_total_cost(work_order_id, connection=None):
        own_connection = connection is None

        conn = (
            connection
            if connection is not None
            else Database.connect()
        )

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    COALESCE(
                        SUM(labour_cost),
                        0
                    )
                FROM work_order_labour
                WHERE work_order_id = ?
            """, (work_order_id,))

            row = cursor.fetchone()

            return float(row[0] or 0)

        finally:
            if own_connection:
                conn.close()