from PySide6.QtGui import QColor

from app.base.crud_page import CrudPage
from app.dialogs.preventive_maintenance_dialog import (
    PreventiveMaintenanceDialog
)
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)
from app.ui.generated.ui_preventive_maintenance_page import (
    Ui_PMWindow
)


class PreventiveMaintenancePage(CrudPage):

    PAGE_TITLE = "Preventive Maintenance"
    ENTITY_NAME = "PM Schedule"
    RECORD_NAME = "preventive maintenance schedules"

    TABLE_COLUMNS = [
        ("pm_number", "PM Number"),
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("task", "Task"),
        ("frequency_type", "Frequency"),
        ("frequency_value", "Value"),
        ("last_service_date", "Last Service"),
        ("next_due_date", "Next Due"),
        ("due_status", "Due Status"),
        ("priority", "Priority"),
        ("active_display", "Active"),
    ]

    SEARCH_FIELDS = [
        "pm_number",
        "asset_number",
        "asset_name",
        "task",
        "description",
        "frequency_type",
        "priority",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PMWindow()
        self.ui.setupUi(self)

        self.service = PreventiveMaintenanceService
        self.dialog_class = PreventiveMaintenanceDialog
        self.table = self.ui.tblPM
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.setup_page()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.load_data()

    # ---------------------------------------------------------
    # Data
    # ---------------------------------------------------------

    def load_data(self):
        super().load_data()
        self.apply_due_highlighting()

    def search(self, text):
        super().search(text)
        self.apply_due_highlighting()

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.btnAdd.clicked.connect(
            self.add_record
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_record
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.search_widget.textChanged.connect(
            self.search
        )

        self.ui.btnGenerateWorkOrder.clicked.connect(
            self.generate_work_order
        )

        self.table.itemDoubleClicked.connect(
            lambda _item: self.edit_record()
        )

    # ---------------------------------------------------------
    # Highlighting
    # ---------------------------------------------------------

    def apply_due_highlighting(self):
        status_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.TABLE_COLUMNS)
                if field == "due_status"
            ),
            None,
        )

        if status_column is None:
            return

        for row in range(self.table.rowCount()):
            status_item = self.table.item(
                row,
                status_column,
            )

            if status_item is None:
                continue

            status = status_item.text().strip()

            if status == "Overdue":
                background = QColor("#f8d7da")
                tooltip = (
                    "This preventive maintenance schedule "
                    "is overdue and requires attention."
                )

            elif status == "Due Today":
                background = QColor("#ffe5b4")
                tooltip = (
                    "This preventive maintenance schedule "
                    "is due today."
                )

            elif status == "Due Soon":
                background = QColor("#fff3cd")
                tooltip = (
                    "This schedule is due within the next "
                    "seven days."
                )

            elif status == "Inactive":
                background = QColor("#dddddd")
                tooltip = "This schedule is inactive."

            else:
                continue

            status_item.setBackground(background)
            status_item.setToolTip(tooltip)

    # ---------------------------------------------------------
    # Generate Work Order
    # ---------------------------------------------------------

    def generate_work_order(self):
        pm_id = self.selected_id()

        if pm_id is None:
            self.warning(
                "Generate Work Order",
                "Please select a PM schedule.",
            )
            return

        if not self.confirm(
            "Generate Work Order",
            (
                "Generate a new work order from the selected "
                "preventive maintenance schedule?"
            ),
        ):
            return

        try:
            work_order_id = (
                PreventiveMaintenanceService
                .generate_work_order(pm_id)
            )

        except ValueError as error:
            self.warning(
                "Generate Work Order",
                str(error),
            )
            return

        except Exception as error:
            self.error(
                "Generate Work Order",
                (
                    "Could not generate the work order."
                    f"\n\n{error}"
                ),
            )
            return

        self.information(
            "Generate Work Order",
            (
                "Work order generated successfully."
                f"\n\nRecord ID: {work_order_id}"
            ),
        )

        self.load_data()