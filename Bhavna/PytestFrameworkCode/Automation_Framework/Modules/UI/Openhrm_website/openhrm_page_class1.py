import time

from ....Base.selenium_base1 import SeleniumBase
from .openhrm_page_locator1 import Openhrm_locator as lc


class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username_value):
        self.fill_text(lc.username_field, username_value)

    def enter_password(self, password_value):
        self.fill_text(lc.password_field, password_value)

    def click_to_login_button(self):
        self.click_element(lc.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_to_login_button()

    def PIM_module(self):
        self.click_element(lc.PIM)

    def employee(self, first_name, last_name):
        self.click_element(lc.e_list)
        self.fill_text(lc.e_firstname, first_name)
        self.fill_text(lc.e_lastname, last_name)
        self.click_element(lc.save_button)
        time.sleep(5)

    def pim_1(self, firstname, lastname):           #changes PIM to pim_1
        self.PIM_module()
        self.employee(firstname, lastname)
        time.sleep(5)

    def leave(self):
        self.click_element(lc.leave)
        time.sleep(2)
