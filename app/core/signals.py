from PySide6.QtCore import QObject, Signal


class AppSignals(QObject):

    # Emitted whenever data changes
    data_changed = Signal(str)


# Global instance
signals = AppSignals()