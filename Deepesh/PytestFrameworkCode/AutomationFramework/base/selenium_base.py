import logging
from datetime import datetime
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

    def take_screenshot(self, *args):
        self.log.info(f"{args}")
        # get logs folder path
        log_path = os.path.join(os.getcwd(), "logs")
        # get images folder path
        images_path = os.path.join(log_path, "images")
        # check images folder is available, if not, then create new folder
        if not os.path.exists(images_path):
            os.mkdir(images_path)
        # generate unique file name
        file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # png file name
        png_file_name = f"{file_name}.png"
        # screenshot file path
        file_path = os.path.join(images_path, png_file_name)
        # add screenshot file path in log file
        self.log.info(f"screenshot: {file_path}")
        # take screenshot and save it to target path.
        self.driver.save_screenshot(file_path)

    def get_element(self, locator, cond=ec.visibility_of_element_located):
        self.log.info(f"finding element with locator: {locator}")
        try:
            element = self.wait.until(cond(locator))
            return element
        except Exception as e:
            self.take_screenshot("get_element")
            self.log.info(f"{e}")
            raise

    def click_element(self, locator, **kwargs):
        self.log.info(f"clicking on {locator}")
        try:
            element = self.get_element(locator=locator, **kwargs)
            element.click()
        except Exception as e:
            self.take_screenshot("click_element")
            self.log.info(f"{e}")
            raise

    def fill_text(self, locator, value):
        self.log.info(f"entering text: {value} on {locator}")
        try:
            element = self.get_element(locator=locator)
            element.send_keys(value)
        except Exception as e:
            self.take_screenshot("fill_text")
            self.log.info(f"{e}")
            raise

    def get_text(self, locator):
        self.log.info(f"getting text of: {locator}")
        try:
            element = self.get_element(locator=locator)
            return element.text
        except Exception as e:
            self.take_screenshot("get_text")
            self.log.info(f"{e}")
            raise

    def select_dropdown_value(self, locator, value):
        self.log.info(f"selecting dropdown value {value} of locator: {locator}")
        try:
            element = self.get_element(locator=locator)
            select = Select(element)
            select.select_by_visible_text(value)
        except Exception as e:
            self.take_screenshot("select_dropdown_value")
            self.log.info(f"{e}")
            raise
