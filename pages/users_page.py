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

        headers = self.page.locator(self.table_headers)

        return [headers.nth(i).text_content().strip()
            for i in range(headers.count())]