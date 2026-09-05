from PySide6.QtWidgets import (
    QDialog,
    QHeaderView,
    QTableWidgetItem,
)

from PySide6.QtCore import Qt

from app.services.asset_history_service import (
    AssetHistoryService
)
from app.services.asset_service import (
    AssetService
)
from app.ui.generated.ui_asset_history_dialog import (
    Ui_AssetHistoryDialog
)
from app.dialogs.work_order_dialog import (
    WorkOrderDialog
)

from app.dialogs.preventive_maintenance_dialog import (
    PreventiveMaintenanceDialog
)

from app.dialogs.vehicle_logbook_dialog import (
    VehicleLogbookDialog
)


class AssetHistoryDialog(QDialog):

    def __init__(
        self,
        asset_id,
        parent=None,
    ):
        super().__init__(parent)

        self.asset_id = asset_id

        self.ui = Ui_AssetHistoryDialog()
        self.ui.setupUi(self)

        self.configure_table()
        self.connect_signals()

        self.load_asset()
        self.load_history()

    def configure_table(self):

        self.ui.tblHistory.setColumnCount(6)

        self.ui.tblHistory.setHorizontalHeaderLabels([
            "Date",
            "Type",
            "Reference",
            "Description",
            "Status",
            "Meter",
        ])

        self.ui.tblHistory.setSelectionBehavior(
            self.ui.tblHistory.SelectionBehavior.SelectRows
        )

        self.ui.tblHistory.setEditTriggers(
            self.ui.tblHistory.EditTrigger.NoEditTriggers
        )

        header = (
            self.ui.tblHistory.horizontalHeader()
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            5,
            QHeaderView.ResizeMode.ResizeToContents
        )

    def connect_signals(self):

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.tblHistory.itemDoubleClicked.connect(
            self.open_source_record
        )

    def load_asset(self):

        asset = AssetService.get_by_id(
            self.asset_id
        )

        if asset is None:
            self.ui.lblAsset.setText(
                "Asset: Unknown"
            )
            return

        self.ui.lblAsset.setText(
            (
                f"Asset: {asset['asset_number']} - "
                f"{asset['asset_name']}"
            )
        )

    def load_history(self):

        records = (
            AssetHistoryService.get_history(
                self.asset_id
            )
        )

        self.ui.tblHistory.setRowCount(
            len(records)
        )

        for row, record in enumerate(records):

            meter = record["meter"]

            if meter is None:
                meter_text = ""
            else:
                meter_text = (
                    f"{float(meter):,.2f}"
                )

            values = [
                record["event_date"] or "",
                record["event_type"] or "",
                record["reference"] or "",
                record["description"] or "",
                record["status"] or "",
                meter_text,
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(
                    str(value)
                )

                self.ui.tblHistory.setItem(
                    row,
                    column,
                    item
                )

            first_item = (
                self.ui.tblHistory.item(
                    row,
                    0
                )
            )

            if first_item is not None:

                first_item.setData(
                    Qt.ItemDataRole.UserRole,
                    {
                        "source_type":
                            record["source_type"],

                        "source_id":
                            record["source_id"],
                    }
                )

    def open_source_record(self, item):

        row = item.row()

        first_item = self.ui.tblHistory.item(
            row,
            0
        )

        if first_item is None:
            return

        source_data = first_item.data(
            Qt.ItemDataRole.UserRole
        )

        if not source_data:
            return

        source_type = source_data.get(
            "source_type"
        )

        source_id = source_data.get(
            "source_id"
        )

        if source_id is None:
            return

        #-----------------------------------------------
        # Work Order
        #-----------------------------------------------

        if source_type == "work_order":

            dialog = WorkOrderDialog(
                self
            )

            dialog.edit_record(
                source_id
            )

            dialog.exec()

            self.load_history()
            return

        #-----------------------------------------------
        # Preventive Maintenance
        #-----------------------------------------------

        if source_type == "pm":

            dialog = PreventiveMaintenanceDialog(
                self
            )

            dialog.edit_record(
                source_id
            )

            dialog.exec()

            self.load_history()
            return

        #-----------------------------------------------
        # Vehicle Logbook
        #-----------------------------------------------

        if source_type == "vehicle_logbook":

            dialog = VehicleLogbookDialog(
                self
            )

            dialog.edit_record(
                source_id
            )

            dialog.exec()

            self.load_history()
            return

        #-----------------------------------------------
        # Meter Reading
        #-----------------------------------------------

        if source_type == "meter_reading":
            return
