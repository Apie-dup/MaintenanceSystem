from app.database.connection import Database


class PMServiceHistoryModel:

    @staticmethod
    def create(data, conn=None):

        owns_connection = conn is None

        if owns_connection:
            conn = Database.connect()

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO pm_service_history
                (
                    pm_id,
                    work_order_id,
                    asset_id,
                    service_date,
                    meter_type,
                    meter_reading,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                data["pm_id"],
                data.get("work_order_id"),
                data["asset_id"],
                data["service_date"],
                data.get("meter_type"),
                data.get("meter_reading"),
                data.get("notes"),
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
    def get_by_pm_id(pm_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                pm_service_history.id,
                pm_service_history.pm_id,
                pm_service_history.work_order_id,
                pm_service_history.asset_id,
                pm_service_history.service_date,
                pm_service_history.meter_type,
                pm_service_history.meter_reading,
                pm_service_history.notes,
                pm_service_history.created_at,

                preventive_maintenance.pm_number,
                preventive_maintenance.task,

                work_orders.work_order_number,

                assets.asset_number,
                assets.asset_name

            FROM pm_service_history

            INNER JOIN preventive_maintenance
                ON pm_service_history.pm_id
                    = preventive_maintenance.id

            INNER JOIN assets
                ON pm_service_history.asset_id
                    = assets.id

            LEFT JOIN work_orders
                ON pm_service_history.work_order_id
                    = work_orders.id

            WHERE pm_service_history.pm_id = ?

            ORDER BY
                pm_service_history.service_date DESC,
                pm_service_history.id DESC
        """, (pm_id,))

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def get_by_asset_id(asset_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                pm_service_history.id,
                pm_service_history.pm_id,
                pm_service_history.work_order_id,
                pm_service_history.asset_id,
                pm_service_history.service_date,
                pm_service_history.meter_type,
                pm_service_history.meter_reading,
                pm_service_history.notes,
                pm_service_history.created_at,

                preventive_maintenance.pm_number,
                preventive_maintenance.task,

                work_orders.work_order_number

            FROM pm_service_history

            INNER JOIN preventive_maintenance
                ON pm_service_history.pm_id
                    = preventive_maintenance.id

            LEFT JOIN work_orders
                ON pm_service_history.work_order_id
                    = work_orders.id

            WHERE pm_service_history.asset_id = ?

            ORDER BY
                pm_service_history.service_date DESC,
                pm_service_history.id DESC
        """, (asset_id,))

        rows = cursor.fetchall()

        conn.close()

        return rows