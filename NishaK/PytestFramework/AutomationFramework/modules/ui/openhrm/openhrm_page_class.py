from base.selenium_base_file import SeleniumBase
from .openhrm_page_locator import openhrm_locator as loc


class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username_value):
        self.fill_text(loc.username_field, username_value)

    def enter_password(self, password_value):
        self.fill_text(loc.password_field, password_value)

    def click_to_login_button(self):
        self.click_element(loc.login_button)

    def login_openhrm(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_to_login_button()