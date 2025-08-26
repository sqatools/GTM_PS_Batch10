import time

import pytest
from openhrm_page_class import OpenHRM


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.hrm = OpenHRM(self.driver)


    def test_login_open_hrm(self):
        self.hrm.enter_username(username_value='Admin')
        self.hrm.enter_password(pass_value='admin123')
        self.hrm.click_to_login_button()
        time.sleep(10)

