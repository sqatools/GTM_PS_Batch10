import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class HandleDropdown:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()

    def get_element(self, locator):
        """
        This method returns single element of specified locator
        :param locator:
        :return:
        """
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self, locator):
        """
        This method returns list of elements of specified locator
        :param locator:
        :return:
        """
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def select_value_from_dropdown(self, locator):
        dropdown_element = self.get_element(locator)
        select = Select(dropdown_element)
        return select


    def select_value_by_visible_text(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID, "admorepass"))
        select_obj = Select(dd_element)
        select_obj.select_by_visible_text("Add 3 more passenger (200%)")
        time.sleep(5)

    def select_dropdown_data_by_value(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID, "billing_country"))
        select_obj = Select(dd_element)
        select_obj.select_by_value("BE")
        time.sleep(5)

    def select_dropdown_data_by_index(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID, "billing_country"))
        select_obj = Select(dd_element)
        select_obj.select_by_index(5)
        time.sleep(5)

    def get_all_dropdown_data(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.ID, "billing_country"))
        select_obj = Select(dd_element)
        data = select_obj.options
        for val in data:
            print(val.text)
        time.sleep(5)


    def select_dropdown_data_by_index_framework(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        self.select_value_from_dropdown(locator=(By.ID, "billing_country")).select_by_index(5)
        options_list = self.select_value_from_dropdown(locator=(By.ID, "billing_country")).options
        for val in options_list:
            print(val.text)
        time.sleep(5)

    def perform_dropdown_operations(self):
        self.select_value_by_visible_text()
        self.select_dropdown_data_by_value()
        self.select_dropdown_data_by_index()
        self.get_all_dropdown_data()
        #self.enter_first_name()

    def enter_first_name(self, user_name):
        user_name = self.get_element("locator")
        user_name.send_keys(user_name)


obj = HandleDropdown()
# obj.select_value_by_visible_text()
# obj.select_dropdown_data_by_value()
# obj.select_dropdown_data_by_index()
# obj.get_all_dropdown_data()
obj.perform_dropdown_operations()



# Home work:
# automate the entire dummy website page with framework concept.
# https://sqatools.in/dummy-booking-website/

# weekend Home work
# https://www.goibibo.com/




