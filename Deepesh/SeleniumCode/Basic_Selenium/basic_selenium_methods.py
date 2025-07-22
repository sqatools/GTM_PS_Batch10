import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumMethods:

    def __init__(self, url, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url


    def get_text_of_element(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        element = self.driver.find_element(By.XPATH, "//div[contains(text(),'quick and easy')]//preceding-sibling::div")
        return element.text

    def check_enable_displayed_selected(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        radio_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='1']")
        print("check radio button is enabled :", radio_button.is_enabled())
        print("check radio button is displayed :", radio_button.is_displayed())
        print("check radio button is selected before click :", radio_button.is_selected())
        radio_button.click()
        time.sleep(5)
        print("check radio button is selected after click :", radio_button.is_selected())










obj = SeleniumMethods(url='https://www.facebook.com')
obj.check_enable_displayed_selected()
"""
check radio button is enabled : True
check radio button is displayed : True
check radio button is selected before click : False
check radio button is selected after click : True

"""
# print(obj.get_text_of_element())
# print(obj.get_current_url())
# print(obj.get_title())

