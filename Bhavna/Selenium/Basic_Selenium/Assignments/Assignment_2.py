# 17/07/2025 Session Assignment
# Automating redbus website

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")
driver.find_element(By.XPATH,"//div[contains(text(), 'From')]").click()
src_element = driver.find_element(By.XPATH,"//div[contains(@class, 'suggestionsWrapper')]//input")
src_element.send_keys("Pune")

time.sleep(3)
element1 = driver.find_element(By.XPATH,"//*[contains(text(), 'Wakad')]")
element1.click()

dest_element = driver.find_element(By.XPATH,"//div[contains(@class, 'suggestionsWrapper')]//input")
dest_element.send_keys("Nagpur")

element2 = driver.find_element(By.XPATH,"//*[contains(text(), 'Chatrapathi')]")
element2.click()

calender_date = driver.find_element(By.XPATH,"//span[contains(text(), 'Date of Journey')]//parent::div")
calender_date.click()

time.sleep(3)
calender_wrappers = driver.find_elements(By.XPATH,"//div[contains(@class, 'datePickerWrapper')]//*")
for element in calender_wrappers:
    if element.text.strip() == '29':
        element.click()
        break

driver.find_element(By.XPATH,"//button[contains(@class,'primaryButton')]").click()
# driver.find_element(By.XPATH,"//div[contains(@class,'timeFareBoWrap')]//parent::li[@id='40004376']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='40004376']").click()

# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/button").click()
driver.find_element(By.XPATH,"//button[contains(@aria-label,'Close Bottom')]").click()

seat = driver.find_elements(By.XPATH,"//span[contains(text(),'Sold')]")

for x in seat:
    if x != 'sold':
        x.click()

driver.find_element(By.XPATH,"//span[contains(@aria-label,'Seat number DL3')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Select boarding & dropping points')]").click()
s_point = driver.find_element(By.XPATH,"//div[text()='Boarding points']//ancestor::div[@data-autoid='bpdpContainer']//div[text()='Wakad']//ancestor::div[contains(@class, 'bpdpSelection')]//label")
# s_point = driver.find_element(By.XPATH,"//*[@id='bp-point-0']/div[3]/div/label")
s_point.click()
d_point = driver.find_element(By.XPATH,"//div[text()='Dropping points']//ancestor::div[@data-autoid='bpdpContainer']//div[text()='Chatrapathi']//ancestor::div[contains(@class, 'bpdpSelection')]//label")
d_point.click()

driver.find_element(By.CSS_SELECTOR,"input[name='Phone']").send_keys('9876543211')
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter email')]").send_keys("user@gmail.com")
driver.find_element(By.XPATH,"//*[text()='State of Residence']").click()
time.sleep(3)

driver.close()
