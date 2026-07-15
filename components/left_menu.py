from pages.base_page import BasePage


class LeftMenu(BasePage):

    companies_menu = "//span[text()='Companies']"

    # users_menu = "text=All Users"
    users_menu = "//aside//span[text()='All Users']"

    plans_menu = "text=Plans"

    payments_menu = "text=Payments"

    invoices_menu = "text=Invoices"

    audit_logs_menu = "text=Audit Logs"

    visitor_logs_menu = "text=Visitor Logs"

    announcements_menu = "text=Announcements"

    email_logs_menu = "text=Email Logs"

    coupons_menu = "text=Coupons"

    leads_menu = "text=Leads"

    support_tickets_menu = "text=Support Tickets"

    platform_settings_menu = "text=Platform Settings"

    def click_companies(self):

        self.page.locator(
            self.companies_menu
        ).scroll_into_view_if_needed()

        self.click(
            self.companies_menu
        )

    def click_users(self):

        self.page.locator(
            self.users_menu
        ).scroll_into_view_if_needed()

        self.click(
            self.users_menu
        )

    def click_payments(self):

        self.page.locator(
            self.payments_menu
        ).scroll_into_view_if_needed()

        self.click(
            self.payments_menu
        )

    def click_coupons(self):

        self.page.locator(
            self.coupons_menu
        ).scroll_into_view_if_needed()

        self.click(
            self.coupons_menu
        )

    def click_platform_settings(self):

        self.page.locator(
            self.platform_settings_menu
        ).scroll_into_view_if_needed()

        self.click(
            self.platform_settings_menu
        )