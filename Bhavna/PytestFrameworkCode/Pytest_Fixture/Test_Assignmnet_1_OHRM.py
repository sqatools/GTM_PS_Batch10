import time

import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("get_driver")

class TestOHRM:
    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver = get_driver


    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME,"username").send_keys('Admin')
        self.driver.find_element(By.NAME,"password").send_keys('admin123')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)

    def test_admin(self):
        self.driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        self.driver.find_element(By.XPATH,"//div[contains(@class,'orangehrm-header')]//button[@type='button']").click()
        self.driver.find_element(By.XPATH,"//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][1]").click()
        self.driver.find_element(By.XPATH,"//div[@role='option']//span[text()='Admin']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[contains(@placeholder,'Type for')]").send_keys('Peter')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='oxd-autocomplete-option']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Enabled']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//label[text()='Username']//following::input[1]").send_keys('user_peter1')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//label[text()='Password']//following::input[1]").send_keys('Peter@1')
        self.driver.find_element(By.XPATH,"//label[text()='Password']//following::input[2]").send_keys('Peter@1')
        self.driver.find_element(By.XPATH,"//button[text()=' Save ']").click()
        time.sleep(10)

    def test_search_system_user(self):
        self.driver.find_element(By.XPATH,"//input[contains(@placeholder,'Type for')]").send_keys('Peter')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@role='listbox']//div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[text()=' Search ']").click()
        time.sleep(2)

    def test_delete(self):
        self.driver.find_element(By.XPATH,"//div[text()='user_peter1']//following::i[@class='oxd-icon bi-trash'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='orangehrm-modal-footer']//button[@type='button'][2]").click()
        time.sleep(5)

    def test_PIM(self):
        self.driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        time.sleep(5)

    def test_add_employee(self):
        self.driver.find_element(By.XPATH,"//div[contains(@class,'orangehrm-header')]//button[@type='button']").click()
        self.driver.find_element(By.NAME,"firstName").send_keys('Javed')
        time.sleep(2)
        self.driver.find_element(By.NAME,"lastName").send_keys('Khan')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
