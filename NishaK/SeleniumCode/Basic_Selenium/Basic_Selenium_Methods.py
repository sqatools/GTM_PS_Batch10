import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumMethods():


    def __init__(self, url, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text_of_element(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        element = self.driver.find_element(By.XPATH, "//div[contains(text(),'quick and easy')]//preceding-sibling::div")
        return element.text

    def check_enable_displayed_selected(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        radio_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='1']")
        print("Check radio button is enabled :", radio_button.is_enabled())
        print("Check radio button is displayed :", radio_button.is_displayed())
        print("Check radio button is selected before click :", radio_button.is_selected())
        radio_button.click()
        time.sleep(5)
        print("Check radio button is selected before click :", radio_button.is_selected())

    def get_attribute_value(self):
        self.driver.get("https://www.nseindia.com/")
        registered_user_link = self.driver.find_element(By.XPATH, "//p[text()='Registered Investors']//parent::div//a")
        print("Link :", registered_user_link.get_attribute("href"))

    def take_screenshots(self):
        self.driver.get("https://www.nseindia.com/")
        registered_user_link = self.driver.find_element(By.XPATH, "//p[text()='Registered Investors']//parent::div//a")
        registered_user_link.screenshot("registered_users.png")
        file_name = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        self.driver.save_screenshot(f"{file_name}_nse.png")


    def get_value_of_list_of_elements(self):
        self.driver.get("https://www.nseindia.com/")
        time.sleep(3)

        rows_list_table = self.driver.find_elements(By.XPATH, "//div[@class='market_turnover']//table/tbody//tr")

        # iterate through list of rows
        for row in rows_list_table:
            column_list = row.find_elements(By.TAG_NAME, "td")

            # iterate through each column in a row
            for column in column_list:
                # get text value of each column block
                print(column.text, end=" | ")
            print()


    def forward_back_refresh(self):
        self.driver.get("https://www.facebook.com")
        time.sleep(2)
        # navigate to create account page
        self.driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()
        time.sleep(2)
        # navigate back to login page
        self.driver.back()
        time.sleep(2)
        # navigate back to create account page with forward
        self.driver.forward()
        time.sleep(2)
        # navigate back to login page
        self.driver.back()
        time.sleep(2)
        # refresh the page
        self.driver.refresh()
        time.sleep(2)


obj = SeleniumMethods(url = 'https://www.facebook.com')

obj.forward_back_refresh()

# obj.get_value_of_list_of_elements()
"""
Equity | 360.26 Cr | 96,122.81 | - | 16:00 | 
Equity Derivatives | 7.62 Cr | 1,96,382.50 | 2.06 Cr | 15:30 | 
Currency Derivatives | 4.32 L | 3,736.69 | 11.20 L | 17:00 | 
Interest Rate Derivatives | 7.65 K | 156.89 | 31.43 K | 16:34 | 
Commodity Derivatives | 43.85 K | 77.97 | 2.76 K | 23:30 | 
Debt | - | 13,881.51 | - | 17:09 | 
Mutual Fund | - | 247.86 | - | 15:30 | 
Total | 367.93 Cr | 3,10,606.23 | 2.18 Cr |  | 
"""

# obj.take_screenshots()
# obj.get_attribute_value()
# Link : https://www.nseindia.com/registered-investors

# obj.check_enable_displayed_selected()
"""
Check radio button is enabled : True
Check radio button is displayed : True
Check radio button is selected before click : False
Check radio button is selected before click : True
"""

# print(obj.get_text_of_element())
# Create a new account

# print(obj.get_current_url())
# https://www.facebook.com/

# print(obj.get_title())
# Facebook – log in or sign up
