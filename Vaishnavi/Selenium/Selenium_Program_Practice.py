from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.automationexercise.com/")
time.sleep(5)
driver.find_element(By.XPATH,"//h4[@class='panel-title']//following::div[@class='panel-heading']//following-sibling::span[@class='badge pull-right']").click()
time.sleep(10)
data=driver.find_element(By.XPATH,"//a[text()='Tshirts ']").is_displayed()
print(data)
element1="//h2[text()='Category']//following::div[@class='panel-group category-products']//following-sibling::div[@class='panel panel-default'][3]//child::span[@class='badge pull-right']"
driver.find_element(By.XPATH,element1).click()
time.sleep(5)
data1=driver.find_element(By.XPATH,"//*[text()='Tops & Shirts ']").is_displayed()
print(data1)
time.sleep(20)