from app.base.base_dialog import BaseDialog
from app.helpers.table_helper import TableHelper
from app.services.vehicle_sop_service import (
    VehicleSopService
)
from app.services.vehicle_sop_item_service import (
    VehicleSopItemService
)
from app.services.message_service import (
    MessageService
)
from app.dialogs.vehicle_sop_item_dialog import (
    VehicleSopItemDialog
)
from app.ui.generated.ui_vehicle_sop_checklist_dialog import (
    Ui_VehicleSopChecklistDialog
)


class VehicleSopChecklistDialog(BaseDialog):

    TABLE_COLUMNS = [
        ("sequence", "Seq."),
        ("check_description", "Check Description"),
        ("required", "Required"),
    ]

    def __init__(
        self,
        sop_id,
        parent=None,
    ):
        super().__init__(parent)

        self.ui = Ui_VehicleSopChecklistDialog()
        self.ui.setupUi(self)

        self.sop_id = sop_id

        self.configure_table()
        self.load_sop()
        self.load_items()
        self.connect_signals()

    def configure_table(self):

        TableHelper.setup(
            self.ui.tblChecklist,
            self.TABLE_COLUMNS
        )

    def connect_signals(self):

        self.ui.btnAdd.clicked.connect(
            self.add_item
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_item
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_item
        )

        self.ui.tblChecklist.itemDoubleClicked.connect(
            self.edit_item
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

        self.ui.buttonBox.accepted.connect(
            self.accept
        )

    def load_sop(self):

        sop = VehicleSopService.get_by_id(
            self.sop_id
        )

        if sop is None:
            MessageService.error(
                self,
                "Vehicle SOP Checklist",
                "Unable to load the selected Vehicle SOP."
            )
            self.reject()
            return

        self.setWindowTitle(
            f"Checklist - {sop['sop_number']}"
        )

        self.ui.lblSop.setText(
            (
                f"{sop['sop_number']} - "
                f"{sop['sop_name']}"
            )
        )

        self.ui.lblAsset.setText(
            (
                f"{sop['asset_number']} - "
                f"{sop['asset_name']}"
            )
        )

        self.ui.lblFrequency.setText(
            sop["frequency"] or ""
        )

    def load_items(self):

        records = (
            VehicleSopItemService.get_by_sop_id(
                self.sop_id
            )
        )

        display_records = []

        for record in records:

            item = dict(record)

            item["required"] = (
                "Yes"
                if item["required"]
                else "No"
            )

            display_records.append(item)

        TableHelper.populate(
            self.ui.tblChecklist,
            display_records,
            self.TABLE_COLUMNS
        )

    def selected_id(self):

        return TableHelper.selected_id(
            self.ui.tblChecklist
        )

    def require_selection(self):

        item_id = self.selected_id()

        if item_id is None:
            MessageService.warning(
                self,
                "Vehicle SOP Checklist",
                "Please select a checklist item."
            )
            return None

        return item_id

    def add_item(self):

        dialog = VehicleSopItemDialog(
            self.sop_id,
            self
        )

        dialog.new_record()

        if dialog.exec():
            self.load_items()

    def edit_item(self):

        item_id = self.require_selection()

        if item_id is None:
            return

        dialog = VehicleSopItemDialog(
            self.sop_id,
            self
        )

        dialog.edit_record(
            item_id
        )

        if dialog.exec():
            self.load_items()

    def delete_item(self):

        item_id = self.require_selection()

        if item_id is None:
            return

        confirmed = MessageService.confirm(
            self,
            "Delete Checklist Item",
            (
                "Are you sure you want to delete "
                "the selected checklist item?"
            )
        )

        if not confirmed:
            return

        try:

            VehicleSopItemService.delete(
                item_id
            )

            self.load_items()

        except Exception as error:

            MessageService.error(
                self,
                "Vehicle SOP Checklist",
                (
                    "Unable to delete checklist item."
                    f"\n\n{error}"
                )
            )