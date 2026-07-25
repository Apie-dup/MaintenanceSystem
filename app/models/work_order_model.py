from app.database.connection import Database

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
                id,
                work_order_number,
                asset_id,
                title,
                priority,
                status,
                technician_ id,
                due_date
            FROM work_orders
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
    
    # ---------------------------------------------------------
    # Get one work order
    # ---------------------------------------------------------
    
    @staticmethod
    def get(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM work_orders
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    # ---------------------------------------------------------
    # Insert
    # ---------------------------------------------------------

    @staticmethod
    def insert(work_order):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO work_orders(
                work_order_number,
                asset_id,
                title,
                description,
                priority,
                status,
                technician_id,
                requested_by,
                date_due,
                estimated_cost,
                actual_cost,
                labour_hours,
                notes)
            )
            VALUES(
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?,
                ?, ?
            )
        """, work_order)

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

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
                prioriy = ?,
                status = ?,
                technician_id = ?,
                requested_by = ?,
                date_due = ?,
                estimated_cost = ?,
                labour_hours = ?,
                notes = ?
            WHERE id = ?
        """, work_order)
        
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
            SELECT FROM work_orders
            WHERE id = ?
        """, (record_id,))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    @staticmethod
    def search(text):

        conn = Database.connect()
        cursor = conn.cursor()

        search = f"%{text}%"

        cursor.execute("""
            SELECT
                id,
                work_order_number,
                asset_id,
                title,
                priority,
                status,
                technician_id,
                due_date
            FROM work_orders
            WHERE
                work_order_number LIKE ?
                OR title LIKR ?
                OR priority LIKE ?
                OR status LIKE ?
                OR requested_by LIKE ?
            ORDER BY id DESC
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
    
    # ---------------------------------------------------------
    # Next Work Order Number
    # ---------------------------------------------------------

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


