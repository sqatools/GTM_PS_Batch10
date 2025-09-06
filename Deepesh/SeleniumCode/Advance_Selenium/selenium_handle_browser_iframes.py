import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HandleIframes:
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

    def handle_iframes(self):
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
        time.sleep(5)
        heading_locator = (By.XPATH, "//div[@class='page_heading']/h1")
        main_page_heading = self.get_element(locator=heading_locator)
        print("Main Page Heading :", main_page_heading.text)

        iframe_loc = (By.XPATH, "//iframe[@name='globalSqa']")
        iframe_elem = self.get_element(locator=iframe_loc)

        # switch to iframe
        self.driver.switch_to.frame(iframe_elem)

        # get iframe heading
        iframe_heading = self.get_element(locator=heading_locator)
        print("iframe heading text :", iframe_heading.text)

        # click on menu in iframe
        self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu_toggler']")).click()
        time.sleep(3)

        # get cheatsheets option iframe
        self.get_element(locator=(By.XPATH, "//div[@id='mobile_menu']//a[text()='CheatSheets']")).click()
        time.sleep(3)


        # switch back to main page
        self.driver.switch_to.default_content()

        # get menu from main page and click
        freebook_menu_loc = (By.XPATH, "//div[@id='menu']//a[text()='Free Ebooks']")
        freebook_menu_elem = self.get_element(locator=freebook_menu_loc)
        freebook_menu_elem.click()

        time.sleep(5)
        self.driver.close()


obj = HandleIframes()
obj.handle_iframes()






