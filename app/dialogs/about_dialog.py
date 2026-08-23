from app.base.base_dialog import BaseDialog
from app.core.version import (
    APP_NAME,
    VERSION,
    BUILD,
    AUTHOR,
)
from app.database.migrations import MigrationManager
from app.services.settings_service import SettingsService
from app.ui.generated.ui_about_dialog import Ui_AboutDialog


class AboutDialog(BaseDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        self.setup_dialog()

    def setup_dialog(self):

        self.setWindowTitle(
            f"About {APP_NAME}"
        )

        self.ui.lblTitle.setText(
            SettingsService.system_name()
        )

        self.ui.lblOrganization.setText(
            SettingsService.organization_name()
        )

        self.ui.lblVersion.setText(
            f"Version: {VERSION}"
        )

        self.ui.lblBuild.setText(
            f"Build: {BUILD}"
        )

        self.ui.lblAuthor.setText(
            f"Author: {AUTHOR}"
        )

        database_version = (
            MigrationManager.get_database_version()
        )

        self.ui.lblDatabaseVersion.setText(
            f"Database Version: {database_version}"
        )

        self.ui.lblDescription.setText(
            "Maintenance and Asset Management System"
        )

        self.ui.btnClose.clicked.connect(
            self.accept
        )