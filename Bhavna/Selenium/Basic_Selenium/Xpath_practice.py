import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")

driver.find_element(By.XPATH,"//div[text()='From']//parent::div[1]").click()

# all_elements = driver.find_elements(By.XPATH,"//div[contains(@class, 'suggestionsWrapper')]//*")
# for element in all_elements:
#     print(element.tag_name)

time.sleep(5)
src_element_text = driver.find_element(By.XPATH,"//div[contains(@class, 'suggestionsWrapper')]//input")
src_element_text.send_keys('Chennai')

time.sleep(5)
suggestion_element = driver.find_element(By.XPATH,"//*[contains(text(), 'Koyambedu')]")
suggestion_element.click()

src_element_text = driver.find_element(By.XPATH,"//div[contains(@class, 'suggestionsWrapper')]//input")
src_element_text.send_keys('Bangalore')

time.sleep(3)
dest_suggestion_element = driver.find_element(By.XPATH,"//*[contains(text(), 'Madiwala')]")
dest_suggestion_element.click()

calender_Section = driver.find_element(By.XPATH,"//span[contains(text(), 'Date of Journey')]//parent::div")
calender_Section.click()

time.sleep(3)

calender_wrappers = driver.find_elements(By.XPATH,"//div[contains(@class, 'datePickerWrapper')]//*")
for element in calender_wrappers:
    if element.text.strip() == '23':
        element.click()
        break


# //div[contains(@id,'bp-point-1')]//div[contains(@class,'radioContainer___3f71ea')]//label




time.sleep(5)
driver.close()