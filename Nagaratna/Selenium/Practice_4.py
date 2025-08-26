"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def practice_4():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    driver.find_element(By.XPATH,'//*[@name="q"]').send_keys("python interview questions")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="jZ2SBf"]/div[1]/span').click()

    time.sleep(5)
practice_4()
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def practice5():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@class="oxd-input oxd-input--active"]').send_keys("Leave")
    time.sleep(3)
    driver.find_element(By.XPATH,'//span[text()="Leave"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//span[@class="oxd-topbar-body-nav-tab-item"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//a[@class="oxd-topbar-body-nav-tab-link"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"]').click()
    time.sleep(5)
    options=driver.find_element(By.XPATH,'//div[@class="oxd-select-text-input"]').click()
    options.send_keys("")
    time.sleep(3)
practice5()

