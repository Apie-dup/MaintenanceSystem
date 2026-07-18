from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from app.ui.generated.ui_main_window import Ui_MainWindow
from app.core.page_manager import PageManager
from app.core.navigation_manager import NavigationManager
from app.core.application_manager import ApplicationManager

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

        self.page_manager = PageManager()
        self.navigation = NavigationManager(
            self.ui.stackedWidget
        )

        self.app = ApplicationManager(
            self.ui.stackedWidget,
            user
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
    # Insert pages into the stacked pages
    # -------------------------------------------------------

    def load_pages(self):

        self.app.page_manager.register(
            self.ui.pageDashboard,
            DashboardPage
        )

        self.app.page_manager.register(
            self.ui.pageAssets,
            AssetsPage
        )

        self.app.page_manager.register(
            self.ui.pageWorkOrders,
            WorkOrdersPage
        )

        self.app.page_manager.register(
            self.ui.pagePM,
            PMPage
        )

        self.app.page_manager.register(
            self.ui.pageTechnicians,
            TechniciansPage
        )

        self.app.page_manager.register(
            self.ui.pageInventory,
            InventoryPage
        )

        self.app.page_manager.register(
            self.ui.pageSuppliers,
            SuppliersPage
        )

        self.app.page_manager.register(
            self.ui.pageReports,
            ReportsPage
        )

        self.app.page_manager.register(
            self.ui.pageSettings,
            SettingsPage
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

        self.ui.btnDashboard.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageDashboard)
        )

        self.ui.btnAssets.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageAssets)
        )

        self.ui.btnWorkOrders.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageWorkOrders)
        )

        self.ui.btnPM.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pagePM)
        )

        self.ui.btnTechnicians.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageTechnicians)
        )

        self.ui.btnInventory.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageInventory)
        )

        self.ui.btnSuppliers.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageSuppliers)
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageReports)
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.app.navigation.show(self.ui.pageSettings)
        )

        self.ui.btnLogout.clicked.connect(self.close)

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