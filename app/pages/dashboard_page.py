from datetime import datetime

from app.base.base_page import BasePage
from app.helpers.format_helper import FormatHelper
from app.helpers.table_helper import TableHelper
from app.services.dashboard_service import DashboardService
from app.ui.generated.ui_dashboard_page import Ui_DashboardPage

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QHeaderView

COLOR_OVERDUE = QColor(255, 200, 200)     # light red
COLOR_DUE_TODAY = QColor(255, 230, 200)   # light orange
COLOR_DUE_SOON = QColor(255, 255, 200)    # light yellow
COLOR_UPCOMING = QColor(255, 255, 255)    # normal white


class DashboardPage(BasePage):

    URGENT_WORK_ORDER_COLUMNS = [
        ("work_order_number", "Work Order"),
        ("asset_name", "Asset"),
        ("priority", "Priority"),
        ("status", "Status"),
        ("due_date", "Due Date"),
    ]

    PM_DUE_COLUMNS = [
        ("pm_number", "PM Number"),
        ("asset_name", "Asset"),
        ("task", "Task"),
        ("next_due_date", "Next Due"),
        ("due_status", "Status"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)

        self.setup_page()

    def setup_page(self):
        if hasattr(self.ui, "dashboardTitle"):
            self.ui.dashboardTitle.setStyleSheet("")

        if hasattr(self.ui, "dashboardSubtitle"):
            self.ui.dashboardSubtitle.setStyleSheet("")

        self.setup_tables()

        header = self.ui.tblUrgentWorkOrders.horizontalHeader()
        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.Stretch
        )

        header = self.ui.tblPMDue.horizontalHeader()
        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeMode.Stretch
        )

        self.refresh_dashboard()

    def setup_tables(self):
        TableHelper.setup(
            self.ui.tblUrgentWorkOrders,
            self.URGENT_WORK_ORDER_COLUMNS
        )
        
        self.ui.tblUrgentWorkOrders.clearSelection()

        TableHelper.setup(
            self.ui.tblPMDue,
            self.PM_DUE_COLUMNS
        )

        self.ui.tblPMDue.clearSelection()

    def refresh_dashboard(self):
        summary = DashboardService.get_summary()

        self.ui.lblAssetsValue.setText(
            FormatHelper.integer(
                summary["assets"]
            )
        )

        self.ui.lblOpenWorkOrdersValue.setText(
            FormatHelper.integer(
                summary["open_work_orders"]
            )
        )

        pm_due_today_text = FormatHelper.integer(
            summary["pm_due_today"]
        )

        pm_due_week_text = FormatHelper.integer(
            summary["pm_due_week"]
        )

        if hasattr(self.ui, "lblPMDueTodayValue"):
            self.ui.lblPMDueTodayValue.setText(
                pm_due_today_text
            )
        else:
            self.ui.lblPMDueWeekValue.setText(
                pm_due_today_text
            )

        if hasattr(self.ui, "lblPMDueWeekValue_2"):
            self.ui.lblPMDueWeekValue_2.setText(
                pm_due_week_text
            )
        elif hasattr(self.ui, "lblPMDueTodayValue"):
            self.ui.lblPMDueWeekValue.setText(
                pm_due_week_text
            )

        self.ui.lblPMOverdueValue.setText(
            FormatHelper.integer(
                summary["pm_overdue"]
            )
        )

        self.ui.lblTechniciansValue.setText(
            FormatHelper.integer(
                summary["technicians"]
            )
        )

        inventory_value_text = FormatHelper.currency(
            summary["inventory_value"]
        )

        if hasattr(self.ui, "lblInventoryValue"):
            self.ui.lblInventoryValue.setText(
                inventory_value_text
            )
        else:
            self.ui.lblInventoryValueValue.setText(
                inventory_value_text
            )

        self.ui.lblLowStockValue.setText(
            FormatHelper.integer(
                summary["low_stock"]
            )
        )

        subtitle_text = datetime.now().strftime(
            "Maintenance overview - %d %B %Y, %H:%M"
        )

        if hasattr(self.ui, "lblDashboardSubtitle"):
            self.ui.lblDashboardSubtitle.setText(
                subtitle_text
            )
        elif hasattr(self.ui, "labelOverview"):
            self.ui.labelOverview.setText(
                subtitle_text
            )

        self.load_urgent_work_orders()
        self.load_pm_due()

    def load_urgent_work_orders(self):
        records = (
            DashboardService.get_urgent_work_orders()
        )

        TableHelper.populate(
            self.ui.tblUrgentWorkOrders,
            records,
            self.URGENT_WORK_ORDER_COLUMNS
        )

    def load_pm_due(self):
        records = DashboardService.get_pm_due_list()

        TableHelper.populate(
            self.ui.tblPMDue,
            records,
            self.PM_DUE_COLUMNS
        )

        status_col_index = next(
            (
                index
                for index, (field, _label) in enumerate(self.PM_DUE_COLUMNS)
                if field == "due_status"
            ),
            None
        )

        if status_col_index is None:
            return

        for row in range(self.ui.tblPMDue.rowCount()):
            item = self.ui.tblPMDue.item(row, status_col_index)
            if not item:
                continue

            status = item.text().strip()

            # Apply colors
            if status == "Overdue":
                color = COLOR_OVERDUE
            elif status == "Due Today":
                color = COLOR_DUE_TODAY
            elif status == "Due Soon":
                color = COLOR_DUE_SOON
            else:
                color = COLOR_UPCOMING

            # Apply background color to entire row
            for col in range(self.ui.tblPMDue.columnCount()):
                cell = self.ui.tblPMDue.item(row, col)
                if cell:
                    cell.setBackground(color)
