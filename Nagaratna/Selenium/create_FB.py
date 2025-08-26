import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("https://www.facebook.com")

