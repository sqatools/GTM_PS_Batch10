# 28/07/2025 Session

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ExecuteJavascript:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()

    def get_element(self,locator):
        """
                This method returns single element of specified locator
                :param locator:
                :return:
                """
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        """
        This method returns list of elements of specified locator
        :param locator:
        :return:
                """
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def HRM_Website(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        user_name = self.driver.execute_script(("return document.getElementsByName('username');"))
        user_name[0].send_keys
