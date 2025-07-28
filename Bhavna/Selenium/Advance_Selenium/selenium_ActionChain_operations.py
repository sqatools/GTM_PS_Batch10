import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumActionchain:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

    def element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        elements = self.wait.until(ec.presence_of_all_elements_located(locator))
        return elements

    def launch_website_url(self,url):
        self.driver.get(url)

    def perform_mouse_hover(self):
        self.launch_website_url(url="https://www.nseindia.com/")
        time.sleep(3)
        market_data = self.element(locator=(By.XPATH,"//a[text()='Market Data']"))
        self.action.move_to_element(market_data).perform()
        time.sleep(5)

        derivative_market = self.element(locator=(By.XPATH,"//a[text()='Derivatives Market']"))
        self.action.click(derivative_market).perform()
        time.sleep(5)


        self.driver.close()


obj = SeleniumActionchain()
obj.perform_mouse_hover()