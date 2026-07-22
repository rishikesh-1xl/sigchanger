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

    auto_sync_checkbox = "label:has-text('Auto-Sync') input[type='checkbox']"

    sync_interval_dropdown = "label:has-text('Sync Interval') + select"   

#--------------Pricing & Limits-------------------------

    billing_interval_dropdown = "//label[text()='Billing Interval']/following-sibling::select"

#-----------------------------Country-wise Package form.------------------

    add_country_button = "button:has-text('+ Add Country')"

    country_package_form = "//label[text()='Country']"

    country_dropdown =  "role=combobox >> nth=1"

    currency_dropdown = "role=combobox >> nth=2"

    price_field = "//label[text()='Price']/following-sibling::input"

    plan_price_field = "//input[@placeholder='Enter Price in USD']"

    country_package_interval_dropdown = "//label[text()='Interval']/following-sibling::select"

    active_checkbox = "//label[normalize-space()='Active']/input[@type='checkbox']"

    country_package_rows = "//div[contains(@class,'grid') and .//label[text()='Country']]"

    delete_country_button = "button[title='Remove']"

        # Plan Details
    plan_name = "input[placeholder='Enter Plan Name']"
    slug = "input[placeholder='Enter Slug']"
    description = "input[placeholder='Enter Description']"

    # Pricing & Limits
    max_users = "input[placeholder='Enter Max Users']"
    max_templates = "input[placeholder='Enter Max Templates']"

#----------delete plan-----------------------
    confirm_delete_btn = "button:has-text('Delete')"
    delete_popup_heading = "//h2[text()='Delete Plan']"
    cancel_delete_btn = "button:has-text('Cancel')"
    delete_success_toast = "text=deleted successfully"

    # ===========================
    # Toast Messages
    # ===========================

    plan_created_successfully_toast = "text=Plan created successfully"

    plan_deleted_successfully_toast = "text=Plan deleted successfully"

    plan_updated_successfully_toast = "text=Plan updated successfully"

    # ---------------- Plan Cards ----------------

    plan_cards = (
    "div.grid.grid-cols-1.sm\\:grid-cols-2.lg\\:grid-cols-4.gap-5 "
    "> div.bg-white.rounded-2xl"
    )
    # first_plan_name = ".rounded-2xl h3"

    first_plan_slug = ".rounded-2xl .text-orange-500"
    
    #----------------------edit plan--------------------

    edit_plan_heading = "//h1[normalize-space()='Edit Plan']"

    update_plan_btn = "button:has-text('Update Plan')"

    trial_period = "//label[text()='Trial Period (days)']/following-sibling::input"


    def get_page_title(self):

        return self.page.locator(
            self.page_heading
        ).text_content().strip()


    # def is_plans_page_displayed(self):

    #     return self.page.locator(
    #         self.page_heading
    #     ).is_visible()

    def is_plans_page_displayed(self):

        return self.is_visible_with_wait(
            self.page_heading
        )
    
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
   
    def uncheck_checkbox(self, locator):

        checkbox = self.page.locator(locator)

        checkbox.scroll_into_view_if_needed()

        checkbox.wait_for(state="visible")

        checkbox.uncheck()
    
    def is_visible(self, locator):

        return self.page.locator(locator).is_visible()
    

    def wait_for_state(self, locator, state="visible", timeout=5000):

        self.page.locator(locator).wait_for(
            state=state,
            timeout=timeout
        )
    
#-----------------------------Country-wise Package form.------------------

    def click_add_country(self):

        self.click(self.add_country_button)

    def enter_price(self, price):

        self.enter_text(
            self.price_field,
            price
        )

    def get_price(self):

        return self.page.locator(
            self.price_field
        ).input_value()
        
    def get_country_package_count(self):

        return self.page.locator(
            self.country_package_rows
        ).count()


    def click_delete_country(self):

        self.click(
            self.delete_country_button
        )

#-------create new plan--------------------

    def enter_plan_name(self, plan_name):

        self.enter_text(
            self.plan_name,
            plan_name
        )


    def enter_slug(self, slug):

        self.enter_text(
            self.slug,
            slug
        )


    def enter_description(self, description):

        self.enter_text(
            self.description,
            description
        )


    def enter_max_users(self, max_users):

        self.enter_text(
            self.max_users,
            max_users
        )


    def enter_max_templates(self, max_templates):

        self.enter_text(
            self.max_templates,
            max_templates
        )

    # def is_plan_present(self, slug):

    #     return self.page.locator(
    #         f"text={slug.upper()}"
    #     ).is_visible()


    def is_plan_present(self, plan_name):
        return self.get_plan_card(plan_name) is not None


    # def click_delete_plan(self, plan_name):

    #     card = self.page.locator(
    #         f"div:has(h3:text('{plan_name}'))"
    #     )

    #     card.locator("button[title='Delete']").click()

    def click_delete_plan(self, plan_name):

        card = self.get_plan_card(plan_name)

        if card is None:
            raise Exception(f"Plan '{plan_name}' not found.")

        card.get_by_title("Delete").click()
        
    def confirm_delete(self):

        self.click(self.confirm_delete_btn)
    
    def is_delete_popup_displayed(self):

        return self.is_visible_with_wait(
            self.delete_popup_heading
        )

    def click_confirm_delete(self):

        self.click(
            self.confirm_delete_btn
        )
    def click_cancel_delete(self):

        self.click(
            self.cancel_delete_btn
        )
    
    def is_delete_success_message_displayed(self):

        return self.is_visible_with_wait(
            self.delete_success_toast
        )
    
    def is_plan_deleted(self, plan_name):

        return self.get_plan_card(plan_name) is None
    
    def is_plan_created_successfully(self):
        return self.is_visible_with_wait(
            self.plan_created_successfully_toast
        )

    def is_plan_deleted_successfully(self):
        return self.is_visible_with_wait(
            self.plan_deleted_successfully_toast
        )

    def is_plan_updated_successfully(self):
        return self.is_visible_with_wait(
            self.plan_updated_successfully_toast
        )
    
    def get_first_plan_name(self):

        first_card = self.page.locator(
            self.plan_cards
        ).first

        return first_card.locator("h3").text_content().strip()
    
    
    def get_first_plan_slug(self):

        return self.page.locator(
            self.first_plan_slug
        ).first.text_content().strip()
    

    def get_plan_card(self, plan_name):

        # Give the list time to refetch after redirect
        self.page.wait_for_load_state("networkidle")

        all_cards = self.page.locator(self.plan_cards)

        try:
            all_cards.first.wait_for(state="visible", timeout=15000)
        except Exception:
            return None

        card = all_cards.filter(has_text=plan_name)

        try:
            card.first.wait_for(state="visible", timeout=10000)
        except Exception:
            return None

        return card.first
    
    def select_country(self, country):

        self.select_dropdown_by_text(
            self.country_dropdown,
            country
        )

    def get_selected_currency(self):

        return self.get_selected_dropdown_value(self.currency_dropdown)

    def enter_country_price(self, price):

        self.enter_text(
            self.price_field,
            price
        )
    
    def enter_plan_price(self, price):

        self.enter_text(
            self.plan_price_field,
            price
        )
    
    #--------------edit plan------------------------------

    def click_edit_plan(self, plan_name):

        self.page.locator(
            f"//h3[normalize-space()='{plan_name}']/ancestor::div[contains(@class,'rounded-2xl')]//button[contains(.,'Edit')]"
        ).click()

    def is_edit_plan_page_displayed(self):

        return self.is_visible_with_wait(
            self.edit_plan_heading
        )
    
    def get_plan_name(self):

        return self.page.locator(
            self.plan_name
        ).input_value()
    
    def get_slug(self):

        return self.page.locator(
            self.slug
        ).input_value()

    def get_description(self):

        return self.page.locator(
            self.description
        ).input_value()
    
    def get_plan_price(self):

        return self.page.locator(
            self.plan_price_field
        ).input_value()

    def get_max_users(self):

        return self.page.locator(
            self.max_users
        ).input_value()
    
    def get_max_templates(self):

        return self.page.locator(
            self.max_templates
        ).input_value()
    
    #------------update plan---------------

    def enter_trial_days(self, days):

        self.enter_text(
            self.trial_period,
            days
        )
    
    def click_update_plan(self):

        self.click(
            self.update_plan_btn
        )

    def get_trial_days(self):

        return self.page.locator(
            self.trial_period
        ).input_value()

    def get_selected_sync_interval(self):

        return self.get_selected_dropdown_value(
            self.sync_interval_dropdown
        )
    
    def get_selected_sync_interval(self):

        return self.get_selected_dropdown_text(
            self.sync_interval_dropdown
        )