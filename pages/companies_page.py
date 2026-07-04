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
    
#-------------------------Methods---------------------------------#

    def is_companies_page_loaded(self):

        return "companies" in self.page.url.lower()

    def are_page_controls_displayed(self):
        

        dropdown_count = self.page.locator("select").count()

        return (self.is_visible_with_wait(self.search_box)

            and

            self.is_visible_with_wait(self.add_company_btn)

            and

            dropdown_count >= 3

            and

            self.is_visible_with_wait(self.export_csv_btn)

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


    def is_company_visible(self, company_name):

        return self.page.locator(f"text={company_name}").count() > 0
    


    def open_company_actions_menu(self,company_name):

        row = self.page.locator(f"tr:has-text('{company_name}')")

        row.locator("button[title='More actions']").click()

    def delete_company(self, company_name):

        self.open_company_actions_menu(company_name)

        self.page.get_by_text("Delete Company").click()

        self.page.get_by_role("button",name="Delete").click()

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
    

    def open_company_details(
        self,company_name):

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
        