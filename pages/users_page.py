import email

from pages.base_page import BasePage


class UsersPage(BasePage):

    page_title = "h1"

    search_box = "input[placeholder='Search by User Name or Email ID...']"

    role_dropdown = "select >> nth=0"

    status_dropdown = "select >> nth=1"

    company_dropdown = "select >> nth=2"

    export_csv_btn = "text=Export CSV"

    export_success_msg = \
    "text=Users exported successfully."

    add_user_btn = "text=Add User"

    #----------------bedcrum navigation-----------------

    breadcrumb = "nav[aria-label='breadcrumb']"
    current_page_breadcrumb = "text=All Users"

    #-----------table headers------------------
    table_headers = "table thead th"

    #--------------add user form-----------------

    first_name_txt = "input[placeholder='Enter First Name']"

    last_name_txt = "input[placeholder='Enter Last Name']"

    email_txt = "input[placeholder='Enter Email ID']"

    contact_number_txt = "input[placeholder='Enter Contact Number']"

    company_dropdown_add_user = "select >> nth=0"

    role_dropdown_add_user = "select >> nth=1"

    designation_txt = "input[placeholder='Enter Designation']"

    department_txt = "input[placeholder='Enter Department']"

    cancel_btn = "button:text('Cancel')"

    add_user_save_btn = "button:has-text('Add User')"

    first_name_required_msg = "text=First Name is required"

    last_name_required_msg = "text=Last Name is required"

    email_required_msg = "text=Email ID is required"

    company_required_msg = "text=Please select a Company."

    role_required_msg = "text=Please select a Role."

    invalid_first_name_msg = \
    "text=First Name must contain only letters and one space between words."

    invalid_email_msg = \
    "text=Please enter a valid Email ID."

    invalid_phone_msg = \
    "text=Please enter a valid Indian Contact Number starting with 6, 7, 8 or 9."

    success_popup = "text=User Created Successfully"

    success_toast = "text=/User created successfully/i"

    #-----toggle user status-----------------
    user_status_toggle = "button[title='Deactivate User']"

    #----------eye icon locators---------------#

    impersonate_popup_title = "text=Impersonate User"

    start_impersonation_btn = "text=Start Impersonation"

    cancel_impersonation_btn = "text=Cancel"

    # Reset Password Icon

    reset_password_icon = "button[title='Reset Password']"
    
    reset_password_popup_title = "h2:has-text('Reset Password')"

    cancel_reset_password_btn = "text=Cancel"

    confirm_reset_password_btn = "text=Reset Password"

    #-----------------Edit Company Details-----------------

    edit_user_icon = "button[title='Edit User']"

    edit_user_page_title = "h1:has-text('Edit User')"

    email_field = "input[placeholder='Enter Email ID']"

    company_dropdown_edit = "select[name='company']"

    cancel_edit_user_btn = "text=Cancel"

    #----------------validate role selection ---------------#

    edit_role_dropdown = "select[name='role']"
    update_user_btn = "button:has-text('Update User')"
    
    #---------deactivate user-----------------

    deactivate_user_popup_title = "text=Deactivate User"

    confirm_deactivate_btn = "button:has-text('Deactivate')"

    user_deactivated_success_msg = \
        "text=User deactivated successfully"


    def get_page_title(self):

        return self.get_text(self.page_title).strip()

    def is_users_page_loaded(self):

        return "users" in self.page.url.lower()
    
    #-------------page controls---------------------------#

    def are_page_controls_displayed(self):

        search = self.is_visible_with_wait(self.search_box)

        role = self.page.locator(self.role_dropdown).is_visible()

        status = self.page.locator(self.status_dropdown).is_visible()

        company = self.page.locator(self.company_dropdown).is_visible()

        export_csv = self.is_visible_with_wait(self.export_csv_btn)
        add_user = self.is_visible_with_wait(self.add_user_btn)

        return (
            search
            and role
            and status
            and company
            and export_csv
            and add_user)

    
    
    #-----------------bedcrumb navigation check-----------------
        
    def get_breadcrumb_text(self):

        return (self.page.locator(self.breadcrumb).text_content().strip())
    
    #-----------verify role dropdown-----------------#

    def get_role_dropdown_options(self):

        return self.get_dropdown_options(self.role_dropdown)

    
    #-----------verify status dropdown-----------------#

    def get_status_dropdown_options(self):
        return self.get_dropdown_options(self.status_dropdown)
    
    #---------Verify Company Dropdown Loads Companies----

    def is_company_dropdown_enabled(self):

        return self.page.locator(self.company_dropdown).is_enabled()


    def get_company_dropdown_options(self):

        return self.get_dropdown_options(self.company_dropdown)
        
    #---------verify table header-----------------#

    def get_table_headers(self):
        self.page.wait_for_selector(self.table_headers, timeout=10000)
        headers = self.page.locator(self.table_headers)
        return [
            headers.nth(i).text_content().strip()
            for i in range(headers.count())
            if headers.nth(i).text_content().strip() != ""
        ]
    
    #--------------add user form-----------------
    def click_add_user(self):

        self.click(self.add_user_btn)
    
    def enter_user_details(
        self,
        first_name,
        last_name,
        email,
        phone,
        designation,
        department
):

        self.fill(self.first_name_txt, first_name)

        self.fill(self.last_name_txt, last_name)

        self.fill(self.email_txt, email)

        self.fill(self.contact_number_txt, phone)

        self.fill(self.designation_txt, designation)

        self.fill(self.department_txt, department)


    def select_company(self, company_name):

        dropdown = self.page.locator(
            self.company_dropdown_add_user
        )

        options = dropdown.locator("option")

        for i in range(options.count()):

            option_text = options.nth(i).text_content().strip()

            if company_name in option_text:

                dropdown.select_option(index=i)
                return

        raise Exception(
            f"Company '{company_name}' not found in dropdown"
        )


    def select_role(self, role):

        self.page.locator(
            self.role_dropdown_add_user
        ).select_option(label=role)
    
    def search_user(self, email):

        self.fill(self.search_box, email)
    
    def is_user_visible(self, email):

        return self.page.locator(
            f"tbody tr:has-text('{email}')"
        ).count() > 0

    def click_cancel(self):

        self.click(self.cancel_btn)
    
    def click_add_user_save(self):

        self.click(self.add_user_save_btn)
    
    def are_required_validations_displayed(self):

        return (
            self.is_visible_with_wait(self.first_name_required_msg)
            and
            self.is_visible_with_wait(self.last_name_required_msg)
            and
            self.is_visible_with_wait(self.email_required_msg)
            and
            self.is_visible_with_wait(self.company_required_msg)
            and
            self.is_visible_with_wait(self.role_required_msg)
    )

    def enter_invalid_user_details(self):

        self.fill(self.first_name_txt,"324sdf")

        self.fill(self.last_name_txt,"Test")

        self.fill(self.email_txt,"vdgff")

        self.fill(self.contact_number_txt,"15454")

        self.fill(self.designation_txt,"QA")

        self.fill(self.department_txt,"Testing")

    def are_invalid_field_validations_displayed(self):

        return (
            self.is_visible_with_wait(self.invalid_first_name_msg)
            and
            self.is_visible_with_wait(self.invalid_email_msg)
            and
            self.is_visible_with_wait(self.invalid_phone_msg)
        )
    
    def is_user_created_success_toast_displayed(self):
        self.page.wait_for_timeout(2000)
        return self.is_visible_with_wait(self.success_toast)

    def is_user_present(self, email):
        return self.page.locator(f"text={email}").is_visible()
    
    def is_role_present(self, role):
        return self.is_visible_with_wait(f"text={role}")
    
    def get_first_row_text(self):

        return self.page.locator("tbody tr").first.text_content()
    
    #-----------------toggle user status-----------------
    def is_user_status_toggle_visible(self, email):

        row = self.page.locator(
            f"tbody tr:has-text('{email}')"
        )

        toggle = row.locator(
            "button[title='Deactivate User']"
        )

        return toggle.count() > 0
    
    #----------------View user icon---------------#

    def click_view_user(self, email):

        row = self.page.locator(f"tr:has-text('{email}')")

        row.locator("button[title='Impersonate (view only)']").click()

    def is_impersonate_popup_displayed(self):

        return self.is_visible_with_wait(self.impersonate_popup_title)
    
    def click_cancel_impersonation(self):

        self.click(self.cancel_impersonation_btn)

        #----------------Reset Password Icon----------------#
    
    def click_reset_password(self, email):

        row = self.page.locator(f"tr:has-text('{email}')")

        row.locator("button[title='Reset Password']").click()
    
    def is_reset_password_popup_displayed(self):

        return self.is_visible_with_wait(self.reset_password_popup_title)
    
    def click_cancel_reset_password(self):

        self.click(self.cancel_reset_password_btn)
    
     #-----------------Edit Company Details-----------------

    def click_edit_user(self, email):

        row = self.page.locator(f"tr:has-text('{email}')")

        row.locator(self.edit_user_icon).click()
    
    def is_edit_user_page_displayed(self):

        return self.is_visible_with_wait(self.edit_user_page_title)
    
    def is_email_field_disabled(self):

        return self.page.locator(self.email_field).is_disabled()
    
    def is_company_dropdown_disabled(self):

        return self.page.locator(self.company_dropdown_edit).is_disabled()

    def click_cancel_edit_user(self):

        self.click(self.cancel_edit_user_btn)

        #----------------validate role selection ---------------#
    
    def get_user_role(self, email):

        row = self.page.locator(f"tr:has-text('{email}')")

        return row.locator("td").nth(4).text_content().strip()
    
    def select_edit_role(self, role):

        self.select_dropdown_by_text(self.edit_role_dropdown,role)

    def click_update_user(self):

        self.click(self.update_user_btn)

    #---------deactivate user-----------------

    def click_status_toggle(self, email):

        row = self.page.locator(
            f"tr:has-text('{email}')"
        )

        row.locator(
            "button[title='Deactivate User']"
        ).click()

    def is_deactivate_popup_displayed(self):

        return self.is_visible_with_wait(
            self.deactivate_user_popup_title
        )
    
    def click_confirm_deactivate(self):

        self.click(
            self.confirm_deactivate_btn
        )

    def is_user_deactivated_successfully(self):

        return self.is_visible_with_wait(
            self.user_deactivated_success_msg
        )

    def get_user_status(self, email):

        row = self.page.locator(
            f"tr:has-text('{email}')"
        )

        return (
            row.locator("span")
            .filter(has_text="Active")
            .first
            .text_content()
            .strip()
        )
#--------------export button functionality-----------------

    def click_export_csv(self):

        self.click(self.export_csv_btn)
    
    def is_export_success_msg_displayed(self):

        return self.is_visible_with_wait(self.export_success_msg)