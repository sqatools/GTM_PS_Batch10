import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = None
def get_browser(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    return driver


driver = get_browser('Chrome')
driver.maximize_window()
driver.implicitly_wait(20)


driver.get("https://www.redbus.in/")
element = driver.find_element(By.XPATH, "//div[text()='From']")
element.click()
time.sleep(5)
src_element_text = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestionsWrapper')]//input")
src_element_text.send_keys("Chennai")

time.sleep(3)
suggestion_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Koyambedu')]")
suggestion_element.click()

dest_element_text = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestionsWrapper')]//input")
dest_element_text.send_keys("Bangalore")
time.sleep(3)

dest_suggestion_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Madiwala')]")
dest_suggestion_element.click()

calender_section = driver.find_element(By.XPATH, "//span[text()='Date of Journey']//parent::div")
calender_section.click()

time.sleep(3)
calender_wrapper_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'datePickerWrapper')]//*")
for element in calender_wrapper_elements:
    if element.text.strip() == '21':
        element.click()
        break



time.sleep(5)
driver.close()
