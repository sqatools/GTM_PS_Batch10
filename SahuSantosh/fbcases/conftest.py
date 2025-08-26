import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    try:
        d = webdriver.Chrome()
        d.maximize_window()
        d.get('https://www.facebook.com/login.php/')
        d.implicitly_wait(4)
        yield d
    except Exception as e:
        raise Exception ('URL not found')
    finally:
        d.quit()
