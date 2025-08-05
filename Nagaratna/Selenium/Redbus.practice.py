import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def redbus_find():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.redbus.com")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@id="src"]').send_keys("Bangalore, Karnataka, India")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@id="dest"]').send_keys("Honavar, Karnataka, India")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@id="onward_cal"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//div[text()="From"]').click()
    driver.find_element((By.XPATH,'//div[text()="To"]')).click()
    driver.find_element(By.XPATH,'//div[text() ="Booking for women"]').click()
    driver.find_element(By.XPATH,'//button[text()="Search buses"]').click()
    
redbus_find()


