class Settings:
    """
    Static application configuration values.

    User-configurable values such as organization name,
    system name, currency symbol, date format, and theme
    are stored in app_settings and accessed through
    SettingsService.
    """

    # Application
    VERSION = "1.0.0"

    # UI
    TITLE_FONT_SIZE = 20
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 32
    FORM_MARGIN = 12
    FORM_SPACING = 8
    TABLE_ROW_HEIGHT = 28

    # Formatting
    CURRENCY_DECIMALS = 2
    QUANTITY_DECIMALS = 2

    # Logging
    LOG_FOLDER = "logs"
    LOG_FILE = "maintenance.log"