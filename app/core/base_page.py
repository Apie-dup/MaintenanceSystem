from PySide6.QtWidgets import (
    QWidget,
    QAbstractItemView,
    QTableWidgetItem,
    QHeaderView
)


class BasePage(QWidget):

    def __init__(self):
        super().__init__()

    # --------------------------------------------------
    # Configure a table
    # --------------------------------------------------

    def configure_table(self, table):

        table.setAlternatingRowColors(True)

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table.setSortingEnabled(True)

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    # --------------------------------------------------
    # Populate a table
    # --------------------------------------------------

    def populate_table(
        self,
        table,
        records,
        status_label=None,
        record_name="records"
    ):

        table.setSortingEnabled(False)
        table.setRowCount(len(records))

        for row, record in enumerate(records):

            for column, value in enumerate(record):

                if value is None:
                    value = ""

                table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        table.setColumnHidden(0, True)
        table.setSortingEnabled(True)

        if status_label:
            status_label.setText(
                f"Showing {len(records)} {record_name}"
            )

    # --------------------------------------------------
    # Return selected ID
    # --------------------------------------------------

    def selected_id(self, table):

        row = table.currentRow()

        if row < 0:
            return None

        return int(table.item(row, 0).text())