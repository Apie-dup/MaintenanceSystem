from PySide6.QtWidgets import QWidget, QMessageBox, QApplication

from app.services.settings_service import SettingsService
from app.ui.generated.ui_settings_page import Ui_SettingsPage
from app.core.theme import AppTheme


class SettingsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_window = parent

        self.ui = Ui_SettingsPage()
        self.ui.setupUi(self)

        self.setup_page()

    def setup_page(self):
        self.load_combo_values()
        self.connect_signals()
        self.load_settings()

    def load_combo_values(self):

        self.ui.cmbDateFormat.clear()
        self.ui.cmbDateFormat.addItems([
            "dd-MMM-yyyy",
            "dd/MM/yyyy",
            "yyyy-MM-dd",
            "MM/dd/yyyy",
        ])

        self.ui.cmbTheme.clear()
        self.ui.cmbTheme.addItems([
            "Light",
            "Dark",
        ])

    def connect_signals(self):

        self.ui.btnSave.clicked.connect(
            self.save_settings
        )

        self.ui.btnReload.clicked.connect(
            self.load_settings
        )

    def load_settings(self):

        self.ui.txtOrganizationName.setText(
            SettingsService.organization_name()
        )

        self.ui.txtSystemName.setText(
            SettingsService.system_name()
        )

        self.ui.txtCurrencySymbol.setText(
            SettingsService.currency_symbol()
        )

        self.ui.txtCurrencyCode.setText(
            SettingsService.currency_code()
        )

        self.ui.cmbDateFormat.setCurrentText(
            SettingsService.date_format()
        )

        theme = SettingsService.theme_mode().capitalize()

        self.ui.cmbTheme.setCurrentText(
            theme
        )

        self.ui.lblStatus.setText(
            "Settings loaded."
        )

    def save_settings(self):

        organization_name = (
            self.ui.txtOrganizationName
            .text()
            .strip()
        )

        system_name = (
            self.ui.txtSystemName
            .text()
            .strip()
        )

        currency_symbol = (
            self.ui.txtCurrencySymbol
            .text()
            .strip()
        )

        currency_code = (
            self.ui.txtCurrencyCode
            .text()
            .strip()
            .upper()
        )

        if len(currency_code) != 3:
                    QMessageBox.warning(
                        self,
                        "Settings",
                        "Currency Code must contain exactly 3 characters."
                    )
                    return
        

        date_format = (
            self.ui.cmbDateFormat
            .currentText()
        )

        theme_mode = (
            self.ui.cmbTheme
            .currentText()
            .lower()
        )

        if not organization_name:
            QMessageBox.warning(
                self,
                "Settings",
                "Organization Name is required."
            )
            return

        if not system_name:
            QMessageBox.warning(
                self,
                "Settings",
                "System Name is required."
            )
            return

        if not currency_symbol:
            QMessageBox.warning(
                self,
                "Settings",
                "Currency Symbol is required."
            )
            return

        SettingsService.set(
            "organization_name",
            organization_name
        )

        SettingsService.set(
            "system_name",
            system_name
        )

        SettingsService.set(
            "currency_symbol",
            currency_symbol
        )

        SettingsService.set(
            "currency_code",
            currency_code
        )

        SettingsService.set(
            "date_format",
            date_format
        )

        SettingsService.set(
            "theme_mode",
            theme_mode
        )

        app = QApplication.instance()

        if app is not None:
            AppTheme.apply(
                app,
                theme_mode
            )

        if (
            self.main_window is not None
            and hasattr(
                self.main_window,
                "update_application_identity"
            )
        ):
            self.main_window.update_application_identity()

        self.ui.lblStatus.setText(
            "Settings saved successfully."
        )

        QMessageBox.information(
            self,
            "Settings",
            "Settings saved successfully."
        )