from app.database.connection import Database

class WorkOrderPartsModel:

    @staticmethod
    def add(part):

        conn = Database.connect()
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
            VALUES(?, ?, ?, ?, ?, ?)
        """, part)

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_work_order(work_order_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                wp.id,
                wp.inventory_id,
                i.part_number,
                i.part_name,
                wp.quantity,
                wp.unit_cost,
                wp.total_cost,
                wp.notes
            FROM work_order-parts wp
            JOIN inventory i
                ON wp.inventory_id = i.is
            WHERE wp.work_order_id = ?
            ORDER BY i.part_name
        """, (work_order_id,))

        rows = cursor.fetchall()

        conn.close()

    @staticmethod
    def delete(work_order_part_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM work_order_parts
            WHERE id = ?
        """, (work_order_part_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_by_work_order(work_order_id):

        conn= Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM work_order_parts
            WHERE work_order_id = ?
        """, (work_order_id))

        conn.commit()
        conn.close()