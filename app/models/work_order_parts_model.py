from app.database.connection import Database


class WorkOrderPartModel:

    # ---------------------------------------------------------
    # Get parts issued to a work order
    # ---------------------------------------------------------

    @staticmethod
    def get_by_work_order(work_order_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_order_parts.id,
                work_order_parts.work_order_id,
                work_order_parts.inventory_id,
                inventory.part_number,
                inventory.part_name,
                inventory.unit,
                work_order_parts.quantity,
                work_order_parts.unit_cost,
                work_order_parts.total_cost,
                work_order_parts.notes,
                work_order_parts.created_at
            FROM work_order_parts
            INNER JOIN inventory
                ON work_order_parts.inventory_id = inventory.id
            WHERE work_order_parts.work_order_id = ?
            ORDER BY work_order_parts.id
        """, (work_order_id,))

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get one issued-part record
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(record_id):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                work_order_parts.id,
                work_order_parts.work_order_id,
                work_order_parts.inventory_id,
                inventory.part_number,
                inventory.part_name,
                inventory.unit,
                work_order_parts.quantity,
                work_order_parts.unit_cost,
                work_order_parts.total_cost,
                work_order_parts.notes,
                work_order_parts.created_at
            FROM work_order_parts
            INNER JOIN inventory
                ON work_order_parts.inventory_id = inventory.id
            WHERE work_order_parts.id = ?
        """, (record_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------------------------------------------------
    # Insert issued part
    # ---------------------------------------------------------

    @staticmethod
    def insert(data, connection=None):
        owns_connection = connection is None
        conn = connection or Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO work_order_parts
            (
                work_order_id,
                inventory_id,
                quantity,
                unit_cost,
                total_cost,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["work_order_id"],
            data["inventory_id"],
            data["quantity"],
            data["unit_cost"],
            data["total_cost"],
            data["notes"],
        ))

        record_id = cursor.lastrowid

        if owns_connection:
            conn.commit()
            conn.close()

        return record_id

    # ---------------------------------------------------------
    # Delete issued part
    # ---------------------------------------------------------

    @staticmethod
    def delete(record_id, connection=None):
        owns_connection = connection is None
        conn = connection or Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM work_order_parts
            WHERE id = ?
        """, (record_id,))

        if owns_connection:
            conn.commit()
            conn.close()

    # ---------------------------------------------------------
    # Total material cost for a work order
    # ---------------------------------------------------------

    @staticmethod
    def get_total_cost(
        work_order_id,
        connection=None

        ):

        owns_connection = connection is None

        conn = connection or Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COALESCE(
                SUM(total_cost),
                0
            ) AS material_cost
            FROM work_order_parts
            WHERE work_order_id = ?
        """, (work_order_id,))

        row = cursor.fetchone()

        if owns_connection:
            conn.close()

        return float(row["material_cost"] or 0)