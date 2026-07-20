from playwright.sync_api import Page

from pages.base_page import BasePage


class PlansPage(BasePage):

    # Header

    page_heading = "h1:text('Plans')"

    create_plan_btn = "a[href='/plans/new']"

    #-------------------------------- Toggle---------------------------------

    monthly_toggle = "//button[text()='Monthly']"

    yearly_toggle = "//button[text()='Yearly']"

    # Plan Cards

    plan_cards = ".rounded-xl"

    #---------------------- Actions --------------------------------------

    edit_btn = "button:has-text('Edit')"

    delete_btn = "button svg"

    # Status

    active_badge = "text=Active"

    # ----------------Create Plan Page ---------------------------

    create_plan_heading = "//h1[text()='Create Plan']"

    cancel_btn = "button:has-text('Cancel')"

    create_plan_save_btn = "a[href='/plans/new']"

    submit_create_plan_btn = "button:has-text('Create Plan')"

    # -----------Validation Messages-------------------

    plan_name_validation = "text='Plan Name is required.'"

    slug_validation = "text='Slug is required.'"

    max_users_validation = "text='Max Users is required and must be a whole number of at least 1.'"

    max_templates_validation = "text='Max Templates is required and must be a whole number of at least 1.'"

    #---------------create plan checkbox------------------

    priority_support_checkbox = "label:has-text('Priority Support') input[type='checkbox']"

    custom_integrations_checkbox = "label:has-text('Custom Integrations') input[type='checkbox']"

    most_popular_badge_checkbox = "label:has-text(\"Show 'Most Popular' badge\") input[type='checkbox']"

    enterprise_checkbox = "label:has-text('Enterprise (custom pricing)') input[type='checkbox']"


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

#------------create plan-----------------
    def is_create_plan_page_displayed(self):

        return self.is_visible_with_wait(
            self.create_plan_heading
        )

    def click_cancel(self):

        self.click(self.cancel_btn)


    def click_submit_create_plan(self):

        self.click(self.submit_create_plan_btn)

    
    def get_validation_message(self, locator):

        return self.page.locator(locator).text_content().strip()
   

    