from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QIcon

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
from app.controllers.lookup_controller import LookupController

from app.core.page_manager import PageManager
from app.core.navigation_manager import NavigationManager


class MainController(QMainWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configure_main_layout()
        self.ensure_lookup_button()
        self.configure_navigation_buttons()
        self.normalize_sidebar_layout()
        self.setup_navigation_icons()

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

    def configure_main_layout(self):
        self.ui.stackedWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        # Keep sidebar fixed and allow page area to consume width.
        self.ui.horizontalLayout.setStretch(0, 0)
        self.ui.horizontalLayout.setStretch(1, 1)

    def setup_navigation_icons(self):
        icons_dir = (
            Path(__file__).resolve().parent.parent
            / "resources"
            / "icons"
        )

        dashboard_icon = icons_dir / "dashboard.png"

        if dashboard_icon.exists():
            self.ui.btnDashboard.setIcon(
                QIcon(str(dashboard_icon))
            )

        assets_icon = icons_dir / "assets.png"

        if assets_icon.exists():
            self.ui.btnAssets.setIcon(
                QIcon(str(assets_icon))
            )

        work_orders_icon = icons_dir / "workorders.png"

        if work_orders_icon.exists():
            self.ui.btnWorkOrders.setIcon(
                QIcon(str(work_orders_icon))
            )

        pm_icon = icons_dir / "pm.png"

        if not pm_icon.exists():
            pm_icon = icons_dir / "preventive_maintenance.png"

        if pm_icon.exists():
            self.ui.btnPM.setIcon(
                QIcon(str(pm_icon))
            )

        technicians_icon = icons_dir / "technicians.png"

        if not technicians_icon.exists():
            technicians_icon = icons_dir / "technicians.png.png"

        if technicians_icon.exists():
            self.ui.btnTechnicians.setIcon(
                QIcon(str(technicians_icon))
            )

        inventory_icon = icons_dir / "inventory.png"

        if inventory_icon.exists():
            self.ui.btnInventory.setIcon(
                QIcon(str(inventory_icon))
            )

        suppliers_icon = icons_dir / "suppliers.png"
        if suppliers_icon.exists():
            self.ui.btnSuppliers.setIcon(
                QIcon(str(suppliers_icon))
            )

        reports_icon = icons_dir / "reports.png"

        if reports_icon.exists():
            self.ui.btnReports.setIcon(
                QIcon(str(reports_icon))
            )

        lookup_icon = icons_dir / "lookup.png"

        if lookup_icon.exists():
            self.ui.btnLookups.setIcon(
                QIcon(str(lookup_icon))
            )

        settings_icon = icons_dir / "settings.png"

        if settings_icon.exists():
            self.ui.btnSettings.setIcon(
                QIcon(str(settings_icon))
            )

        logout_icon = icons_dir / "logout.png"

        if logout_icon.exists():
            self.ui.btnLogout.setIcon(
                QIcon(str(logout_icon))
            )

    def ensure_lookup_button(self):
        if hasattr(self.ui, "btnLookups"):
            return

        self.ui.btnLookups = QPushButton(self.ui.navigationFrame)
        self.ui.btnLookups.setObjectName("btnLookups")
        self.ui.btnLookups.setText("Lookup Management")
        self.ui.btnLookups.setCheckable(False)

    def navigation_buttons(self):
        return [
            self.ui.btnDashboard,
            self.ui.btnAssets,
            self.ui.btnWorkOrders,
            self.ui.btnPM,
            self.ui.btnTechnicians,
            self.ui.btnInventory,
            self.ui.btnSuppliers,
            self.ui.btnReports,
            self.ui.btnSettings,
        ]

    def configure_navigation_buttons(self):
        for button in self.navigation_buttons():
            button.setProperty("navigation", True)
            button.setCheckable(True)
            button.setAutoExclusive(True)

        self.ui.btnLookups.setProperty("navigation", True)
        self.ui.btnLogout.setProperty("navigation", True)

    @staticmethod
    def refresh_button_style(button):
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()

    def set_active_navigation(self, active_button):
        for button in self.navigation_buttons():
            is_active = button is active_button
            button.setProperty("current", is_active)
            button.setChecked(is_active)
            self.refresh_button_style(button)

        for button in (self.ui.btnLookups, self.ui.btnLogout):
            button.setProperty("current", False)
            self.refresh_button_style(button)

        QApplication.processEvents()

    def normalize_sidebar_layout(self):
        sidebar = self.ui.navigationFrame
        sidebar.setMinimumSize(220, 0)
        sidebar.setMaximumSize(220, 16777215)

        self.ui.lblCompany.setText("Your Organization")
        self.ui.lblCompany.setWordWrap(True)

        existing_layout = sidebar.layout()
        if existing_layout is not None:
            QWidget().setLayout(existing_layout)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(11, 11, 11, 16)
        layout.setSpacing(8)

        layout.addWidget(self.ui.lblLogo)
        layout.addWidget(self.ui.lblCompany)
        layout.addSpacing(12)

        buttons = [
            self.ui.btnDashboard,
            self.ui.btnAssets,
            self.ui.btnWorkOrders,
            self.ui.btnPM,
            self.ui.btnTechnicians,
            self.ui.btnInventory,
            self.ui.btnSuppliers,
            self.ui.btnReports,
            self.ui.btnLookups,
            self.ui.btnSettings,
            self.ui.btnLogout,
        ]

        for button in buttons[:-1]:
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )
            layout.addWidget(button)

        layout.addStretch(1)

        logout_button = buttons[-1]
        logout_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        layout.addWidget(logout_button)

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
            self.show_reports
        )

        if hasattr(self.ui, "btnLookups"):
            self.ui.btnLookups.clicked.connect(
                self.open_lookups
            )

        self.ui.btnSettings.clicked.connect(
            self.show_settings
        )

        self.ui.btnLogout.clicked.connect(
            self.close
        )

    def show_dashboard(self):
        self.set_active_navigation(self.ui.btnDashboard)
        self.dashboard_page.refresh_dashboard()
        self.navigation.show(
            self.ui.pageDashboard
        )

    def show_assets(self):
        self.set_active_navigation(self.ui.btnAssets)
        self.assets_page.load_data()
        self.navigation.show(
            self.ui.pageAssets
        )

    def show_work_orders(self):
        self.set_active_navigation(self.ui.btnWorkOrders)
        self.work_orders_page.load_data()
        self.navigation.show(
            self.ui.pageWorkOrders
        )

    def show_pm(self):
        self.set_active_navigation(self.ui.btnPM)
        self.pm_page.load_data()
        self.navigation.show(
            self.ui.pagePM
        )

    def show_technicians(self):
        self.set_active_navigation(self.ui.btnTechnicians)
        self.technicians_page.load_data()
        self.navigation.show(
            self.ui.pageTechnicians
        )

    def show_inventory(self):
        self.set_active_navigation(self.ui.btnInventory)
        self.inventory_page.load_data()
        self.navigation.show(
            self.ui.pageInventory
        )

    def show_suppliers(self):
        self.set_active_navigation(self.ui.btnSuppliers)
        self.suppliers_page.load_data()
        self.navigation.show(
            self.ui.pageSuppliers
        )

    def show_reports(self):
        self.set_active_navigation(self.ui.btnReports)
        self.navigation.show(
            self.ui.pageReports
        )

    def show_settings(self):
        self.set_active_navigation(self.ui.btnSettings)
        self.navigation.show(
            self.ui.pageSettings
        )

    def open_lookups(self):
        self.lookup_window = LookupController()
        self.lookup_window.show()