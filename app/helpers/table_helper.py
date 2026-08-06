from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidgetItem,
)


class TableHelper:
    """
    Shared setup and population logic for QTableWidget controls.
    """

    ROW_HEIGHT = 32

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    @classmethod
    def setup(
        cls,
        table,
        columns,
        stretch_last=True,
        sorting=True,
    ):
        table.setColumnCount(len(columns))

        table.setHorizontalHeaderLabels(
            [heading for _field, heading in columns]
        )

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
        table.setSortingEnabled(sorting)
        table.setWordWrap(False)

        table.verticalHeader().setVisible(False)
        table.verticalHeader().setDefaultSectionSize(
            cls.ROW_HEIGHT
        )

        header = table.horizontalHeader()

        header.setSectionsClickable(True)
        header.setStretchLastSection(stretch_last)

        for column in range(len(columns)):
            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeMode.ResizeToContents
            )

        if stretch_last and columns:
            header.setSectionResizeMode(
                len(columns) - 1,
                QHeaderView.ResizeMode.Stretch
            )

    # ---------------------------------------------------------
    # Populate
    # ---------------------------------------------------------

    @staticmethod
    def populate(table, records, columns):
        sorting_enabled = table.isSortingEnabled()

        table.setSortingEnabled(False)
        table.setRowCount(0)

        for record in records:
            row = table.rowCount()
            table.insertRow(row)

            record_id = record["id"]

            for column, (field_name, _heading) in enumerate(columns):
                value = record[field_name]

                item = QTableWidgetItem(
                    "" if value is None else str(value)
                )

                if column == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        record_id
                    )

                table.setItem(
                    row,
                    column,
                    item
                )

        table.setSortingEnabled(sorting_enabled)
        table.clearSelection()

    # ---------------------------------------------------------
    # Selected ID
    # ---------------------------------------------------------

    @staticmethod
    def selected_id(table):
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
    # Selected row
    # ---------------------------------------------------------

    @staticmethod
    def selected_row(table):
        row = table.currentRow()

        if row < 0:
            return None

        return [
            table.item(row, column).text()
            if table.item(row, column) is not None
            else ""
            for column in range(table.columnCount())
        ]

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------

    @staticmethod
    def clear(table):
        table.setRowCount(0)
        table.clearSelection()