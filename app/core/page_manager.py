from PySide6.QtWidgets import QVBoxLayout

from app.core.module_registry import MODULES


class PageManager:

    def __init__(self):

        self.pages = {}

    def register(self, container, page_class):

        page = page_class()

        layout = container.layout()

        if layout is None:

            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

        if layout.count() == 0:
            layout.addWidget(page)

        self.pages[container.objectName()] = page

        return page

    def get_page(self, name):

        return self.pages.get(name)

    def refresh(self, name):

        page = self.get_page(name)

        if page and hasattr(page, "refresh"):
            page.refresh()

    def refresh_all(self):

        for page in self.pages.values():

            if hasattr(page, "refresh"):
                page.refresh()

    def register_modules(self, ui):

        for page_name,page_class in MODULES.items():

            container = getattr(ui, page_name)
            self.register(container, page_class)