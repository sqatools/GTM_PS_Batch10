# 28/07/2025 Session Assignment
# Automate OrangeHRM Website - PIM Module

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class AutomateOHRM:
    website_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

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
        time.sleep(2)

    def Login(self, username, password):
        self.get_element(locator=(By.NAME, "username")).send_keys(username)
        self.get_element(locator=(By.NAME, "password")).send_keys(password)
        self.get_element(locator=(By.XPATH, "//button[@type='submit']")).click()
        time.sleep(5)

    def PIM(self):
        self.get_element(locator=(By.XPATH,"//span[text()='PIM']")).click()
        time.sleep(10)

    def add(self,first_name,last_name):
        self.get_element(locator=(By.XPATH,"//div[contains(@class,'orangehrm-header')]//button[@type='button']")).click()
        self.get_element(locator=(By.NAME,"firstName")).send_keys(first_name)
        time.sleep(2)
        self.get_element(locator=(By.NAME,"lastName")).send_keys(last_name)
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//button[@type='submit']")).click()
        time.sleep(5)

    def empl_list(self):
        self.get_element(locator=(By.XPATH,"//label[text()='Female']")).click()
        self.get_element(locator=(By.XPATH,"//p[text()=' * Required']//following-sibling::button[@type='submit']")).click()
        time.sleep(3)



    def abc(self):
        self.Login('Admin','admin123')
        self.PIM()
        self.add('Employee','three')
        self.empl_list()


        time.sleep(5)
        self.driver.close()


obj = AutomateOHRM()
obj.abc()


