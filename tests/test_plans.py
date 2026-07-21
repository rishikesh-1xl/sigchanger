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


@pytest.mark.tc_plans_005
def test_create_plan_page_opens(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."


@pytest.mark.tc_plans_006
def test_cancel_button_returns_to_plans_page(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_cancel()

    assert plans_page.is_plans_page_displayed(), \
        "User is not redirected to Plans page after clicking Cancel."
    
@pytest.mark.tc_plans_007
def test_mandatory_field_validations(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed()

    plans_page.click_submit_create_plan()

    assert plans_page.get_validation_message(
        plans_page.plan_name_validation
    ) == "Plan Name is required."

    assert plans_page.get_validation_message(
        plans_page.slug_validation
    ) == "Slug is required."

    assert plans_page.get_validation_message(
        plans_page.max_users_validation
    ) == "Max Users is required and must be a whole number of at least 1."

    assert plans_page.get_validation_message(
        plans_page.max_templates_validation
    ) == "Max Templates is required and must be a whole number of at least 1."

@pytest.mark.tc_plans_008
def test_priority_support_checkbox(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_checkbox(
        plans_page.priority_support_checkbox
    )

    assert plans_page.is_checkbox_checked(
        plans_page.priority_support_checkbox
    ), "Priority Support checkbox is not checked."

    
@pytest.mark.tc_plans_009
def test_custom_integrations_checkbox(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_checkbox(
        plans_page.custom_integrations_checkbox
    )

    assert plans_page.is_checkbox_checked(
        plans_page.custom_integrations_checkbox
    ), "Custom Integrations checkbox is not checked."
    
@pytest.mark.tc_plans_010
def test_most_popular_badge_checkbox(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_checkbox(
        plans_page.most_popular_badge_checkbox
    )

    assert plans_page.is_checkbox_checked(
        plans_page.most_popular_badge_checkbox
    ), "Most Popular Badge checkbox is not checked."
    
@pytest.mark.tc_plans_011
def test_enterprise_checkbox(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_checkbox(
        plans_page.enterprise_checkbox
    )

    assert plans_page.is_checkbox_checked(
        plans_page.enterprise_checkbox
    ), "Enterprise checkbox is not checked."

@pytest.mark.tc_plans_012
def test_sync_interval_visibility_based_on_auto_sync(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    # Verify Auto-Sync is unchecked by default
    assert not plans_page.is_checkbox_checked(
        plans_page.auto_sync_checkbox
    ), "Auto-Sync checkbox should be unchecked by default."

    # Verify Sync Interval dropdown is hidden
    assert not plans_page.is_visible(
        plans_page.sync_interval_dropdown
    ), "Sync Interval dropdown should not be visible."

    # Check Auto-Sync
    plans_page.click_checkbox(
    plans_page.auto_sync_checkbox
)

    plans_page.wait_for_state(
        plans_page.sync_interval_dropdown,
        state="visible"
    )

    assert plans_page.is_visible(
        plans_page.sync_interval_dropdown
    )

    plans_page.uncheck_checkbox(
        plans_page.auto_sync_checkbox
    )

    plans_page.wait_for_state(
        plans_page.sync_interval_dropdown,
        state="hidden"
    )

    assert not plans_page.is_visible(
        plans_page.sync_interval_dropdown
    ), "Sync Interval dropdown should be hidden."


@pytest.mark.tc_plans_013
def test_sync_interval_dropdown_options(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_checkbox(
        plans_page.auto_sync_checkbox
    )

    assert plans_page.is_visible_with_wait(
        plans_page.sync_interval_dropdown
    )

    expected_options = [
        "None",
        "Hourly",
        "Daily",
        "Weekly",
        "Monthly",
        "Custom"
    ]

    actual_options = plans_page.get_dropdown_options(
        plans_page.sync_interval_dropdown
    )

    assert actual_options == expected_options, \
        f"Expected {expected_options}, but got {actual_options}"
    
@pytest.mark.tc_plans_014
def test_billing_interval_dropdown_options(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    expected_options = [
        "Monthly",
        "Yearly"
    ]

    actual_options = plans_page.get_dropdown_options(
        plans_page.billing_interval_dropdown
    )

    assert actual_options == expected_options, \
        f"Expected {expected_options}, but got {actual_options}"
    
#-----------------------------Country-wise Package form.------------------


@pytest.mark.tc_plans_015
def test_add_country_button_opens_country_package_form(plans_page):

    plans_page.click_create_plan()

    assert plans_page.is_create_plan_page_displayed(), \
        "Create Plan page is not displayed."

    plans_page.click_add_country()

    assert plans_page.is_visible_with_wait(
        plans_page.country_package_form
    ), "Country-wise Package form is not displayed."


