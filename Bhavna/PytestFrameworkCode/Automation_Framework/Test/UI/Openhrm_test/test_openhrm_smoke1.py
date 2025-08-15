import time

import pytest
from ....Modules.UI.Openhrm_website.openhrm_page_class1 import OpenHRM
from ....Modules.UI.Openhrm_website.openhrm_page_data1 import *
from ....Modules.UI.ophrm_admin.admin_page_class import AdminPage
from ....Modules.UI.ophrm_pim.pim_page_class import PIMPage
from ....Modules.UI.ophrm_admin.admin_page_data import *
from ....Modules.UI.ophrm_pim.pim_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestOpenhrm:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hrm = OpenHRM(self.driver)
        self.admin = AdminPage(self.driver)
        self.pim = PIMPage(self.driver)

    @pytest.mark.smoke
    def test_login(self,request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.hrm.login(username_value,password_value)

    @pytest.mark.sanity
    def test_admin(self,request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.admin.admin_module_user(e_name1,e_username1,e_password1,c_password1,user_name)
        self.admin.admin_job(jobtitle,desc,value1,gradename,minsal,maxsal,name)
        # self.admin.admin_organization(register_no,lname,lcity,lstate,pcode,lphone,laddress)
        # self.admin.admin_qualification(sname,sdesc,edu_level,language)

    @pytest.mark.skip
    def test_pim(self,request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.pim.PIM_Module(f_name,l_name,street_1,street_2,e_city,e_state,pincode,number)




        time.sleep(10)
