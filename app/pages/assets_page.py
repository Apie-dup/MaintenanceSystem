from app.base.crud_page import CrudPage
from app.dialogs.asset_dialog import AssetDialog
from app.services.asset_service import AssetService
from app.ui.generated.ui_assets_page import Ui_AssetsWindow
from app.helpers.format_helper import FormatHelper
from app.core.permissions import Permissions
from app.helpers.table_helper import TableHelper
from app.dialogs.asset_meter_reading_dialog import AssetMeterReadingDialog
from app.dialogs.asset_history_dialog import(
    AssetHistoryDialog
)
from app.dialogs.asset_documents_dialog import (
    AssetDocumentsDialog
)


class AssetsPage(CrudPage):

    PAGE_TITLE = "Assets"
    ENTITY_NAME = "Asset"
    RECORD_NAME = "assets"

    TABLE_COLUMNS = [
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset Name"),
        ("description", "Description"),
        ("category", "Category"),
        ("location", "Location"),
        ("manufacturer", "Manufacturer"),
        ("model", "Model"),
        ("serial_number", "Serial Number"),
        ("purchase_date", "Purchase Date"),
        ("purchase_cost", "Purchase Cost"),
        ("warranty_expiry", "Warranty Expiry"),
        ("status", "Status"),
        ("notes", "Notes"),
    ]

    SEARCH_FIELDS = [
        "asset_number",
        "asset_name",
        "description",
        "category",
        "location",
        "manufacturer",
        "model",
        "serial_number",
        "status",
        "notes",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.service = AssetService
        self.dialog_class = AssetDialog
        self.table = self.ui.tblAssets
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.user = getattr(parent, "user", {})
        self.role = self.user.get("role", "")

        self.main_controller = parent

        self.setup_page()

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.apply_permissions()
        self.load_data()

    def connect_signals(self):
        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.btnAdd.clicked.connect(
            self.add_record
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_record
        )

        self.ui.btnHistory.clicked.connect(
            self.open_history
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.ui.btnMeterReadings.clicked.connect(
            self.open_meter_readings
        )

        self.search_widget.textChanged.connect(
            self.search
        )

        self.table.itemDoubleClicked.connect(
            self.handle_double_click
        )

        self.ui.btnDocuments.clicked.connect(
            self.open_documents
        )

    def handle_double_click(self, _item):

        record_id = TableHelper.selected_id(
            self.table
        )

        if record_id is None:
            return

        # Users with edit permissions
        if Permissions.has_permission(
            self.role,
            "assets.edit"
        ):
            self.edit_record()
            return

        # View-only users
        if Permissions.has_permission(
            self.role,
            "assets"
        ):

            dialog = self.dialog_class(
                parent=self
            )

            dialog.edit_record(
                record_id,
            )

            if hasattr(
                dialog,
                "set_asset_read_only"
            ):
                dialog.set_asset_read_only(
                    True
                )

            dialog.exec()
            

    def add_record(self):

        if not Permissions.has_permission(
            self.role,
            "assets.create"
        ):
            self.warning(
                "Assets",
                "You do not have permission "
                "to add assets."
            )
            return

        super().add_record()


    def edit_record(self):

        if not Permissions.has_permission(
            self.role,
            "assets.edit"
        ):
            self.warning(
                "Assets",
                "You do not have permission "
                "to edit assets."
            )
            return

        super().edit_record()


    def delete_record(self):

        if not Permissions.has_permission(
            self.role,
            "assets.delete"
        ):
            self.warning(
                "Assets",
                "You do not have permission "
                "to delete assets."
            )
            return

        super().delete_record()

    def populate_table(self, records):

        super().populate_table(records)

        purchase_cost_column_index = next(
            (
                index
                for index, (field, _header) in enumerate(
                    self.TABLE_COLUMNS
                )
                if field == "purchase_cost"
            ),
            None,
        )

        if purchase_cost_column_index is None:
            return

        for row in range(self.table.rowCount()):
            item = self.table.item(
                row,
                purchase_cost_column_index
            )

            if item is None:
                continue

            try:
                value = float(
                    item.text() or 0
                )

                item.setText(
                    FormatHelper.currency(
                    value
                    )
                )

            except ValueError:
                pass

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "assets.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "assets.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "assets.delete"
        )

        can_view_meter_readings = Permissions.has_permission(
            self.role,
            "asset_meter_readings"
        )

        self.ui.btnAdd.setVisible(
            can_create
        )

        self.ui.btnEdit.setVisible(
            can_edit
        )

        self.ui.btnDelete.setVisible(
            can_delete
        )

        self.ui.btnMeterReadings.setVisible(
            can_view_meter_readings
        )

        can_view_documents = Permissions.has_permission(
            self.role,
            "asset_documents"
        )

        self.ui.btnDocuments.setVisible(
            can_view_documents
        )

    def open_meter_readings(self):

        record_id = TableHelper.selected_id(
            self.table
        )

        if record_id is None:
            self.warning(
                "Meter Readings",
                "Please select an asset."
            )
            return

        dialog = AssetMeterReadingDialog(
            asset_id=record_id,
            user=self.user,
            parent=self,
        )

        dialog.reading_recorded.connect(
            self.handle_meter_reading_recorded
        )

        dialog.exec()

    def handle_meter_reading_recorded(
        self,
        asset_id,
    ):
        if self.main_controller is None:
            return

        self.main_controller.refresh_after_meter_reading(
            asset_id
        )

    def open_history(self):

        record_id = self.require_selection()

        if record_id is None:
            return

        dialog = AssetHistoryDialog(
            asset_id=record_id,
            parent=self,
        )

        dialog.exec()

    # ---------------------------------------------------------
    # Asset Documentation
    # ---------------------------------------------------------

    def open_documents(self):

        if not Permissions.has_permission(
            self.role,
            "asset_documents"
        ):
            self.warning(
                "Asset Documentation",
                "You do not have permission to view asset documents."
            )
            return

        record_id = self.require_selection()

        if record_id is None:
            return

        dialog = AssetDocumentsDialog(
            asset_id=record_id,
            user=self.user,
            parent=self,
        )

        dialog.exec()