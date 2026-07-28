from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)


class TableHelper:

    @staticmethod
    def setup(table, columns):

        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(
            [header for _, header in columns]
        )

        table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStrechLastSection(True)

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContants
        )

    @staticmethod
    def populate(table, rows, columns, id_field="id"):

        table.setRowCount(0)

        for record in rows:

            row = table.rowCount()
            table.insertRow(row)

            for column, (field, _) in enumerate(columns):

                value = record[field]

                if value is None:
                    value = ""

                item = QTableWidgetItem(str(value))

                if column == 0:
                    item.setData(
                        Qt.UserRole,
                        record[id_field]
                    )

                    table.setItem(
                        row,
                        column,
                        item
                    )


