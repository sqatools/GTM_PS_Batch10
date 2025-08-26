import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def get_browser(browser):
    if browser.lower() == 'chrome':
        return webdriver.Chrome()
    elif browser.lower() == 'edge':
        return webdriver.Edge()
    elif browser.lower() == 'firefox':
        return webdriver.Firefox()

driver = get_browser('chrome')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "//input[@value='radio_345']").click()

driver.find_element(By.ID, "firstname").send_keys("Prasanna")
driver.find_element(By.ID, "firstname").send_keys("Suraj")
driver.find_element(By.ID, "birthday").send_keys("25-07-2025")
driver.find_element(By.ID, "female").click()
driver.find_element(By.ID, "admorepass").click()
driver.find_element(By.ID, "roundtrip").click()
driver.find_element(By.ID, "fromcity").send_keys("Hyderabad")
driver.find_element(By.ID, "destcity").send_keys("Bangalore")
driver.find_element(By.ID, "departdate").send_keys("25-07-2025")
driver.find_element(By.ID, "returndate").send_keys("31-07-2025")
driver.find_element(By.ID, "visadate").send_keys("6-08-2025")
driver.find_element(By.ID, "eamil").click()
driver.find_element(By.ID, "billing_name").send_keys("Prasanna")
driver.find_element(By.ID, "billing_phone").send_keys("9912691064")
driver.find_element(By.ID, "billing_email").send_keys("prasanna@gmail.com")
driver.find_element(By.ID, "billing_address").send_keys("Hyderabad")
driver.find_element(By.ID, "billing_country").click()
driver.find_element(By.XPATH, "//option[@vlaue='IN']").click()
driver.find_element(By.ID, "postcode").send_keys("502032")
driver.find_element(By.ID, "Prefecture").send_keys("Hyderabad")
driver.find_element(By.ID, "street_address1").send_keys("Nallagandla")
driver.find_element(By.ID, "street_address2").send_keys("MIG")
driver.find_element(By.XPATH, "//input[@value='checkbox']").click()
time.sleep(5)
driver.close()
