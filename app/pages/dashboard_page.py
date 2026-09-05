from datetime import datetime

from app.base.base_page import BasePage
from app.helpers.format_helper import FormatHelper
from app.helpers.table_helper import TableHelper
from app.services.dashboard_service import DashboardService
from app.ui.generated.ui_dashboard_page import Ui_DashboardPage
from app.services.settings_service import SettingsService
from app.helpers.theme_helper import ThemeHelper
from PySide6.QtWidgets import QHeaderView


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
        ("due_display", "Due At"),
        ("due_status", "Status"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_controller = parent

        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)

        self.setup_page()

    def setup_page(self):

        if hasattr(self.ui, "dashboardTitle"):
            self.ui.dashboardTitle.setStyleSheet("")

        if hasattr(self.ui, "dashboardSubtitle"):
            self.ui.dashboardSubtitle.setStyleSheet("")

        self.refresh_identity()

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

        self.connect_signals()

        self.refresh_dashboard()

    def connect_signals(self):
        self.ui.btnVehicleDefects.clicked.connect(
            self.open_vehicle_defects
        )

        self.ui.tblUrgentWorkOrders.itemDoubleClicked.connect(
            self.open_urgent_work_order
        )

    def open_vehicle_defects(self):

        if self.main_controller is None:
            return

        self.main_controller.show_vehicle_logbook(
            unresolved_defects=True
        )

    def open_urgent_work_order(self):

        record_id = TableHelper.selected_id(
            self.ui.tblUrgentWorkOrders
        )

        if record_id is None:
            return

        if self.main_controller is None:
            return

        self.main_controller.open_work_order_by_id(
            record_id
        )

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

        self.ui.lblVehicleDefectsValue.setText(
            str(summary["vehicle_defects"])
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

        display_records = []

        meter_types = {
            "Running Hours",
            "Kilometers",
            "Cycles",
        }

        for record in records:

            pm = dict(record)

            frequency_type = (
                pm.get("frequency_type") or ""
            ).strip()

            #------------------------------------------
            # Meter-based PM
            #------------------------------------------

            if frequency_type in meter_types:

                next_due_meter = pm.get(
                    "next_due_meter"
                )

                if next_due_meter is not None:

                    value = float(
                        next_due_meter
                    )

                    if frequency_type == "Running Hours":
                        unit = "Hours"

                    elif frequency_type == "Kilometers":
                        unit = "km"

                    elif frequency_type == "Cycles":
                        unit = "Cycles"

                    else:
                        unit = frequency_type

                    pm["due_display"] = (
                        f"{value:,.2f} {unit}"
                    )

                else:
                    pm["due_display"] = ""

            #------------------------------------------
            # Calendar-based PM
            #------------------------------------------

            else:
                pm["due_display"] = (
                    pm.get("next_due_date") or ""
                )

            display_records.append(pm)

        TableHelper.populate(
            self.ui.tblPMDue,
            display_records,
            self.PM_DUE_COLUMNS
        )

        status_col_index = next(
            (
                index
                for index, (field, _lable)
                in enumerate(self.PM_DUE_COLUMNS)
                if field == "due_status"
            ),
            None
        )

        if status_col_index is None:
            return

        for row in range(
            self.ui.tblPMDue.rowCount()
        ):

            item = self.ui.tblPMDue.item(
                row,
                status_col_index
            )

            if not item:
                continue

            status = item.text().strip()

            color = ThemeHelper.status_color(
                self,
                status
            )

            if color is None:
                continue

            # Dashboard: highlight entire PM row
            for col in range(
                self.ui.tblPMDue.columnCount()
            ):

                cell = self.ui.tblPMDue.item(
                    row,
                    col
                )

                if cell:
                    cell.setBackground(color)

    def refresh_identity(self):
        if hasattr(self.ui, "dashboardTitle"):
            self.ui.dashboardTitle.setText(
                SettingsService.system_name()
            )

        if hasattr(self.ui, "dashboardSubtitle"):
            self.ui.dashboardSubtitle.setText(
                SettingsService.organization_name()
            )
