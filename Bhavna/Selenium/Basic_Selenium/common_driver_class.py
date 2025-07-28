# 22/05/2025 Session

import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

class DriverClass:

    def __init__(self,browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        self.driver.maximize_window()