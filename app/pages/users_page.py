from app.base.base_page import BasePage
from app.helpers.table_helper import TableHelper
from app.services.user_service import UserService
from app.dialogs.user_dialog import UserDialog
from app.ui.generated.ui_users_page import Ui_UsersPage


class UsersPage(BasePage):

    USER_COLUMNS = [
        ("username", "Username"),
        ("fullname", "Full Name"),
        ("role", "Role"),
        ("active", "Status"),
        ("created_at", "Created At"),
    ]

    def __init__(
        self,
        current_user,
        parent=None
    ):
        super().__init__(parent)

        self.current_user = current_user

        self.ui = Ui_UsersPage()
        self.ui.setupUi(self)

        self.records = []

        self.setup_page()

    # -------------------------------------------------
    # Setup
    # -------------------------------------------------

    def setup_page(self):

        TableHelper.setup(
            self.ui.tblUsers,
            self.USER_COLUMNS
        )

        self.connect_signals()

        self.load_data()

    def connect_signals(self):

        self.ui.txtSearch.textChanged.connect(
            self.search
        )

        self.ui.btnAdd.clicked.connect(
            self.add_user
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_user
        )

        self.ui.btnDeactivate.clicked.connect(
            self.toggle_active
        )

        self.ui.btnRefresh.clicked.connect(
            self.load_data
        )

        self.ui.tblUsers.itemDoubleClicked.connect(
            lambda _item: self.edit_user()
        )

    # -------------------------------------------------
    # Load
    # -------------------------------------------------

    def load_data(self):

        self.records = list(
            UserService.get_all()
        )

        self.populate_table(
            self.records
        )

        self.ui.lblStatus.setText(
            f"{len(self.records)} user(s)."
        )

    def populate_table(self, records):

        display_records = []

        for record in records:

            display_records.append({
                "id": record["id"],
                "username": record["username"],
                "fullname": record["fullname"],
                "role": record["role"],
                "active": (
                    "Active"
                    if record["active"]
                    else "Inactive"
                ),
                "created_at": record["created_at"],
            })

        TableHelper.populate(
            self.ui.tblUsers,
            display_records,
            self.USER_COLUMNS
        )

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(self):

        text = (
            self.ui.txtSearch
            .text()
            .strip()
            .lower()
        )

        if not text:
            self.populate_table(
                self.records
            )
            return

        filtered = []

        for record in self.records:

            values = (
                record["username"],
                record["fullname"],
                record["role"],
            )

            if any(
                text in str(value or "").lower()
                for value in values
            ):
                filtered.append(record)

        self.populate_table(
            filtered
        )

        self.ui.lblStatus.setText(
            f"{len(filtered)} user(s) found."
        )

    # -------------------------------------------------
    # Selection
    # -------------------------------------------------

    def selected_user_id(self):

        row = (
            self.ui.tblUsers.currentRow()
        )

        if row < 0:
            return None

        username_item = (
            self.ui.tblUsers.item(
                row,
                0
            )
        )

        if username_item is None:
            return None

        username = username_item.text()

        for record in self.records:
            if record["username"] == username:
                return record["id"]

        return None

    # -------------------------------------------------
    # Add
    # -------------------------------------------------

    def add_user(self):

        dialog = UserDialog(
            parent=self
        )

        dialog.new_record()

        if dialog.exec():
            self.load_data()

    # -------------------------------------------------
    # Edit
    # -------------------------------------------------

    def edit_user(self):

        record_id = (
            self.selected_user_id()
        )

        if record_id is None:
            self.warning(
                "User Management",
                "Please select a user."
            )
            return

        dialog = UserDialog(
            parent=self
        )

        dialog.edit_record(
            record_id
        )

        if dialog.exec():
            self.load_data()

    # -------------------------------------------------
    # Activate / Deactivate
    # -------------------------------------------------

    def toggle_active(self):

        record_id = (
            self.selected_user_id()
        )

        if record_id is None:
            self.warning(
                "User Management",
                "Please select a user."
            )
            return

        record = UserService.get_by_id(
            record_id
        )

        if record is None:
            return

        if (
            record_id == self.current_user["id"]
            and record["active"]
        ):
            self.warning(
                "User Management",
                "You cannot deactivate "
                "your own logged-in account."
            )
            return

        new_active = not bool(
            record["active"]
        )

        action = (
            "activate"
            if new_active
            else "deactivate"
        )

        if not self.confirm(
            "User Management",
            (
                f"Are you sure you want to "
                f"{action} user "
                f"'{record['username']}'?"
            )
        ):
            return

        try:

            UserService.set_active(
                record_id,
                new_active
            )

        except ValueError as error:
            self.warning(
                "User Management",
                str(error)
            )

            return

        self.load_data()