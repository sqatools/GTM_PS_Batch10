import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.find_element(By.XPATH, "//div[contains(text(),'From')]").click()
src_element = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestionsWrapper')]//input")
src_element.send_keys("Banglore")

dest_element = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestionsWrapper')]//input")
dest_element.send_keys("Chennai")
#dest_element = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestionsWrapper')]//input")