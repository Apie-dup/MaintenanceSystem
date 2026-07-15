from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from app.ui.generated.ui_main_window import Ui_MainWindow

# Pages
"from app.pages.dashboard_page import DashboardPage"
from app.pages.assets_page import AssetsPage
"from app.pages.work_orders_page import WorkOrdersPage"
"from app.pages.pm_page import PMPage"
"from app.pages.technicians_page import TechniciansPage"
"from app.pages.inventory_page import InventoryPage"
"from app.pages.suppliers_page import SuppliersPage"
"from app.pages.reports_page import ReportsPage"
"from app.pages.settings_page import SettingsPage"


class MainController(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        "self.dashboard_page = DashboardPage()"

        self.assets_page = AssetsPage()

        "self.work_orders_page = WorkOrdersPage()"

        "self.pm_page = PMPage()"

        "self.technicians_page = TechniciansPage()"

        "self.inventory_page = InventoryPage()"

        "self.suppliers_page = SuppliersPage()"

        "self.reports_page = ReportsPage()"

        "self.settings_page = SettingsPage()"

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
            lambda: self.show_page(self.ui.pageTechnicians)
        )

        self.ui.btnInventory.clicked.connect(
            lambda: self.show_page(self.ui.pageInventory)
        )

        self.ui.btnSuppliers.clicked.connect(
            lambda: self.show_page(self.ui.pageSuppliers)
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.show_page(self.ui.pageReports)
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.show_page(self.ui.pageSettings)
        )

        self.ui.btnLogout.clicked.connect(self.close)

    # -------------------------------------------------------
    # Switch pages
    # -------------------------------------------------------

    def show_page(self, page):

        self.ui.stackedWidget.setCurrentWidget(page)