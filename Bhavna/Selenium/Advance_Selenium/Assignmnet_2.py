# 24/07/2025 Session Assignment
# Automate this website - " https://www.goibibo.com/"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Automate_goibibo:

    website_url = "https://www.goibibo.com/"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.launch_website_url(url=self.website_url)

    def get_element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def launch_website_url(self,url):
        self.driver.get(url)
        time.sleep(2)

    def pop_up(self):
        try:
            self.get_element(locator=(By.XPATH,"//span[@class='logSprite icClose']")).click()
            self.get_element(locator=(By.XPATH,"//div[@data-id='dweb_pip_id']//p[@class='sc-jlwm9r-1 ewETUe']")).click()
        except:
            pass
        time.sleep(2)

    def choose(self):
        self.get_element(locator=(By.XPATH,"//p[text()='Round-trip']//preceding-sibling::span")).click()
        time.sleep(2)

    def city(self,f_city,t_city):
        self.get_element(locator=(By.XPATH,"//span[text()='From']//following-sibling::p")).click()
        self.get_element(locator=(By.XPATH,"//input[@type='text']")).send_keys(f_city)
        self.get_element(locator=(By.XPATH,"//li[@tabindex='0']")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//input[@type='text']")).send_keys(t_city)
        self.get_element(locator=(By.XPATH,"//li[@tabindex='0']")).click()
        time.sleep(2)

    def dates(self):
        self.get_element(locator=(By.XPATH,"//span[text()='Departure']")).click()
        time.sleep(2)
        self.get_element(locator=(By.XPATH,"//div[@aria-label='Fri Aug 08 2025']")).click()
        self.get_element(locator=(By.XPATH,"//div[@aria-label='Fri Aug 15 2025']")).click()
        time.sleep(3)

    def travellers_n_search(self):
        self.get_element(locator=(By.XPATH,"//p[text()='economy']")).click()
        self.get_element(locator=(By.XPATH,"//p[text()='Adults']//following::div//span[text()=1]//following-sibling::span")).click()
        self.get_element(locator=(By.XPATH,"//a[text()='Done']")).click()
        self.get_element(locator=(By.XPATH,"//span[text()='SEARCH FLIGHTS']")).click()
        # time.sleep(3)
        try:
            self.get_element(locator=(By.XPATH,"//button[text()='OKAY, GOT IT!']")).click()
        except:
            pass


        time.sleep(5)
        self.driver.close()

    def goibibo(self):
        self.pop_up()
        self.choose()
        self.city('Nagpur','Pune')
        self.dates()
        self.travellers_n_search()

obj = Automate_goibibo()
obj.goibibo()

