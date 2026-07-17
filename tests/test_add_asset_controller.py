import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PySide6.QtWidgets import QApplication
from app.controllers.add_asset_controller import AddAssetController


app = QApplication.instance() or QApplication([])


def test_add_asset_controller_populates_lookups():
    controller = AddAssetController()

    category_items = [controller.ui.cmbCategory.itemText(i) for i in range(controller.ui.cmbCategory.count())]
    location_items = [controller.ui.cmbLocation.itemText(i) for i in range(controller.ui.cmbLocation.count())]

    assert category_items
    assert location_items
    assert "Electrical" in category_items
    assert "Reception" in location_items
