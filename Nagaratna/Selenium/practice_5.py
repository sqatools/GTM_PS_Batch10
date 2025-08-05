import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def practice_5():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(5)
practice_5()