from PySide6.QtWidgets import QVBoxLayout

class PageManager:

    def __init__(self, stacked_widget):

        self.stacked_widget = stacked_widget

        self.pages = {}

    def register(self, name, container, page):

        self.pages[name] = {
            "container": container,
            "page": page
        }

        layout = container.layout()

        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)

            layout.addWidget

    def show(self, name):

        if name in self.pages:

            container = self.pages[name]["container"]

            self.stacked_widget.setCurrentWidget(container)

    def page(self, name):

        if name in self.pages:
            return self.pages[name]["pages"]
        
        return None
    
    def refresh(self, name):

        page = self.page(name)

        if page and hasattr(page, "refresh"):
            page.refresh()

    def refresh_all(self):

        for name in self.pages:
            self.refresh(name)