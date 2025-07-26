
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
-> ID = "id" 
XPATH = "xpath"
-> LINK_TEXT = "link text"
-> PARTIAL_LINK_TEXT = "partial link text"
-> NAME = "name"
-> TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def get_element_with_id():
    driver.get("https://www.facebook.com")
    driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
    driver.implicitly_wait(10)

# get_element_with_id()

def get_element_with_name():
    driver.get("https://www.facebook.com")
    driver.find_element(By.NAME,"pass").send_keys("12345")
    time.sleep(5)
    # find element with the help of ID attribute of the web element
    Pass_element = driver.find_element(By.NAME,"login")
    print(Pass_element)
    Pass_element.click()
    time.sleep(5)
    driver.close()

# get_element_with_name()

def get_elements_with_link_text_partial_linktext():
    driver.get("https://automationbysqatools.blogspot.com/p/home.html")
    # link text will get element with full text value
    driver.find_element(By.LINK_TEXT,"Manual Testing").click()
    time.sleep(5)

    # Partial link text with partial value text of any specific link
    driver.find_element(By.PARTIAL_LINK_TEXT,"What is").click()
    time.sleep(5)
    driver.close()

# get_elements_with_link_text_partial_linktext()

def get_element_with_tagname():
    driver.get("https://automationbysqatools.blogspot.com/p/python.html")
    heading = driver.find_element(By.TAG_NAME,"h3")
    print(heading.text)
    time.sleep(5)
    driver.close()
# get_element_with_tagname()

def get_element_with_absolute_relative_xpath():
    driver.get("https://www.facebook.com/")
    # absolute xpath
    xpath_val_username = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input"
    driver.find_element(By.XPATH,xpath_val_username).send_keys("user@gmail.com")

    # relative xpath
    driver.find_element(By.XPATH,"//input[@data-testid='royal-pass']").send_keys("Pass123")

    # login button with relative xpath
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)
    driver.close()

get_element_with_absolute_relative_xpath()

