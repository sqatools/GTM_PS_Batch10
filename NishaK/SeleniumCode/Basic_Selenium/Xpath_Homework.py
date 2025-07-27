import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


correct_option = driver.find_element(By.XPATH, "(//input[@value='radio_558'])[2]")
correct_option.click()
time.sleep(5)

first_name = driver.find_element(By.ID, 'firstname')
first_name.send_keys('Nisha')
time.sleep(2)


last_name = driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]")
last_name.send_keys('Pawar')
time.sleep(2)

birth_date = driver.find_element(By.XPATH, "//span[contains(text(),'Last Name')]//following::input[@type='date']")
birth_date.send_keys('22-08-1995')
time.sleep(2)

driver.find_element(By.XPATH, "//span[text()='Female']//preceding::input[@id='female']").click()
time.sleep(2)


driver.find_element(By.XPATH, "//option[@value='3']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//option[@value='3']//following::input[@id='oneway']").click()
time.sleep(2)

from_city = driver.find_element(By.NAME, "fromcity")
from_city.send_keys('Pune')
time.sleep(2)


dest_city = driver.find_element(By.ID, "destcity")
dest_city.send_keys('Mumbai')
time.sleep(2)

driver.close()
