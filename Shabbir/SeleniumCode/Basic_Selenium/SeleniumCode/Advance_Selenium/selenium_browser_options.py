import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options

class BrowserOptions:
    def __init__(self, browser, headless=True):
        if browser.lower() == 'chrome':
            chr_opt = chrome_options()
            if headless:
                chr_opt.add_argument("--headless")
            chr_opt.add_argument("--disable-notification")
            chr_opt.add_argument("--window-size=1920*1080")
            #chr_opt.add_argument("--incognito")
            prefs_dict = {
                "download.default_directory" : "E:\\Filesdata\\DownloadFiles",
                "download.prompt_for_download" : False,
                "safebrowsing.enabled" : True
            }
            chr_opt.add_experimental_option("detach", True)
            chr_opt.add_experimental_option("prefs", prefs_dict)
            self.driver = webdriver.Chrome(options=chr_opt)

        elif browser.lower() == 'firefox':
            fox_opt = firefox_options()
            if headless:
                fox_opt.add_argument("--headless")

            self.driver = webdriver.Firefox(options=fox_opt)

        elif browser.lower() == 'edge':
            edg_opt = edge_options()
            if headless:
                edg_opt.add_argument("--headless")
            self.driver = webdriver.Edge(options=edg_opt)

        self.wait = WebDriverWait(self.driver, 30)

    def get_element(self, locator):
        """
        This method returns single element of specified locator
        :param locator:
        :return:
        """
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self, locator):
        """
        This method returns list of elements of specified locator
        :param locator:
        :return:
        """
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def handle_multiple_browsers_tabs(self):
        self.driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

        # get software testing principle locator
        testing_principle_locator = (By.LINK_TEXT, "Software Testing Principles")
        testing_element = self.get_element(testing_principle_locator)
        testing_element.click()
        time.sleep(5)

        # get list of windows
        windows_list = self.driver.window_handles

        # Navigate to new window tab
        self.driver.switch_to.window(windows_list[1])


        # get list of all the testing principle headings
        headings_locator = (By.XPATH, "//h3//span")
        elements_list = self.get_elements(headings_locator)
        for elem in elements_list:
            print(elem.text)


        # Navigate to back to original tab.
        self.driver.switch_to.window(windows_list[0])

        rf_locator = (By.LINK_TEXT, "Robot Framework")
        rf_element = self.get_element(rf_locator)
        rf_element.click()

        time.sleep(5)

        # Navigate to back to new window tab to close it.
        self.driver.switch_to.window(windows_list[1])
        time.sleep(5)
        # close new tab window
        self.driver.save_screenshot("latest_page.png")
        #self.driver.close()

    def download_python_installer(self):
        self.driver.get("https://www.python.org/downloads/")
        download_elem = self.get_element(locator=(By.XPATH, "//div[@class='download-os-windows']//a[text()='Download Python 3.13.5']"))
        download_elem.click()

        time.sleep(20)



obj = BrowserOptions(browser='chrome', headless=False)
#obj.handle_multiple_browsers_tabs()
obj.download_python_installer()
