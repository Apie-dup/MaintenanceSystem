from app.core.page_manager import PageManager
from app.core.navigation_manager import NavigationManager


class ApplicationManager:

    def __init__(self, stacked_widget, user):

        self.user = user

        self.page_manager = PageManager()

        self.navigation = NavigationManager(
            stacked_widget
        )

    def refresh(self):

        self.page_manager.refresh_all()

    def current_user(self):

        return self.user
