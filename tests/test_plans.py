import pytest

#--------------validations--------------------------

@pytest.mark.tc_plans_001
def test_plans_page_navigation(plans_page):

    assert plans_page.is_plans_page_displayed()

    assert plans_page.get_page_title() == "Plans"

@pytest.mark.tc_plans_002
def test_create_plan_button_visible(plans_page):

    assert plans_page.is_create_plan_btn_visible(), \
        "Create Plan button is not visible"
    
@pytest.mark.tc_plans_003
def test_monthly_toggle_visible(plans_page):

    assert plans_page.is_visible_with_wait(
        plans_page.monthly_toggle
    ), "Monthly toggle is not visible"

@pytest.mark.tc_plans_004
def test_yearly_toggle_visible(plans_page):

    assert plans_page.is_visible_with_wait(
        plans_page.yearly_toggle
    ), "Yearly toggle is not visible"