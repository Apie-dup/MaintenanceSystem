from PySide6.QtWidgets import QMainWindow

from app.ui.generated.ui_assets import Ui_AssetsWindow


class AssetsController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_AssetsWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Assets")