from app.database.connection import Database


class AssetMeterReadingModel:

    @staticmethod
    def add(
        asset_id,
        meter_type,
        reading,
        reading_date,
        notes=None,
        source_type="Manual",
        work_order_id=None,
        logbook_id=None,
        conn=None,
    ):

        owns_connection = (
            conn is None
        )

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO asset_meter_readings
                (
                    asset_id,
                    meter_type,
                    reading,
                    reading_date,
                    notes,
                    source_type,
                    work_order_id,
                    logbook_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                asset_id,
                meter_type,
                reading,
                reading_date,
                notes,
                source_type,
                work_order_id,
                logbook_id,
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
    def get_latest_reading(
        asset_id,
        meter_type,
        conn=None,
    ):

        owns_connection = (
            conn is None
        )

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT
                    id,
                    asset_id,
                    meter_type,
                    reading,
                    reading_date,
                    source_type,
                    work_order_id,
                    logbook_id,
                    notes,
                    created_at
                FROM asset_meter_readings
                WHERE asset_id = ?
                AND meter_type = ?
                ORDER BY
                    reading_date DESC,
                    id DESC
                LIMIT 1
            """, (
                asset_id,
                meter_type,
            ))

            return cursor.fetchone()

        finally:

            if owns_connection:
                conn.close()

        

    @staticmethod
    def get_history(
        asset_id,
        meter_type=None,
    ):
        conn = Database.connect()
        cursor = conn.cursor()

        if meter_type:
            cursor.execute("""
                SELECT
                    asset_meter_readings.id,
                    asset_meter_readings.asset_id,
                    asset_meter_readings.meter_type,
                    asset_meter_readings.reading,
                    asset_meter_readings.reading_date,
                    asset_meter_readings.source_type,
                    asset_meter_readings.work_order_id,
                    asset_meter_readings.logbook_id,
                    work_orders.work_order_number,
                    asset_meter_readings.notes,
                    asset_meter_readings.created_at
                FROM asset_meter_readings
                LEFT JOIN work_orders
                    ON asset_meter_readings.work_order_id
                        = work_orders.id
                WHERE asset_meter_readings.asset_id = ?
                    AND asset_meter_readings.meter_type = ?
                ORDER BY
                    asset_meter_readings.reading_date DESC,
                    asset_meter_readings.id DESC
            """, (
                asset_id,
                meter_type,
            ))

        else:
            cursor.execute("""
                SELECT
                    asset_meter_readings.id,
                    asset_meter_readings.asset_id,
                    asset_meter_readings.meter_type,
                    asset_meter_readings.reading,
                    asset_meter_readings.reading_date,
                    asset_meter_readings.source_type,
                    asset_meter_readings.work_order_id,
                    asset_meter_readings.logbook_id,
                    work_orders.work_order_number,
                    asset_meter_readings.notes,
                    asset_meter_readings.created_at
                FROM asset_meter_readings
                LEFT JOIN work_orders
                    ON asset_meter_readings.work_order_id
                        = work_orders.id
                WHERE asset_meter_readings.asset_id = ?
                ORDER BY
                    asset_meter_readings.reading_date DESC,
                    asset_meter_readings.id DESC
            """, (
                asset_id,
            ))

        rows = cursor.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_by_logbook_id(
        logbook_id,
        meter_type,
        conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT *
                FROM asset_meter_readings
                WHERE logbook_id = ?
                    AND meter_type = ?
                LIMIT 1
            """, (
                logbook_id,
                meter_type,

            ))

            return cursor.fetchone()

        finally:

            if owns_connection:
                conn.close()

    @staticmethod
    def update_logbook_reading(
        logbook_id,
        meter_type,
        asset_id,
        reading,
        reading_date,
        conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE asset_meter_readings
                
                SET
                    asset_id = ?,
                    reading = ?,
                    reading_date = ?,
                    source_type = 'Vehicle Logbook'
                    
                WHERE logbook_id = ?
                    AND meter_type = ? 
            """, (
                asset_id,
                reading,
                reading_date,
                logbook_id,
                meter_type,
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
    def delete_by_logbook_id(
        logbook_id,
        conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM asset_meter_readings
                WHERE logbook_id = ?
            """, (
                logbook_id,
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
    def delete_by_logbook_id_and_meter_type(
        logbook_id,
        meter_type,
        conn=None,
    ):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM asset_meter_readings
                WHERE logbook_id = ?
                    AND meter_type = ?
            """, (
                logbook_id,
                meter_type,
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