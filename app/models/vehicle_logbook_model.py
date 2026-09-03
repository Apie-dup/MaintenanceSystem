from app.database.connection import Database


class VehicleLogbookModel:

    @staticmethod
    def get_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_logbook.id,
                vehicle_logbook.asset_id,
                assets.asset_number,
                assets.asset_name,

                vehicle_logbook.log_date,
                vehicle_logbook.driver_name,

                vehicle_logbook.start_meter,
                vehicle_logbook.end_meter,
                vehicle_logbook.distance,

                vehicle_logbook.origin,
                vehicle_logbook.destination,
                vehicle_logbook.purpose,

                vehicle_logbook.fuel_quantity,
                vehicle_logbook.fuel_cost,

                vehicle_logbook.notes,

                vehicle_logbook.user_id,
                vehicle_logbook.work_order_id,
                work_orders.work_order_number,
                vehicle_logbook.username,
                vehicle_logbook.created_at

            FROM vehicle_logbook

            LEFT JOIN assets
                ON vehicle_logbook.asset_id = assets.id

            LEFT JOIN work_orders
                ON vehicle_logbook.work_order_id = work_orders.id

            ORDER BY
                vehicle_logbook.log_date DESC,
                vehicle_logbook.id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_by_id(record_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM vehicle_logbook
            WHERE id = ?
        """, (record_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    @staticmethod
    def get_by_asset(asset_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_logbook.*,
                assets.asset_number,
                assets.asset_name,
                vehicle_logbook.work_order_id

            FROM vehicle_logbook

            INNER JOIN assets
                ON vehicle_logbook.asset_id = assets.id

            WHERE vehicle_logbook.asset_id = ?

            ORDER BY
                vehicle_logbook.log_date DESC,
                vehicle_logbook.id DESC
        """, (asset_id,))

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def create(data, conn=None):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO vehicle_logbook
                (
                    asset_id,
                    log_date,
                    driver_name,

                    start_meter,
                    end_meter,
                    distance,

                    origin,
                    destination,
                    purpose,

                    fuel_quantity,
                    fuel_cost,

                    notes,

                    user_id,
                    username
                )
                VALUES
                (
                    ?, ?, ?,
                    ?, ?, ?,
                    ?, ?, ?,
                    ?, ?,
                    ?,
                    ?, ?
                )
            """, (
                data["asset_id"],
                data["log_date"],
                data.get("driver_name"),

                data["start_meter"],
                data["end_meter"],
                data["distance"],

                data.get("origin"),
                data.get("destination"),
                data.get("purpose"),

                data.get("fuel_quantity", 0),
                data.get("fuel_cost", 0),

                data.get("notes"),

                data.get("user_id"),
                data.get("username"),
            ))

            record_id = cursor.lastrowid

            if owns_connection:
                conn.commit()

            return record_id

        except Exception:

            if owns_connection:
                conn.rollback()

            raise

        finally:

            if owns_connection:
                conn.close()

    @staticmethod
    def update(
        record_id,
          data,
          conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE vehicle_logbook
                
                SET
                    asset_id = ?,
                    log_date = ?,
                    driver_name = ?,
                    
                    start_meter = ?,
                    end_meter = ?,
                    distance = ?,
                    
                    origin = ?,
                    destination = ?,
                    purpose = ?,
                    
                    fuel_quantity = ?,
                    fuel_cost = ?,
                    
                    notes = ?
                
                WHERE id = ?
            """ , (
                data["asset_id"],
                data["log_date"],
                data.get("driver_name"),

                data["start_meter"],
                data["end_meter"],
                data["distance"],

                data.get("origin"),
                data.get("destination"),
                data.get("purpose"),

                data.get("fuel_quantity", 0),
                data.get("fuel_cost", 0),

                data.get("notes"),

                record_id,
            ))

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
    def delete(
        record_id,
        conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM vehicle_logbook
                WHERE id = ?
            """, (
                record_id,
            ))

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
    def search(text):

        conn = Database.connect()
        cursor = conn.cursor()

        search_text = f"%{text}%"

        cursor.execute("""
            SELECT
                vehicle_logbook.id,
                vehicle_logbook.asset_id,
                assets.asset_number,
                assets.asset_name,

                vehicle_logbook.log_date,
                vehicle_logbook.driver_name,

                vehicle_logbook.start_meter,
                vehicle_logbook.end_meter,
                vehicle_logbook.distance,

                vehicle_logbook.origin,
                vehicle_logbook.destination,
                vehicle_logbook.purpose,

                vehicle_logbook.fuel_quantity,
                vehicle_logbook.fuel_cost,

                vehicle_logbook.notes,

                vehicle_logbook.user_id,
                vehicle_logbook.username,
                vehicle_logbook.work_order_id,
                vehicle_logbook.created_at

            FROM vehicle_logbook

            INNER JOIN assets
                ON vehicle_logbook.asset_id = assets.id

            WHERE
                assets.asset_number LIKE ?
                OR assets.asset_name LIKE ?
                OR vehicle_logbook.driver_name LIKE ?
                OR vehicle_logbook.origin LIKE ?
                OR vehicle_logbook.destination LIKE ?
                OR vehicle_logbook.purpose LIKE ?

            ORDER BY
                vehicle_logbook.log_date DESC,
                vehicle_logbook.id DESC
        """, (
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
            search_text,
        ))
        rows = cursor.fetchall()

        conn.close()

        return rows

    def get_by_asset_and_date_range(
            asset_id,
            from_date,
            to_date
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                vehicle_logbook.id,
                vehicle_logbook.asset_id,
                assets.asset_number,
                assets.asset_name,
                vehicle_logbook.log_date,
                vehicle_logbook.driver_name,
                vehicle_logbook.start_meter,
                vehicle_logbook.end_meter,
                vehicle_logbook.distance,
                vehicle_logbook.origin,
                vehicle_logbook.destination,
                vehicle_logbook.purpose,
                vehicle_logbook.fuel_quantity,
                vehicle_logbook.fuel_cost,
                vehicle_logbook.notes,
                vehicle_logbook.work_order_id
            FROM vehicle_logbook
            LEFT JOIN assets
                ON vehicle_logbook.asset_id = assets.id
            WHERE vehicle_logbook.asset_id = ?
                AND vehicle_logbook.log_date BETWEEN ? AND ?
            ORDER BY
                vehicle_logbook.log_date,
                vehicle_logbook.id
        """, (
            asset_id,
            from_date,
            to_date, 
        ))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def set_work_order_id(
        logbook_id,
        work_order_id,
        conn=None
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE vehicle_logbook
            SET work_order_id = ?
            WHERE id = ?
        """, (
            work_order_id,
            logbook_id,
        ))

        if owns_connection:
            conn.commit()
            conn.close()