import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=None

def get_web_browser(browser):
    if browser.lower()=="chrome":
        driver=webdriver.Chrome()
    if browser.lower()=="edge":
        driver=webdriver.edge()
    return driver

driver=get_web_browser("chrome")

driver.maximize_window()
driver.implicitly_wait(20)

def get_elemnt_with_xpath():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    time.sleep(6)
    driver.find_element(By.XPATH,"//input[@value='radio_123']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Harsh")
    time.sleep(3)
    driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Sharma")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("22-11-1996")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='male']").click()
    time.sleep(3)
    sub_heading=driver.find_element(By.TAG_NAME,"h2")
    print(sub_heading)
    time.sleep(3)
    driver.find_element(By.XPATH,"(//input[@value='checkbox'])[1]").click()
    time.sleep(3)

get_elemnt_with_xpath()

