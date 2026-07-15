import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QAbstractItemView

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.controllers.work_order_controller import WorkOrderController


app = QApplication.instance() or QApplication([])


def test_work_order_table_disables_inline_editing():
    controller = WorkOrderController()
    assert controller.ui.tblWorkOrders.editTriggers() == QAbstractItemView.EditTrigger.NoEditTriggers
