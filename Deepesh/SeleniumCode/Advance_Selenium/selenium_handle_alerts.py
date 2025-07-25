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
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.launch_website_url(url=self.website_url)
        self.alert = Alert(self.driver)


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


    def handle_alert_box(self):
        time.sleep(5)
        self.get_element(locator=(By.ID, "btnShowMsg")).click()
        print("Alert msg :", self.alert.text)
        time.sleep(5)
        self.alert.accept()

    def handle_confirm_box(self, confirm_value, confirm_msg):
        time.sleep(5)
        self.get_element(locator=(By.ID, "button")).click()
        time.sleep(3)
        if confirm_value == 'yes':
            print("msg :", self.alert.text)
            self.alert.accept()
            time.sleep(5)
            accept_msg = self.get_element(locator=(By.ID, "demo")).text
            assert accept_msg == confirm_msg
        else:
            print("msg :", self.alert.text)
            self.alert.dismiss()
            time.sleep(5)
            accept_msg = self.get_element(locator=(By.ID, "demo")).text
            assert accept_msg == confirm_msg


    def handle_prompt_box(self, confirm_value, prompt_input, confirm_msg):
        time.sleep(5)
        self.get_element(locator=(By.ID, "promptbtn")).click()
        time.sleep(3)
        if confirm_value == 'yes':
            print("msg :", self.alert.text)
            self.alert.send_keys(prompt_input)
            time.sleep(3)
            self.alert.accept()
            time.sleep(5)
            accept_msg = self.get_element(locator=(By.ID, "prompt")).text
            assert accept_msg == confirm_msg
        else:
            print("msg :", self.alert.text)
            self.alert.dismiss()
            time.sleep(5)
            accept_msg = self.get_element(locator=(By.ID, "prompt")).text
            assert accept_msg == confirm_msg





obj = HandleAlerts()
#obj.handle_alert_box()
#obj.handle_confirm_box(confirm_value='yes', confirm_msg='You pressed OK!')
#obj.handle_confirm_box(confirm_value='No', confirm_msg='You pressed Cancel!')
#obj.handle_prompt_box(confirm_value='yes', confirm_msg='Hello SQATools! How are you today?', prompt_input="SQATools")
#obj.handle_prompt_box(confirm_value='yes', confirm_msg='User cancelled the prompt.', prompt_input="")











