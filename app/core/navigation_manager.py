class NavigationManager:

    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget

    def show(self, page):
        """
        Display the selected page.
        """
        self.stacked_widget.setCurrentWidget(page)

    def current_page(self):
        return self.stacked_widget.currentWidget()