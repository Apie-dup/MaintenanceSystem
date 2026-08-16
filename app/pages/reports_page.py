from PySide6.QtWidgets import (
    QWidget,
    QFileDialog,
    QMessageBox,
)

from app.helpers.table_helper import TableHelper
from app.services.report_service import ReportService
from app.ui.generated.ui_reports_page import (
    Ui_ReportsPage
)
from app.helpers.report_export_helper import ReportExportHelper
from PySide6.QtCore import QDate


class ReportsPage(QWidget):

    WORK_ORDER_COLUMNS = [
        ("work_order_number", "Work Order"),
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("technician_display", "Technician"),
        ("priority", "Priority"),
        ("status", "Status"),
        ("date_created", "Created"),
        ("due_date", "Due"),
        ("completed_date", "Completed"),
        ("labour_hours", "Labour Hours"),
        ("estimated_cost", "Estimated Cost"),
        ("actual_cost", "Actual Cost"),
    ]

    MAINTENANCE_COST_COLUMNS = [
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("work_order_count", "Work Orders"),
        ("labour_hours", "Labour Hours"),
        ("labour_cost", "Labour Cost"),
        ("material_cost", "Material Cost"),
        ("total_cost", "Total Cost"),
    ]

    INVENTORY_STOCK_COLUMNS = [
        ("part_number", "Part Number"),
        ("part_name", "Part Name"),
        ("category", "Category"),
        ("supplier_name", "Supplier"),
        ("quantity", "Quantity"),
        ("minimum_quantity", "Minimum"),
        ("reorder_quantity", "Reorder Qty"),
        ("unit_cost", "Unit Cost"),
        ("stock_value", "Stock Value"),
        ("location", "Location"),
        ("status", "Status"),
        ("stock_level", "Stock Level"),
    ]

    PREVENTIVE_MAINTENANCE_COLUMNS = [
        ("pm_number", "PM Number"),
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("task", "Task"),
        ("frequency_type", "Frequency"),
        ("frequency_value", "Value"),
        ("last_service_date", "Last Service"),
        ("next_due_date", "Next Due"),
        ("priority", "Priority"),
        ("due_status", "Due Status"),
    ]

    TECHNICIAN_PERFORMANCE_COLUMNS = [
        ("employee_number", "Employee Number"),
        ("technician_name", "Technician"),
        ("trade", "Trade"),
        ("work_order_count", "Work Orders"),
        ("completed_count", "Completed"),
        ("labour_hours", "Labour Hours"),
        ("labour_cost", "Labour Cost"),
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ReportsPage()
        self.ui.setupUi(self)

        self.setup_page()

    def setup_page(self):

        today = QDate.currentDate()

        self.ui.dtToDate.setDate(
            today
        )

        self.ui.dtFromDate.setDate(
            today.addMonths(-1)
        )

        self.ui.cmbReportType.currentTextChanged.connect(
            self.update_date_filter_state
        )

        self.update_date_filter_state()

        self.connect_signals()

        TableHelper.setup(
            self.ui.tblReport,
            self.WORK_ORDER_COLUMNS
        )

        self.generate_report()

    def connect_signals(self):
        self.ui.btnGenerate.clicked.connect(
            self.generate_report
        )

        self.ui.btnExport.clicked.connect(
            self.export_report
        )

        self.ui.btnClear.clicked.connect(
            self.clear_filters
        )

        self.ui.cmbReportType.currentTextChanged.connect(
            self.generate_report
        )

    def generate_report(self):

        report_type = (
            self.ui.cmbReportType
            .currentText()
            .strip()
        )

        from_date = (
            self.ui.dtFromDate
            .date()
            .toString("yyyy-MM-dd")
        )

        to_date = (
            self.ui.dtToDate
            .date()
            .toString("yyyy-MM-dd")
        )

        if from_date > to_date:
            self.ui.lblStatus.setText(
                "From Date cannot be after To Date."
            )
            return

        if report_type == "Work Orders":

            columns = self.WORK_ORDER_COLUMNS

            rows = ReportService.get_work_orders(
                from_date,
                to_date
            )

        elif report_type == "Maintenance Costs":

            columns = self.MAINTENANCE_COST_COLUMNS

            rows = (
                ReportService.get_maintenance_costs(
                    from_date,
                    to_date
                )
            )

        elif report_type == "Inventory Stock":

            columns = self.INVENTORY_STOCK_COLUMNS

            rows = (
                ReportService.get_inventory_stock()
            )

        elif report_type == "Preventive Maintenance":

            columns = self.PREVENTIVE_MAINTENANCE_COLUMNS

            rows = (
                ReportService.get_preventive_maintenance()
            )

        elif report_type == "Technician Performance":

            columns = self.TECHNICIAN_PERFORMANCE_COLUMNS

            rows = ReportService.get_technician_performance(
                from_date,
                to_date
            )

        else:
            self.ui.lblStatus.setText(
                "This report is not implemented yet."
            )
            return

        TableHelper.setup(
            self.ui.tblReport,
            columns
        )

        TableHelper.populate(
            self.ui.tblReport,
            rows,
            columns
        )

        self.format_report(
            report_type
        )

        self.ui.lblStatus.setText(
            f"Showing {len(rows)} records"
        )

    def clear_filters(self):
        self.generate_report()

    def format_report(self, report_type):

        table = self.ui.tblReport

        if report_type == "Work Orders":

            labour_column = 9
            estimated_column = 10
            actual_column = 11

            for row in range(
                table.rowCount()
            ):
                
                item = table.item(
                    row,
                    labour_column
                )

                if item is not None:
                    try:
                        item.setText(
                            f"{float(item.text()):.2f}"
                        )
                    except ValueError:
                        pass

                for column in (
                    estimated_column,
                    actual_column,
                ):

                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text()
                        )

                        item.setText(
                            f"N$ {value:,.2f}"
                        )

                    except ValueError:
                        pass

        elif report_type == "Maintenance Costs":
            
            labour_hours_column = 3

            cost_columns = (
                4,  # Labour Cost
                5,  # Material Cost
                6,  # Total Cost
            )

            for row in range(
                table.rowCount()
            ):

                item = table.item(
                    row,
                    labour_hours_column
                )

                if item is not None:
                    try:
                        item.setText(
                            f"{float(item.text()):.2f}"
                        )
                    except ValueError:
                        pass

            for row in range(
                table.rowCount()
            ):

                for column in cost_columns:
                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text()
                        )

                        item.setText(
                            f"N$ {value:,.2f}"
                        )

                    except ValueError:
                        pass

        elif report_type == "Inventory Stock":

            quantity_columns = (
                4,  # Quantity
                5,  # Minimum Quantity
                6,  # Reorder Quantity
            )

            cost_columns = (
                7,  # Unit Cost
                8,  # Stock Value
            )

            for row in range(
                table.rowCount()
            ):

                for column in quantity_columns:
                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text()
                        )

                        item.setText(
                            f"{value:.2f}"
                        )

                    except ValueError:
                        pass

            for row in range(
                table.rowCount()
            ):

                for column in cost_columns:
                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    try:
                        value = float(
                            item.text()
                        )

                        item.setText(
                            f"N$ {value:,.2f}"
                        )

                    except ValueError:
                        pass

        elif report_type == "Technician Performance":

            labour_hours_column = 5
            labour_cost_column = 6

            for row in range(table.rowCount()):

                #------------------------------
                # Labour Hours
                #------------------------------
                item = table.item(
                    row,
                    labour_hours_column
                )

                if item is not None:
                    try:
                        value = float(
                            item.text()
                            .replace(",", "")
                        )

                        item.setText(
                            f"{value:.2f}"
                        )
                    except ValueError:
                        pass

                #---------------------------
                # Labour Cost
                #---------------------------
                item = table.item(
                    row,
                    labour_cost_column
                )

                if item is not None:
                    try:
                        value = float(
                            item.text()
                            .replace("N$", "")
                            .replace(",", "")
                            .strip()
                        )

                        item.setText(
                            f"N$ {value:,.2f}"
                        )

                    except ValueError:
                        pass

    def update_date_filter_state(self):

        report_type = (
            self.ui.cmbReportType.currentText()
        )

        uses_date_filter = report_type in (
            "Work Orders",
            "Maintenance Costs",
            "Technician Performance",
        )

        self.ui.dtFromDate.setEnabled(
            uses_date_filter
        )

        self.ui.dtToDate.setEnabled(
            uses_date_filter
        )

    def export_report(self):

        table = self.ui.tblReport

        if table.rowCount() == 0:
            QMessageBox.warning(
                self,
                "Export Report",
                "There are no records to export."
            )
            return

        report_type = (
            self.ui.cmbReportType
            .currentText()
            .strip()
        )

        default_name = (
            report_type
            .lower()
            .replace(" ", "_")
            + ".xlsx"
        )

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Report",
            default_name,
            "Excel Workbook (*.xlsx)"
        )

        if not file_path:
            return

        if not file_path.lower().endswith(
            ".xlsx"
        ):
            file_path += ".xlsx"

        try:
            ReportExportHelper.export_table_to_excel(
                table,
                file_path,
                report_type
            )

            QMessageBox.information(
                self,
                "Export Report",
                "Report exported successfully."
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Export Report",
                (
                    "The report could not be exported.\n\n"
                    f"{error}"
                )
            )