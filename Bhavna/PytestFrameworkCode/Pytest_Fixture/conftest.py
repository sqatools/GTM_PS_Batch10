import pytest
from selenium import webdriver

@pytest.fixture(scope='function',autouse=True)
def setup():
    print("--- start function fixture from fixture common file ---")
    yield
    print("--- end function fixture from fixture common file ---")


@pytest.fixture(scope='class')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # driver.get("https://www.facebook.com/")
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.close()
