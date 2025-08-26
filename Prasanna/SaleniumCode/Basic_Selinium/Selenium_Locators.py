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

def get_element_with_id_name():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, "email").send_keys("prasanna.kamana@gmail.com")
    pass_element = driver.find_element(By.NAME, "pass").send_keys("pass")
    print(pass_element)
    pass_element.send_keys("Prasanna@123")
    time.sleep(5)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    driver.close()
get_element_with_id_name()
time.slee(10)

def get_element_with_link_text_partial_linktext():
    driver.get("https://automationbysqatools.blogspot.com/p/home.html")
    # link text will get element with full text value
    driver.find_element(By.LINK_TEXT, "Python 3 Tutorial").click()
    time.sleep(5)


    # Partial link text with partial value text of any specific link
    driver.find_element(By.PARTIAL_LINK_TEXT, "Features and Its Contribution").click()
    time.sleep(5)

    driver.close()

get_element_with_link_text_partial_linktext()


def get_element_with_tagname():
    driver.get("https://automationbysqatools.blogspot.com/p/python.html")
    heading = driver.find_element(By.TAG_NAME, "h3")
    print(heading.text)
    time.sleep(5)
    driver.close()
get_element_with_tagname()

def get_element_with_absolute_relative_xpath():
    driver.get("https://www.facebook.com/")

    # absolute xpath
    xpath_val_username = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input"
    driver.find_element(By.XPATH, xpath_val_username).send_keys("user1test@gmail.com")
get_element_with_absolute_relative_xpath()

