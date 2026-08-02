from app.base.base_dialog import BaseDialog
from app.services.work_order_parts_service import WorkOrderPartService
from app.services.validation_service import ValidationService
from app.ui.generated.ui_issue_part import Ui_IssuePartDialog


class IssuePartDialog(BaseDialog):

    ENTITY_NAME = "Issue Part"

    def __init__(self, work_order_id, parent=None):
        super().__init__(parent)

        self.work_order_id = work_order_id

        self.ui = Ui_IssuePartDialog()
        self.ui.setupUi(self)

        self.parts = []

        self.setup_dialog()

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------

    def setup_dialog(self):
        self.load_parts()
        self.connect_signals()

        self.ui.txtAvailable.setReadOnly(True)
        self.ui.txtUnitCost.setReadOnly(True)
        self.ui.txtTotalCost.setReadOnly(True)

        self.ui.spnQuantity.setDecimals(2)
        self.ui.spnQuantity.setMinimum(0.01)
        self.ui.spnQuantity.setMaximum(999999.00)
        self.ui.spnQuantity.setValue(1.00)

        self.update_part_details()

    def connect_signals(self):
        self.ui.cmbPart.currentIndexChanged.connect(
            self.update_part_details
        )

        self.ui.spnQuantity.valueChanged.connect(
            self.update_total_cost
        )

        self.ui.buttonBox.accepted.connect(
            self.save_and_close
        )

        self.ui.buttonBox.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Load inventory
    # ---------------------------------------------------------

    def load_parts(self):
        self.ui.cmbPart.clear()

        self.parts = WorkOrderPartService.inventory_lookup()

        for part in self.parts:
            display_text = (
                f'{part["part_number"]} - '
                f'{part["part_name"]}'
            )

            self.ui.cmbPart.addItem(
                display_text,
                part["id"]
            )

    # ---------------------------------------------------------
    # Selected part
    # ---------------------------------------------------------

    def selected_part(self):
        inventory_id = self.ui.cmbPart.currentData()

        for part in self.parts:
            if part["id"] == inventory_id:
                return part

        return None

    # ---------------------------------------------------------
    # Update display
    # ---------------------------------------------------------

    def update_part_details(self):
        part = self.selected_part()

        if part is None:
            self.ui.txtAvailable.clear()
            self.ui.txtUnitCost.clear()
            self.ui.txtTotalCost.clear()
            return

        available = float(part["quantity"] or 0)
        unit_cost = float(part["unit_cost"] or 0)

        self.ui.txtAvailable.setText(
            f"{available:g}"
        )

        self.ui.txtUnitCost.setText(
            f"N$ {unit_cost:,.2f}"
        )

        self.ui.spnQuantity.setMaximum(
            max(0.01, available)
        )

        if available > 0:
            self.ui.spnQuantity.setValue(
                min(
                    max(self.ui.spnQuantity.value(), 0.01),
                    available
                )
            )

        self.update_total_cost()

    def update_total_cost(self):
        part = self.selected_part()

        if part is None:
            self.ui.txtTotalCost.clear()
            return

        quantity = self.ui.spnQuantity.value()
        unit_cost = float(part["unit_cost"] or 0)

        total = quantity * unit_cost

        self.ui.txtTotalCost.setText(
            f"N$ {total:,.2f}"
        )

    # ---------------------------------------------------------
    # BaseDialog methods
    # ---------------------------------------------------------

    def clear_fields(self):
        self.ui.cmbPart.setCurrentIndex(0)
        self.ui.spnQuantity.setValue(1.00)
        self.ui.txtNotes.clear()

        self.update_part_details()

    def get_form_data(self):
        return {
            "work_order_id": self.work_order_id,
            "inventory_id": self.ui.cmbPart.currentData(),
            "quantity": self.ui.spnQuantity.value(),
            "notes": self.ui.txtNotes.toPlainText().strip(),
        }

    def set_form_data(self, data):
        inventory_index = self.ui.cmbPart.findData(
            data["inventory_id"]
        )

        if inventory_index >= 0:
            self.ui.cmbPart.setCurrentIndex(
                inventory_index
            )

        self.ui.spnQuantity.setValue(
            float(data["quantity"] or 1)
        )

        self.ui.txtNotes.setPlainText(
            data["notes"] or ""
        )

    def load_record(self, record_id):
        raise NotImplementedError(
            "Issued parts are not edited. Remove and reissue instead."
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self):
        data = self.get_form_data()

        if data["inventory_id"] is None:
            self.warning(
                "Validation",
                "Please select an inventory item."
            )
            self.ui.cmbPart.setFocus()
            return False

        if not ValidationService.check(
            self,
            ValidationService.positive_number(
                data["quantity"],
                "Quantity"
            )
        ):
            self.ui.spnQuantity.setFocus()
            return False

        part = self.selected_part()

        if part is None:
            self.warning(
                "Validation",
                "The selected inventory item could not be found."
            )
            return False

        available = float(part["quantity"] or 0)

        if data["quantity"] > available:
            self.warning(
                "Validation",
                f"Only {available:g} is available."
            )
            self.ui.spnQuantity.setFocus()
            return False

        return True

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(self):
        WorkOrderPartService.issue_part(
            self.get_form_data()
        )
