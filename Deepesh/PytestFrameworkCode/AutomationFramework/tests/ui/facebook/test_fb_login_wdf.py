import time

import pytest
import os
from selenium.webdriver.common.by import By
from ....modules.ui.facebook_page.fb_page_class import FBPage
from ....utilities.util_tools import Utils

@pytest.mark.usefixtures("get_driver_wdf")
class TestFBLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = FBPage(self.driver)
        self.utils = Utils()
        file_path = os.path.join(os.getcwd(), "modules/ui/facebook_page/fb_input_data.json")
        self.data = self.utils.read_json_file(file_path)

    def test_facebook_login(self):
        self.fb.navigate_to_login_page(self.data['fb_url'])
        self.fb.fb_login(username=self.data['fb_username'], password=self.data['fb_password'])
        time.sleep(10)


    def test_upload_file_and_verify(self):
        self.fb.driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")
        self.fb.fill_text(locator=(By.ID, "myFile"), value=r"E:\Filesdata\batch11\count_name.txt")
        time.sleep(5)
        self.fb.click_element(locator=(By.XPATH, "//form/input[@type='submit']"))
        time.sleep(5)