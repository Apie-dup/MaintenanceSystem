from app.services.asset_service import AssetService
from app.services.inventory_service import InventoryService
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)
from app.services.technician_service import TechnicianService
from app.services.work_order_service import WorkOrderService


class DashboardService:

    @staticmethod
    def get_summary():
        return {
            "assets": len(
                AssetService.get_all()
            ),

            "open_work_orders":
                WorkOrderService.get_open_count(),

            "pm_due_today":
                PreventiveMaintenanceService
                .get_due_today_count(),

            "pm_overdue":
                PreventiveMaintenanceService
                .get_overdue_count(),

            "pm_due_week":
                PreventiveMaintenanceService
                .get_due_this_week_count(),

            "technicians": len(
                TechnicianService.get_all()
            ),

            "inventory_value":
                InventoryService.get_total_stock_value(),

            "low_stock": len(
                InventoryService.get_low_stock()
            ),
        }

    @staticmethod
    def get_urgent_work_orders():
        return WorkOrderService.get_urgent(
            limit=10
        )

    @staticmethod
    def get_pm_due_list():
        return PreventiveMaintenanceService.get_due_list(
            limit=10
        )