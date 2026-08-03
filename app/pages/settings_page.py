from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SettingsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Settings Page")
        )

    def refresh(self):
        self.load_settings()