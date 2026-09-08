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
from app.services.asset_service import AssetService


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
        ("last_service_meter", "Last Meter"),
        ("next_due_meter", "Next Due Meter"),
        ("priority", "Priority"),
        ("due_status", "Due Status"),
    ]

    TECHNICIAN_PERFORMANCE_COLUMNS = [
        ("employee_number", "Employee Number"),
        ("technician_name", "Technician"),
        ("trade", "Trade"),
        ("work_order_count", "Work Orders"),
        ("completed_count", "Completed"),
        ("completion_rate", "Completion %"),
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

        self.load_status_filter()
        self.load_asset_filter()

        self.ui.cmbReportType.currentTextChanged.connect(
            self.update_date_filter_state
        )

        self.update_date_filter_state()

        self.connect_signals()

        self.apply_permissions()

        TableHelper.setup(
            self.ui.tblReport,
            self.WORK_ORDER_COLUMNS
        )

        self.generate_report()

    def load_status_filter(self):

        self.ui.cmbStatus.clear()

        self.ui.cmbStatus.addItem(
            "All Statuses",
            None
        )

        statuses = [
            "Open",
            "Assigned",
            "In Progress",
            "On Hold",
            "Completed",
            "Closed",
            "Cancelled",
        ]

        for status in statuses:
            self.ui.cmbStatus.addItem(
                status,
                status
            )

    def load_asset_filter(self):

        self.ui.cmbAsset.clear()

        self.ui.cmbAsset.addItem(
            "All Assets",
            None
        )

        assets = AssetService.get_all()

        for asset in assets:

            display_text = (
                f'{asset["asset_number"]} - '
                f'{asset["asset_name"]}'
            )

            self.ui.cmbAsset.addItem(
                display_text,
                asset["asset_number"]
            )

    def reset_summary(self):

        self.ui.lblTotalValue.setText(
            "0"
        )

        self.ui.lblOpenValue.setText(
            "0"
        )

        self.ui.lblCompletedValue.setText(
            "0"
        )

        self.ui.lblTotalCostValue.setText(
            SettingsService.format_currency(
                0
            )
        )

    def apply_permissions(self):

        #-----------------------------------------------
        # Export permission
        #-----------------------------------------------

        can_export = Permissions.has_permission(
            self.role,
            "reports.export"
        )

        self.ui.btnExport.setVisible(
            can_export
        )

        #-----------------------------------------------
        # Print permission
        #-----------------------------------------------

        can_print = Permissions.has_permission(
            self.role,
            "reports.print"
        )

        self.ui.btnPrint.setVisible(
            can_print
        )

        #----------------------------------------------
        # Initial table setup
        #----------------------------------------------

        TableHelper.setup(
            self.ui.tblReport,
            self.WORK_ORDER_COLUMNS
        )

        #----------------------------------------------
        # Load initial report
        #----------------------------------------------

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
            self.report_type_changed
        )

        self.ui.btnPrint.clicked.connect(
            self.print_report
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

            selected_status = (
                self.ui.cmbStatus.currentText()
                .strip()
            )

            selected_asset_number = (
                self.ui.cmbAsset.currentData()
            )

            status = (
                None
                if selected_status == "All Statuses"
                else selected_status
            )

            rows = ReportService.get_work_orders(
                from_date,
                to_date,
                status=status,
                asset_number=selected_asset_number,

            )

        elif report_type == "Maintenance Costs":

            columns = self.MAINTENANCE_COST_COLUMNS

            selected_status = (
                self.ui.cmbStatus.currentText()
                .strip()
            )

            selected_asset_number = (
                self.ui.cmbAsset.currentData()
            )

            status = (
                None
                if selected_status == "All Statuses"
                else selected_status
            )

            rows = (
                ReportService.get_maintenance_costs(
                    from_date,
                    to_date,
                    status=status,
                    asset_number=selected_asset_number,
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

            selected_status = (
                self.ui.cmbStatus.currentText()
                .strip()
            )

            selected_asset_number = (
                self.ui.cmbAsset.currentData()
            )

            filtered_rows = []

            for record in rows:

                row = dict(record)

                #----------------------------------------------
                # PM Due Status filter
                #----------------------------------------------

                if selected_status != "All Statuses":

                    if (
                        row.get("due_status") or ""
                    ) != selected_status:
                        continue

                #----------------------------------------------
                # Asset filter
                #----------------------------------------------

                if selected_asset_number is not None:

                    if (
                        row.get("asset_number") or ""
                    ) != selected_asset_number:
                        continue

                filtered_rows.append(
                    record
                )

            rows = filtered_rows

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
            report_type,
            rows
        )

        count = self.ui.tblReport.rowCount()

        self.ui.lblStatus.setText(
            f"Showing {count} record"
            if count == 1
            else f"Showing {count} records"
        )

    def report_type_changed(self):

        report_type = (
            self.ui.cmbReportType.currentText()
        )

        # --------------------------------------------------
        # Update available status choices
        # --------------------------------------------------

        self.update_status_filter(
            report_type
        )

        # --------------------------------------------------
        # Determine available filters
        # --------------------------------------------------

        filters_enabled = (
            report_type
            not in {
                "Inventory Stock",
                "Technician Performance",
            }
        )

        self.ui.cmbStatus.setEnabled(
            filters_enabled
        )

        self.ui.cmbAsset.setEnabled(
            filters_enabled
        )

        if not filters_enabled:

            self.ui.cmbStatus.setCurrentIndex(
                0
            )

            self.ui.cmbAsset.setCurrentIndex(
                0
            )

        # --------------------------------------------------
        # Update summary labels
        # --------------------------------------------------

        self.update_summary_labels(
            report_type
        )

        # --------------------------------------------------
        # Generate selected report
        # --------------------------------------------------

        self.generate_report()

    def clear_filters(self):
        
        today = QDate.currentDate()

        #---------------------------------------------------
        # Reset date range
        #---------------------------------------------------

        self.ui.dtToDate.setDate(
            today
        )

        self.ui.dtFromDate.setDate(
            today.addMonths(-1)
        )

        #---------------------------------------------------
        # Reset filters
        #---------------------------------------------------

        if self.ui.cmbStatus.count() > 0:
            self.ui.cmbStatus.setCurrentIndex(
                0
            )

        if self.ui.cmbAsset.count() > 0:
            self.ui.cmbAsset.setCurrentIndex(
                0
            )

        #-----------------------------------------------------
        # Regenerate current report
        #-----------------------------------------------------

        self.generate_report()

    def format_report(self, report_type, rows):

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

            completion_rate_column = 5
            labour_hours_column = 6
            labour_cost_column = 7

            for row in range(table.rowCount()):

                #------------------------------
                # Completion Rate
                #------------------------------

                item = table.item(
                    row,
                    completion_rate_column
                )

                if item is not None:
                    try:
                        value = float(
                            item.text()
                            .replace("%", "")
                            .strip()
                        )

                        item.setText(
                            f"{value:.2f}%"
                        )

                    except ValueError:
                        pass

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

            meter_columns = (
                8, # Last Meter
                9, # Next Due Meter
            )

            for row in range(
                table.rowCount()
            ):

                #------------------------------
                # Dates
                #------------------------------

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

                #------------------------------
                # Meter reading
                #------------------------------

                for column in meter_columns:

                    item = table.item(
                        row,
                        column
                    )

                    if item is None:
                        continue

                    text = item.text().strip()

                    if not text:
                        continue

                    try:
                        value = float(text)

                        item.setText(
                            f"{value:,.2f}"
                        )

                    except ValueError:
                        pass

        self.update_summary(
            report_type,
            rows,
        )

    def update_summary(
            self,
            report_type,
            rows,
    ):

        self.update_summary_labels(
            report_type
        )

        #--------------------------------------------------------------
        # Reset summary
        #--------------------------------------------------------------

        self.reset_summary()

        total_count = len(rows)

        self.ui.lblTotalValue.setText(
            str(total_count)
        )

        #------------------------------------------------------------
        # Work Orders
        #------------------------------------------------------------

        if report_type == "Work Orders":

            open_count = sum(
                1
                for row in rows
                if row["status"] not in {
                    "Completed",
                    "Closed",
                    "Cancelled",
                }
            )

            completed_count = sum(
                1
                for row in rows
                if row["status"] in {
                    "Completed",
                    "Closed",
                }
            )

            total_cost = sum(
                float(
                    row["actual_cost"] or 0
                )
                for row in rows
            )

            self.ui.lblOpenValue.setText(
                str(open_count)
            )

            self.ui.lblCompletedValue.setText(
                str(completed_count)
            )

            self.ui.lblTotalCostValue.setText(
                SettingsService.format_currency(
                    total_cost
                )
            )

            return

        #---------------------------------------------------------
        # Preventive Maintenance
        #---------------------------------------------------------

        if report_type == "Preventive Maintenance":

            due_today_count = sum(
                1
                for row in rows
                if row["due_status"] == "Due Today"
            )

            due_soon_count = sum(
                1
                for row in rows
                if row["due_status"] == "Due Soon"
            )

            overdue_count = sum(
                1
                for row in rows
                if row["due_status"] == "Overdue"
            )

            self.ui.lblOpenValue.setText(
                str(due_today_count)
            )

            self.ui.lblCompletedValue.setText(
                str(due_soon_count)
            )

            self.ui.lblTotalCostValue.setText(
                str(overdue_count)
            )

            return

        #-------------------------------------------------------
        # Maintenance Costs
        #---------------------------------------------------------

        if report_type == "Maintenance Costs":

            work_order_count = sum(
                int(row["work_order_count"] or 0)
                for row in rows
            )

            labour_cost = sum(
                float(row["labour_cost"] or 0)
                for row in rows
            )

            material_cost = sum(
                float(row["material_cost"] or 0)
                for row in rows
            )

            total_cost = sum(
                float(row["total_cost"] or 0)
                for row in rows
            )

            self.ui.lblTotalValue.setText(
                str(work_order_count)
            )

            self.ui.lblOpenValue.setText(
                SettingsService.format_currency(
                    labour_cost
                )
            )

            self.ui.lblCompletedValue.setText(
                SettingsService.format_currency(
                    material_cost
                )
            )

            self.ui.lblTotalCostValue.setText(
                SettingsService.format_currency(
                    total_cost
                )
            )

            return

        #---------------------------------------------------------
        # Inventory Stock
        #---------------------------------------------------------

        if report_type == "Inventory Stock":

            item_count = len(rows)

            low_stock_count = sum(
                1
                for row in rows
                if row["stock_level"] == "Low Stock"
            )

            out_of_stock_count = sum(
                1
                for row in rows
                if float(row["quantity"] or 0) <= 0
            )

            stock_value = sum(
                float(row["stock_value"] or 0)
                for row in rows
            )

            self.ui.lblTotalValue.setText(
                str(item_count)
            )

            self.ui.lblOpenValue.setText(
                str(low_stock_count)
            )

            self.ui.lblCompletedValue.setText(
                str(out_of_stock_count)
            )

            self.ui.lblTotalCostValue.setText(
                SettingsService.format_currency(
                    stock_value
                )
            )

            return

        #---------------------------------------------------------
        # Technician Performance
        #---------------------------------------------------------

        if report_type == "Technician Performance":

            technician_count = len(rows)

            work_order_count = sum(
                int(
                    row["work_order_count"] or 0
                )
                for row in rows
            )

            labour_hours = sum(
                float(
                    row["labour_hours"] or 0
                )
                for row in rows
            )

            labour_cost = sum(
                float(
                    row["labour_cost"] or 0
                )
                for row in rows
            )

            self.ui.lblTotalValue.setText(
                str(technician_count)
            )
            
            self.ui.lblOpenValue.setText(
                str(work_order_count)
            )

            self.ui.lblCompletedValue.setText(
                f"{labour_hours:.2f}"
            )

            self.ui.lblTotalCostValue.setText(
                SettingsService.format_currency(
                    labour_cost
                )
            )

            return

    def update_summary_labels(
        self,
        report_type,
    ):

        if report_type == "Preventive Maintenance":

            self.ui.lblTotal.setText(
                "Total"
            )

            self.ui.lblOpen.setText(
                "Due Today"
            )

            self.ui.lblCompleted.setText(
                "Due Soon"
            )

            self.ui.lblTotalCost.setText(
                "Overdue"
            )

            return

        if report_type == "Maintenance Costs":

            self.ui.lblTotal.setText(
                "Work Orders"
            )

            self.ui.lblOpen.setText(
                "Labour Cost"
            )

            self.ui.lblCompleted.setText(
                "Material Cost"
            )

            self.ui.lblTotalCost.setText(
                "Total Cost"
            )

            return

        if report_type == "Inventory Stock":

            self.ui.lblTotal.setText(
                "Items"
            )

            self.ui.lblOpen.setText(
                "Low Stock"
            )

            self.ui.lblCompleted.setText(
                "Out of Stock"
            )

            self.ui.lblTotalCost.setText(
                "Stock Value"
            )

            return

        if report_type == "Technician Performance":

            self.ui.lblTotal.setText(
                "Technicians"
            )

            self.ui.lblOpen.setText(
                "Work Orders"
            )

            self.ui.lblCompleted.setText(
                "Labour Hours"
            )

            self.ui.lblTotalCost.setText(
                "Labour Cost"
            )

            return

        # Default: Work Orders
        self.ui.lblTotal.setText(
            "Total"
        )

        self.ui.lblOpen.setText(
            "Open"
        )

        self.ui.lblCompleted.setText(
            "Completed"
        )

        self.ui.lblTotalCost.setText(
            "Total Cost"
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

        filters = {
            "Status": (
                self.ui.cmbStatus.currentText()
                if self.ui.cmbStatus.isEnabled()
                else None
            ),

            "Asset": (
                self.ui.cmbAsset.currentText()
                if self.ui.cmbAsset.isEnabled()
                else None
            ),
        }

        summary = {
            self.ui.lblTotal.text():
                self.ui.lblTotalValue.text(),

            self.ui.lblOpen.text():
                self.ui.lblOpenValue.text(),

            self.ui.lblCompleted.text():
                self.ui.lblCompletedValue.text(),

            self.ui.lblTotalCost.text():
                self.ui.lblTotalCostValue.text(),
        }

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
                    to_date,
                    filters=filters,
                    summary=summary,
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

    def update_status_filter(
        self,
        report_type,
    ):

        self.ui.cmbStatus.blockSignals(True)

        try:
            self.ui.cmbStatus.clear()

            # --------------------------------------------------
            # Work Orders / Maintenance Costs
            # --------------------------------------------------

            if report_type in {
                "Work Orders",
                "Maintenance Costs",
            }:

                statuses = [
                    "All Statuses",
                    "Open",
                    "Assigned",
                    "In Progress",
                    "On Hold",
                    "Completed",
                    "Closed",
                    "Cancelled",
                ]

            # --------------------------------------------------
            # Preventive Maintenance
            # --------------------------------------------------

            elif report_type == "Preventive Maintenance":

                statuses = [
                    "All Statuses",
                    "Scheduled",
                    "Due Soon",
                    "Due Today",
                    "Overdue",
                    "WO Open",
                ]

            # --------------------------------------------------
            # Reports without status filtering
            # --------------------------------------------------

            else:

                statuses = [
                    "All Statuses",
                ]

            self.ui.cmbStatus.addItems(
                statuses
            )

            self.ui.cmbStatus.setCurrentIndex(
                0
            )

        finally:
            self.ui.cmbStatus.blockSignals(False)

    def print_report(self):

        if not Permissions.has_permission(
            self.role,
            "reports.print"
        ):
            QMessageBox.warning(
                self,
                "Print Report",
                "You do not have permission "
                "to print reports."
            )
            return

        table = self.ui.tblReport

        if table.rowCount() == 0:
            QMessageBox.warning(
                self,
                "Print Report",
                "There are no records to print."
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
            + ".pdf"
        )

        file_path, _ = (
            QFileDialog.getSaveFileName(
                self,
                "Save Report",
                default_name,
                "PDF Document (*.pdf)"
            )
        )

        if not file_path:
            return

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

        filters = {
            "Status": (
                self.ui.cmbStatus.currentText()
                if self.ui.cmbStatus.isEnabled()
                else None
            ),

            "Asset": (
                self.ui.cmbAsset.currentText()
                if self.ui.cmbAsset.isEnabled()
                else None
            ),
        }

        summary = {
            self.ui.lblTotal.text():
                self.ui.lblTotalValue.text(),

            self.ui.lblOpen.text():
                self.ui.lblOpenValue.text(),

            self.ui.lblCompleted.text():
                self.ui.lblCompletedValue.text(),

            self.ui.lblTotalCost.text():
                self.ui.lblTotalCostValue.text(),

        }

        try:

            PdfReportExportHelper.export_table_to_pdf(
                table,
                file_path,
                report_type,
                from_date,
                to_date,
                filters=filters,
                summary=summary,
            )

            QMessageBox.information(
                self,
                "Print Report",
                "Report PDF created successfully."
            )

        except PermissionError:

            QMessageBox.warning(
                self,
                "Print Report",
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
                "Print Report",
                (
                    "The report could not be created.\n\n"
                    f"{error}"
                )
            )


        