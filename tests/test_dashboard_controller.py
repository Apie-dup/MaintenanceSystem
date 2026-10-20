import sys
import unittest
from pathlib import Path

from PySide6.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.controllers.dashboard_controller import DashboardController
from app.models.vehicle_logbook_model import VehicleLogbookModel
from app.services.dashboard_service import DashboardService


class DashboardControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_dashboard_statistics_include_technicians(self):
        stats = DashboardService.get_statistics()
        self.assertIn("technicians", stats)
        self.assertIsInstance(stats["technicians"], int)

    def test_dashboard_page_sets_technician_value_label(self):
        from unittest.mock import patch
        from app.pages.dashboard_page import DashboardPage

        summary = {
            "assets": 10,
            "open_work_orders": 3,
            "overdue_work_orders": 1,
            "pm_due_today": 2,
            "pm_due_week": 4,
            "pm_overdue": 0,
            "technicians": 5,
            "due_today_work_orders": 1,
            "low_stock": 2,
            "vehicle_defects": 0,
        }

        with patch.object(
            DashboardService,
            "get_summary",
            return_value=summary
        ), patch.object(
            DashboardPage,
            "refresh_identity"
        ), patch.object(
            DashboardPage,
            "load_urgent_work_orders"
        ), patch.object(
            DashboardPage,
            "load_pm_due"
        ):
            page = DashboardPage()

        self.assertEqual(
            page.ui.lblTechniciansValue.text(),
            "5"
        )

    def test_vehicle_logbook_unresolved_defects_query_runs(self):
        rows = VehicleLogbookModel.get_unresolved_defects()
        self.assertIsInstance(rows, list)


if __name__ == "__main__":
    unittest.main()
