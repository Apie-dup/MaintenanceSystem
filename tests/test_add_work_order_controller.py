import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.controllers.add_work_order_controller import AddWorkOrderController


app = QApplication.instance() or QApplication([])


def test_load_work_order_handles_missing_work_order():
    controller = AddWorkOrderController(999999)
    assert controller.ui.txtWorkOrderNumber.text() == ""
