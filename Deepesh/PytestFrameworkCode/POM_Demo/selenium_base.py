from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator=locator)
        element.click()

    def fill_text(self, locator, value):
        element = self.get_element(locator=locator)
        element.send_keys(value)

    def get_text(self, locator):
        element = self.get_element(locator=locator)
        return element.text

    def select_dropdown_value(self, locator, value):
        element = self.get_element(locator=locator)
        select = Select(element)
        select.select_by_visible_text(value)







