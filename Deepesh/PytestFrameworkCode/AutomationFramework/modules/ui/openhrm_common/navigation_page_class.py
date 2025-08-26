from ....base.selenium_base import SeleniumBase
from .navigation_page_locator import navigation_locator as loc


class NavigationPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_module(self, module_name):
        mapping = {
            "Admin": loc.admin_link,
            "PIM": loc.pim_link,
            "Leave": loc.leave_link,
            "Time": loc.time_link,
            "Recruitment": loc.recruitment_link,
            "My Info": loc.my_info_link,
            "Performance": loc.performance_link,
            "Dashboard": loc.dashboard_link,
            "Directory": loc.directory_link,
            "Maintenance": loc.maintenance_link,
        }
        if module_name not in mapping:
            raise ValueError(f"Unsupported module: {module_name}")
        self.click_element(mapping[module_name])

    def get_page_header(self):
        return self.get_text(loc.page_header)


