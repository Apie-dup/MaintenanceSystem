from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_dashboard import Ui_DashboardWindow
from app.services.dashboard_service import DashboardService
from app.controllers.asset_controller import AssetsController
from app.controllers.work_order_controller import WorkOrderController


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
        self.ui.btnAssets.clicked.connect(self.open_assets)
        self.ui.btnWorkOrders.clicked.connect(self.open_work_orders)

    def open_assets(self):

        self.assets_window = AssetsController()
        self.assets_window.show()

    def open_work_orders(self):

        self.work_order_window = WorkOrderController()
        self.work_order_window.show()


    