from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView
)


class BasePage(QWidget):

    def __init__(self):
        super().__init__()

    # -------------------------------------------------
    # Configure Table
    # -------------------------------------------------

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

        table.horizontalHeader().setStretchLastSection(True)

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    # -------------------------------------------------
    # Populate Table
    # -------------------------------------------------

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

                item = QTableWidgetItem(str(value))

                table.setItem(
                    row,
                    column,
                    item
                )

        if table.columnCount() > 0:
            table.setColumnHidden(0, True)

        table.setSortingEnabled(True)

        if status_label:

            count = len(records)

            if count == 1:
                status_label.setText(
                    f"Showing 1 {record_name[:-1]}"
                )
            else:
                status_label.setText(
                    f"Showing {count} {record_name}"
                )

    # -------------------------------------------------
    # Selected Record ID
    # -------------------------------------------------

    def selected_id(self, table):

        row = table.currentRow()

        if row < 0:
            return None

        item = table.item(row, 0)

        if item is None:
            return None

        return int(item.text())

    # -------------------------------------------------
    # Confirmation Dialog
    # -------------------------------------------------

    def confirm_delete(
        self,
        title,
        message
    ):

        return QMessageBox.question(
            self,
            title,
            message,
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        ) == QMessageBox.StandardButton.Yes

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    def information(
        self,
        title,
        message
    ):

        QMessageBox.information(
            self,
            title,
            message
        )

    # -------------------------------------------------
    # Warning
    # -------------------------------------------------

    def warning(
        self,
        title,
        message
    ):

        QMessageBox.warning(
            self,
            title,
            message
        )

    # -------------------------------------------------
    # Error
    # -------------------------------------------------

    def error(
        self,
        title,
        message
    ):

        QMessageBox.critical(
            self,
            title,
            message
        )

    # -------------------------------------------------
    # Refresh
    # -------------------------------------------------

    def refresh(self):
        """
        Override this in each page.
        """
        pass

    def selected_row(self, table):

        row = table.currentRow()

        if row < 0:
            return None

        values = []

        for column in range(table.columnCount()):

            item = table.item(row, column)

            values.append("" if item is None else item.text())

        return values
    
    def selected_id(self, table):

        row = self.selected_row(table)

        if row is None:
            return None

        return int(row[0])
    
    def selected_value(
        self,
        table,
        column
    ):

        row = self.selected_row(table)

        if row is None:
            return None

        return row[column]
    
    def has_selection(self, table):

        return table.currentRow() >= 0
    
    def clear_table(self, table):

        table.setRowCount(0)

    def set_status(
        self,
        label,
        message
    ):

        if label:
            label.setText(message)