import email

from pages.base_page import BasePage


class UsersPage(BasePage):

    page_title = "h1"

    search_box = "input[placeholder='Search by User Name or Email ID...']"

    role_dropdown = "select >> nth=0"

    status_dropdown = "select >> nth=1"

    company_dropdown = "select >> nth=2"

    export_csv_btn = "text=Export CSV"

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

        print("Toggle Count =", toggle.count())

        return toggle.count() > 0