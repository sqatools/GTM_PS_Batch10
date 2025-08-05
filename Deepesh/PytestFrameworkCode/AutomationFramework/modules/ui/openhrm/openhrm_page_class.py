from base.selenium_base import SeleniumBase
from .openhrm_page_locator import openrhm_locator as loc


class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username_value):
        self.fill_text(loc.username_field, username_value)

    def enter_password(self, pass_value):
        self.fill_text(loc.password_field, pass_value)

    def click_to_login_button(self):
        self.click_element(loc.login_button)


    def login_openhrm(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_to_login_button()

