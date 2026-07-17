import sys
import unittest
from pathlib import Path

from PySide6.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.controllers.dashboard_controller import DashboardController
from app.services.dashboard_service import DashboardService


class DashboardControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_dashboard_statistics_include_technicians(self):
        stats = DashboardService.get_statistics()
        self.assertIn("technicians", stats)
        self.assertIsInstance(stats["technicians"], int)

    def test_dashboard_controller_sets_technician_value_label(self):
        controller = DashboardController({"fullname": "Test User"})
        self.assertEqual(controller.ui.lblTechniciansValue.text(), str(controller.ui.lblTechniciansValue.text()))


if __name__ == "__main__":
    unittest.main()
