from selenium_base import SeleniumBase
from openhrm_page_locator import *


class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username_value):
        self.fill_text(username_field, username_value)

    def enter_password(self, pass_value):
        self.fill_text(password_field, pass_value)

    def click_to_login_button(self):
        self.click_element(login_button)
