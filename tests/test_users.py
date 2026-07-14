import pytest
import time
from requests import options

from components.left_menu import LeftMenu
from pages.users_page import UsersPage
from utilities.test_data_generator import TestDataGenerator

@pytest.mark.tc_user_001
def test_users_page_navigation(users_page):

    assert users_page.is_users_page_loaded()

    assert users_page.get_page_title() == "All Users"

#---------verify page controls---------------#

@pytest.mark.tc_user_002
def test_users_page_controls(users_page):

    assert users_page.are_page_controls_displayed(), \
        "One or more All Users page controls are not displayed"
    
#--------------bedcrumb navigation----------------

@pytest.mark.tc_user_003
def test_users_breadcrumb_navigation(users_page):

    breadcrumb = users_page.get_breadcrumb_text()

    assert "Dashboard" in breadcrumb

    assert "All Users" in breadcrumb

#--------------verify role dropdown--------------

@pytest.mark.tc_user_004
def test_role_dropdown_values(users_page):

    expected = [
        "All Roles",
        "Platform Admin",
        "Company Admin",
        "Employee"
    ]

    actual = users_page.get_role_dropdown_options()

    assert actual == expected

#-----------verify status dropdown-----------------#

@pytest.mark.tc_user_005
def test_status_dropdown_values(users_page):
    expected = [
        "All Status",
        "Active",
        "Inactive"
    ]
    actual = users_page.get_status_dropdown_options()
    assert actual == expected

#---------------Verify Company Dropdown Loads Companies---------#

@pytest.mark.tc_user_006
def test_company_dropdown_loads_companies(users_page):

    assert users_page.is_company_dropdown_enabled(), \
        "Company dropdown is disabled"

    options = users_page.get_company_dropdown_options()

    assert len(options) > 1, \
        "Company dropdown did not load companies"


#---------verify table header-----------------#

@pytest.mark.tc_user_007
def test_users_table_headers(users_page):

    expected = [
        "Sr. No.",
        "User Name",
        "Email ID",
        "Role",
        "Company Name",
        "Status",
        "Last Login",
        "Created At",
        "Actions"
    ]

    actual = users_page.get_table_headers()

    assert actual == expected

#---------------add user form------------------#

# @pytest.mark.tc_user_008
# def test_add_user_cancel_functionality(companies_page,users_page):

#     company_data = (
#         TestDataGenerator.generate_company_data()
#     )

#     user_data = (
#         TestDataGenerator.generate_user_data()
#     )

#     # Create Company

#     companies_page.click_add_company()

#     companies_page.enter_company_details(
#         company_data["company_name"],
#         company_data["domain"],
#         company_data["first_name"],
#         company_data["last_name"],
#         company_data["email"],
#         company_data["designation"],
#         company_data["department"]
#     )

#     companies_page.click_create_company()

#     assert companies_page.is_company_created_popup_displayed()

#     companies_page.click_done()

#     # Navigate to Users

#     menu = LeftMenu(users_page.page)

#     menu.click_users()

#     users_page.click_add_user()

#     users_page.enter_user_details(
#         user_data["first_name"],
#         user_data["last_name"],
#         user_data["email"],
#         user_data["phone"],
#         user_data["designation"],
#         user_data["department"]
#     )

#     users_page.select_company(
#         company_data["company_name"]
#     )

#     users_page.select_role(
#         "Employee"
#     )

#     users_page.click_cancel()

#     users_page.search_user(
#         user_data["email"]
#     )

#     assert not users_page.is_user_visible(
#         user_data["email"]
#     )

#     # Cleanup

#     menu.click_companies()

#     companies_page.search_company(
#         company_data["company_name"]
#     )

#     companies_page.delete_company(
#         company_data["company_name"]
#     )

@pytest.mark.tc_user_008
def test_add_user_cancel_functionality(companies_page):

    # Generate test data
    company_data = TestDataGenerator.generate_company_data()
    user_data = TestDataGenerator.generate_user_data()

    # ---------------- Create Company ----------------

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed(), \
        "Company Created Successfully popup not displayed"

    companies_page.click_done()

    # ---------------- Navigate to Users ----------------

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # ---------------- Open Add User ----------------

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    # ---------------- Cancel ----------------

    users_page.click_cancel()

    # ---------------- Verify User Not Created ----------------

    users_page.search_user(
        user_data["email"]
    )

    assert not users_page.is_user_visible(
        user_data["email"]
    ), "User should not be created after clicking Cancel"

    # ---------------- Cleanup ----------------

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )

    companies_page.search_company(
        company_data["company_name"]
    )

    assert not companies_page.is_company_visible(
        company_data["company_name"]
    )

@pytest.mark.tc_user_009
def test_add_user_required_field_validation(users_page):

    users_page.click_add_user()

    users_page.click_add_user_save()

    assert users_page.are_required_validations_displayed(), \
        "Required field validations are not displayed"

@pytest.mark.tc_user_010
def test_add_user_invalid_business_rules(users_page):

    users_page.click_add_user()

    users_page.enter_invalid_user_details()

    users_page.click_add_user_save()

    assert users_page.is_visible_with_wait(users_page.invalid_first_name_msg)

    assert users_page.is_visible_with_wait(users_page.invalid_email_msg)

    assert users_page.is_visible_with_wait(users_page.invalid_phone_msg)

# @pytest.mark.tc_user_011
# def test_add_company_admin_user_successfully(companies_page):

#     company_data = TestDataGenerator.generate_company_data()
#     user_data = TestDataGenerator.generate_user_data()
#     user_data["email"] = (f"user{int(time.time())}@{company_data['domain']}"
# )

#     # Create Company

#     companies_page.click_add_company()

#     companies_page.enter_company_details(
#         company_data["company_name"],
#         company_data["domain"],
#         company_data["first_name"],
#         company_data["last_name"],
#         company_data["email"],
#         company_data["designation"],
#         company_data["department"]
#     )

#     companies_page.click_create_company()

#     assert companies_page.is_company_created_popup_displayed()

#     companies_page.click_done()

#     # Navigate to Users

#     menu = LeftMenu(companies_page.page)

#     menu.click_users()

#     users_page = UsersPage(companies_page.page)

#     # Add User

#     users_page.click_add_user()

#     users_page.enter_user_details(
#         user_data["first_name"],
#         user_data["last_name"],
#         user_data["email"],
#         user_data["phone"],
#         user_data["designation"],
#         user_data["department"]
#     )

#     users_page.select_company(
#         company_data["company_name"]
#     )

#     users_page.select_role(
#         "Company Admin"
#     )

#     users_page.click_add_user_save()
#     users_page.page.wait_for_timeout(3000)

#     print(users_page.page.locator("body").text_content())

#     # Verify Success Toast

#     assert users_page.is_user_created_success_toast_displayed(), \
#         "User creation success toast not displayed"

#     # Verify user exists in table

#     users_page.search_user(
#         user_data["email"]
#     )

#     assert users_page.is_user_present(
#         user_data["email"]
#     ), \
#         "Company Admin user not found in Users table"


@pytest.mark.tc_user_011
def test_add_company_admin_user_successfully(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate to Users

    menu = LeftMenu(companies_page.page)
    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Search created Company Admin

    users_page.search_user(
        company_data["email"]
    )

    # print(users_page.page.locator("tbody tr").first.text_content())

    # Verify User Exists

    assert users_page.is_user_present(
        company_data["email"]
    ), "Company Admin user not found"

    # Verify Role

    # assert users_page.is_role_present(
    #     "Company Admin"
    # ), "Company Admin role not found"

    assert "Company Admin" in \
       users_page.get_first_row_text()
    
   # Cleanup

    menu.click_companies()

    companies_page.search_company(company_data["company_name"])

    companies_page.delete_company(company_data["company_name"])

@pytest.mark.tc_user_012
def test_add_employee_user_successfully(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    user_data = TestDataGenerator.generate_user_data()

    user_data["email"] = (
        f"user{int(time.time())}@{company_data['domain']}"
    )

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate to Users

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Add Employee

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    users_page.click_add_user_save()

    # Verify User Exists

    users_page.search_user(
        user_data["email"]
    )

    assert users_page.is_user_present(
        user_data["email"]
    ), "Employee user not found"

    # Verify Role

    row_text = (
        users_page.page
        .locator("tbody tr")
        .first
        .text_content()
    )

    assert "Employee" in row_text, \
        "Employee role not found"

    # Cleanup

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )

    companies_page.search_company(
        company_data["company_name"]
    )

    assert not companies_page.is_company_visible(
        company_data["company_name"]
    ), "Company was not deleted successfully"

@pytest.mark.tc_user_013
def test_user_status_toggle_visible(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    user_data = TestDataGenerator.generate_user_data()

    user_data["email"] = (
        f"user{int(time.time())}@{company_data['domain']}"
    )

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate to Users

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Create Employee

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    users_page.click_add_user_save()

    # Search User

    users_page.search_user(
        user_data["email"]
    )

    # Verify Toggle Visible

    assert users_page.is_user_status_toggle_visible(user_data["email"]), "User status toggle is not visible"

    # Cleanup

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )

@pytest.mark.tc_user_014
def test_view_user_icon_opens_popup(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    user_data = TestDataGenerator.generate_user_data()

    user_data["email"] = (
        f"user{int(time.time())}@{company_data['domain']}"
    )

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate to Users

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Create Employee

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    users_page.click_add_user_save()

    # Search User

    users_page.search_user(
        user_data["email"]
    )

    # Click View User Icon

    users_page.click_view_user(
        user_data["email"]
    )

    # Verify Popup Opened

    assert users_page.is_impersonate_popup_displayed(), \
        "Impersonate User popup not displayed"

    # Close Popup

    users_page.click_cancel_impersonation()

    # Cleanup

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )

@pytest.mark.tc_user_015
def test_reset_password_icon_opens_popup(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    user_data = TestDataGenerator.generate_user_data()

    user_data["email"] = (
        f"user{int(time.time())}@{company_data['domain']}"
    )

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate to Users

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Create Employee

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    users_page.click_add_user_save()

    # Search User

    users_page.search_user(
        user_data["email"]
    )

    # Click Reset Password

    users_page.click_reset_password(
        user_data["email"]
    )

    # Verify Popup

    assert users_page.is_reset_password_popup_displayed(), \
        "Reset Password popup not displayed"

    # Close Popup

    users_page.click_cancel_reset_password()

    # Cleanup

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )

@pytest.mark.tc_user_016
def test_edit_user_icon_opens_edit_screen(companies_page):

    company_data = TestDataGenerator.generate_company_data()

    user_data = TestDataGenerator.generate_user_data()

    user_data["email"] = (
        f"user{int(time.time())}@{company_data['domain']}"
    )

    # Create Company

    companies_page.click_add_company()

    companies_page.enter_company_details(
        company_data["company_name"],
        company_data["domain"],
        company_data["first_name"],
        company_data["last_name"],
        company_data["email"],
        company_data["designation"],
        company_data["department"]
    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    # Navigate Users

    menu = LeftMenu(companies_page.page)

    menu.click_users()

    users_page = UsersPage(companies_page.page)

    # Create Employee

    users_page.click_add_user()

    users_page.enter_user_details(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["phone"],
        user_data["designation"],
        user_data["department"]
    )

    users_page.select_company(
        company_data["company_name"]
    )

    users_page.select_role(
        "Employee"
    )

    users_page.click_add_user_save()

    # Search User

    users_page.search_user(
        user_data["email"]
    )

    # Click Edit

    users_page.click_edit_user(
        user_data["email"]
    )

    # Verify Edit Screen

    assert users_page.is_edit_user_page_displayed()

    # Verify Email Disabled

    assert users_page.is_email_field_disabled()

    # Verify Company Disabled

    assert users_page.is_company_dropdown_disabled()

    # Return to User List

    users_page.click_cancel_edit_user()

    # Cleanup

    menu.click_companies()

    companies_page.search_company(
        company_data["company_name"]
    )

    companies_page.delete_company(
        company_data["company_name"]
    )