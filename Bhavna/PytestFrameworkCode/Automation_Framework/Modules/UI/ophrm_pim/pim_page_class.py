import time
from Base.selenium_base1 import *
from .pim_page_locator import *

class PIMPage(SeleniumBase):

    def __init__(self,driver):
        super().__init__(driver)

    def click_on_PIM(self):
        self.click_element(pim_locator.choose_PIM)

    def add_employee(self,fname,lname,s1,s2,city1,state1,pc,numb):
        self.click_element(pim_locator.add)
        self.fill_text(pim_locator.first_name,fname)
        self.fill_text(pim_locator.last_name,lname)
        self.click_element(pim_locator.save)
        time.sleep(10)
        self.click_element(pim_locator.select_cont_dls)
        time.sleep(2)
        self.fill_text(pim_locator.street1,s1)
        self.fill_text(pim_locator.street2,s2)
        self.fill_text(pim_locator.city,city1)
        self.fill_text(pim_locator.state,state1)
        self.fill_text(pim_locator.postal_code,pc)
        self.click_element(pim_locator.country_dd)
        time.sleep(3)
        self.click_element(pim_locator.select_country)
        self.fill_text(pim_locator.mobile,numb)
        self.click_element(pim_locator.save)
        time.sleep(5)












    def PIM_Module(self,fname,lname,s1,s2,city1,state1,pc,numb):
        self.click_on_PIM()
        self.add_employee(fname,lname,s1,s2,city1,state1,pc,numb)
