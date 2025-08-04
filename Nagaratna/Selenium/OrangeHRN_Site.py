import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
def orange_site():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@name="username"]').send_keys("Admin")
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@name="password"]').send_keys("admin123")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//i[contains(@class, 'oxd-topbar-header-hamburger')]").click()
orange_site()


