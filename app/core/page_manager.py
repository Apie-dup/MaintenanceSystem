from PySide6.QtWidgets import QSizePolicy, QVBoxLayout


class PageManager:

    @staticmethod
    def add_page(container, page):

        container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        page.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        layout = container.layout()

        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Prevent duplicate widgets if called again
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().setParent(None)

        layout.addWidget(page)
        layout.setStretch(0, 1)