from app.models.settings_model import SettingsModel


class SettingsService:

    @staticmethod
    def get_all():
        return SettingsModel.get_all()

    @staticmethod
    def get(key, default=None):
        return SettingsModel.get_value(
            key,
            default
        )

    @staticmethod
    def set(key, value):
        SettingsModel.set_value(
            key,
            value
        )

    @staticmethod
    def organization_name():
        return SettingsService.get(
            "organization_name",
            "Your Organization"
        )

    @staticmethod
    def system_name():
        return SettingsService.get(
            "system_name",
            "Maintenance Management System"
        )

    @staticmethod
    def currency_symbol():
        return SettingsService.get(
            "currency_symbol",
            "N$"
        )

    @staticmethod
    def currency_code():
        return SettingsService.get(
            "currency_code",
            "NAD"
        )

    @staticmethod
    def date_format():
        return SettingsService.get(
            "date_format",
            "dd-MMM-yyyy"
        )

    @staticmethod
    def theme_mode():
        return SettingsService.get(
            "theme_mode",
            "light"
        )

    @staticmethod
    def format_currency(value):

        symbol = (
            SettingsService.currency_symbol()
        )

        try:
            amount = float(
                value or 0
            )
        except (
            TypeError,
            ValueError
        ):
            amount = 0

        return (
            f"{symbol} "
            f"{amount:,.2f}"
        )