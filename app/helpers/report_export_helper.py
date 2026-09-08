from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from app.services.settings_service import SettingsService

class ReportExportHelper:

    @staticmethod
    def export_table_to_excel(
        table,
        file_path,
        report_title,
        from_date=None,
        to_date=None,
        filters=None,
        summary=None,
    ):

        currency_symbol = (
            SettingsService.currency_symbol()
        )
        
        workbook = Workbook()

        worksheet = workbook.active
        worksheet.title = "Report"

        column_count = table.columnCount()
        row_count = table.rowCount()

        # -------------------------------------------------
        # Report title
        # -------------------------------------------------

        if column_count > 0:
            worksheet.merge_cells(
                start_row=1,
                start_column=1,
                end_row=1,
                end_column=column_count
            )

        title_cell = worksheet.cell(
            row=1,
            column=1,
            value=report_title
        )

        title_cell.font = Font(
            bold=True,
            size=16
        )

        title_cell.alignment = Alignment(
            horizontal="center"
        )

        #--------------------------------------------------
        # Report period
        #--------------------------------------------------

        date_based_reports = {
            "Work Orders",
            "Maintenance Costs",
            "Technician Performance",
        }

        if (
            report_title in date_based_reports
            and from_date
            and to_date
        ):
            period_cell = worksheet.cell(
                row=2,
                column=1,
                value=(
                    f"Period: {from_date} to {to_date}"
                )
            )

            period_cell.font = Font(
                italic=True,
                size=10
            )

        # -------------------------------------------------
        # Column headings
        # -------------------------------------------------

        header_row = 3

        for column in range(column_count):

            header_item = (
                table.horizontalHeaderItem(
                    column
                )
            )

            heading = (
                header_item.text()
                if header_item is not None
                else ""
            )

            cell = worksheet.cell(
                row=header_row,
                column=column + 1,
                value=heading
            )

            cell.font = Font(
                bold=True
            )

            cell.alignment = Alignment(
                horizontal="center"
            )

        # -------------------------------------------------
        # Report data
        # -------------------------------------------------

        for row in range(row_count):

            for column in range(column_count):

                item = table.item(
                    row,
                    column
                )

                text = (
                    item.text().strip()
                    if item is not None
                    else ""
                )

                cell = worksheet.cell(
                    row=row + 4,
                    column=column + 1
                )

                # -----------------------------------------
                # Empty cell
                # -----------------------------------------

                if text == "":
                    cell.value = ""
                    continue

                # -----------------------------------------
                # Currency value
                # -----------------------------------------

                if text.startswith(currency_symbol):

                    try:
                        numeric_value = float(
                            text
                            .replace(currency_symbol, "")
                            .replace(",", "")
                            .strip()
                        )

                        cell.value = numeric_value

                        cell.number_format = (
                            f'"{currency_symbol}" #,##0.00'
                        )

                    except ValueError:
                        cell.value = text

                    continue

                # -----------------------------------------
                # Normal numeric value
                # -----------------------------------------

                try:
                    numeric_value = float(
                        text.replace(",", "")
                    )

                    cell.value = numeric_value

                    if "." in text:
                        cell.number_format = (
                            "#,##0.00"
                        )

                except ValueError:

                    # Text such as:
                    # EMP-000003
                    # Abraham du Plessis
                    # General Maintenance
                    cell.value = text

        # -------------------------------------------------
        # Automatically size columns
        # -------------------------------------------------

        for column in range(
            1,
            column_count + 1
        ):

            max_length = 0

            column_letter = (
                get_column_letter(
                    column
                )
            )

            for cell in worksheet[
                column_letter
            ]:

                if cell.value is None:
                    continue

                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

            worksheet.column_dimensions[
                column_letter
            ].width = min(
                max_length + 2,
                40
            )

        # -------------------------------------------------
        # Freeze headings
        # -------------------------------------------------

        worksheet.freeze_panes = "A4"

        # -------------------------------------------------
        # Excel filters
        # -------------------------------------------------

        if (
            column_count > 0
            and row_count > 0
        ):
            worksheet.auto_filter.ref = (
                f"A3:"
                f"{get_column_letter(column_count)}"
                f"{row_count + 3}"
            )

        # -------------------------------------------------
        # Save workbook
        # -------------------------------------------------

        workbook.save(
            file_path
        )