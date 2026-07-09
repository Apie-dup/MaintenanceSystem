from app.database.connection import Database

class WorkOrderModel:

    @staticmethod
    def get_all():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                wo.id,

                wo.work_order_number,

                a.asset_number || ' - ' || a.asset_name,

                wo.title,

                wo.priority,

                wo.status,

                COALESCE(wo.technician_id, 'Unassigned'),
                       
                wo.due_date
                       
                FROM JOIN assets a
                    ON wo.asset_id a.id
                       
            ORDER BY wo.work_order_number
        """)

        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_next_work_order_number():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT work_order_number
            FROM work_orders
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return "WO-000001"

        number = int(row[0].split("-")[1]) + 1
        return f"WO-{number:06d}"

    @staticmethod
    def insert(work_order):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO work_orders (
                work_order_number,
                asset_id,
                title,
                description,
                priority,
                status,
                technician,
                request_by,
                date_created,
                due_date,
                estimated_cost,
                actual_cost,
                labour_hours,
                notes
            )
            VALUES (
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?
            )
        """, work_order)

        conn.commit()
        conn.close()

    @staticmethod
    def update(work_order):

       conn = Database.connect()
       cursor = conn.cursor()

       cursor.execute("""
            UPDATE work_orders
            SET
                asset_id = ?,
                title = ?,
                description = ?,
                priority = ?,
                status = ?,
                technician_id = ?
                requested_by =?,
                date_created = ?,
                due_date = ?,
                estimadted_cost = ?,
                actual_cost = ?,
                labour_hours = ?,
                notes = ?
            WHERE id = ?
        """, work_order)
       
       conn.commit()
       conn.close

    @staticmethod
    def get_by_id(work_order_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM work_orders
            WHERE id = ?
        """, (work_order_id,))

        row = cursor.fetchone()
        conn.close()
        return row

    @staticmethod
    def delete(work_order_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM work_orders
            WHERE id = ?
        """, (work_order_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search(search_text):
        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{search_text}%"

        cursor.execute("""
            SELECT
                wo.id,
                wo.work_order_number,
                a.asset_number || ' - ' || a.asset_name,
                wo.title,
                wo.priority,
                wo.status,
                wo.technician_id,
                wo.due_date
            FROM work_orders wo
                       
            LEFT JOIN assets a
                ON wo.asset_id = a.id
                       
            WHERE
                wo.work_order_number LIKE ?
                OR wo.title LIKE ?
                OR wo.priority LIKE ?
                OR wo.status LIKE ?
            ORDER BY wo.work_order_number
        """, (
            search,
            search,
            search,
            search
        ))

        rows = cursor.fetchall()
        conn.close()
        return rows

