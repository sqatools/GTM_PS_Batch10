import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
def get_element1():
    driver.get("https://www.facebook.com")
    create_button = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
    create_button.click()

    time.sleep(3)

    heading = driver.find_element(By.XPATH, "//div[contains(text(), 'Create a new account')]")
    print(heading.text)
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys( "mithika!")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Naik")
    time.sleep(5)
    driver.find_element(By.ID,'day').send_keys("12")
    time.sleep(3)
    driver.find_element(By.ID, 'year').send_keys("2014")
    time.sleep(3)
    driver.find_element(By.ID, 'month').send_keys("Aug")
    time.sleep(3)
    driver.find_element(By.XPATH, "(//input[@data-type='text'])[5]").send_keys("mytest@gmail.com")
    time.sleep(5)
    driver.find_element(By.XPATH,  "//input[@type='radio' and @value='1']")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-type='password']").send_keys("MYTST")
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[contains(text(),'Already have an account?')]").click()
    time.sleep(5)


get_element1()
