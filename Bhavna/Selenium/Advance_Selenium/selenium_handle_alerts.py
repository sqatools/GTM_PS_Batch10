# 25/07/2025 Session

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

class HandleAlerts:
    website_url = "https://automationbysqatools.blogspot.com/2020/08/alerts.html"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.launch_website_url(url=self.website_url)
        self.alert = Alert(self.driver)

    def get_element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def launch_website_url(self,url):
        self.driver.get(url)

    def handle_alert(self):
        time.sleep(3)
        self.get_element(locator=(By.ID,"btnShowMsg")).click()
        print("Alert msg:",self.alert.text)
        time.sleep(5)
        self.alert.accept()

    def handle_confirm_box(self,con_value,con_msg):
        time.sleep(3)
        self.get_element(locator=(By.ID,"button")).click()
        time.sleep(3)
        if con_value == 'yes':
            print('msg:',self.alert.text)
            self.alert.accept()
            time.sleep(5)
            accept_msg = self.get_element(locator=(By.ID,"demo")).text
            assert accept_msg == con_msg
        else:
            print("msg:",self.alert.text)
            self.alert.dismiss()
            time.sleep(3)
            acccept_msg = self.get_element(locator=(By.ID,"demo")).text
            assert acccept_msg == con_msg






obj = HandleAlerts()
# obj.handle_alert()
obj.handle_confirm_box('yes','You pressed OK!')