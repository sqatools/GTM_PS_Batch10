
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.redbus.in/")
time.sleep(5)
driver.find_element(By.XPATH,"//div[contains(@class,'inputAndSwapWrapper')]").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[contains(@class,'searchSuggestionWrappe')]//child::div[contains(@class,'leftListCont')]//child::div[contains(text(),'Pune')]").click()
time.sleep(5)

driver.find_element(By.XPATH,"(//div[contains(@class,'srcDestWrapper')])[2]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//div[contains(@class,'suggestionsWrapper')]//following::div[contains(@class,'searchSuggestionWrapper')]//following-sibling::div[contains(@class,'searchCateg')]//following::div[contains(text(),'Belagavi')]").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[contains(@class,'dateInputWrapper')]").click()
time.sleep(10)