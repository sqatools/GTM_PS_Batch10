import pytest
import os
from datetime import datetime
from selenium import webdriver
from ..Base.webdriver_code import WebdriverFactory


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # create a class variable, that we use in the class with self.driver
    request.cls.driver = driver
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default='chrome', help='browser to execute the automation code')
    parser.addoption("--headlessValue", action="store", default=False, help='headless mode execution for browser')

@pytest.fixture(scope='class')
def get_driver_wdf(request, pytestconfig):
    browser = pytestconfig.getoption("browserName")
    headless = pytestconfig.getoption("headlessValue")
    if browser and headless:
        wdf = WebdriverFactory(browser=browser, headless=headless)
    elif browser:
        wdf = WebdriverFactory(browser=browser, headless=False)
    else:
        wdf = WebdriverFactory(browser="chrome", headless=False)
    driver = wdf.get_driver_instance()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # create a class variable, that we use in the class with self.driver
    request.cls.driver = driver
    yield driver
    driver.close()


def pytest_configure(config):
    logs_path = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    unique_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    log_file_name = f"{unique_name}_trace.log"
    log_file_path = os.path.join(logs_path, log_file_name)
    config.option.log_file = log_file_path
