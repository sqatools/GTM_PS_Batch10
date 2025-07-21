"""
install selenium with below command
->  pip install selenium
"""
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
driver = None
# launch specific browser and initiate the driver
def get_browser(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    return driver

driver = get_browser('Chrome')
# maximize browser
driver.maximize_window()
driver.implicitly_wait(20)
def get_element_with_id_name():
    # launch web with get method
    driver.get("https://www.facebook.com")
    # find element with the help of ID attribute of the web element
    driver.find_element(By.ID, "email").send_keys("user1@gmail.com")

    # find element with the help of ID attribute of the web element
    pass_element = driver.find_element(By.NAME, "pass")
    print(pass_element)
    pass_element.send_keys("user1@12345")
    time.sleep(5)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    driver.close()

#get_element_with_id_name()

def get_element_with_link_text_partial_linktext():
    driver.get("https://automationbysqatools.blogspot.com/p/home.html")
    # link text will get element with full text value
    driver.find_element(By.LINK_TEXT, "Python 3 Tutorial").click()
    time.sleep(5)

    # Partial link text with partial value text of any specific link
    driver.find_element(By.PARTIAL_LINK_TEXT, "Features and Its Contribution").click()
    time.sleep(5)

    driver.close()

#get_element_with_link_text_partial_linktext()

def get_element_with_tagname():
    driver.get("https://automationbysqatools.blogspot.com/p/python.html")
    heading = driver.find_element(By.TAG_NAME, "h3")
    print(heading.text)
    time.sleep(5)
    driver.close()


#get_element_with_tagname()


def get_element_with_absolute_relative_xpath():
    driver.get("https://www.facebook.com/")

    # absolute xpath
    xpath_val_username = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input"
    driver.find_element(By.XPATH, xpath_val_username).send_keys("user1test@gmail.com")

    # relative xpath
    driver.find_element(By.XPATH, "//input[@data-testid='royal-pass']").send_keys("admin@1234")

    # login button with relative xpath
    driver.find_element(By.XPATH, "//button[@data-testid='royal-login-button']").click()

    time.sleep(5)
    driver.close()


get_element_with_absolute_relative_xpath()
