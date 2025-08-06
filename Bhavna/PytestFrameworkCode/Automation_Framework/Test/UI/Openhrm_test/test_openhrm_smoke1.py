import time

import pytest
from Modules.UI.Openhrm_website.openhrm_page_class1 import OpenHRM
from Modules.UI.Openhrm_website.openhrm_page_data1 import *

@pytest.mark.usefixtures("get_driver")
class TestOpenhrm:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.hrm = OpenHRM(self.driver)

    def test_website(self):
        self.hrm.login(username_value,password_value)
        self.hrm.admin(e_name1,e_username1,e_password1,c_password1,user_name,jobtitle,desc)
        self.hrm.PIM(first_name,last_name)
        self.hrm.leave()


        time.sleep(10)
