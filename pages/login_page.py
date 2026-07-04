from pages.base_page import BasePage


class LoginPage(BasePage):

    email_txt = "input[placeholder='Enter your Email ID']"

    password_txt = "input[placeholder='Enter your Password']"

    sign_in_btn = "button[type='submit']"

    def navigate_to_login(self, base_url):

        self.page.goto(base_url)

        self.page.get_by_role("link",name="Company Sign In").first.click()

    def login(self, username, password):

        self.fill(self.email_txt, username)

        self.fill(self.password_txt, password)

        self.click(self.sign_in_btn)

        self.page.wait_for_url("**/dashboard")