from pages.base_page import BasePage


class CompaniesPage(BasePage):

    search_box = "input[placeholder='Search by Company Name...']"

    add_company_btn = "text=Add Company"

    export_csv_btn = "text=Export CSV"

    all_plans_dropdown = "select >> nth=0"

    all_status_dropdown = "select >> nth=1"

    all_types_dropdown = "select >> nth=2"

    table_headers = "table thead th"

    success_toast = "text=Companies exported successfully."


    # Add Company Form

    company_name = "input[placeholder='Enter Company Name']"

    domain = "input[placeholder='Enter Google Workspace Domain']"

    first_name = "input[placeholder='Enter First Name']"

    last_name = "input[placeholder='Enter Last Name']"

    admin_email = "input[placeholder='Enter Admin Email ID']"

    designation = "input[placeholder='Enter Designation']"

    department = "input[placeholder='Enter Department']"

    cancel_btn = "button:text('Cancel')"

    create_company_btn = "button:text('Create Company')"

    # Validation

    company_required_error = "text=Company Name is required."

    # Delete Company

    delete_company_menu = "text=Delete Company"

    delete_btn = "button:text('Delete')"

    success_popup = "h2:has-text('Company Created Successfully')"

    done_btn = "button:has-text('Done')"

    workspace_domain = "input[name='domain']"

    #--------------3 dots menus-----------------------------------#

    more_actions_btn = "tbody tr:first-child button[title='More actions']"

    suspend_company_option = "text=Suspend Company"

    deactivate_company_option = "text=Deactivate Company"

    reset_admin_password_option = "text=Reset Admin Password"

    change_plan_option = "text=Change Plan"

    delete_company_option = "text=Delete Company"

    # ------------------visible icons---------------------------------#
    view_company_btn = "button[title='View Company Details']"

    company_details_popup = "div[role='dialog']"

    popup_company_name = "div.flex.items-center.gap-3 h3"

    close_popup_btn = "button:has-text('Close')"

    edit_company_btn = "button:has-text('Edit Company')"

    # ----------------- Edit Company -----------------

    edit_company_menu_option = "text=Edit Company"
    update_company_btn = "button:has-text('Update Company')"
    update_success_toast = "text=Company updated successfully."
    admin_details_locked_banner = "text=The admin's name and Email ID cannot be changed after registration."
    duplicate_company_name_error = "text=A company with this name already exists."

    # ----------------- Suspend / Unsuspend Company -----------------

    suspend_menu_option = "text=Suspend Company"
    activate_menu_option = "text=Activate Company"   # confirm exact label once suspended

    suspend_reason_textbox = "textarea[placeholder='Enter reason for suspension...']"
    confirm_suspend_btn = "button:has-text('Suspend')"
    confirm_activate_btn = "button:has-text('Activate')"   # confirm exact label/button text

    suspend_success_toast = "text=Company suspended."
    activate_success_toast = "text=Company unsuspended."     # confirm exact toast text

    status_badge = "span:has-text('{status}')"   # generic, filled per row below
    unsuspend_menu_option = "text='Unsuspend Company'"   # exact match (quotes = exact in Playwright text engine)
    confirm_unsuspend_btn = "button:has-text('Unsuspend')"

    unsuspend_success_toast = "text=Company unsuspended."

    #---------------search box----------------------------#
    no_companies_found_message = "text=No companies found."

    #-------------change plan----------------------------#
    change_plan_menu = "text=Change Plan"

    plan_dropdown = "select"

    update_plan_btn = "button:has-text('Update Plan')"

    change_plan_popup = "text=Change Plan"


    
#-------------------------Methods---------------------------------#

    def is_companies_page_loaded(self):

        return "companies" in self.page.url.lower()

    
    def are_page_controls_displayed(self):

        search = self.is_visible_with_wait(self.search_box)
        add_company = self.is_visible_with_wait(self.add_company_btn)
        export_csv = self.is_visible_with_wait(self.export_csv_btn)

        plans = self.page.locator(self.all_plans_dropdown).is_visible()
        status = self.page.locator(self.all_status_dropdown).is_visible()
        types = self.page.locator(self.all_types_dropdown).is_visible()

        return (
            search
            and add_company
            and export_csv
            and plans
            and status
            and types
        )


    def get_all_plans_options(self):
        return self.get_dropdown_options(self.all_plans_dropdown)

    def get_all_status_options(self):
        return self.get_dropdown_options(self.all_status_dropdown)

    def get_all_types_options(self):
        return self.get_dropdown_options(self.all_types_dropdown)
    
    
    def get_table_headers(self):

        headers = self.page.locator(self.table_headers)

        return [headers.nth(i).text_content().strip()

            for i in range(headers.count())

        ]
    
    def click_export_csv(self):

        self.click(self.export_csv_btn)

    
    def is_export_successful(self):

        return self.is_visible_with_wait(self.success_toast)
    
    def click_add_company(self):

        self.click(self.add_company_btn)

    def enter_company_details(

        self,
        company,
        domain,
        first_name,
        last_name,
        email,
        designation,
        department

):

        self.fill(self.company_name,company)

        self.fill(self.domain,domain)

        self.fill(self.first_name,first_name)

        self.fill(self.last_name,last_name)

        self.fill(self.admin_email,email)

        self.fill(self.designation,designation)

        self.fill(self.department,department)


    def click_cancel(self):

        self.click(self.cancel_btn)


    def click_create_company(self):

        self.click(self.create_company_btn)


    def is_company_name_required_error_displayed(self):

        return self.is_visible_with_wait(self.company_required_error)
    
    
    def search_company(self, company_name):

        self.fill(self.search_box,company_name)


    # def is_company_visible(self, company_name):

    #     return self.page.locator(f"text={company_name}").count() > 0
    
    def is_company_visible(self,company_name):

        return self.page.locator(f"tbody tr:has-text('{company_name}')").count() > 0


    def open_company_actions_menu(self,company_name):

        row = self.page.locator(f"tr:has-text('{company_name}')")

        row.locator("button[title='More actions']").click()

    def delete_company(self, company_name):

        self.open_company_actions_menu(company_name)

        self.page.get_by_text("Delete Company").click()

        self.page.get_by_role("button",name="Delete").click()

        self.page.wait_for_timeout(2000)


    def click_done(self):

        self.click(self.done_btn)


    def is_company_created_popup_displayed(self):

        try:

            self.page.get_by_text("Company Created Successfully").wait_for(timeout=15000)

            return True

        except:

            return False
    

    def are_company_actions_visible(self):

        return (self.is_visible_with_wait(self.suspend_company_option)

            and

            self.is_visible_with_wait(self.deactivate_company_option)

            and

            self.is_visible_with_wait(self.reset_admin_password_option)

            and

            self.is_visible_with_wait(self.change_plan_option)

            and

            self.is_visible_with_wait(self.delete_company_option)

        )
    

    def open_company_details(self,company_name):

        row = self.page.locator(f"tr:has-text('{company_name}')")

        row.locator(self.view_company_btn).click()


    def get_popup_company_name(self):

        return self.page.locator(self.popup_company_name).text_content().strip()


    def is_company_details_popup_displayed(self):
        return self.is_visible_with_wait(self.edit_company_btn)


    def is_close_button_visible(self):

        return self.is_visible_with_wait(self.close_popup_btn)


    def is_edit_company_button_visible(self):

        return self.is_visible_with_wait(self.edit_company_btn)


    def close_company_details_popup(self):

        self.click(self.close_popup_btn)
    
    def close_actions_menu(self):

        self.page.mouse.click(100,100)

    def open_edit_company(self, company_name):
        self.open_company_details(company_name)   # opens the view popup
        self.click(self.edit_company_btn)          # already defined -> navigates to edit page

    def update_designation_and_department(self, designation, department):
        self.page.locator(self.designation).fill(designation)
        self.page.locator(self.department).fill(department)

    def click_update_company(self):
        self.click(self.update_company_btn)
    
    def is_update_successful(self):
        return self.is_visible_with_wait(self.update_success_toast)
        
    # ----------------- Edit Company: field state checks -----------------

    def is_domain_field_disabled(self):
        return self.page.locator(self.domain).is_disabled()

    def is_company_name_field_disabled(self):
        return self.page.locator(self.company_name).is_disabled()

    def is_admin_details_locked_banner_displayed(self):
        return self.is_visible_with_wait(self.admin_details_locked_banner)
    
    def update_company_name(self, new_name):
        self.page.locator(self.company_name).fill(new_name)

    def get_company_name_value(self):
        return self.page.locator(self.company_name).input_value()
    
    #-------------suspend compny-----------------------------

    def click_suspend_company(self, company_name):
        self.open_company_actions_menu(company_name)
        self.click(self.suspend_menu_option)

    def enter_suspend_reason(self, reason):
        self.fill(self.suspend_reason_textbox, reason)

    def confirm_suspend(self):
        self.click(self.confirm_suspend_btn)

    def is_suspend_successful(self):
        return self.is_visible_with_wait(self.suspend_success_toast)

    def click_activate_company(self, company_name):
        self.open_company_actions_menu(company_name)
        self.click(self.activate_menu_option)

    def confirm_activate(self):
        self.click(self.confirm_activate_btn)

    def is_activate_successful(self):
        return self.is_visible_with_wait(self.activate_success_toast)

    def get_company_status(self, company_name):
        row = self.page.locator(f"tr:has-text('{company_name}')")
        # adjust selector below to match the actual status badge markup in that row
        return row.locator("td span").filter(has_text="Active").or_(
            row.locator("td span").filter(has_text="Suspended")
        ).text_content().strip()
    
    def is_unsuspend_successful(self):
        return self.is_visible_with_wait(self.activate_success_toast)
    
    def click_unsuspend_company(self, company_name):
        self.open_company_actions_menu(company_name)
        self.click(self.unsuspend_menu_option)

    def confirm_unsuspend(self):
        self.click(self.confirm_unsuspend_btn)

    def is_unsuspend_successful(self):
        return self.is_visible_with_wait(self.unsuspend_success_toast)  
    
    def is_no_companies_found_message_displayed(self):

        return self.is_visible_with_wait(
            self.no_companies_found_message
        )
    
    def select_company_plan(self, plan_name):

        self.page.locator(self.plan_dropdown).select_option(label=plan_name)

    def click_update_plan(self):

        self.click(self.update_plan_btn)

    def get_company_plan(self, company_name):

        row = self.page.locator(f"tbody tr:has-text('{company_name}')")

        return row.locator("td").nth(2).text_content().strip()
    
    def wait_for_plan_update(self):

        self.page.wait_for_timeout(2000)
    
    def click_change_plan(self, company_name):

        self.open_company_actions_menu(company_name)

        self.click(self.change_plan_menu)

    def select_company_plan(self, plan_name):

        self.page.get_by_role("combobox").last.select_option(label=plan_name)
