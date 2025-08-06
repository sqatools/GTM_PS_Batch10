import time

from Base.selenium_base1 import SeleniumBase
from .openhrm_page_locator1 import Openhrm_locator as lc

class OpenHRM(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self,url):
        self.driver.get(url)

    def enter_username(self,username_value):
        self.fill_text(lc.username_field,username_value)

    def enter_password(self,password_value):
        self.fill_text(lc.password_field,password_value)

    def click_to_login_button(self):
        self.click_element(lc.login_button)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_to_login_button()

    def click_on_admin(self):
        self.click_element(lc.choose_admin)

    def add_user(self):
        self.click_element(lc.add_user)
        self.click_element(lc.select_dd)
        self.click_element(lc.select_admin_dd)

    def e_name(self,e_name1):
        self.fill_text(lc.e_name,e_name1)
        time.sleep(5)
        self.click_element(lc.select_employee)

    def status(self):
        self.click_element(lc.status)
        self.click_element(lc.e_status)

    def e_username_password(self,e_username1,e_password1,c_password1):
        self.fill_text(lc.e_username,e_username1)
        self.fill_text(lc.e_password,e_password1)
        self.fill_text(lc.c_password,c_password1)
        self.click_element(lc.save_button)
        time.sleep(5)

    def system_user(self,user_name):
        self.fill_text(lc.s_username,user_name)
        time.sleep(5)
        self.click_element(lc.search_user)
        time.sleep(3)

    def delete_user(self):
        self.click_element(lc.delete1_user)
        time.sleep(3)
        self.click_element(lc.delete2_user)
        self.click_element(lc.reset)

    def job(self,jobtitle,desc):
        self.click_element(lc.admin_job)
        self.click_element(lc.job_title)
        self.click_element(lc.add_title)
        self.fill_text(lc.add_jobtitle,jobtitle)
        self.fill_text(lc.add_desc,desc)
        self.click_element(lc.save_button)
        time.sleep(5)

    def admin(self,employee_name,eusername,epassword,cpassword,username,title,description):
        self.click_on_admin()
        self.add_user()
        self.e_name(employee_name)
        self.status()
        self.e_username_password(eusername,epassword,cpassword)
        self.system_user(username)
        self.delete_user()
        self.job(title,description)
        time.sleep(3)


    def PIM_module(self):
        self.click_element(lc.PIM)

    def employee(self,first_name,last_name):
        self.click_element(lc.e_list)
        self.fill_text(lc.e_firstname,first_name)
        self.fill_text(lc.e_lastname,last_name)
        self.click_element(lc.save_button)
        time.sleep(5)

    def PIM(self,firstname,lastname):
        self.PIM_module()
        self.employee(firstname,lastname)
        time.sleep(5)

    def leave(self):
        self.click_element(lc.leave)
        time.sleep(2)

