from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)
from app.services.settings_service import SettingsService
from app.helpers.date_helper import DateHelper



class PdfReportExportHelper:

    @staticmethod
    def export_table_to_pdf(
        table,
        file_path,
        report_title,
        from_date=None,
        to_date=None,
        filters=None,
        summary=None
    ):
        page_size = landscape(A4)

        document = SimpleDocTemplate(
            file_path,
            pagesize=page_size,
            rightMargin=10 * mm,
            leftMargin=10 * mm,
            topMargin=12 * mm,
            bottomMargin=18 * mm,
        )

        styles = getSampleStyleSheet()

        elements = []

        # -------------------------------------------------
        # Report title
        # -------------------------------------------------

        title = Paragraph(
            f"<b>{report_title}</b>",
            styles["Title"]
        )

        elements.append(title)

        #-------------------------------------------------
        # Report period
        #-------------------------------------------------

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
            period_text = (
                f"Period: "
                f"{DateHelper.display(from_date)} "
                f"to "
                f"{DateHelper.display(to_date)}"
            )

            period = Paragraph(
                period_text,
                styles["Normal"]
            )

            elements.append(period)
            elements.append(
                Spacer(1, 4 * mm)
            )

        else:
            elements.append(
            Spacer(1, 6 * mm)
        )

        column_count = table.columnCount()
        row_count = table.rowCount()

        data = []

        #-------------------------------------------------
        # Active filters
        #--------------------------------------------------

        if filters:

            filter_parts = []

            for label, value in filters.items():

                if value:
                    filter_parts.append(
                        f"{label}: {value}"
                    )

            if filter_parts:

                filter_text = (
                    " | ".join(filter_parts)
                )

                elements.append(
                    Paragraph(
                        filter_text,
                        styles["Normal"]
                    )
                )

                elements.append(
                    Spacer(1, 4 * mm)
                )

        # -------------------------------------------------
        # Report summary
        # -------------------------------------------------

        if summary:

            summary_data = []

            headings = []
            values = []

            for label, value in summary.items():

                headings.append(label)
                values.append(str(value))

            summary_data.append(headings)
            summary_data.append(values)

            summary_table = Table(
                summary_data,
                colWidths=[
                    (
                        page_size[0]
                        - document.leftMargin
                        - document.rightMargin
                    )
                    / len(headings)
                ]
                * len(headings)
            )

            summary_table.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("333333")
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.4,
                        colors.grey
                    ),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, -1),
                        8
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    ),
                ])
            )

            elements.append(
                summary_table
            )

            elements.append(
                Spacer(1, 6 * mm)
            )

        # -------------------------------------------------
        # Column headings
        # -------------------------------------------------

        headings = []

        for column in range(column_count):

            item = table.horizontalHeaderItem(
                column
            )

            headings.append(
                item.text()
                if item is not None
                else ""
            )

        data.append(headings)

        # -------------------------------------------------
        # Report rows
        # -------------------------------------------------

        for row in range(row_count):

            row_data = []

            for column in range(column_count):

                item = table.item(
                    row,
                    column
                )

                row_data.append(
                    item.text()
                    if item is not None
                    else ""
                )

            data.append(row_data)

        # -------------------------------------------------
        # Available table width
        # -------------------------------------------------

        available_width = (
            page_size[0]
            - document.leftMargin
            - document.rightMargin
        )

        # -------------------------------------------------
        # Calculate column widths
        # -------------------------------------------------

        column_weights = []

        for column in range(column_count):

            maximum_length = 1

            for row in data:

                if column < len(row):

                    value = str(
                        row[column]
                    )

                    maximum_length = max(
                        maximum_length,
                        len(value)
                    )

            # Prevent one long column from taking
            # most of the page.
            maximum_length = min(
                maximum_length,
                30
            )

            column_weights.append(
                maximum_length
            )

        total_weight = sum(
            column_weights
        )

        if total_weight == 0:
            total_weight = 1

        column_widths = []

        for weight in column_weights:

            width = (
                available_width
                * weight
                / total_weight
            )

            column_widths.append(
                width
            )

        # -------------------------------------------------
        # Choose font size
        # -------------------------------------------------

        if column_count <= 7:
            font_size = 8

        elif column_count <= 10:
            font_size = 7

        else:
            font_size = 6

        # -------------------------------------------------
        # Build table
        # -------------------------------------------------

        pdf_table = Table(
            data,
            colWidths=column_widths,
            repeatRows=1
        )

        pdf_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#333333")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, 0),
                    "CENTER"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.grey
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    font_size
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F3F3F3")
                    ]
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    3
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    3
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
            ])
        )

        elements.append(
            pdf_table
        )

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        def draw_footer(canvas, doc):

            canvas.saveState()

            generated = datetime.now().strftime(
                "%d-%b-%Y %H:%M"
            )

            organization_name = (
                SettingsService.organization_name()
            )

            system_name = (
                SettingsService.system_name()
            )

            footer_text = (
                f"{organization_name} - {system_name}"
            )

            canvas.setFont(
                "Helvetica",
                8
            )

            canvas.drawString(
                document.leftMargin,
                8 * mm,
                footer_text
            )

            page_text = (
                f"Generated: {generated}"
                f"    |    Page {doc.page}"
            )

            canvas.drawRightString(
                page_size[0]
                - document.rightMargin,
                8 * mm,
                page_text
            )

            canvas.restoreState()

        # -------------------------------------------------
        # Create PDF
        # -------------------------------------------------

        document.build(
            elements,
            onFirstPage=draw_footer,
            onLaterPages=draw_footer
        )

    @staticmethod
    def export_vehicle_logbook_to_pdf(
        records,
        file_path,
        asset_text,
        from_date,
        to_date,
    ):

        page_size = landscape(A4)

        document = SimpleDocTemplate(
            file_path,
            pagesize=page_size,
            rightMargin=10 * mm,
            leftMargin=10 * mm,
            topMargin=12 * mm,
            bottomMargin=18 * mm,
        )

        styles = getSampleStyleSheet()
        elements = []

        # -------------------------------------------------
        # Title
        #--------------------------------------------------

        elements.append(
            Paragraph(
                "<b>Vehicle Logbook</b>",
                styles["Title"]
            )
        )

        # -------------------------------------------------
        # Vehicle
        # -------------------------------------------------
        
        elements.append(
            Spacer(1, 2 * mm)
        )

        elements.append(
            Paragraph(
                f"<b>Vehicle:</b> {asset_text}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 1.5 * mm)
        )

        #---------------------------------------------------
        # Period
        # -------------------------------------------------

        elements.append(
            Paragraph(
                (
                    f"<b>Period:</b> "
                    f"{DateHelper.display(from_date)} "
                    f"to "
                    f"{DateHelper.display(to_date)}"
                ),
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 5 * mm)
        )

        # -------------------------------------------------
        # Column headings
        # -------------------------------------------------

        data = [[
            "Date",
            "Driver",
            "From",
            "To",
            "Start km",
            "End km",
            "Distance",
            "Purpose",
            "Defect / Fault",
            "Fuel",
            "Fuel Cost",
            "Notes",
        ]]

        total_distance = 0.0
        total_fuel = 0.0
        total_fuel_cost = 0.0

        body_style = styles["Normal"]
        body_style.fontSize = 6
        body_style.leading = 7

        #--------------------------------------------------
        # Logbook rows
        # -------------------------------------------------

        for record in records:

            distance = float(
                record["distance"] or 0
            )

            fuel = float(
                record["fuel_quantity"] or 0
            )

            fuel_cost = float(
                record["fuel_cost"] or 0
            )

            total_distance += distance
            total_fuel += fuel
            total_fuel_cost += fuel_cost

            data.append([
                DateHelper.display(
                    record["log_date"]
                ),
                Paragraph(
                    record["driver_name"] or "",
                    body_style
                ),
                Paragraph(
                    record["origin"] or "",
                    body_style
                ),
                Paragraph(
                    record["destination"] or "",
                    body_style
                ),
                f'{float(record["start_meter"] or 0):,.1f}',
                f'{float(record["end_meter"] or 0):,.1f}',
                f"{distance:,.1f}",
                Paragraph(
                    record["purpose"] or "",
                    body_style
                ),
                Paragraph(
                    record["defect_reported"] or "",
                    body_style
                ),
                f"{fuel:,.2f}",
                f"{fuel_cost:,.2f}",
                Paragraph(
                    record["notes"] or "",
                    body_style
                ),
            ])

        # -------------------------------------------------
        # Column widths
        #--------------------------------------------------

        available_width = (
            page_size[0]
            - document.leftMargin
            - document.rightMargin
        )

        column_weights = [
            8, # Date
            12, # Driver
            12, # From
            12, # To
            9, # Start km
            9, # End km
            8, # Distance
            13, # Purpose
            18, # Defect / Fault
            7, # Fuel
            8, # Fuel_cost
            14, # Notes
        ]

        total_weight = sum(
            column_weights
        )

        column_widths = [
            available_width
            * weight
            / total_weight
            for weight in column_weights
        ]

        #---------------------------------------------
        # Build table
        #---------------------------------------------

        pdf_table = Table(
            data,
            colWidths=column_widths,
            repeatRows=1
        )

        pdf_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#333333")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, 0),
                    "CENTER"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.grey
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    6
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F3F3F3")
                    ]
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    3
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    3
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
            ])
        )

        elements.append(
            pdf_table
        )

        #--------------------------------------------
        # Totals
        #--------------------------------------------

        elements.append(
            Spacer(1, 5 * mm)
        )

        totals_style = styles["Normal"]
        totals_style.fontSize = 8
        totals_style.leading = 10

        currency_symbol = (
            SettingsService.currency_symbol()
        )

        elements.append(
            Paragraph(
                (
                    f"<b>Total Distance:</b> "
                    f"{total_distance:,.1f} km"
                    f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                    f"<b>Total Fuel:</b> "
                    f"{total_fuel:,.2f}"
                    f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                    f"<b>Total Fuel Cost:</b> "
                    f"{currency_symbol} "
                    f"{total_fuel_cost:,.2f}"
                ),
                totals_style
            )
        )

        #--------------------------------------------------
        # Footer
        #--------------------------------------------------

        def draw_footer(canvas, doc):

            canvas.saveState()

            generated = datetime.now().strftime(
                "%d-%b-%y %H:%M"
            )

            organization_name = (
                SettingsService.organization_name()
            )

            system_name = (
                SettingsService.system_name()
            )

            footer_text = (
                f"{organization_name} - {system_name}"
            )

            canvas.setFont(
                "Helvetica",
                8
            )

            canvas.drawString(
                document.leftMargin,
                8 * mm,
                footer_text
            )

            canvas.drawRightString(
                page_size[0]
                -document.rightMargin,
                8 * mm,
                (
                    f"Generated: {generated}"
                    f"    |    Page {doc.page}"
                )
            )
            canvas.restoreState()

        #---------------------------------------------------
        # Create PDF
        #---------------------------------------------------

        document.build(
            elements,
            onFirstPage=draw_footer,
            onLaterPages=draw_footer
        )

