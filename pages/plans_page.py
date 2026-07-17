from playwright.sync_api import Page

from pages.base_page import BasePage


class PlansPage(BasePage):

    # Header

    page_heading = "h1:text('Plans')"

    create_plan_btn = "a[href='/plans/new']"

    # Toggle

    monthly_toggle = "//button[text()='Monthly']"

    yearly_toggle = "//button[text()='Yearly']"

    # Plan Cards

    plan_cards = ".rounded-xl"

    # Actions

    edit_btn = "button:has-text('Edit')"

    delete_btn = "button svg"

    # Status

    active_badge = "text=Active"

    def get_page_title(self):

        return self.page.locator(
            self.page_heading
        ).text_content().strip()


    def is_plans_page_displayed(self):

        return self.page.locator(
            self.page_heading
        ).is_visible()
    
    def click_create_plan(self):

        self.page.locator(
            self.create_plan_btn
        ).click()
    
    def click_monthly(self):

        self.page.locator(
            self.monthly_toggle
        ).click()

    def click_yearly(self):

        self.page.locator(
            self.yearly_toggle
        ).click()

    def is_create_plan_btn_visible(self):

        return self.is_visible_with_wait(
            self.create_plan_btn
        )
    def click_create_plan(self):

        self.click(
            self.create_plan_btn
        )
#------------month;y toggle-----------------

    