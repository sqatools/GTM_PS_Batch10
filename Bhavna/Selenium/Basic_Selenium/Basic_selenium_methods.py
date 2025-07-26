import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumMethods:

    def __init__(self,url,browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text_of_element(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        element = self.driver.find_element(By.XPATH,"//div[contains(text(),'quick and easy.')]//preceding-sibling::div")
        return element.text

    def check_enable_displayed_selected(self):
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        radio_button = self.driver.find_element(By.CSS_SELECTOR,"input[value='1']")
        print("check radio button is enabled :",radio_button.is_enabled())
        print("check radio button is displayed :",radio_button.is_displayed())
        print("check radio button is selected before click :",radio_button.is_selected())
        radio_button.click()
        time.sleep(5)
        print("check radio button is selected after click :",radio_button.is_selected())

# 22/07/2025 Session continue

    def get_attribute_value(self):
        self.driver.get("https://www.nseindia.com/")
        registered_user_link = self.driver.find_element(By.XPATH,"//p[(text()='Registered Investors')]//parent::div//a")
        print("Link:",registered_user_link.get_attribute("href"))

    def take_screenshot(self):
        self.driver.get("https://www.nseindia.com/")
        time.sleep(3)
        registered_user_link = self.driver.find_element(By.XPATH,"//p[(text()='Registered Investors')]//parent::div//a")
        # take screenshot of specific element
        registered_user_link.screenshot("registered_users.png")
        file_name = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        self.driver.save_screenshot(f"{file_name}_nse.png")


    def get_value_of_list_of_elements(self):
        self.driver.get("https://www.nseindia.com/")
        time.sleep(3)

        rows_list_table = self.driver.find_elements(By.XPATH,"//div[@class='market_turnover']//table/tbody/tr")
        # iterate through list of rows
        for row in rows_list_table:
            # get list of colum in each row
            column_list = row.find_elements(By.TAG_NAME,"td")
            # iterate through each colum in a row
            for column in column_list:
                # get text value each colum block
                print(column.text,end=" | ")
            print()

    def forward_back_refresh(self):
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
        time.sleep(5)

        # Navigate back to login page
        self.driver.back()
        time.sleep(3)

        # navigate to create account page with forward
        self.driver.forward()
        time.sleep(3)

        # Navigate back to login page
        self.driver.back()
        time.sleep(3)
        # refresh the page.
        self.driver.refresh()
        time.sleep(3)



obj = SeleniumMethods(url='https://www.facebook.com')
# print(obj.get_title())
# print(obj.get_current_url())
# print(obj.get_text_of_element())
# print(obj.check_enable_displayed_selected())
# obj.get_attribute_value()
# obj.take_screenshot()
# obj.get_value_of_list_of_elements()
obj.forward_back_refresh()