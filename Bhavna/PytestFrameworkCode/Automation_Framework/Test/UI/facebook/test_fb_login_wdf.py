import time

import pytest
import os
from ....Modules.UI.facebook.fb_page_class import fbpage
from ....Utilities.util_tools import Utils
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver_wdf")
class TestFblogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = fbpage(self.driver)
        self.utils = Utils()
        file_path = os.path.join(os.getcwd(), "Modules/UI/facebook/fb_input_data.json")
        self.data = self.utils.read_json_files(file_path)

    def test_facebook_login(self):
        self.fb.select_login_page(self.data['url'])
        self.fb.fb_login(username1=self.data['username'], password1=self.data['password'])
        time.sleep(10)

    def test_upload_file_n_verify(self):
        self.fb.driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")
        self.fb.fill_text(locator=(By.ID,"myFile"),value=r"D:\Demo\Batch2\abc_new.txt")
        time.sleep(5)
        self.fb.click_element(locator=(By.XPATH,"//form/input[@type='submit']"))
        time.sleep(5)