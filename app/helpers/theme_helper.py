from PySide6.QtGui import QColor, QPalette


class ThemeHelper:

    @staticmethod
    def is_dark(widget):

        base_color = widget.palette().color(
            QPalette.ColorRole.Base
        )

        return base_color.lightness() < 128

    @staticmethod
    def status_color(widget, status):

        status = (status or "").strip()

        if ThemeHelper.is_dark(widget):

            colors = {
                "Overdue": QColor(105, 45, 45),
                "Due": QColor(115, 70, 30),
                "Due Today": QColor(115, 70, 30),
                "Due Soon": QColor(105, 90, 30),
                "Inactive": QColor(65, 65, 65),
            }

        else:

            colors = {
                "Overdue": QColor(255, 210, 210),
                "Due": QColor(255, 230, 190),
                "Due Today": QColor(255, 230, 190),
                "Due Soon": QColor(255, 248, 190),
                "Inactive": QColor(225, 225, 225),
            }

        return colors.get(status)

    @staticmethod
    def priority_color(widget, priority):

        priority = (priority or "").strip()

        if ThemeHelper.is_dark(widget):

            colors = {
                "Critical": QColor(100, 35, 35),
                "Emergency": QColor(115, 40, 40),
                "High": QColor(110, 65, 30),
                "Medium": QColor(90, 80, 30),
                "Low": QColor(55, 75, 35),
            }

        else:

            colors = {
                "Critical": QColor(255, 205, 205),
                "Emergency": QColor(255, 215, 215),
                "High": QColor(255, 225, 195),
                "Medium": QColor(255, 245, 195),
                "Low": QColor(225, 245, 210),
            }

        return colors.get(priority)