import os
import time

import pytest
from ....modules.ui.openhrm.openhrm_page_class import OpenHRM
from ....modules.ui.openhrm_admin.admin_page_class import AdminPage
from ....modules.ui.openhrm.openhrm_page_data import *
from ....modules.ui.openhrm_admin.admin_page_data import *
from ....utilities.util_tools import Utils


@pytest.mark.usefixtures("get_driver")
class TestOpenHRM:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hrm = OpenHRM(self.driver)
        self.admin = AdminPage(self.driver)
        self.util = Utils()
        self.excel_path = os.path.join(os.getcwd(), "modules/ui/openhrm_admin/admin_data.xlsx")


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
        self.admin.set_user_status(user_status=self.util.read_excel_file(self.excel_path, "Sheet1", "C3"))
        unique_name = self.util.generate_unique_name()
        self.admin.select_employee_name(emp_name=self.util.read_excel_file(self.excel_path, "Sheet1", "C4"))
        self.admin.enter_new_username(new_username=f"{self.util.read_excel_file(self.excel_path, 'Sheet1', 'C5')}_{unique_name}")
        self.admin.enter_new_password(new_password=self.util.read_excel_file(self.excel_path, "Sheet1", "C6"))
        self.admin.enter_confirm_password(confirm_password=self.util.read_excel_file(self.excel_path, "Sheet1", "C7"))
        self.admin.click_on_save_button()
        time.sleep(10)


