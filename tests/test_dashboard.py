from pages.dashboard_page import DashboardPage

def test_dashboard_page(login):

    assert "dashboard" in login.url.lower()
    