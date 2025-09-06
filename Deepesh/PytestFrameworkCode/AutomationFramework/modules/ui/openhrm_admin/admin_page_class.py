#from base.selenium_base import SeleniumBase
from .admin_page_locator import *
from ....base.selenium_base import *
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

    def set_user_status(self, user_status):
        self.click_element(admin_locator.status_dropdown)
        user_status_loc = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{user_status}')]")
        self.click_element(user_status_loc, cond=ec.element_to_be_clickable)

    def enter_new_username(self, new_username):
        self.fill_text(admin_locator.username_name_field, new_username)

    def enter_new_password(self, new_password):
        self.fill_text(admin_locator.user_password_field, new_password)

    def enter_confirm_password(self, confirm_password):
        self.fill_text(admin_locator.confirm_password_field, confirm_password)

    def select_employee_name(self, emp_name):
        self.fill_text(admin_locator.employee_name_field, emp_name)
        emp_name_loc = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{emp_name}')]")
        self.click_element(emp_name_loc)

    def click_on_save_button(self):
        self.click_element(admin_locator.save_button)

    def add_user_details(self):
        pass