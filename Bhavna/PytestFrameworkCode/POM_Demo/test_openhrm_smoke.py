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
        self.hrm.enter_password(password_value='admin123')
        self.hrm.click_to_login_button()
        self.hrm.click_on_admin()
        self.hrm.add_user()
        self.hrm.e_name(e_name1='Peter')
        time.sleep(3)
        self.hrm.status()
        self.hrm.e_username_password(e_username1='user1_peter',e_password1='Peter@1234',c_password1='Peter@1234')
        time.sleep(3)
        self.hrm.system_user(user_name='user1_peter')
        self.hrm.delete_user()
        time.sleep(5)
        self.hrm.job(jobtitle='Manual Tester',desc='Testing of website')
        time.sleep(2)
        self.hrm.PIM_module()




        time.sleep(10)
