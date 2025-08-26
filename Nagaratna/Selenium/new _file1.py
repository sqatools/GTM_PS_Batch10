import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(6)
def get_element_with_id():
    driver.get("https://www.instagram.com")
    email_element=driver.find_element(By.NAME, "username")
    email_element.send_keys("magu@gmai.com")
    pass_element=driver.find_element(By.NAME, "password")
    print(pass_element)
    pass_element.send_keys("Test@1234")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
get_element_with_id()
