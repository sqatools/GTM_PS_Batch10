from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_options
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.edge.options import Options as edge_option


class WebDriverFactory:
    def __init__(self, browser, headless=False):
        self.browser = browser
        self.headless = headless

    def get_driver_instance(self):
        if self.browser.lower() == 'chrome':
            chr_opt = chr_options()
            if self.headless:
                chr_opt.add_argument("--headless")
            driver = webdriver.Chrome(options=chr_opt)

        elif self.browser.lower() == 'firefox':
            frx_opt = firefox_option()
            if self.headless:
                frx_opt.add_argument("--headless")
            driver = webdriver.Firefox(options=frx_opt)

        elif self.browser.lower() == 'edge':
            edge_opt = edge_option()
            if self.headless:
                edge_opt.add_argument("--headless")
            driver = webdriver.Edge(options=edge_opt)

        driver.maximize_window()
        return driver
