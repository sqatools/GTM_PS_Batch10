import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumActionChain:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

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

    def launch_website_url(self, url):
        self.driver.get(url)

    def perform_mouse_hover_operation(self):
        self.launch_website_url(url="https://www.nseindia.com/")
        time.sleep(5)
        market_data_element = self.get_element(locator=(By.XPATH, "//a[text()='Market Data']"))
        self.action.move_to_element(market_data_element).perform()
        time.sleep(5)

        derivative_market_elem = self.get_element(locator=(By.XPATH, "//a[text()='Derivatives Market']"))
        self.action.click(derivative_market_elem).perform()
        time.sleep(5)






obj = SeleniumActionChain()
obj.perform_mouse_hover_operation()

