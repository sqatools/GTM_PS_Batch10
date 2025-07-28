# 15/07/2025 Session Homework
# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def get_element_by_name():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.find_element(By.XPATH,"//input[@value='radio_345']").click()
    driver.find_element(By.NAME,"firstname").send_keys("Aastha")
    driver.find_element(By.XPATH,"//td[text()='Mumbai']//preceding::input[@id='firstname'][1]").send_keys("Aagrawal")
    driver.find_element(By.ID,"birthday").send_keys("04-06-2003")
    driver.find_element(By.ID,"female").click()
    driver.find_element(By.ID,"admorepass").click()
    driver.find_element(By.XPATH,"//option[@value='2']").click()
    driver.find_element(By.XPATH,"//input[@id='oneway']").click()
    time.sleep(1)
    driver.find_element(By.NAME,"fromcity").send_keys("Dubai")
    driver.find_element(By.NAME,"destcity").send_keys("Delhi")
    driver.find_element(By.NAME,"departdate").send_keys("18-07-2025")
    driver.find_element(By.NAME,"returndate").send_keys("21-07-2025")
    # driver.find_element(By.ID,"eamil").click()
    driver.find_element(By.XPATH,"//td[text()='Mumbai']//preceding::input[@id='female'][1]").click()
    driver.find_element(By.ID,"billing_name").send_keys("Rajesh Rana")
    driver.find_element(By.ID,"billing_phone").send_keys("9876543211")
    driver.find_element(By.ID,"billing_email").send_keys("rajesh@gmail.com")
    driver.find_element(By.ID,"billing_address").send_keys("Abc street, delhi")
    driver.find_element(By.XPATH,"//option[@vlaue='IN']").click()
    driver.find_element(By.NAME,"postcode").send_keys("440018")
    driver.find_element(By.XPATH,"//b[text()='Street address*']//following::input[@id='street_address1']").send_keys("House no.6")
    driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys("Bangalore")
    driver.find_element(By.XPATH,"//td[text()='Delhi']//preceding::input[@type='checkbox'][5]").click()
    # driver.find_element(By.XPATH,"//td[text()='Delhi']//preceding-sibling::td[2]").click()

    time.sleep(5)
    driver.close()

get_element_by_name()
