import pytest
from ....modules.ui.openhrm.openhrm_page_class import OpenHRM
from ....modules.ui.openhrm.openhrm_page_data import *
from ....modules.ui.openhrm_common.navigation_page_class import NavigationPage
from ....modules.ui.openhrm_common.navigation_page_data import modules_to_test


@pytest.mark.usefixtures("get_driver")
class TestOpenHRMNavigation:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hrm = OpenHRM(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.smoke
    def test_login(self, request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        self.hrm.login_openhrm(username_value, password_value)

    @pytest.mark.sanity
    @pytest.mark.parametrize("module_name,expected_header", modules_to_test)
    def test_navigate_modules(self, module_name, expected_header, request):
        self.hrm.log.info(f"Test Name: {request.node.name}")
        # assumes already logged in from previous test when running as a class
        self.nav.open_module(module_name)
        header_text = self.nav.get_page_header()
        assert expected_header in header_text


