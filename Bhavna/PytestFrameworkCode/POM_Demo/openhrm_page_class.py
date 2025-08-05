import time

from selenium_base import SeleniumBase
from openhrm_page_locator import *

class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self,url):
        self.driver.get(url)

    def enter_username(self,username_value):
        self.fill_text(username_field,username_value)

    def enter_password(self,password_value):
        self.fill_text(password_field,password_value)

    def click_to_login_button(self):
        self.click_element(login_button)

    def click_on_admin(self):
        self.click_element(choose_admin)

    def add_user(self):
        self.click_element(add_user)
        self.click_element(select_dd)
        self.click_element(select_admin_dd)

    def e_name(self,e_name1):
        self.fill_text(e_name,e_name1)
        time.sleep(5)
        self.click_element(select_employee)

    def status(self):
        self.click_element(status)
        self.click_element(e_status)

    def e_username_password(self,e_username1,e_password1,c_password1):
        self.fill_text(e_username,e_username1)
        self.fill_text(e_password,e_password1)
        self.fill_text(c_password,c_password1)
        self.click_element(save_button)
        time.sleep(5)

    def system_user(self,user_name):
        self.fill_text(s_username,user_name)
        time.sleep(5)
        self.click_element(search_user)
        time.sleep(3)

    def delete_user(self):
        self.click_element(delete1_user)
        time.sleep(3)
        self.click_element(delete2_user)
        self.click_element(reset)

    def job(self,jobtitle,desc):
        self.click_element(admin_job)
        self.click_element(job_title)
        self.click_element(add_title)
        self.fill_text(add_jobtitle,jobtitle)
        self.fill_text(add_desc,desc)
        self.click_element(save_button)

    def PIM_module(self):
        self.click_element(PIM)


