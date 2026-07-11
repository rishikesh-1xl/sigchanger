import pytest

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
