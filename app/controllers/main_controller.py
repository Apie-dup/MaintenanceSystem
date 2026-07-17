from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from app.ui.generated.ui_main_window import Ui_MainWindow
from app.core.page_manager import PageManager
from app.core.navigation_manager import NavigationManager

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


class MainController(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.page_manager = PageManager(
            self.ui.stackedWidget
        )

        self.setWindowTitle(
            f"Maintenance Management System - {user.get('fullname', '')}"
        )

        self.create_pages()
        self.load_pages()
        self.connect_navigation()

        # Start on Dashboard
        self.show_page(self.ui.pageDashboard)

    # -------------------------------------------------------
    # Create all pages
    # -------------------------------------------------------

    def create_pages(self):

        dashboard = DashboardPage()

        self.page_manager.register(
            "dashboard",
            self.ui.pageDashboard,
            dashboard
        )

        self.app.register_module(
            "dashboard",
            dashboard
        )

        assets = AssetsPage

        self.page_manager.register(
            "assets",
            self.ui.pageAssets,
            assets
        )

        self.app.register_module(
            "assets",
            assets
        )

        work_orders = WorkOrdersPage
        
        self.page_manager.register(
            "work_orders",
            self.ui.pageWorkOrders,
            work_orders
        )

        self.app.register_module(
            "wor_orders",
            work_orders
        )

        pm = PMPage

        self.page_manager.register(
            "pm",
            self.ui.pagePM,
            pm
        )

        self.app.register_module(
            "pm",
            pm
        )

        technicians = TechniciansPage

        self.page_manager.register(
            "technicians",
            self.ui.pageTechnicians,
            technicians
        )

        self.app.register_module(
            "technicians",
            technicians
        )

        inventory = InventoryPage

        self.page_manager.register(
            "inventory",
            self.ui.pageInventory,
            inventory
        )

        self.app.register_module(
            "inventory",
            inventory
        )

        suppliers = SuppliersPage

        self.page_manager.register(
            "suppliers",
            self.ui.pageSuppliers,
            suppliers
        )

        self.app.register_module(
            "suppliers",
            suppliers
        )

        reports = ReportsPage

        self.page_manager.register(
            "reports",
            self.ui.pageReports,
            reports
        )

        self.app.register_module(
            "reports",
            reports
        )

        settings = SettingsPage

        self.page_manager.register(
            "settings",
            self.ui.pageSettings,
            settings
        )

        self.app.register_module(
            "settings",
            settings
        )

    # -------------------------------------------------------
    # Insert pages into the stacked pages
    # -------------------------------------------------------

    def load_pages(self):

        self.add_page(
            self.ui.pageDashboard,
            self.dashboard_page
        )

        self.add_page(
            self.ui.pageAssets,
            self.assets_page
        )

        self.add_page(
            self.ui.pageWorkOrders,
            self.work_orders_page
        )

        self.add_page(
            self.ui.pagePM,
            self.pm_page
        )

        self.add_page(
            self.ui.pageTechnicians,
            self.technicians_page
        )

        self.add_page(
            self.ui.pageInventory,
            self.inventory_page
        )

        self.add_page(
            self.ui.pageSuppliers,
            self.suppliers_page
        )

        self.add_page(
            self.ui.pageReports,
            self.reports_page
        )

        self.add_page(
            self.ui.pageSettings,
            self.settings_page
        )

    # -------------------------------------------------------
    # Helper
    # -------------------------------------------------------

    def add_page(self, container, page):

        layout = container.layout()

        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(page)

    # -------------------------------------------------------
    # Navigation
    # -------------------------------------------------------

    def connect_navigation(self):

        self.navigation = NavigationManager(
            self.page_manager
        )

    def register_navigation(self):

        self.navigation.register(
            self.ui.btnDashboard,
            "dashboard"
        )

        self.navigation.register(
            self.ui.btnAssets,
            "assets"
        )

        self.navigation.register(
            self.ui.btnWorkOrders,
            "work_orders"
        )

        self.navigation.register(
            self.ui.btnPM,
            "pm"
        )

        self.navigation.register(
            self.ui.btnTechnicians,
            "technicians"
        )

        self.navigation.register(
            self.ui.btnInventory,
            "inventory"
        )

        self.navigation.register(
            self.ui.btnSuppliers,
            "suppliers"
        )

        self.navigation.register(
            self.ui.btnReports,
            "reports:"
        )

        self.navigation.register(
            self.ui.btnSettings
        )

    # -------------------------------------------------------
    # Switch pages
    # -------------------------------------------------------

    def show_page(self, page):

        self.ui.stackedWidget.setCurrentWidget(page)

    # -------------------------------------------------------
    # Refresh pages
    # -------------------------------------------------------

    def refresh_pages(self, page_name):


        pages = {
            "dashboard": self.dashboard_page,
            "assets": self.assets_page,
            "work_orders": self.work_orders_page,
            "pm": self.pm_page,
            "inventory": self.inventory_page,
            "technicians": self.technicians_page,
            "suppliers": self.suppliers_page,
            "reports": self.reports_page,
            "settings": self.settings_page,
        }

        page = page.get(page_name)

        if page and hasattr(page, "refresh"):
            page.refresh()