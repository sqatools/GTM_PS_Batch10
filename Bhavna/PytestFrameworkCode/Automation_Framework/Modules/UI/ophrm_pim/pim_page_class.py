import time
from Base.selenium_base1 import *
from .pim_page_locator import *


class PIMPage(SeleniumBase):

    def __init__(self, driver):
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


    def add_emergency_cont(self, name, relshp, mob):
        self.click_element(pim_locator.select_emerg_cnt)
        self.click_element(pim_locator.add_cont)
        self.fill_text(pim_locator.Name, name)
        self.fill_text(pim_locator.relationship, relshp)
        self.fill_text(pim_locator.mobile, mob)
        self.click_element(pim_locator.save)
        time.sleep(5)

    def add_job(self, date):
        self.click_element(pim_locator.select_job)
        time.sleep(3)
        self.fill_text(pim_locator.join_date,date)
        self.click_element(pim_locator.job_title_dd)
        self.click_element(pim_locator.select_job_title)
        time.sleep(2)
        self.click_element(pim_locator.job_category_dd)
        self.click_element(pim_locator.job_category)
        time.sleep(2)
        self.click_element(pim_locator.sub_unit_dd)
        self.click_element(pim_locator.sub_unit)
        time.sleep(2)
        self.click_element(pim_locator.location_dd)
        self.click_element(pim_locator.location)
        self.click_element(pim_locator.save)
        time.sleep(5)


    # def attachments(self, filepath):
    #     self.click_element(pim_locator.add_attach)
    #     time.sleep(2)
    #     self.send_keys(pim_locator.file_input,filepath)
    #     time.sleep(2)
    #     self.click_element(pim_locator.save)

        time.sleep(5)





    def PIM_Module(self,fname,lname,s1,s2,city1,state1,pc,numb,name, relshp, mob, date):
        self.click_on_PIM()
        self.add_employee(fname,lname,s1,s2,city1,state1,pc,numb)
        self.add_emergency_cont(name, relshp, mob)
        self.add_job(date)
        # self.attachments(filepath)
