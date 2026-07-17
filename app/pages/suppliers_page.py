from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SuppliersPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Suppliers Page")
        )

    def refresh(self):
        self.load_suppliers()