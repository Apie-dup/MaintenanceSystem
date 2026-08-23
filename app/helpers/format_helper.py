from app.helpers.currency_helper import CurrencyHelper
from app.core.settings import Settings


class FormatHelper:
    """
    Helper class for formatting values consistently
    throughout the application.
    """

    # -------------------------------------------------
    # Currency
    # -------------------------------------------------

    @staticmethod
    def currency(value):

        if value is None:
            value = 0

        return CurrencyHelper.display(value)

    # -------------------------------------------------
    # Quantity
    # -------------------------------------------------

    @staticmethod
    def quantity(value):

        if value is None:
            value = 0

        return (
            f"{float(value):,.{Settings.QUANTITY_DECIMALS}f}"
        )

    # -------------------------------------------------
    # Percentage
    # -------------------------------------------------

    @staticmethod
    def percent(value):

        if value is None:
            value = 0

        return f"{float(value):.2f}%"

    # -------------------------------------------------
    # Integer
    # -------------------------------------------------

    @staticmethod
    def integer(value):

        if value is None:
            value = 0

        return f"{int(value):,}"

    # -------------------------------------------------
    # Yes / No
    # -------------------------------------------------

    @staticmethod
    def yes_no(value):

        return "Yes" if value else "No"