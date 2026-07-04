import pytest
import time
from utilities.test_data_generator import TestDataGenerator


@pytest.mark.tc_comp_001
def test_companies_page_navigation(companies_page):

    assert "companies" in companies_page.page.url.lower()

@pytest.mark.tc_comp_002
def test_companies_page_controls(companies_page):

    assert companies_page.are_page_controls_displayed(), \
        "One or more Companies page controls are not displayed"

@pytest.mark.tc_comp_003
def test_all_plans_dropdown(companies_page):
    actual = companies_page.get_dropdown_options(companies_page.all_plans_dropdown)

    expected = [
        "All Plans", "Fresh", "Demo plan", "Basic", "Diamond",
        "diamond one", "EXCLUSIVE", "Demo123", "Free",
        "Enterprise", "Gold", "Silver"
    ]

    assert actual == expected

@pytest.mark.tc_comp_004
def test_all_status_dropdown(companies_page):

    expected = [
        "All Status",
        "Pending",
        "Active",
        "Inactive",
        "Suspended",
        "Rejected"
    ]

    assert companies_page.get_all_status_options() == expected


@pytest.mark.tc_comp_005
def test_all_types_dropdown(companies_page):

    expected = [
        "All Types",
        "Self-Registered",
        "Created by Admin"
    ]

    assert companies_page.get_all_types_options() == expected

@pytest.mark.tc_comp_006
def test_companies_table_headers(companies_page):

    expected = [
    "Sr. No.",
    "Company Name",
    "Plan",
    "Users",
    "Templates",
    "Deployed",
    "Status",
    "Type",
    "Created At",
    "Actions"
]

    actual = companies_page.get_table_headers()
    
    assert actual == expected

@pytest.mark.tc_comp_007
def test_export_csv(companies_page):

    companies_page.click_export_csv()

    assert companies_page.is_export_successful(),"Export success toast message not displayed"

@pytest.mark.tc_comp_008
@pytest.mark.add_company
def test_add_company_cancel(companies_page):

    data = TestDataGenerator.generate_company_data()

    companies_page.click_add_company()

    companies_page.enter_company_details(

        data["company_name"],

        data["domain"],

        data["first_name"],

        data["last_name"],

        data["email"],

        data["designation"],

        data["department"]

    )

    companies_page.click_cancel()

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_visible(data["company_name"])


@pytest.mark.tc_comp_009
@pytest.mark.add_company
def test_add_company_required_validation(
    companies_page
):

    companies_page.click_add_company()

    companies_page.click_create_company()

    assert companies_page.is_company_name_required_error_displayed()



@pytest.mark.tc_comp_010
@pytest.mark.add_company
def test_create_and_delete_company(
        companies_page
):

    data = TestDataGenerator.generate_company_data()

    companies_page.click_add_company()

    companies_page.enter_company_details(

        data["company_name"],

        data["domain"],

        data["first_name"],

        data["last_name"],

        data["email"],

        data["designation"],

        data["department"]

    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    companies_page.search_company(data["company_name"])

    assert companies_page.is_company_visible(data["company_name"])

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_visible(data["company_name"])

@pytest.mark.tc_comp_011
@pytest.mark.add_company
def test_add_company_invalid_business_rules(companies_page):

    data = TestDataGenerator.generate_company_data()

    companies_page.click_add_company()

    companies_page.enter_text(companies_page.company_name,"Auto_123")

    companies_page.enter_text(companies_page.workspace_domain,"Auto_123.com")

    companies_page.enter_text(companies_page.first_name,data["first_name"])

    companies_page.enter_text(companies_page.last_name,data["last_name"])

    companies_page.enter_text(companies_page.admin_email,"john@gmail.com")

    companies_page.click_create_company()

    assert companies_page.is_visible_with_wait("text=Company Name must contain only letters and numbers.")

@pytest.mark.tc_comp_012
@pytest.mark.add_company
def test_company_actions_menu_options(companies_page):

    data = TestDataGenerator.generate_company_data()

    companies_page.click_add_company()

    companies_page.enter_company_details(

        data["company_name"],

        data["domain"],

        data["first_name"],

        data["last_name"],

        data["email"],

        data["designation"],

        data["department"]

    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    companies_page.search_company(data["company_name"])

    companies_page.open_company_actions_menu(data["company_name"])

    assert companies_page.are_company_actions_visible()

    # Close menu after validation
    companies_page.close_actions_menu()

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_visible(data["company_name"])

@pytest.mark.tc_comp_013
@pytest.mark.add_company
def test_view_company_details_popup(
        companies_page
):

    data = TestDataGenerator.generate_company_data()

    companies_page.click_add_company()

    companies_page.enter_company_details(

        data["company_name"],

        data["domain"],

        data["first_name"],

        data["last_name"],

        data["email"],

        data["designation"],

        data["department"]

    )

    companies_page.click_create_company()

    assert companies_page.is_company_created_popup_displayed()

    companies_page.click_done()

    companies_page.search_company(data["company_name"])

    assert companies_page.is_company_visible(data["company_name"] )


    companies_page.open_company_details(data["company_name"])

    companies_page.page.wait_for_timeout(3000)

    companies_page.page.screenshot(path="view_details_popup.png")

    print( "Current URL:",companies_page.page.url)

    assert companies_page.is_company_details_popup_displayed()

    assert (companies_page.get_popup_company_name()== data["company_name"])

    assert companies_page.is_close_button_visible()

    assert companies_page.is_edit_company_button_visible()

    companies_page.close_company_details_popup()

    companies_page.search_company(data["company_name"])

    companies_page.delete_company(data["company_name"])

    companies_page.search_company(data["company_name"])

    assert not companies_page.is_company_visible(data["company_name"])