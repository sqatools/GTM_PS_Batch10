import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
@pytest.mark.usefixtures("get_driver")
class TestFacebook:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver = get_driver

    def select_dd(self,locator,value):
        element = self.driver.find_element(*locator)
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)

    def test_facebook_login(self):
        self.driver.find_element(By.NAME,"email").send_keys("user2@gmail.com")
        self.driver.find_element(By.NAME,"pass").send_keys("user1234")
        self.driver.find_element(By.NAME,"login").click()
        time.sleep(10)

    def test_facebook_signup(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.find_element(By.NAME,"firstname").send_keys("Dummy")
        self.driver.find_element(By.NAME,"lastname").send_keys("Data")
        self.select_dd(locator=(By.ID,"day"),value='14')
        self.select_dd(locator=(By.ID,"month"),value='Apr')
        self.select_dd(locator=(By.ID,"year"),value='2017')
        self.driver.find_element(By.XPATH,"//label[text()='Female']").click()
        self.driver.find_element(By.XPATH,"//input[@aria-label='Mobile number or email address']").send_keys("9898989898")
        self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys('123456789')
        self.driver.find_element(By.NAME,"websubmit").click()
        time.sleep(10)