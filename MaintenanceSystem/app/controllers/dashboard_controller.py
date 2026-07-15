from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon, QPixmap

from app.ui.generated.ui_dashboard import Ui_DashboardWindow
from app.services.dashboard_service import DashboardService
from app.pages.assets_page import AssetsPage
from app.pages.work_orders_page import WorkOrderPage
from app.controllers.lookup_controller import LookupController
from app.pages.pm_page import PMPage
from app.pages.technicians_page import TechniciansPage
from datetime import datetime
from app.database.connection import Database


class DashboardController(QMainWindow):

    def __init__(self, user):

        super().__init__()

        self.ui = Ui_DashboardWindow()

        self.ui.setupUi(self)
        stats = DashboardService.get_statistics()

        self.load_statistics

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status_bar)
        self.timer. start(1000)  # Update every second

        self.update_status_bar

        pixmap = QPixmap("app/resources/logo.png")

        self.ui.lblLogo.setPixmap(
           pixmap.scale(
              90,
              90
           )
        )

        self.user = user

        self.setWindowTitle(f"Maintenance Management System - {user.get('fullname', '')}")
        self.ui.btnAssets.clicked.connect(self.open_assets)
        self.ui.btnWorkOrders.clicked.connect(self.open_work_orders)
        self.ui.btnThecnicians.clicked.connect(self.open_technicians)
        self.ui.btnLookups.clicked.connect(self.open_lookups)
        self.ui.btnPM.clicked.connect(self.open_pm)
        self.ui.btnHome.clickde.connect(self.load_statistics)
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSuppliers.clicked.connect(self.open_suppliers)
        self.ui.btnReports.clicked.connect(self.open_reports)
        self.ui.btnSettings.clicked.connect(self.open_setting)
        self.ui.btnLogout.clicked.connect(self.logout)

        self.lblUser = QLabel()
        self.lblDatabase = QLabel()
        self.lblClock = QLabel()

        self.statusBar().addPermanentWidget(self.lblUser)
        self.statusBar().addPermanentWidget(self.lblDatabase)
        self.statusBar().addPermanentWidget(self.lblClock)

        self.create_toolbar()


    def open_assets(self):

        self.assets_window = AssetsPage()
        self.assets_window.show()

        self.assets_window.destroyed.connect(
            self.load_statistics
        )

    def open_work_orders(self):

        self.work_order_window = WorkOrderPage()
        self.work_order_window.show()

        self.work_order_window.destroyed.connect(
            self.load_statistics
        )

    def open_technicians(self):
        

        self.technician_window = TechniciansPage()
        self.technician_window.show()

        self.technician_window.destroyed.connect(
            self.load_statistics
        )

    def open_lookups(self):

        self.lookup_window = LookupController()
        self.lookup_window.show()

    def open_pm(self):

        self.pm_window = PMPage()
        self.pm_window.show()

    def load_statistics(self):

        def load_statistics(self):

         stats = DashboardService.get_statistics()

         self.ui.lblAssetsValue.setText(str(stats["assets"]))
         self.ui.lblOpenWorkOrdersValue.setText(str(stats["work_orders"]))
         self.ui.lblPMDueValue.setText(str(stats["pm_due"]))
         self.ui.lblLowStockValue.setText(str(stats["low_stock"]))
         self.ui.lblTechniciansValue.setText(str(stats["technicians"]))

    def update_status_bar(self):

        self.lblUser.setText(
            f"User: {self.user.get('fullname', '')}"
        )

        if Database.is_connected():

         self.lblDatabase.setText("Database: Connected")
         self.lblDatabase.setStyleSheet(
         "color: green; font-weight: bold;"
        )

        else:

         self.lblDatabase.setText("Database: Disconnected")
         self.lblDatabase.setStyleSheet(
         "color: red; font-weight: bold;"
        )

        self.lblClock.setText(
            datetime.now().strftime("%d %b %Y %H:%M:%S")
        )

    def create_toolbar(self):

        toolbar = self.ui.mainToolBar

        action_assets = QAction(
            QIcon("app/resources/icons/assets.png"),
            "Assets",
           self
        )
        action_assets.triggered.connect(self.open_assets)
        toolbar.addAction(action_assets)

        action_workorders = QAction(
            QIcon("app/resources/icons/workorders.png"),
            "Work Orders",
           self
        )
        action_workorders.triggered.connect(self.open_work_orders)
        toolbar.addAction(action_workorders)

        action_pm = QAction(
            QIcon("app/resources/icons/pm.png"),
            "PM",
           self
        )
        action_pm.triggered.connect(self.open_pm)
        toolbar.addAction(action_pm)

        action_technicians = QAction(
            QIcon("app/resources/icons/technicians.png"),
            "Technicians",
           self
        )
        action_technicians.triggered.connect(self.open_technicians)
        toolbar.addAction(action_technicians)

        toolbar.addSeparator()

        action_refresh = QAction(
            QIcon("app/resources/icons/refresh.png"),
            "Refresh",
           self
        )
        action_refresh.triggered.connect(self.load_statistics)
        toolbar.addAction(action_refresh)

        toolbar.addSeparator()

        action_exit = QAction(
            QIcon("app/resources/icons/exit.png"),
            "Exit",
           self
        )
        action_exit.triggered.connect(self.close)
        toolbar.addAction(action_exit)



    