from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ReportsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Reports Page")
        )

    def refresh(self):
        self.load_reorts()