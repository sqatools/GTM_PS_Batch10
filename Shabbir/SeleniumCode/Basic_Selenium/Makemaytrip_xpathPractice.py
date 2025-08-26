import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
def get_element():
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    driver.find_element(By.CLASS_NAME,'commonModal__close').click()
    driver.implicitly_wait(3)

    driver.find_element(By.XPATH,"//li[@class='menu_Buses']").click()
    city_from = driver.find_element(By.XPATH,"//span[text()='From']")
    city_from.click()
    time.sleep(5)
    From=driver.find_element(By.XPATH, "//input[@placeholder='From']")
    time.sleep(10)
    From.send_keys('Bangalore')
    time.sleep(10)
    From.send_keys(Keys.ARROW_DOWN)
    time.sleep(10)
    From.send_keys(Keys.ENTER)
    time.sleep(10)

    To_drive = driver.find_element(By.XPATH,"//span[text()='To']")
    time.sleep(10)
    To_drive.click()
    To_drive.send_keys('Hopset,')
    time.sleep(10)
    To_drive.send_keys(Keys.ARROW_DOWN)
    time.sleep(10)
    To_drive.send_keys(Keys.ENTER)
    time.sleep(5)



get_element()

