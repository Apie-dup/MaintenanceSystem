from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from xml.sax.saxutils import escape
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
            "Inventory Transactions",
            "Asset Maintenance History",
            "Technician Work History",
             "Purchase Orders",
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

        notes_column = next(
            (
                index
                for index, heading in enumerate(
                    headings
                )
                if heading == "Notes"
            ),
            None
        )

        body_cell_style = ParagraphStyle(
            "ReportBodyCell",
            parent=styles["Normal"],
            fontSize=6,
            leading=7,
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

                text = (
                    item.text()
                    if item is not None
                    else ""
                )

                if (
                    notes_column is not None
                    and column == notes_column
                ):

                    row_data.append(
                        Paragraph(
                            escape(text),
                            body_cell_style
                        )
                    )

                else:

                    row_data.append(
                        text
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

            # -------------------------------------------------
            # Notes needs extra width because it may contain
            # longer descriptive text.
            # -------------------------------------------------

            if (
                notes_column is not None
                and column == notes_column
            ):
                column_weights.append(50)
                continue

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
            "Start Hrs",
            "End Hrs",
            "Hours Used",
            "Purpose",
            "Defect / Fault",
            "Fuel",
            "Fuel Cost",
            "Notes",
        ]]

        total_distance = 0.0
        total_hours = 0.0
        total_fuel = 0.0
        total_fuel_cost = 0.0

        body_style = ParagraphStyle(
            "VehicleLogbookBody",
            parent=styles["Normal"],
            fontSize=6,
            leading=7,
        )

        #--------------------------------------------------
        # Logbook rows
        # -------------------------------------------------

        for record in records:

            distance = float(
                record["distance"] or 0
            )

            hours_used = float(
                record["hours_used"] or 0
            )

            fuel = float(
                record["fuel_quantity"] or 0
            )

            fuel_cost = float(
                record["fuel_cost"] or 0
            )

            total_distance += distance
            total_hours += hours_used
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
                f'{float(record["start_hours"] or 0):,.1f}',
                f'{float(record["end_hours"] or 0):,.1f}',
                f"{hours_used:,.1f}",

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
            7,   # Date
            10,  # Driver
            9,   # From
            9,   # To
            7,   # Start km
            7,   # End km
            6,   # Distance
            7,   # Start Hrs
            7,   # End Hrs
            7,   # Hours Used
            11,  # Purpose
            14,  # Defect / Fault
            6,   # Fuel
            7,   # Fuel Cost
            11,  # Notes
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

        totals_style = ParagraphStyle(
            "VehicleLogbookTotals",
            parent=styles["Normal"],
            fontSize=8,
            leading=10,
        )

        currency_symbol = (
            SettingsService.currency_symbol()
        )

        elements.append(
            Paragraph(
                (
                    f"<b>Total Distance:</b> "
                    f"{total_distance:,.1f} km"
                    f"&nbsp;&nbsp;&nbsp;&nbsp;"
                    f"<b>Total Hours:</b> "
                    f"{total_hours:,.1f} hrs"
                    f"&nbsp;&nbsp;&nbsp;&nbsp;"
                    f"<b>Total Fuel:</b> "
                    f"{total_fuel:,.2f}"
                    f"&nbsp;&nbsp;&nbsp;&nbsp;"
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

    @staticmethod
    def export_sop_inspection_form_to_pdf(
        sop,
        items,
        file_path,
    ):

        page_size = A4

        document = SimpleDocTemplate(
            file_path,
            pagesize=page_size,
            rightMargin=15 * mm,
            leftMargin=15 * mm,
            topMargin=12 * mm,
            bottomMargin=18 * mm,
        )

        styles = getSampleStyleSheet()
        elements = []

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        organization_name = (
            SettingsService.organization_name()
        )

        elements.append(
            Paragraph(
                f"<b>{escape(organization_name)}</b>",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 2 * mm)
        )

        elements.append(
            Paragraph(
                "<b>VEHICLE / EQUIPMENT INSPECTION</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1, 5 * mm)
        )

        # -------------------------------------------------
        # SOP details
        # -------------------------------------------------

        details = [
            [
                "SOP No.",
                sop["sop_number"],
                "Frequency",
                sop["frequency"],
            ],
            [
                "SOP",
                sop["sop_name"],
                "",
                "",
            ],
            [
                "Asset",
                (
                    f'{sop["asset_number"]} - '
                    f'{sop["asset_name"]}'
                ),
                "",
                "",
            ],
        ]

        details_table = Table(
            details,
            colWidths=[
                25 * mm,
                75 * mm,
                25 * mm,
                50 * mm,
            ]
        )

        details_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, -1),
                    "Helvetica-Bold"
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
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

        elements.append(details_table)

        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Inspection details completed by operator
        # -------------------------------------------------

        operator_data = [
            [
                "Inspection Date:",
                "________________________",
                "Operator / Driver:",
                "____________________________",
            ],
            [
                "Meter Type:",
                "________________________",
                "Meter Reading:",
                "____________________________",
            ],
        ]

        operator_table = Table(
            operator_data,
            colWidths=[
                28 * mm,
                55 * mm,
                30 * mm,
                62 * mm,
            ]
        )

        operator_table.setStyle(
            TableStyle([
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    3
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
            ])
        )

        elements.append(operator_table)
        elements.append(Spacer(1, 4 * mm))

        # -------------------------------------------------
        # Checklist
        # -------------------------------------------------

        checklist_data = [[
            "No.",
            "Inspection Item",
            "Req.",
            "Pass",
            "Fail",
            "N/A",
            "Comments",
        ]]

        body_style = ParagraphStyle(
            "SopInspectionFormBody",
            parent=styles["Normal"],
            fontSize=8,
            leading=9,
        )

        for item in items:

            checklist_data.append([
                str(item["sequence"]),
                Paragraph(
                    escape(
                        item["check_description"]
                        or ""
                    ),
                    body_style
                ),
                "Yes" if item["required"] else "No",
                "",
                "",
                "",
                "",
            ])

        checklist_table = Table(
            checklist_data,
            colWidths=[
                9 * mm,    # No.
                61 * mm,   # Inspection Item
                12 * mm,   # Required
                12 * mm,   # Pass
                12 * mm,   # Fail
                12 * mm,   # N/A
                57 * mm,   # Comments
            ],
            repeatRows=1,
        )

        checklist_table.setStyle(
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
                    "ALIGN",
                    (0, 1),
                    (0, -1),
                    "CENTER"
                ),
                (
                    "ALIGN",
                    (2, 1),
                    (5, -1),
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
                    0.5,
                    colors.grey
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    8
                ),
                (
                    "TOPPADDING",
                    (0, 1),
                    (-1, -1),
                    5
                ),
                (
                    "BOTTOMPADDING",
                    (0, 1),
                    (-1, -1),
                    5
                ),
            ])
        )

        elements.append(checklist_table)
        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # General defects / comments
        # -------------------------------------------------

        elements.append(
            Paragraph(
                "<b>DEFECTS / GENERAL COMMENTS</b>",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 2 * mm)
        )

        comments_table = Table(
            [
                [""],
                [""],
                [""],
            ],
            colWidths=[175 * mm],
            rowHeights=[8 * mm, 8 * mm, 8 * mm],
        )

        comments_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
            ])
        )

        elements.append(comments_table)
        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Operator declaration
        # -------------------------------------------------

        declaration_style = ParagraphStyle(
            "SopInspectionDeclaration",
            parent=styles["Normal"],
            fontSize=8,
            leading=10,
        )

        elements.append(
            Paragraph(
                (
                    "I confirm that the above inspection was "
                    "performed and that the information recorded "
                    "on this form is correct."
                ),
                declaration_style
            )
        )

        elements.append(Spacer(1, 4 * mm))

        signature_table = Table(
            [[
                "Operator Signature:",
                "____________________________",
                "Date:",
                "__________________",
            ]],
            colWidths=[
                32 * mm,
                62 * mm,
                15 * mm,
                45 * mm,
            ],
        )

        signature_table.setStyle(
            TableStyle([
                (
                    "FONTNAME",
                    (0, 0),
                    (0, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
            ])
        )

        elements.append(signature_table)
        elements.append(Spacer(1, 6 * mm))

        # -------------------------------------------------
        # Maintenance follow-up
        # -------------------------------------------------

        elements.append(
            Paragraph(
                "<b>MAINTENANCE FOLLOW-UP</b>",
                styles["Normal"]
            )
        )
        elements.append(
            Spacer(1, 2 * mm)
        )

        follow_up_data = [
            [
                "Work Order No.:",
                "____________________________",
            ],
            [
                "Action / Comments:",
                "",
            ],
            [
                "",
                "",
            ],
        ]

        follow_up_table = Table(
            follow_up_data,
            colWidths=[
                38 * mm,
                137 * mm,
            ],
            rowHeights=[
                8 * mm,
                9 * mm,
                9 * mm,
            ],
        )

        follow_up_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, 1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),
            ])
        )

        elements.append(follow_up_table)

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
                f"Form generated: {generated}"
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
    def export_completed_sop_inspection_to_pdf(
        inspection,
        items,
        file_path,
    ):

        page_size = A4

        document = SimpleDocTemplate(
            file_path,
            pagesize=page_size,
            rightMargin=15 * mm,
            leftMargin=15 * mm,
            topMargin=12 * mm,
            bottomMargin=18 * mm,
        )

        styles = getSampleStyleSheet()
        elements = []

        organization_name = (
            SettingsService.organization_name()
        )

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        elements.append(
            Paragraph(
                f"<b>{escape(organization_name)}</b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 2 * mm))

        elements.append(
            Paragraph(
                "<b>COMPLETED VEHICLE / EQUIPMENT INSPECTION</b>",
                styles["Heading2"]
            )
        )

        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Inspection / SOP details
        # -------------------------------------------------

        asset_text = (
            f'{inspection["asset_number"]} - '
            f'{inspection["asset_name"]}'
        )

        details = [
            [
                "Inspection No.",
                inspection["inspection_number"],
                "Status",
                inspection["status"],
            ],
            [
                "Inspection Date",
                inspection["inspection_date"],
                "Frequency",
                inspection["frequency"],
            ],
            [
                "SOP No.",
                inspection["sop_number"],
                "SOP",
                inspection["sop_name"],
            ],
            [
                "Asset",
                asset_text,
                "",
                "",
            ],
            [
                "Operator",
                inspection["operator_name"] or "",
                "",
                "",
            ],
        ]

        details_table = Table(
            details,
            colWidths=[
                28 * mm,
                60 * mm,
                25 * mm,
                62 * mm,
            ]
        )

        details_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
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

        elements.append(details_table)
        elements.append(Spacer(1, 4 * mm))

        # -------------------------------------------------
        # Meter
        # -------------------------------------------------

        meter_type = (
            inspection["meter_type"]
            or ""
        )

        meter_reading = (
            ""
            if inspection["meter_reading"] is None
            else str(inspection["meter_reading"])
        )

        meter_table = Table(
            [[
                "Meter Type:",
                meter_type,
                "Meter Reading:",
                meter_reading,
            ]],
            colWidths=[
                25 * mm,
                60 * mm,
                28 * mm,
                62 * mm,
            ]
        )

        meter_table.setStyle(
            TableStyle([
                (
                    "FONTNAME",
                    (0, 0),
                    (0, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
            ])
        )

        elements.append(meter_table)
        elements.append(Spacer(1, 4 * mm))

        # -------------------------------------------------
        # Checklist
        # -------------------------------------------------

        checklist_data = [[
            "No.",
            "Inspection Item",
            "Req.",
            "Result",
            "Comments",
            "Work Order",
        ]]

        body_style = ParagraphStyle(
            "CompletedSopInspectionBody",
            parent=styles["Normal"],
            fontSize=8,
            leading=9,
        )

        for item in items:

            checklist_data.append([
                str(item["sequence"]),
                Paragraph(
                    escape(
                        item["check_description"]
                        or ""
                    ),
                    body_style
                ),
                (
                    "Yes"
                    if item["required"]
                    else "No"
                ),
                item["result"] or "",
                Paragraph(
                    escape(
                        item["comments"]
                        or ""
                    ),
                    body_style
                ),
                item["work_order_number"] or "",
            ])

        checklist_table = Table(
            checklist_data,
            colWidths=[
                9 * mm,
                55 * mm,
                12 * mm,
                18 * mm,
                56 * mm,
                25 * mm,
            ],
            repeatRows=1,
        )

        checklist_table.setStyle(
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
                    "ALIGN",
                    (0, 1),
                    (0, -1),
                    "CENTER"
                ),
                (
                    "ALIGN",
                    (2, 1),
                    (3, -1),
                    "CENTER"
                ),
                (
                    "ALIGN",
                    (5, 1),
                    (5, -1),
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
                    0.5,
                    colors.grey
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    8
                ),
                (
                    "TOPPADDING",
                    (0, 1),
                    (-1, -1),
                    4
                ),
                (
                    "BOTTOMPADDING",
                    (0, 1),
                    (-1, -1),
                    4
                ),
            ])
        )

        elements.append(checklist_table)
        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Inspection comments
        # -------------------------------------------------

        elements.append(
            Paragraph(
                "<b>INSPECTION COMMENTS</b>",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 2 * mm))

        comments = (
            inspection["comments"]
            or ""
        )

        comments_table = Table(
            [[
                Paragraph(
                    escape(comments),
                    body_style
                )
            ]],
            colWidths=[175 * mm],
            rowHeights=[18 * mm],
        )

        comments_table.setStyle(
            TableStyle([
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),
            ])
        )

        elements.append(comments_table)

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        def draw_footer(canvas, doc):

            canvas.saveState()

            generated = datetime.now().strftime(
                "%d-%b-%Y %H:%M"
            )

            system_name = (
                SettingsService.system_name()
            )

            canvas.setFont(
                "Helvetica",
                8
            )

            canvas.drawString(
                document.leftMargin,
                8 * mm,
                (
                    f"{organization_name} - "
                    f"{system_name}"
                )
            )

            canvas.drawRightString(
                page_size[0]
                - document.rightMargin,
                8 * mm,
                (
                    f"Printed: {generated}"
                    f"    |    Page {doc.page}"
                )
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
    def export_vehicle_logbook_form_to_pdf(
        asset,
        file_path,
    ):
        page_size = landscape(A4)

        document = SimpleDocTemplate(
            file_path,
            pagesize=page_size,
            rightMargin=10 * mm,
            leftMargin=10 * mm,
            topMargin=10 * mm,
            bottomMargin=15 * mm,
        )

        styles = getSampleStyleSheet()
        elements = []

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        organization_name = (
            SettingsService.organization_name()
        )

        elements.append(
            Paragraph(
                f"<b>{escape(organization_name)}</b>",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 2 * mm)
        )

        elements.append(
            Paragraph(
                "<b>VEHICLE / EQUIPMENT LOGBOOK</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1, 4 * mm)
        )

        # -------------------------------------------------
        # Asset / period details
        # -------------------------------------------------

        asset_number = (
            asset["asset_number"]
            if asset
            else ""
        )

        asset_name = (
            asset["asset_name"]
            if asset
            else ""
        )

        details = [
            [
                "Asset Number",
                asset_number,
                "Asset Name",
                asset_name,
            ],
            [
                "Period",
                "____________________________",
                "Sheet No.",
                "____________",
            ],
        ]

        details_table = Table(
            details,
            colWidths=[
                28 * mm,
                75 * mm,
                25 * mm,
                75 * mm,
            ]
        )

        details_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    4
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

        elements.append(details_table)
        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Blank logbook table
        # -------------------------------------------------

        headers = [
            "Date",
            "Driver /\nOperator",
            "Start\nKm",
            "End\nKm",
            "Km",
            "Start\nHrs",
            "End\nHrs",
            "Hrs",
            "From",
            "To",
            "Purpose",
            "Fuel\nQty",
            "Fuel\nCost",
            "Defect / Remarks",
        ]

        table_data = [headers]

        # Blank rows for manual entries.
        for _ in range(12):
            table_data.append(
                [""] * len(headers)
            )

        logbook_table = Table(
            table_data,
            colWidths=[
                16 * mm,   # Date
                24 * mm,   # Driver / Operator
                16 * mm,   # Start Km
                16 * mm,   # End Km
                13 * mm,   # Km
                16 * mm,   # Start Hrs
                16 * mm,   # End Hrs
                13 * mm,   # Hrs
                18 * mm,   # From
                18 * mm,   # To
                29 * mm,   # Purpose
                15 * mm,   # Fuel Qty
                17 * mm,   # Fuel Cost
                35 * mm,   # Defect / Remarks
            ],
            repeatRows=1,
            rowHeights=[
                10 * mm
            ] + [
                8 * mm
            ] * 12,
        )

        logbook_table.setStyle(
            TableStyle([
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    6.5
                ),
                (
                    "FONTSIZE",
                    (0, 1),
                    (-1, -1),
                    7
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
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    2
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    2
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    2
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    2
                ),
            ])
        )

        elements.append(logbook_table)
        elements.append(Spacer(1, 5 * mm))

        # -------------------------------------------------
        # Totals / authorization
        # -------------------------------------------------

        totals = [
            [
                "Total Kilometres",
                "____________________",
                "Total Running Hours",
                "____________________",
            ],
            [
                "Checked By",
                "____________________",
                "Signature",
                "____________________",
            ],
            [
                "Date",
                "____________________",
                "",
                "",
            ],
        ]

        totals_table = Table(
            totals,
            colWidths=[
                32 * mm,
                70 * mm,
                35 * mm,
                70 * mm,
            ]
        )

        totals_table.setStyle(
            TableStyle([
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (2, 0),
                    (2, 1),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),
            ])
        )

        elements.append(totals_table)

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        def draw_footer(canvas, doc):
            canvas.saveState()

            canvas.setFont(
                "Helvetica",
                7
            )

            canvas.drawCentredString(
                page_size[0] / 2,
                7 * mm,
                (
                    "Maintenance Management System"
                    f"    |    Page {doc.page}"
                )
            )

            canvas.restoreState()

        document.build(
            elements,
            onFirstPage=draw_footer,
            onLaterPages=draw_footer
        )