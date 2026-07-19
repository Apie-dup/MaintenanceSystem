from PySide6.QtWidgets import QVBoxLayout


class PageManager:

    @staticmethod
    def add_page(container, page):

        layout = container.layout()

        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

        # Prevent duplicate widgets if called again
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().setParent(None)

        layout.addWidget(page)