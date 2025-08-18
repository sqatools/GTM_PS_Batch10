import time

import pytest
from modules.ui.openhrm.openhrm_page_class import OpenHRM
from modules.ui.openhrm_admin.admin_page_class import AdminPage
from modules.ui.openhrm.openhrm_page_data import *
from modules.ui.openhrm_admin.admin_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.hrm = OpenHRM(self.driver)
        self.admin = AdminPage(self.driver)

    @pytest.mark.smoke
    def test_login_open_hrm(self):
        self.hrm.enter_username(username_value=username_value)
        self.hrm.enter_password(password_value=password_value)
        self.hrm.click_to_login_button()
        time.sleep(5)

    @pytest.mark.sanity
    def test_admin_add_user(self):
        self.admin.navigate_to_admin_page()
        self.admin.click_to_add_user()
        self.admin.select_user_role(role_name=user_role_value)
        self.admin.select_status(status=status)
        self.admin.enter_employee_name(employee_name_value=employee_name)
        self.admin.enter_username_name(username_value=username)
        self.admin.enter_password(password_value=password)
        self.admin.confirm_password(con_password_value=con_password)
        assert password == con_password
        self.admin.click_to_save_button()
        time.sleep(5)

    def test_job_tab(self):
       # self.admin.click_to_job_tab(job_title=job_title, job_desc=job_desc, note=note)
        time.sleep(10)
        self.admin.job_title_modification(new_note=new_note)
        time.sleep(5)
