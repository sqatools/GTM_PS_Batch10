import time

import pytest
from modules.ui.openhrm.openhrm_page_class import OpenHRM
from modules.ui.openhrm_admin.admin_page_class import AdminPage
from modules.ui.openhrm.openhrm_page_data import *
from modules.ui.openhrm_admin.admin_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hrm = OpenHRM(self.driver)
        self.admin = AdminPage(self.driver)


    # def test_login_open_hrm(self):
    #     self.hrm.enter_username(username_value=username_value)
    #     self.hrm.enter_password(pass_value=password_value)
    #     self.hrm.click_to_login_button()
    #     time.sleep(10)

    @pytest.mark.smoke
    def test_login_openhrm(self, request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.hrm.login_openhrm(username_value, password_value)

    @pytest.mark.sanity
    def test_admin_add_user(self, request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.admin.navigate_to_admin_page()
        self.admin.click_to_add_user_btn()
        self.admin.select_user_role(role_name=user_role_value)
        time.sleep(10)


