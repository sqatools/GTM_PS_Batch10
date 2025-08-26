import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("get_driver")
class TestFacebook:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver

    def select_dropdown_value(self, locator, value):
        element = self.driver.find_element(*locator)
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)


    def test_facebook_login(self):
        self.driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("user12345")
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(10)


    def test_facebook_singup(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.find_element(By.NAME, "firstname").send_keys("John")
        self.driver.find_element(By.NAME, "lastname").send_keys("Jack")
        self.select_dropdown_value(locator=(By.ID, "day"), value='10')
        self.select_dropdown_value(locator=(By.ID, "month"), value='May')
        self.select_dropdown_value(locator=(By.ID, "year"), value='2002')
        time.sleep(10)


# Home Work
# write 5 test cases from given website
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 1.   login
# 2.   Admin
# 3.   PIM
# 4.   Time
# 5    Recruitment