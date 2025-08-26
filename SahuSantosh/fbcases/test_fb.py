from time import sleep

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class TestFbCase:

    @pytest.fixture(autouse=True)
    def d_setup(self, setup):
        self.f = setup

    def find_element(self, locator, value):
        self.f.find_element(*locator).send_keys(value)

    def dropdownsel(self, loc, vtext):
        Select(self.f.find_element(*loc)).select_by_visible_text(vtext)

    def rb(self, l):
        self.f.find_element(*l).click()

    def test_fblogin(self):
        self.find_element((By.ID, 'email'), 'hai')
        self.f.find_element(By.ID, 'pass').send_keys('coolk1234')
        self.f.find_element(By.NAME, 'login').click()
        sleep(3)

    def test_signup(self):
        self.f.get('https://www.facebook.com/r.php?locale=en_GB&display=page')
        self.find_element((By.NAME, 'firstname'), 'chiru')
        self.find_element((By.NAME, 'lastname'), 'mega')
        sleep(1)
        self.dropdownsel((By.ID, 'day'), "28")
        sleep(1)
        self.dropdownsel((By.ID, 'month'), "Dec")
        sleep(1)
        self.dropdownsel((By.ID, 'year'), "2019")
        sleep(1)
        self.rb((By.XPATH, "//*[@data-name='gender_wrapper']//label[contains(text(),'Male')]"))
        sleep(1)
        self.find_element((By.XPATH, "//*[contains(@aria-label,'Mobile number')]"), '798959')
        sleep(1)
        self.find_element((By.XPATH, "//*[contains(@class,'inputtext _') and @type='password']"), '12346789')
        sleep(3)
