from pages.base_page import BasePage


class DashboardPage(BasePage):

    dashboard_header = "h1"

    def is_dashboard_loaded(self):

        return self.is_visible(self.dashboard_header)