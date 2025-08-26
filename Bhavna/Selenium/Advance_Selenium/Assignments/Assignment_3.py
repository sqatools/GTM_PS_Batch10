# 28/07/2025 Session Assignment
# Automate OrangeHRM Website - Admin Module

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class AutomateOHRM:
    website_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.launch_website_url(url=self.website_url)

    def get_element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def launch_website_url(self,url):
        self.driver.get(url)
        time.sleep(3)

    def Login(self,username,password):
        self.get_element(locator=(By.NAME,"username")).send_keys(username)
        self.get_element(locator=(By.NAME,"password")).send_keys(password)
        self.get_element(locator=(By.XPATH,"//button[@type='submit']")).click()

    def Admin(self):
        self.get_element(locator=(By.XPATH,"//span[text()='Admin']")).click()
        time.sleep(2)


    def add_user(self):
        self.get_element(locator=(By.XPATH,"//div[contains(@class,'orangehrm-header')]//button[@type='button']")).click()
        self.get_element(locator=(By.XPATH,"//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][1]")).click()
        self.get_element(locator=(By.XPATH,"//div[@role='option']//span[text()='Admin']")).click()
        time.sleep(3)

    def add_Emp_Name(self,employee_name):
        self.get_element(locator=(By.XPATH,"//input[contains(@placeholder,'Type for')]")).send_keys(employee_name)
        time.sleep(5)
        self.get_element(locator=(By.XPATH,"//div[@class='oxd-autocomplete-option']")).click()
        time.sleep(5)

    def status(self):
        self.get_element(locator=(By.XPATH,"//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][2]")).click()
        self.get_element(locator=(By.XPATH,"//span[text()='Enabled']")).click()
        time.sleep(3)
    def username(self,username,password,c_pass):
        self.get_element(locator=(By.XPATH,"//label[text()='Username']//following::input[1]")).send_keys(username)
        time.sleep(5)
        self.get_element(locator=(By.XPATH,"//label[text()='Password']//following::input[1]")).send_keys(password)
        self.get_element(locator=(By.XPATH,"//label[text()='Password']//following::input[2]")).send_keys(c_pass)
        time.sleep(3)
        self.get_element(locator=(By.XPATH,"//button[text()=' Save ']")).click()
        time.sleep(8)

    def search_system_user(self, e_name):
        # self.get_element(locator=(By.XPATH, "//label[text()='Username']/following::input[1]")).send_keys(user_name)
        # self.get_element(locator=(By.XPATH,"//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][1]")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH, "//input[contains(@placeholder,'Type for')]")).send_keys(e_name)
        time.sleep(10)
        self.get_element(locator=(By.XPATH,"//div[@role='listbox']//div")).click()
        time.sleep(3)
        self.get_element(locator=(By.XPATH, "//button[text()=' Search ']")).click()

        time.sleep(5)
    def delete(self):
        self.get_element(locator=(By.XPATH,"//div[text()='sourabh_jain_8']//following::div//i[@class='oxd-icon bi-trash']")).click()
        self.get_element(locator=(By.XPATH,"//div[@class='orangehrm-modal-footer']//button[@type='button'][2]")).click()

        time.sleep(5)
        self.driver.close()


    def Admin_Module(self):
        self.Login('Admin','admin123')
        self.Admin()
        self.add_user()
        self.add_Emp_Name('Radha')
        self.status()
        self.username('sourabh_jain_1','Sourabh1','Sourabh1')
        time.sleep(8)
        self.search_system_user('Radha')
        # self.delete()
        time.sleep(5)

obj = AutomateOHRM()
obj.Admin_Module()