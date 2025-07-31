import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumActionchain:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

    def element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        elements = self.wait.until(ec.presence_of_all_elements_located(locator))
        return elements

    def launch_website_url(self,url):
        self.driver.get(url)

    def perform_mouse_hover(self):
        self.launch_website_url(url="https://www.nseindia.com/")
        time.sleep(3)
        market_data = self.element(locator=(By.XPATH,"//a[text()='Market Data']"))
        self.action.move_to_element(market_data).perform()
        time.sleep(5)

        derivative_market = self.element(locator=(By.XPATH,"//a[text()='Derivatives Market']"))
        self.action.click(derivative_market).perform()
        time.sleep(5)

    def perform_drag_drop_opertion(self):
        self.launch_website_url(url="https://www.globalsqa.com/demo-site/draganddrop/")
        time.sleep(5)

        #switch to iframe
        iframe_element = self.element(locator=(By.XPATH,"//iframe[@class='demo-frame lazyloaded']"))
        self.driver.switch_to.frame(iframe_element)

        # Get image and trash element
        image1_element = self.element(locator=(By.XPATH,"//h5[text()='High Tatras']"))
        trash_element = self.element(locator=(By.ID,"trash"))

        # perform drag and drop operation
        self.action.drag_and_drop(image1_element,trash_element).perform()
        time.sleep(5)


        image_headings = ['High Tatras 2','High Tatras 3','High Tatras 4']
        for image_name in image_headings:
            image1_element = self.element(locator=(By.XPATH,f"//h5[text()='{image_name}']"))
            trash_element = self.element(locator=(By.ID, "trash"))
            self.action.drag_and_drop(image1_element,trash_element).perform()
            time.sleep(3)
        time.sleep(5)

    def scroll_to_target_element(self):
        self.launch_website_url(url="https://sqatools.in/dummy-booking-website/")
        time.sleep(5)
        pandas_link_element = self.element(locator=(By.XPATH,"//div[@class='inside-right-sidebar']//a[text()='Python Pandas Programs']"))
        # perform scroll page operation till target element.
        self.action.scroll_to_element(pandas_link_element).perform()
        #self.action.click(pandas_link_elem).perform()
        time.sleep(5)

    def context_click_operation(self):
        import pyautogui
        self.launch_website_url(url="https://sqatools.in/dummy-booking-website/")
        time.sleep(5)
        pandas_link_elem = self.element(locator=(By.XPATH,"//div[@class='inside-right-sidebar']//a[text()='Python Pandas Programs']"))
        self.action.context_click(pandas_link_elem).perform()
        time.sleep(10)
        pyautogui.press('up')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(10)



        self.driver.close()


obj = SeleniumActionchain()
# obj.perform_mouse_hover()
# obj.perform_drag_drop_opertion()
# obj.scroll_to_target_element()
obj.context_click_operation()