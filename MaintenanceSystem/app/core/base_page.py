from PySide6.QtWidgets import (
    QWidget,
    QAbstractItemView,
    QHeaderView,
    QTableWidgetItem,
    QMessageBox
)


class BasePage(QWidget):

    def __init__(self):
        super().__init__()

    def configure_table(self, table):

        table.setAlternatingRowColors(True)

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table.setSortingEnabled(True)

        table.horizontalHeader().setStretchLastSection(True)

    def populate_table(
            self,
            table,
            records,
            status_label=None,
            record_name="records"
    ):
            
            table.setRowCount(len(records))

            for row, records in enumerate(records):

                for column, value in enumerate(records):

                    if value is None:
                         value = ""

                    table.setItem(
                        row,
                        column,
                        QTableWidgetItem(str(value))
                    )

                table.setColumnHidden(0, True)

                table.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch
                )

                if status_label:

                    status_label.setText(
                        f"Showing {len(records)} {record_name}"
                    )

    def select_id(self, table):
            
            row = table.currentRow()

            if row < 0:
                return None
            
            return int(table.item(row, 0).text())
        
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