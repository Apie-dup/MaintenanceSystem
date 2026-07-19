from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_main_window import Ui_MainWindow

# Pages
from app.pages.dashboard_page import DashboardPage
from app.pages.assets_page import AssetsPage
from app.pages.work_orders_page import WorkOrdersPage
from app.pages.pm_page import PMPage
from app.pages.technicians_page import TechniciansPage
from app.pages.inventory_page import InventoryPage
from app.pages.suppliers_page import SuppliersPage
from app.pages.reports_page import ReportsPage
from app.pages.settings_page import SettingsPage

from app.core.page_manager import PageManager
from app.core.navigation_manager import NavigationManager


class MainController(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(
            f"Maintenance Management System - {user.get('fullname', '')}"
        )

        # Core managers
        self.page_manager = PageManager()
        self.navigation = NavigationManager(self.ui.stackedWidget)

        # Build application
        self.create_pages()
        self.register_pages()
        self.register_navigation()

        # Show dashboard
        self.navigation.show(self.ui.pageDashboard)

    def create_pages(self):

        self.dashboard_page = DashboardPage()
        self.assets_page = AssetsPage()
        self.work_orders_page = WorkOrdersPage()
        self.pm_page = PMPage()
        self.technicians_page = TechniciansPage()
        self.inventory_page = InventoryPage()
        self.suppliers_page = SuppliersPage()
        self.reports_page = ReportsPage()
        self.settings_page = SettingsPage()

    def register_pages(self):

        self.page_manager.add_page(
            self.ui.pageDashboard,
            self.dashboard_page
        )

        self.page_manager.add_page(
            self.ui.pageAssets,
            self.assets_page
        )

        self.page_manager.add_page(
            self.ui.pageWorkOrders,
            self.work_orders_page
        )

        self.page_manager.add_page(
            self.ui.pagePM,
            self.pm_page
        )

        self.page_manager.add_page(
            self.ui.pageTechnicians,
            self.technicians_page
        )

        self.page_manager.add_page(
            self.ui.pageInventory,
            self.inventory_page
        )

        self.page_manager.add_page(
            self.ui.pageSuppliers,
            self.suppliers_page
        )

        self.page_manager.add_page(
            self.ui.pageReports,
            self.reports_page
        )

        self.page_manager.add_page(
            self.ui.pageSettings,
            self.settings_page
        )

    def register_navigation(self):

        self.ui.btnDashboard.clicked.connect(
            lambda: self.navigation.show(self.ui.pageDashboard)
        )

        self.ui.btnAssets.clicked.connect(
            lambda: self.navigation.show(self.ui.pageAssets)
        )

        self.ui.btnWorkOrders.clicked.connect(
            lambda: self.navigation.show(self.ui.pageWorkOrders)
        )

        self.ui.btnPM.clicked.connect(
            lambda: self.navigation.show(self.ui.pagePM)
        )

        self.ui.btnTechnicians.clicked.connect(
            lambda: self.navigation.show(self.ui.pageTechnicians)
        )

        self.ui.btnInventory.clicked.connect(
            lambda: self.navigation.show(self.ui.pageInventory)
        )

        self.ui.btnSuppliers.clicked.connect(
            lambda: self.navigation.show(self.ui.pageSuppliers)
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.navigation.show(self.ui.pageReports)
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.navigation.show(self.ui.pageSettings)
        )

        self.ui.btnLogout.clicked.connect(self.close)