import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class Handledropdown:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()

    def get_element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def select_value_from_dropdown(self,locator):
        dropdown_element = self.get_element(locator)
        select = Select(dropdown_element)
        return select

    def select_value_by_visible_text(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID,"admorepass"))
        select_obj = Select(dd_element)
        select_obj.select_by_visible_text("Add 2 more passenger (200%)")
        time.sleep(5)

    def select_value_by_value(self):
        # self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID,"billing_country"))
        select_obj = Select(dd_element)
        select_obj.select_by_value("BB")
        time.sleep(3)

    def select_dd_by_index(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(3)
        dd_element = self.get_element(locator=(By.ID,"billing_country"))
        select_obj = Select(dd_element)
        select_obj.select_by_index(2)
        time.sleep(2)

    def get_all_data(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(3)
        dd_element = self.get_element(locator=(By.ID,"billing_country"))
        select_obj = Select(dd_element)
        data = select_obj.options
        for val in data:
            print(val.text)

        time.sleep(3)

    def perform_dropdown_operations(self):
        self.select_value_by_visible_text()
        self.select_value_by_value()
        self.select_dd_by_index()
        self.get_all_data()

        self.driver.close()


obj = Handledropdown()
# obj.select_value_by_visible_text()
# obj.select_value_by_value()
# obj.select_dd_by_index()
# obj.get_all_data()
obj.perform_dropdown_operations()