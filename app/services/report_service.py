from app.models.report_model import ReportModel
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)
from app.database.connection import Database


class ReportService:

    @staticmethod
    def get_work_orders(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):
        return ReportModel.get_work_orders(
            from_date,
            to_date,
            status=status,
            asset_number=asset_number,
        )

    @staticmethod
    def get_maintenance_costs(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):
        return ReportModel.get_maintenance_costs(
            from_date,
            to_date,
            status=status,
            asset_number=asset_number,
        )

    @staticmethod
    def get_inventory_stock():
        return ReportModel.get_inventory_stock()

    @staticmethod
    def get_preventive_maintenance():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                preventive_maintenance.id
                    AS id,

                preventive_maintenance.pm_number
                    AS pm_number,

                preventive_maintenance.asset_id
                    AS asset_id,

                assets.asset_number
                    AS asset_number,

                assets.asset_name
                    AS asset_name,

                preventive_maintenance.task
                    AS task,

                preventive_maintenance.frequency_type
                    AS frequency_type,

                preventive_maintenance.frequency_value
                    AS frequency_value,

                preventive_maintenance.last_service_date
                    AS last_service_date,

                preventive_maintenance.next_due_date
                    AS next_due_date,

                preventive_maintenance.last_service_meter
                    AS last_service_meter,

                preventive_maintenance.next_due_meter
                    AS next_due_meter,

                preventive_maintenance.priority
                    AS priority,

                preventive_maintenance.active
                    AS active

            FROM preventive_maintenance

            INNER JOIN assets
                ON preventive_maintenance.asset_id
                = assets.id

            ORDER BY
                preventive_maintenance.pm_number
        """)

        db_rows = cursor.fetchall()

        conn.close()

        rows = []

        for row in db_rows:

            pm = dict(row)

            pm["due_status"] = (
                PreventiveMaintenanceService
                .get_due_status(pm)
            )

            rows.append(pm)

        return rows

    @staticmethod
    def get_technician_performance(
        from_date=None,
        to_date=None
    ):
        return ReportModel.get_technician_performance(
            from_date,
            to_date
        )