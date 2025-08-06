from Base_Code.Base_Test_file import Base_Test_File
from openrhm_Page_locator import openhrm_locator as loc

class OpenHRM(Base_Test_File):

    def __init__(self,driver):
        super().__init__(driver)

    def open_login_page(self,url):
        self.driver.get(url)

    def enter_username(self,username_value):
        self.fill_text(loc.username_feild,username_value)

    def enter_password(self,password_value):
        self.fill_text(loc.password_field,password_value)

    def login_button(self):
        self.click_element(loc.login_button)


