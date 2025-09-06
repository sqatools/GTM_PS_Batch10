# 23/07/2025 Session

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BrowserTabs:
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

    def handle_multiple_browsers_tabs(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # get software testing principle locator
        testing_principle_locator = (By.LINK_TEXT,"Software Testing Principles")
        testing_element = self.get_element(testing_principle_locator)
        testing_element.click()
        time.sleep(3)

        # get list of windows
        windows_list = self.driver.window_handles

        # Navigate to new window tab
        self.driver.switch_to.window(windows_list[1])

        # get list of all the testing principle headings
        headings_locator = (By.XPATH,"//h3//span")
        elements_list = self.get_elements(headings_locator)
        for elem in elements_list:
            print(elem.text)

        # Navigate to back to original tab.
        self.driver.switch_to.window(windows_list[0])

        rf_locator = (By.LINK_TEXT,"Robot Framework")
        rf_element = self.get_element(rf_locator)
        rf_element.click()

        time.sleep(5)

        # Navigate to back to new window tab to close it.
        self.driver.switch_to.window(windows_list[1])
        time.sleep(5)
        self.driver.close()

    def handles_tabs_with_titles(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
        links_text_list = ['Software Testing Methods','Black Box Testing','Grey Box Testing','White Box Testing']
        for links_text_val in links_text_list:
            link_loc = (By.LINK_TEXT,links_text_val)
            self.get_element(link_loc).click()
            time.sleep(3)

        # get list of windows tabs
        windows_list = self.driver.window_handles
        titles_list=[]
        for i in range(1,len(windows_list)):
            self.driver.switch_to.window(windows_list[i])
            titles_list.append(self.driver.title)
            time.sleep(3)

        print("titles list:",titles_list)

        # switch to original tab
        self.driver.switch_to.window(windows_list[0])
        time.sleep(2)

        # switch to each tab with the help of title and close it.
        temp = 1
        for title in titles_list:
            print(title)
            self.driver.switch_to.window(windows_list[temp])

            assert title == self.driver.title
            temp += 1

            time.sleep(3)
            self.driver.close()

        # switch to original tab and close original tab as well
        self.driver.switch_to.window(windows_list[0])
        time.sleep(2)
        self.driver.close()


obj = BrowserTabs()
# obj.handle_multiple_browsers_tabs()
obj.handles_tabs_with_titles()