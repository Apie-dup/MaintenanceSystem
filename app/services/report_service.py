from app.models.report_model import ReportModel
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)


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

        db_rows = (
            ReportModel.get_preventive_maintenance()
        )

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

    @staticmethod
    def get_inventory_transactions(
        from_date,
        to_date
    ):

        return (
            ReportModel.get_inventory_transactions(
                from_date,
                to_date
            )
        )

    @staticmethod
    def get_low_stock_reorder():
        return ReportModel.get_low_stock_reorder()

    @staticmethod
    def get_asset_maintenance_history(
        from_date=None,
        to_date=None,
        status=None,
        asset_number=None,
    ):
        return ReportModel.get_asset_maintenance_history(
            from_date,
            to_date,
            status=status,
            asset_number=asset_number,
        )

    @staticmethod
    def get_technician_work_history(
        from_date=None,
        to_date=None,
        status=None,
        technician_id=None,
    ):

        return (
            ReportModel
            .get_technician_work_history(
                from_date,
                to_date,
                status=status,
                technician_id=technician_id,
            )
        )