import time

import pytest
import os
from ....modules.ui.facebook_page.facebook_page_class import FBPage
from ....utilities.util_tools import Utils

@pytest.mark.usefixtures("get_driver")
class TestFBLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = FBPage(self.driver)
        self.utils = Utils()
        file_path = os.path.join(os.getcwd(), "modules/ui/facebook_page/facebook_page_data.json")
        self.data = self.utils.read_json_file(file_path)

    def test_facebook_login(self):
        self.fb.navigate_to_login_page(self.data['fb_url'])
        self.fb.fb_login(username=self.data['fb_username'], password=self.data['fb_password'])
        time.sleep(10)
