from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_main_window import Ui_MainWindow
from app.pages.assets_page import AssetsPage
from app.pages.work_orders_page import WorkOrderPage
from app.pages.pm_page import PMPage
from app.pages.technicians_page import TechniciansPage


class MainController(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.create_pages()
        self.load_pages()
        self.connect_navigation()

        self.setWindowTitle("Maintenance Management System")

        from PySide6.QtWidgets import QVBoxLayout

        self.assets_page = AssetsPage()

        layout = QVBoxLayout(self.ui.pageAssets)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.assets_page)

        self.setWindowTitle("Maintenance Management System")

        self.connect_navigation()

    def connect_navigation(self):

        self.ui.btnDashboard.clicked.connect(
            lambda: self.show_page(self.ui.pageDashboard)
        )

        self.ui.btnAssets.clicked.connect(
            lambda: self.show_page(self.ui.pageAssets)
        )

        self.ui.btnWorkOrders.clicked.connect(
            lambda: self.show_page(self.ui.pageWorkOrders)
        )

        self.ui.btnPM.clicked.connect(
            lambda: self.show_page(self.ui.pagePM)
        )

        self.ui.btnTechnicians.clicked.connect(
            lambda: self.show_pages(self.ui.pageTechnicians)
        )

        self.ui.btnInventory.clicked.connect(
            lambda: self.show_pages(self.ui.pageInventory)
        )

        self.ui.btnSuppliers.clicked.connect(
            lambda: self.show_page(self.ui.pageSuppliers)
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.show_pages(self.ui.pageReports)
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.show_page(self.ui.pageSettings)
        )

        self.ui.btnLogout.clicked.connect(
            self.close
        )

    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageDashboard
        )

    def show_assets(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageAssets
        )

    def show_work_orders(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageWorkOrders
        )

    def show_pm(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pagePM
        )

    def show_technicians(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageTechnicians
        )

    def show_inventory(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageInventory
        )

    def show_suppliers(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageSuppliers
        )

    def show_reports(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageReports
        )

    def show_settings(self):
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageSettings
        )

    def create_pages(self):

        "self.dashboard_page = DashboardPage()"
        self.assets_page = AssetsPage()
        self.work_orders_page = WorkOrderPage()
        self.pm_page = PMPage()
        self.technicians_page = TechniciansPage()
        "self.inventory_page = InventoryPage()"
        "self.suppliers_page = SuppliersPage()"
        "self.reports_page = ReportsPage()"
        "self.settings_page = SettingsPage()"

    def load_pages(self):

        "self.add.page(self.ui.pageDashboard, self.dashboard_page)"
        self.add.page(self.ui.pageAssets, self.assets_page)
        self.add.page(self.ui.pageWorkOrders, self.work_orders_page)
        self.add.page(self.ui.pagePM, self.pm_page)
        self.add.page(self.ui.pageTechnicians, self.technicians_page)
        "self.add.page(self.ui.pageInventory, self.inventory_page)"
        "self.add.page(self.ui.pageSuppliers, self.suppliers_page)"
        "self.add.page(self.ui.pageReports, self.reports_page)"
        "self.add.page(self.ui.pageSettings, self.settings_page)"

    def show_pages(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)