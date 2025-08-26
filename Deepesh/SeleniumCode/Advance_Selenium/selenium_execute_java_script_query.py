import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ExecuteJavaScript:
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


    def HRM_Website(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("URL :", self.driver.execute_script("return document.URL;"))
        print("title :", self.driver.execute_script("return document.title;"))
        time.sleep(10)
        user_name_field = self.driver.execute_script("return document.getElementsByName('username');")
        user_name_field[0].send_keys("Admin")

        password_field = self.driver.execute_script("return document.getElementsByName('password');")
        password_field[0].send_keys("admin123")

        self.get_element(locator=(By.XPATH, "//button[contains(@class, 'angehrm-login-button')]")).click()

        time.sleep(10)



obj = ExecuteJavaScript()
obj.HRM_Website()