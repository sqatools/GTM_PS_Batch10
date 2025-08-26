import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#automate the entire dummy website page with framework concept.
# https://sqatools.in/dummy-booking-website/
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.XPATH, "//input[@type='radio']").click()
driver.find_element(By.ID, "firstname").send_keys("Archana")
driver.find_element(By.ID, "firstname").send_keys("Mani")
driver.find_element(By.ID, "birthday").send_keys("24/08/1986")
driver.find_element(By.ID, "female").click()
dd_obj = driver.find_element(By.ID, "admorepass")
dd_obj = self.get_element(locator=(By.ID, "billing_country"))
select_obj = Select(dd_obj)
select_obj.select_by_value("1")
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Chennai")
driver.find_element(By.XPATH, "//input[@id='destcity']").send_keys("Banglore")
driver.find_element(By.XPATH, "//input[@id='departdate']").send_keys("4/08/2025")
driver.find_element(By.XPATH, "//input[@id='returndate']").send_keys("10/08/2025")
driver.find_element(By.XPATH, "//input[@id='visadate']").send_keys("15/08/2025")
driver.find_element(By.XPATH, "//input[@id='whatsapp']").send_keys("15/08/2025")
driver.find_element(By.XPATH, "//input[@id='billing_name']").send_keys("Archana")
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("984058576")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("Archan@gamil.com")
driver.find_element(By.XPATH, "//input[@id='billing_address']").send_keys("Chennai")
dd_obj1 = driver.find_element(By.ID, "billing_country")
select_obj1 = Select(dd_obj1)
select_obj1.select_by_value("BE")
driver.find_element(By.XPATH, "//input[@id='postcode']").send_keys("8798")
driver.find_element(By.XPATH, "//input[@id='Prefecture']").send_keys("TN")
driver.find_element(By.XPATH, "//input[@id='street_address1']").send_keys("Chennai")
driver.find_element(By.XPATH, "//input[@id='street_address2']").send_keys("TN")
driver.find_element(By.XPATH, "//td[text()='Delhi']//preceding::input[@type='checkbox'][5]").click()
driver.find_element(By.XPATH, "//td[text()='Delhi']//preceding::input[@type='checkbox'][4]").click()
driver.find_element(By.XPATH, "//td[text()='Delhi']//preceding::input[@type='checkbox'][3]").click()
time.sleep(5)

#"//td[text()='Mumbai']//preceding::input[@id='firstname'][1]").send_keys("Aagrawal"
#driver.find_element(By.XPATH, "//td[text()='Delhi']//preceding::input[@type='checkbox'][5]").click()