from app.models.report_model import ReportModel


class ReportService:

    @staticmethod
    def get_work_orders(
        from_date=None,
        to_date=None
    ):
        return ReportModel.get_work_orders(
            from_date,
            to_date
        )

    @staticmethod
    def get_maintenance_costs(
        from_date=None,
        to_date=None
    ):
        return ReportModel.get_maintenance_costs(
            from_date,
            to_date
        )

    @staticmethod
    def get_inventory_stock():
        return ReportModel.get_inventory_stock()

    @staticmethod
    def get_preventive_maintenance():
        return ReportModel.get_preventive_maintenance()

    @staticmethod
    def get_technician_performance(
        from_date=None,
        to_date=None
    ):
        return ReportModel.get_technician_performance(
            from_date,
            to_date
        )