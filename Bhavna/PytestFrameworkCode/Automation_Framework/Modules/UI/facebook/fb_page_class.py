from ....Base.selenium_base1 import SeleniumBase
from .fb_page_locator import Fbloc


class fbpage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def select_login_page(self,url):
        self.driver.get(url)

    def enter_username(self,username):
        self.fill_text(Fbloc.fb_username_field,username)

    def enter_password(self,password):
        self.fill_text(Fbloc.fb_password_field,password)

    def click_login_button(self):
        self.click_element(Fbloc.fb_login_button)

    def fb_login(self,username1,password1):
        self.enter_username(username1)
        self.enter_password(password1)
        self.click_login_button()
