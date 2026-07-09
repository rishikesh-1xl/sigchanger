from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Open Application
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter Username
    page.fill('input[name="username"]',"Admin")

    # Enter Password
    page.fill('input[name="password"]',"admin123")

    # Click Login
    page.click('button[type="submit"]')

    # Verify Login
    page.wait_for_url("**/dashboard/**")

    assert "dashboard" in page.url.lower()

    print("Login Successful")

    browser.close()