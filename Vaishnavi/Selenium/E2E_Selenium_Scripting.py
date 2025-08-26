import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= None

def get_driver(browser):
    if browser.lower()=="chrome":
        driver=webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    return driver

driver=get_driver('ChRome')

driver.maximize_window()
driver.implicitly_wait(20)

def Book_Ticket_indummy_web():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.implicitly_wait(20)
    data1=driver.title
    print(data1)
    driver.find_element(By.XPATH,"//h1[text()=' Dummy Ticket Booking Website']").screenshot("New_Screenshot_Title.png")
    time.sleep(4)
    driver.find_element(By.XPATH,"//h3//following::div//li//span[text()='Dummy ticket for visa application - $200 ']").is_displayed()
    time.sleep(6)
    driver.find_element(By.XPATH,"(//h3[text()='Choose the correct option:']//following-sibling::div//li/input[@type='radio'])[1]").click()
    time.sleep(4)
    element=driver.find_element(By.XPATH,"(//h3[text()='Choose the correct option:']//following-sibling::div//li/input[@type='radio'])[1]").is_selected()
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[text()='    First Name    ']//ancestor::div//following::h2[text()='Passenger Details']").screenshot("Passanger_Details.png")
    time.sleep(5)
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[1]").send_keys("Vaishnavi")
    time.sleep(5)
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("Rajput")
    time.sleep(5)
    driver.find_element(By.XPATH,"(//input[@type='date'])[1]").send_keys("22-11-1995")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"#female").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//h3[text()=' Number of Additional Passangers']").screenshot("Additional_Pass.png")
    time.sleep(5)
    i=input("enter the value")
    driver.find_element(By.XPATH,f"//option[@value='{int(i)}']").click()
    time.sleep(30)






Book_Ticket_indummy_web()



