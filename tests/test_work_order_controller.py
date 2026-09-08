import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QAbstractItemView, QWidget

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.controllers.work_order_controller import WorkOrderController
from app.dialogs.work_order_dialog import WorkOrderDialog


app = QApplication.instance() or QApplication([])


def test_work_order_table_disables_inline_editing():
    controller = WorkOrderController()
    assert controller.ui.tblWorkOrders.editTriggers() == QAbstractItemView.EditTrigger.NoEditTriggers


def test_work_order_dialog_has_history_highlighting():
    dialog = WorkOrderDialog(parent=QWidget())
    assert hasattr(dialog, "apply_history_highlighting")
    assert callable(dialog.apply_history_highlighting)
