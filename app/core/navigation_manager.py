from PySide6.QtCore import QObject

class NavigationManager(object):

    def __init__(self, page_manager):
        super().__init__()

        self.page_manager = page_manager
        self.routes = {}

    def register(self, button, page_name):

        """
        Register a navigation button.
        """

        self.routes[button] = page_name

        button.clicked.connect(
            lambda checked=False, name=page_name: self.navigate(name)
        )

    def navigate(self, page_name):

        """
        Navigate to a page
        """

        self.page_manager.show(page_name)