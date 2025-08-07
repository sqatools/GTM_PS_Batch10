#from base.selenium_base import SeleniumBase
from .admin_page_locator import *
from base.selenium_base import *
#from selenium.webdriver.support import expected_conditions as ec

class AdminPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)


    def navigate_to_admin_page(self):
        self.click_element(admin_locator.admin_section_loc)


    def click_to_add_user_btn(self):
        self.click_element(admin_locator.add_user_btn)

    def select_user_role(self, role_name):
        self.click_element(admin_locator.user_role_dropdown)
        role_name_loc = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{role_name}')]")
        self.click_element(role_name_loc, cond=ec.element_to_be_clickable)





