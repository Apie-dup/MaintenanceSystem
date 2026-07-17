class ApplicationManager:

    def __init__(self, main_window):

        self.main = main_window

        self.page_manager = None
        self.navigation_manager = None

    def initialize(self):

        from app.core.page_manager import PageManager
        from app.core.navigation_manager import NavigationManager

        self.page_manager = PageManager(self.main)
        self.navigation_manager = NavigationManager(self.main)

        self.page_manager.initialize()
        self.navigation_manager.initialize()
