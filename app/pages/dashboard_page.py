from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from app.core.signals import signals


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(
            QLabel("Dashboard Page")
        )

        signals.data_changed.connect(
            self.refresh_dashboard
        )

    def refresh_dashboard(self, module=None):

        status = DashboardServices.get_statistics()

        self.ui.lblAssetsValue.setText(
            str(stats["assets"])
        )

        self.ui.lblWorkOrdersValue.setText(
            str(stats["work_orders"])
        )

        self.ui.lblPMValue.setText(
            str(stats["pm_due"])
        )

        self.ui.lblTechniciansValue(
            str(stats["technicians"])
        )

        self.ui.lblLowStockValue(
            str(stats["low_stock"])
        )

        self.refresh_dashboard()

    def refresh(self):
        self.load_dashboard()

    

