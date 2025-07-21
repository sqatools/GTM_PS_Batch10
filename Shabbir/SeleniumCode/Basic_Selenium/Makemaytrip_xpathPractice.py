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




    # driver.implicitly_wait(20)
    # driver.find_element(By.ID,"email").send_keys("SHABBIR")c`
    # driver.implicitly_wait(10)
    # driver.find_element(By.NAME,"pass").send_keys("Shabbir@123")
    # driver.implicitly_wait(5)
    # driver.find_element(By.NAME,"login").click()

get_element()

