import logging
from datetime import  datetime
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        self.log.info(f"finding element with locator: {locator}")
        try:
            element = self.wait.until(cond(locator))
            return element
        except Exception as e:
            file_name = datetime.now().strftime("Y%_%m_%d_%H_%M_%S")
            file_path = os.path.join(os.curdir, file_name)
            self.log.info(f"{file_path}")
            self.log.info(f"{e}")

    def click_element(self, locator, **kwargs):
        self.log.info(f"clicking on {locator}")
        element = self.get_element(locator=locator, **kwargs)
        element.click()

    def fill_text(self, locator, value):
        self.log.info(f"entering text: {value} on {locator}")
        element = self.get_element(locator=locator)
        element.send_keys(value)

    def get_text(self, locator):
        self.log.info(f"getting text of: {locator}")
        element = self.get_element(locator=locator)
        return element.text

    def select_dropdown_value(self, locator, value):
        self.log.info(f"selecting dropdown value {value} of locator: {locator}")
        element = self.get_element(locator=locator)
        select = Select(element)
        select.select_by_visible_text(value)
