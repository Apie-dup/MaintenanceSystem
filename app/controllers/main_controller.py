from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_main_window import Ui_MainWindow

from app.pages.dashboard_page import DashboardPage
from app.pages.assets_page import AssetsPage
from app.pages.work_orders_page import WorkOrdersPage
from app.pages.preventive_maintenance_page import PreventiveMaintenancePage
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
            "Maintenance Management System - "
            f"{user.get('fullname', '')}"
        )

        self.page_manager = PageManager()
        self.navigation = NavigationManager(
            self.ui.stackedWidget
        )

        self.create_pages()
        self.register_pages()
        self.register_navigation()

        self.show_dashboard()

    def create_pages(self):
        self.dashboard_page = DashboardPage(self)
        self.assets_page = AssetsPage(self)
        self.work_orders_page = WorkOrdersPage(self)
        self.pm_page = PreventiveMaintenancePage(self)
        self.technicians_page = TechniciansPage(self)
        self.inventory_page = InventoryPage(self)
        self.suppliers_page = SuppliersPage(self)
        self.reports_page = ReportsPage(self)
        self.settings_page = SettingsPage(self)

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
            self.show_dashboard
        )

        self.ui.btnAssets.clicked.connect(
            self.show_assets
        )

        self.ui.btnWorkOrders.clicked.connect(
            self.show_work_orders
        )

        self.ui.btnPM.clicked.connect(
            self.show_pm
        )

        self.ui.btnTechnicians.clicked.connect(
            self.show_technicians
        )

        self.ui.btnInventory.clicked.connect(
            self.show_inventory
        )

        self.ui.btnSuppliers.clicked.connect(
            self.show_suppliers
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.navigation.show(
                self.ui.pageReports
            )
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.navigation.show(
                self.ui.pageSettings
            )
        )

        self.ui.btnLogout.clicked.connect(
            self.close
        )

    def show_dashboard(self):
        self.dashboard_page.refresh_dashboard()
        self.navigation.show(
            self.ui.pageDashboard
        )

    def show_assets(self):
        self.assets_page.load_data()
        self.navigation.show(
            self.ui.pageAssets
        )

    def show_work_orders(self):
        self.work_orders_page.load_data()
        self.navigation.show(
            self.ui.pageWorkOrders
        )

    def show_pm(self):
        self.pm_page.load_data()
        self.navigation.show(
            self.ui.pagePM
        )

    def show_technicians(self):
        self.technicians_page.load_data()
        self.navigation.show(
            self.ui.pageTechnicians
        )

    def show_inventory(self):
        self.inventory_page.load_data()
        self.navigation.show(
            self.ui.pageInventory
        )

    def show_suppliers(self):
        self.suppliers_page.load_data()
        self.navigation.show(
            self.ui.pageSuppliers
        )