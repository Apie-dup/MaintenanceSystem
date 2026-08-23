from app.services.settings_service import SettingsService


class CurrencyHelper:

    @staticmethod
    def display(value):

        if value is None or value == "":
            value = 0

        try:
            amount = float(value)

        except (TypeError, ValueError):
            return str(value)

        symbol = (
            SettingsService.currency_symbol()
        )

        return (
            f"{symbol} "
            f"{amount:,.2f}"
        )

    @staticmethod
    def parse(value):

        if value is None or value == "":
            return 0.0

        if isinstance(value, (int, float)):
            return float(value)

        symbol = (
            SettingsService.currency_symbol()
        )

        text = (
            str(value)
            .replace(symbol, "")
            .replace(",", "")
            .strip()
        )

        return float(text)