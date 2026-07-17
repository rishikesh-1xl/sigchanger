import os
import pytest

from playwright.sync_api import Playwright
from dotenv import load_dotenv

from utilities.config_reader import Config
from pages.login_page import LoginPage
from pages.users_page import UsersPage
from pages.plans_page import PlansPage

from components.left_menu import LeftMenu
from pages.companies_page import CompaniesPage


load_dotenv()


@pytest.fixture(scope="function")
def page(playwright: Playwright):

    browser = playwright.chromium.launch(headless=Config.HEADLESS)

    context = browser.new_context(
        viewport={
            "width": Config.VIEWPORT_WIDTH,
            "height": Config.VIEWPORT_HEIGHT
        },
        record_video_dir="videos/"
    )

    


    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    page.set_default_timeout(Config.TIMEOUT)
    yield page

    os.makedirs("traces", exist_ok=True)

    context.tracing.stop(path="traces/trace.zip")

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots",exist_ok=True)

            page.screenshot(path=f"screenshots/{item.name}.png",full_page=True)


@pytest.fixture(scope="function")
def login(page):

    login_page = LoginPage(page)

    login_page.navigate_to_login(Config.BASE_URL)

    login_page.login(
        os.getenv("SIGCHANGER_USERNAME"),
        os.getenv("SIGCHANGER_PASSWORD")
    )

    yield page

@pytest.fixture(scope="function")
def companies_page(login):

    menu = LeftMenu(login)

    menu.click_companies()

    return CompaniesPage(login)

@pytest.fixture(scope="function")
def users_page(login):

    menu = LeftMenu(login)

    menu.click_users()

    return UsersPage(login)


@pytest.fixture(scope="function")
def plans_page(login):

    menu = LeftMenu(login)

    menu.click_plans()

    return PlansPage(login)