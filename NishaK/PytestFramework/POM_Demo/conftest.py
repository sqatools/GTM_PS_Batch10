import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.close()