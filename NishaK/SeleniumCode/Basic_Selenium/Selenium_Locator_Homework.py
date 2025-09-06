# Home work to automation this website as much as possible
# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html

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


def get_element_with_id_name():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.find_element(By.ID, "firstname").send_keys("Nisha")
    driver.find_element(By.NAME, "birthday").send_keys("01/01/2000")
    time.sleep(5)
    driver.close()


def get_element_with_link_text_partial_linktext():
    driver.get("https://automationbysqatools.blogspot.com/p/home.html?m=1")
    driver.find_element(By.LINK_TEXT, "Manual Testing").click()
    time.sleep(5)
    driver.find_element(By.PARTIAL_LINK_TEXT, "What is Software").click()
    time.sleep(5)
    driver.close()


def get_element_with_tagname():
    driver.get("https://automationbysqatools.blogspot.com/p/python.html")
    heading = driver.find_element(By.TAG_NAME, "h4")
    print(heading.text)
    time.sleep(5)
    driver.close()


# get_element_with_id_name()
# get_element_with_link_text_partial_linktext()
get_element_with_tagname()

# def get_element_with_absolute_relative_xpath():