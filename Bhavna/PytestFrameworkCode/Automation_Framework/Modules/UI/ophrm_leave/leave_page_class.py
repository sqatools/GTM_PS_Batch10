import time
from ....Base.selenium_base1 import *
from .leave_page_locator import *


class LeavePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_leave(self):
        self.click_element(LeaveLocator.choose_leave)

    def entitlements(self, days):
        self.click_element(LeaveLocator.entitlement)
        self.click_element(LeaveLocator.add_entitlement)
        self.click_element(LeaveLocator.multiple_employee)
        self.click_element(LeaveLocator.location_dd)
        time.sleep(3)
        self.click_element(LeaveLocator.location)
        self.click_element(LeaveLocator.sub_unit_dd)
        time.sleep(3)
        self.click_element(LeaveLocator.sub_unit)
        self.click_element(LeaveLocator.leave_type_dd)
        time.sleep(3)
        self.click_element(LeaveLocator.leave_type)
        self.fill_text(LeaveLocator.entitle_day, days)
        self.click_element(LeaveLocator.save)
        time.sleep(3)
        self.click_element(LeaveLocator.confirm)
        time.sleep(5)

    def leave_entitlements(self, name):
        self.fill_text(LeaveLocator.employee_name, name)
        time.sleep(3)
        self.click_element(LeaveLocator.select_employee)
        self.click_element(LeaveLocator.leave_type_dd)
        time.sleep(2)
        self.click_element(LeaveLocator.leave_type)
        self.click_element(LeaveLocator.search)
        time.sleep(5)






    def leave_module(self, days, name):
        self.click_on_leave()
        self.entitlements(days)
        self.leave_entitlements(name)
