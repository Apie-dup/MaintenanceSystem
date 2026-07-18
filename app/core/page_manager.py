from PySide6.QtWidgets import QVBoxLayout

class PageManager:

    def __init__(self):
        self.page = {}

    def add_page(self, container, page):

        """
        Insert a page into a placeholder widget.
        """

        layout = container.layout()

        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

        # Prevent duplicate widgets
        if layout.count() == 0:
            layout.addWidget(page)

    def get_page(self, name):
        return self.page.get(name)
    
    def refresh_page(self, name):
        page = self.get_page(name)

        if page and hasattr(page, "refresh"):
            page.refresh()

    def refresh_all(self):
        for page in self.pages.values():
            if hasattr(page, "refresh"):
                page.refresh()