import time
from selenium.webdriver.common.by import By
import pytest
import os
from ....Modules.UI.facebook.fb_page_class import fbpage
from ....Utilities.util_tools import Utils

@pytest.mark.usefixtures("get_driver")
class TestFblogin:

    @pytest.fixture(autouse=True)
    def setup(self,get_driver):
        self.driver = get_driver
        self.fb = fbpage(self.driver)
        self.utils = Utils()
        file_path = os.path.join(os.getcwd(),"Modules/UI/facebook/fb_input_data.json")
        self.data = self.utils.read_json_files(file_path)

    @pytest.mark.skip
    def test_facebook_login(self):
        self.fb.select_login_page(self.data['url'])
        self.fb.fb_login(username1=self.data['username'],password1=self.data['password'])
        time.sleep(10)

    def test_upload_file_and_verify(self):
        self.fb.driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")
        self.fb.fill_text(locator=(By.ID, "myFile"), value=r"D:\Demo\abc.txt")
        time.sleep(5)
        self.fb.click_element(locator=(By.XPATH,"//form/input[@type='submit']"))
        time.sleep(5)
