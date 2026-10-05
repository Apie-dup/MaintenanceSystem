from app.database.connection import Database


class VehicleSopInspectionItemModel:

    # ---------------------------------------------------------
    # Get by inspection ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_inspection_id(inspection_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_sop_inspection_items.*,
                work_orders.id AS work_order_id,
                work_orders.work_order_number
            FROM vehicle_sop_inspection_items
            LEFT JOIN work_orders
                ON work_orders.sop_inspection_item_id =
                    vehicle_sop_inspection_items.id
                AND work_orders.status NOT IN (
                    'Completed',
                    'Closed',
                    'Cancelled'
                )
            WHERE vehicle_sop_inspection_items.inspection_id = ?
            ORDER BY
                vehicle_sop_inspection_items.sequence,
                vehicle_sop_inspection_items.id
        """, (inspection_id,))

        rows = cursor.fetchall()
        conn.close()

        return rows

    # ---------------------------------------------------------
    # Get by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(item_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM vehicle_sop_inspection_items
            WHERE id = ?
        """, (item_id,))

        row = cursor.fetchone()
        conn.close()

        return row

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO vehicle_sop_inspection_items (
                inspection_id,
                sop_item_id,
                sequence,
                check_description,
                required,
                result,
                comments
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data["inspection_id"],
            data.get("sop_item_id"),
            data["sequence"],
            data["check_description"],
            data.get("required", 1),
            data.get("result"),
            data.get("comments"),
        ))

        item_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return item_id

    # ---------------------------------------------------------
    # Update result
    # ---------------------------------------------------------

    @staticmethod
    def update_result(
        item_id,
        result,
        comments=None,
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE vehicle_sop_inspection_items
            SET
                result = ?,
                comments = ?
            WHERE id = ?
        """, (
            result,
            comments,
            item_id,
        ))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    @staticmethod
    def delete(item_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM vehicle_sop_inspection_items
            WHERE id = ?
        """, (item_id,))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # Delete all for inspection
    # ---------------------------------------------------------

    @staticmethod
    def delete_by_inspection_id(
        inspection_id
    ):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM vehicle_sop_inspection_items
            WHERE inspection_id = ?
        """, (inspection_id,))

        conn.commit()
        conn.close()