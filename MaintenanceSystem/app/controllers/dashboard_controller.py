from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_dashboard import Ui_DashboardWindow
from app.services.dashboard_service import DashboardService


class DashboardController(QMainWindow):

    def __init__(self, user):

        super().__init__()

        self.ui = Ui_DashboardWindow()

        self.ui.setupUi(self)
        stats = DashboardService.get_statistics()

        self.ui.lblAssetsValue.setText(str(stats.get("assets", 0)))
        self.ui.lblOpenWorkOrdersValue.setText(str(stats.get("work_orders", 0)))
        self.ui.lblLowStockValue.setText(str(stats.get("inventory", 0)))
        self.ui.lblPMDueValue.setText(str(stats.get("pm_due", 0)))

        self.user = user

        self.setWindowTitle(f"Maintenance Management System - {user.get('fullname', '')}")