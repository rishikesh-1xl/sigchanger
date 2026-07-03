from playwright.sync_api import expect

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
    
    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    
    def get_dropdown_options(self, locator, timeout=30000):
        select = self.page.locator(locator)
        options = select.locator("option")

        # Locator-based polling — re-resolves the <select> fresh on every check,
        # so it survives React re-mounting/replacing the element.
        expect(options.nth(1)).to_be_attached(timeout=timeout)

        return [
            options.nth(i).text_content().strip()
            for i in range(options.count())
        ]