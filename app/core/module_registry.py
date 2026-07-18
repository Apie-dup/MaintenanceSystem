from app.pages.dashboard_page import DashboardPage
from app.pages.assets_page import AssetsPage
from app.pages.work_orders_page import WorkOrdersPage
from app.pages.pm_page import PMPage
from app.pages.technicians_page import TechniciansPage
from app.pages.inventory_page import InventoryPage
from app.pages.suppliers_page import SuppliersPage
from app.pages.reports_page import ReportsPage
from app.pages.settings_page import SettingsPage


MODULES = {
    "pageDashboard": DashboardPage,
    "pageAssets": AssetsPage,
    "pageWorkOrders": WorkOrdersPage,
    "pagePM": PMPage,
    "pageTechnicians": TechniciansPage,
    "pageInventory": InventoryPage,
    "pageSuppliers": SuppliersPage,
    "pageReports": ReportsPage,
    "pageSettings": SettingsPage,
}