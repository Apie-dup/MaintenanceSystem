class NavigationManager:

    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget

    def show(self, page):
        self.stacked_widget.setCurrentWidget(page)