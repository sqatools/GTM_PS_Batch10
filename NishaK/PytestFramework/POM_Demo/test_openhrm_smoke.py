import time

import pytest
from openhrm_page_class import OpenHRM
from openhrm_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.hrm = OpenHRM(self.driver)

    def test_login_open_hrm(self):
        self.hrm.enter_username(username_value=username_value)
        self.hrm.enter_password(password_value=password_value)
        self.hrm.click_to_login_button()
        time.sleep(10)
