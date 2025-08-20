from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

class Base_Test_File:
    def __int__(self,driver,timeout=20):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout)

    def get_element(self,locator,condn=ec.visibility_of_element_located):
        element=self.wait.until(condn(locator))
        return element

    def click_element(self,locator):
        element=self.get_element(locator=locator)
        element.click()

    def fill_text(self,locator,values):
        element=self.get_element(locator=locator)
        element.send_keys(values)

    def get_text(self,locator):
        element=self.get_element(locator=locator)
        return element.text

    def Select_dropdown(self,locator,value):
        element=self.get_element(locator=locator)
        select=Select(element)
        Select.select_by_visible_text(value)





