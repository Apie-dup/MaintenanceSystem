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
from app.helpers.pdf_report_export_helper import PdfReportExportHelper
from PySide6.QtCore import QDate
from app.services.settings_service import SettingsService
from app.helpers.date_helper import DateHelper
from app.helpers.currency_helper import CurrencyHelper
from app.core.permissions import Permissions


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

        self.user = getattr(
            parent,
            "user",
            {}
        )

        self.role = self.user.get(
            "role",
            ""
        )

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

        self.apply_permissions()

    def apply_permissions(self):

        can_export = Permissions.has_permission(
        self.role,
        "reports.export"
    )

        self.ui.btnExport.setVisible(
            can_export
        )

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

            date_columns = (
                6, #Created
                7, #Due
                8, #Complteted
            )
            
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

            cost_columns = (
                10, # Estimated Cost
                11, # Actual Cost
            )

            date_columns = (
                6, # Created
                7, # Due
                8, # Completed
            )

            for row in range(
                table.rowCount()
            ):

                #------------------------------
                # Labour Hours
                #------------------------------

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

                #------------------------------
                # Costs
                #------------------------------

                for column in cost_columns:

                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    try:
                        value = CurrencyHelper.parse(
                            item.text()
                        )
                        
                        item.setText(
                            CurrencyHelper.display(
                                value
                            )
                        )

                    except ValueError:
                        pass

                #-----------------------------
                # Dates
                #-----------------------------

                for column in date_columns:

                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    item.setText(
                        DateHelper.display(
                            item.text()
                        )
                    )

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
                            SettingsService.format_currency(value)
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
                            SettingsService.format_currency(value)
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
                            .replace(SettingsService.currency_symbol(), "")
                            .replace(",", "")
                            .strip()
                        )

                        item.setText(
                            SettingsService.format_currency(value)
                        )

                    except ValueError:
                        pass

        elif report_type == "Preventive Maintenance":

            date_columns = (
                6, # Last Service
                7, # Next Due
            )

            for row in range(
                table.rowCount()
            ):

                for column in date_columns:

                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    item.setText(
                        DateHelper.display(
                            item.text()
                        )
                    )


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

        if not Permissions.has_permission(
            self.role,
            "reports.export"
        ):
            QMessageBox.warning(
                self,
                "Export Report",
                "You do not have permission "
                "to export reports."
            )
            return

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

        file_path, selected_filter = (
            QFileDialog.getSaveFileName(
                self,
                "Export Report",
                default_name,
                (
                    "Excel Workbook (*.xlsx);;"
                    "PDF Document (*.pdf)"
                )
            )
        )

        if not file_path:
            return

        try:

            if "PDF" in selected_filter:

                if not file_path.lower().endswith(
                    ".pdf"
                ):
                    file_path += ".pdf"

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

                PdfReportExportHelper.export_table_to_pdf(
                    table,
                    file_path,
                    report_type,
                    from_date,
                    to_date
                )

            else:

                if not file_path.lower().endswith(
                    ".xlsx"
                ):
                    file_path += ".xlsx"

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

                ReportExportHelper.export_table_to_excel(
                    table,
                    file_path,
                    report_type,
                    from_date,
                    to_date
                )

            QMessageBox.information(
                self,
                "Export Report",
                "Report exported successfully."
            )

        except PermissionError:

            QMessageBox.warning(
                self,
                "Export Report",
                (
                    "The report could not be saved because "
                    "the file is currently in use.\n\n"
                    "Close the existing PDF file and try again, "
                    "or save the report with a different filename."
                )
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