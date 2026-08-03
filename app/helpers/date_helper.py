from datetime import date, datetime, timedelta
import calendar


class DateHelper:
    """
    Central helper for all date calculations.
    """

    # -------------------------------------------------
    # Today
    # -------------------------------------------------

    @staticmethod
    def today():
        return date.today()

    @staticmethod
    def today_string():
        return date.today().strftime("%Y-%m-%d")

    # -------------------------------------------------
    # Convert
    # -------------------------------------------------

    @staticmethod
    def to_string(value):

        if value is None:
            return ""

        if isinstance(value, datetime):
            value = value.date()

        return value.strftime("%Y-%m-%d")

    @staticmethod
    def from_string(value):

        if not value:
            return None

        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    # -------------------------------------------------
    # Add Days
    # -------------------------------------------------

    @staticmethod
    def add_days(start_date, days):

        return start_date + timedelta(days=days)

    # -------------------------------------------------
    # Add Weeks
    # -------------------------------------------------

    @staticmethod
    def add_weeks(start_date, weeks):

        return start_date + timedelta(weeks=weeks)

    # -------------------------------------------------
    # Add Months
    # -------------------------------------------------

    @staticmethod
    def add_months(start_date, months):

        month = start_date.month - 1 + months
        year = start_date.year + month // 12
        month = month % 12 + 1

        day = min(
            start_date.day,
            calendar.monthrange(year, month)[1]
        )

        return date(year, month, day)

    # -------------------------------------------------
    # Add Years
    # -------------------------------------------------

    @staticmethod
    def add_years(start_date, years):

        try:
            return start_date.replace(
                year=start_date.year + years
            )

        except ValueError:
            # Handles leap years (29 Feb)
            return start_date.replace(
                month=2,
                day=28,
                year=start_date.year + years
            )

    # -------------------------------------------------
    # Difference
    # -------------------------------------------------

    @staticmethod
    def days_between(start_date, end_date):

        return (end_date - start_date).days

    @staticmethod
    def days_until(target_date):

        return (
            target_date - date.today()
        ).days

    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    @staticmethod
    def is_overdue(target_date):

        return target_date < date.today()

    @staticmethod
    def is_due_today(target_date):

        return target_date == date.today()

    @staticmethod
    def is_due_this_week(target_date):

        days = DateHelper.days_until(target_date)

        return 0 <= days <= 7

    @staticmethod
    def calculate_next_due_date(
        start_date,
        frequency_type,
        frequency_value
    ):
        if start_date is None:
            raise ValueError(
                "Last Service Date is required."
            )

        if frequency_value <= 0:
            raise ValueError(
                "Frequency Value must be greater than zero."
            )

        if frequency_type == "Daily":
            return DateHelper.add_days(
                start_date,
                frequency_value
            )

        if frequency_type == "Weekly":
            return DateHelper.add_weeks(
                start_date,
                frequency_value
            )

        if frequency_type == "Monthly":
            return DateHelper.add_months(
                start_date,
                frequency_value
            )

        if frequency_type == "Quarterly":
            return DateHelper.add_months(
                start_date,
                3 * frequency_value
            )

        if frequency_type == "Half Yearly":
            return DateHelper.add_months(
                start_date,
                6 * frequency_value
            )

        if frequency_type == "Yearly":
            return DateHelper.add_years(
                start_date,
                frequency_value
            )

        raise ValueError(
            f"Unsupported frequency type: {frequency_type}"
        )