from ....base.selenium_base import SeleniumBase
from .fb_page_locator import FBLoc


class FBPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_page(self, url):
        self.driver.get(url)

    def enter_fb_username(self, fb_username):
        self.fill_text(FBLoc.fb_username_field, fb_username)

    def enter_fb_password(self, fb_password):
        self.fill_text(FBLoc.fb_password_field, fb_password)

    def click_fb_login_button(self):
        self.click_element(FBLoc.fb_login_button)

    def fb_login(self, username, password):
        self.enter_fb_username(username)
        self.enter_fb_password(password)
        self.click_fb_login_button()
