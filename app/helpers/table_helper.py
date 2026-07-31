from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidgetItem
)


class TableHelper:

    # ---------------------------------------------------------
    # SETUP TABLE
    # ---------------------------------------------------------
    @staticmethod
    def setup(table, columns):

        headers = [
            header
            for field_name, header in columns
        ]

        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(headers)

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table.setAlternatingRowColors(True)

        table.verticalHeader().setVisible(False)

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        table.horizontalHeader().setStretchLastSection(True)

        table.setSortingEnabled(True)

    @staticmethod
    def setup_table(table, columns):

        TableHelper.setup(table, columns)

    # ---------------------------------------------------------
    # POPULATE TABLE
    # ---------------------------------------------------------
    @staticmethod
    def populate(table, records, columns, id_field="id"):

        sorting_enabled = table.isSortingEnabled()

        table.setSortingEnabled(False)
        table.setRowCount(0)

        for row_index, record in enumerate(records):

            table.insertRow(row_index)

            for column_index, column in enumerate(columns):

                field_name = column[0]

                value = TableHelper.get_record_value(
                    record,
                    field_name
                )

                display_value = (
                    ""
                    if value is None
                    else str(value)
                )

                item = QTableWidgetItem(display_value)

                if column_index == 0:

                    record_id = TableHelper.get_record_value(
                        record,
                        id_field
                    )

                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        record_id
                    )

                table.setItem(
                    row_index,
                    column_index,
                    item
                )

        table.setSortingEnabled(sorting_enabled)

        if sorting_enabled:
            table.sortItems(
            0,
            Qt.SortOrder.AscendingOrder
        )

        if table.rowCount() > 0:
            table.selectRow(0)

    @staticmethod
    def populate_table(table, records, columns, id_field="id"):

        TableHelper.populate(
            table,
            records,
            columns,
            id_field
        )

    # ---------------------------------------------------------
    # GET SELECTED RECORD ID
    # ---------------------------------------------------------
    @staticmethod
    def selected_id(table):

        if table is None:
            return None

        row = table.currentRow()

        if row < 0:
            return None

        item = table.item(row, 0)

        if item is None:
            return None

        return item.data(
            Qt.ItemDataRole.UserRole
        )

    # ---------------------------------------------------------
    # GET SELECTED ROW VALUES
    # ---------------------------------------------------------
    @staticmethod
    def selected_row(table):

        if table is None:
            return None

        row_index = table.currentRow()

        if row_index < 0:
            return None

        row_values = []

        for column_index in range(
            table.columnCount()
        ):

            item = table.item(
                row_index,
                column_index
            )

            if item is None:
                row_values.append("")
            else:
                row_values.append(item.text())

        return row_values

    # ---------------------------------------------------------
    # GET VALUE FROM RECORD
    # ---------------------------------------------------------
    @staticmethod
    def get_record_value(record, field_name):

        if record is None:
            return None

        try:
            return record[field_name]

        except (KeyError, IndexError, TypeError):
            return getattr(
                record,
                field_name,
                None
            )