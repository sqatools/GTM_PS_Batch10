import pytest
from selenium import webdriver
from orang_hrm.uitility import LoginPage
import time

@pytest.fixture
def setup(autouse=True):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    page = LoginPage(setup)
    page.login("Admin", "admin123")
    time.sleep(10)
    assert page.is_login_successful()