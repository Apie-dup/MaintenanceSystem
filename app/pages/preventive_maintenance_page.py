from app.base.crud_page import CrudPage
from app.dialogs.preventive_maintenance_dialog import (
    PreventiveMaintenanceDialog
)
from app.services.preventive_maintenance_service import (
    PreventiveMaintenanceService
)
from app.ui.generated.ui_preventive_maintenance_page import (
    Ui_PMWindow
)
from app.core.permissions import Permissions
from app.helpers.format_helper import FormatHelper
from app.helpers.theme_helper import ThemeHelper


class PreventiveMaintenancePage(CrudPage):

    PAGE_TITLE = "Preventive Maintenance"
    ENTITY_NAME = "PM Schedule"
    RECORD_NAME = "preventive maintenance schedules"

    TABLE_COLUMNS = [
        ("pm_number", "PM Number"),
        ("asset_number", "Asset Number"),
        ("asset_name", "Asset"),
        ("task", "Task"),
        ("frequency_type", "Frequency"),
        ("frequency_value", "Value"),
        ("last_service_date", "Last Service"),
        ("next_due_date", "Next Due"),
        ("last_service_meter", "Last Meter"),
        ("current_meter", "Current Meter"),
        ("next_due_meter", "Next Meter"),
        ("due_status", "Due Status"),
        ("priority", "Priority"),
        ("active_display", "Active"),
    ]

    SEARCH_FIELDS = [
        "pm_number",
        "asset_number",
        "asset_name",
        "task",
        "description",
        "frequency_type",
        "priority",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PMWindow()
        self.ui.setupUi(self)

        self.service = PreventiveMaintenanceService
        self.dialog_class = PreventiveMaintenanceDialog
        self.table = self.ui.tblPM
        self.search_widget = self.ui.txtSearch
        self.status_label = self.ui.lblStatus

        self.view_filter = None

        self.user = getattr(
            parent,
            "user",
            {}
        )

        self.role = self.user.get(
            "role",
            ""
        )

        self.setup_page()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_page(self):
        self.validate_configuration()
        self.setup_table()
        self.connect_signals()
        self.apply_permissions()
        self.load_data()

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "pm.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "pm.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "pm.delete"
        )

        can_generate = Permissions.has_permission(
            self.role,
            "pm.generate_work_order"
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

        self.ui.btnGenerateWorkOrder.setVisible(
            can_generate
        )



    # ---------------------------------------------------------
    # Data
    # ---------------------------------------------------------

    def load_data(self):

        records = self.service.get_all()

        records = self.apply_view_filter(
            records
        )

        self.populate_table(
            records
        )

        self.apply_due_status_colors()

    def show_due_filter(
        self,
        due_filter
    ):

        self.set_view_filter(
            due_filter
        )

        self.load_data()

    def set_view_filter(
        self,
        view_filter=None
    ):

        self.view_filter = view_filter

    def apply_view_filter(
        self,
        records
    ):

        status_map = {
            "today": "Due Today",
            "next7": "Due Soon",
            "overdue": "Overdue",
        }

        required_status = status_map.get(
            self.view_filter
        )

        if required_status is None:
            return records

        return [
            record
            for record in records
            if(
                record["due_status"] or ""
            ).strip() == required_status
        ]


    def show_all(self):

        self.set_view_filter(
            None
        )
        
        if self.search_widget is not None:
            self.search_widget.clear()

        self.load_data()

    def search(self, text):

        text = text.strip()

        if text:
            records = self.service.search(
                text
            )

        else:
            records = self.service.get_all()

        records = self.apply_view_filter(
            records
        )

        self.populate_table(
            records
        )

        self.apply_due_status_colors()

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

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

        self.ui.btnDelete.clicked.connect(
            self.delete_record
        )

        self.search_widget.textChanged.connect(
            self.search
        )

        self.ui.btnGenerateWorkOrder.clicked.connect(
            self.generate_work_order
        )

        self.table.itemDoubleClicked.connect(
            self.handle_double_click
        )

    # ---------------------------------------------------------
    # Highlighting
    # ---------------------------------------------------------

    def apply_due_status_colors(self):

        status_column = next(
            (
                index
                for index, (field, _heading)
                in enumerate(self.TABLE_COLUMNS)
                if field == "due_status"
            ),
            None,
        )

        if status_column is None:
            return

        for row in range(
            self.table.rowCount()
        ):

            status_item = self.table.item(
                row,
                status_column,
            )

            if status_item is None:
                continue

            status = (
                status_item.text().strip()
            )

            #--------------------------------------------------
            # Tooltip text
            #--------------------------------------------------

            if status == "Overdue":
                tooltip = (
                    "This preventive maintenance schedule "
                    "is overdue and requires attention."
                )

            elif status == "Due Today":
                tooltip = (
                    "This preventive maintenance schedule "
                    "is due today."
                )

            elif status == "Due Soon":
                tooltip = (
                    "This schedule is due within the next "
                    "seven days."
                )

            elif status == "Inactive":
                tooltip = "This schedule is inactive."

            else:
                continue

            #--------------------------------------------------
            # Theme-aware background
            #--------------------------------------------------

            background = ThemeHelper.status_color(
                self,
                status
            )
            if background is not None:
                status_item.setBackground(
                    background
                )

            status_item.setToolTip(
                tooltip
            )

    # ---------------------------------------------------------
    # Generate Work Order
    # ---------------------------------------------------------

    def generate_work_order(self):

        if not Permissions.has_permission(
            self.role,
            "pm.generate_work_order"
        ):
            self.warning(
                "Generate Work Order",
                "You do not have permission "
                "to generate Work Orders "
                "from PM schedules."
            )
            return

        pm_id = self.selected_id()

        if pm_id is None:
            self.warning(
                "Generate Work Order",
                "Please select a PM schedule."
            )
            return

        if not self.confirm(
            "Generate Work Order",
            (
                "Generate a new Work Order "
                "from the selected PM schedule?"
            )
        ):
            return

        try:
            work_order_id =(
                PreventiveMaintenanceService
                .generate_work_order(
                    pm_id,
                    user=self.user
                )
            )

        except ValueError as error:
            self.warning(
                "Generate Work Order",
                str(error)
            )
            return

        except Exception as error:
            self.error(
                "Generate Work Order",
                (
                    "Could not generate the work order."
                    f"\n\n{error}"
                ),
            )
            return

        self.information(
            "Generate Work Order",
            (
                "Work order generated successfully."
                f"\n\nRecord ID: {work_order_id}"
            ),
        )

        self.load_data()


    def handle_double_click(self, _item):
        record_id = self.selected_id()

        if record_id is None:
            return

        # Users with edit permissins
        if Permissions.has_permission(
            self.role,
            "pm.edit"
        ):
            self.edit_record()
            return

        # View-only users
        if Permissions.has_permission(
            self.role,
            "pm"
        ):
            dialog = self.dialog_class(
                parent=self
            )

            dialog.edit_record(
                record_id
            )

            if hasattr(
                dialog,
                "set_pm_read_only"
            ):
                dialog.set_pm_read_only(
                    True
                )

            dialog.exec()

    def add_record(self):
        if not Permissions.has_permission(
            self.role,
            "pm.create"
        ):
            self.warning(
                "Preventive Maintenance",
                "You do not have permission "
                "to add PM schedules."
            )
            return

        super().add_record()


    def edit_record(self):

        if not Permissions.has_permission(
            self.role,
            "pm.edit"
        ):
            self.warning(
                "Preventive Maintenance",
                "You do not have permission "
                "to edit PM schedules."
            )
            return

        super().edit_record()


    def delete_record(self):

        if not Permissions.has_permission(
            self.role,
            "pm.delete"
        ):
            self.warning(
                "Preventive Maintenance",
                "You do not have permission "
                "to delete PM schedules."
            )
            return

        super().delete_record()

    def populate_table(self, records):

        super().populate_table(records)

        meter_fields = {
            "last_service_meter",
            "next_due_meter"
        }

        meter_columns = [
            index
            for index, (field, _heading)
            in enumerate(self.TABLE_COLUMNS)
            if field in meter_fields
        ]

        for row in range(
            self.table.rowCount()
        ):

            for column in meter_columns:

                item = self.table.item(
                    row,
                    column,
                )

                if item is None:
                    continue

                text = item.text().strip()

                if not text:
                    continue

                try:

                    value = float(text)

                    item.setText(
                        FormatHelper.quantity(
                            value
                        )
                    )

                except ValueError:
                    continue