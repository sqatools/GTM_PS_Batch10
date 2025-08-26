import time
from ....Base.selenium_base1 import *
from .admin_page_locator import *

class AdminPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_admin(self):
        self.click_element(admin_locator.choose_admin)

    def add_user(self):
        self.click_element(admin_locator.add_user)
        self.click_element(admin_locator.select_dd)
        self.click_element(admin_locator.select_admin_dd)

    def e_name(self,e_name1):
        self.fill_text(admin_locator.e_name,e_name1)
        time.sleep(5)
        self.click_element(admin_locator.select_employee)


    def status(self):
        self.click_element(admin_locator.status)
        self.click_element(admin_locator.e_status)

    def e_username_password(self, e_username1, e_password1, c_password1):
        self.fill_text(admin_locator.e_username, e_username1)
        self.fill_text(admin_locator.e_password, e_password1)
        self.fill_text(admin_locator.c_password, c_password1)
        self.click_element(admin_locator.save_button)
        time.sleep(5)

    def system_user(self,user_name):
        self.fill_text(admin_locator.s_username,user_name)
        time.sleep(5)
        self.click_element(admin_locator.search_user)
        time.sleep(3)

    def delete_user(self):
        self.click_element(admin_locator.delete1_user)
        time.sleep(3)
        self.click_element(admin_locator.delete2_user)
        # self.click_element(admin_locator.reset)
        time.sleep(5)


    def job(self,jobtitle,desc):
        self.click_element(admin_locator.admin_job)
        self.click_element(admin_locator.job_title)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.add_jobtitle,jobtitle)
        self.fill_text(admin_locator.add_desc,desc)
        # self.click_element(admin_locator.browse)
        # self.fill_text(admin_locator.browse, value)
        time.sleep(5)
        self.click_element(admin_locator.save_button)
        time.sleep(5)

    def pay_grade(self,gradename,minsal,maxsal):
        self.click_element(admin_locator.admin_job)
        self.click_element(admin_locator.select_pay_grades)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.grade_name,gradename)
        self.click_element(admin_locator.save_button)
        self.click_element(admin_locator.add_currency)
        self.click_element(admin_locator.currency_dd)
        self.click_element(admin_locator.select_currency)
        self.fill_text(admin_locator.min_salary,minsal)
        self.fill_text(admin_locator.max_salary,maxsal)
        time.sleep(2)
        self.click_element(admin_locator.save_currency)
        time.sleep(10)

    def job_category(self,name):
        self.click_element(admin_locator.admin_job)
        self.click_element(admin_locator.select_jobcategory)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.add_name,name)
        self.click_element(admin_locator.save_button)
        time.sleep(5)


    def gen_info(self,register_no1):
        self.click_element(admin_locator.select_organization)
        self.click_element(admin_locator.general_info)
        self.click_element(admin_locator.edit)
        self.fill_text(admin_locator.register_no,register_no1)
        self.click_element(admin_locator.save_button)
        time.sleep(3)

    def locations(self,lname,lcity,lstate,pcode,lphone,laddress):
        self.click_element(admin_locator.select_organization)
        self.click_element(admin_locator.location)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.Name,lname)
        self.fill_text(admin_locator.City,lcity)
        self.fill_text(admin_locator.State,lstate)
        self.fill_text(admin_locator.pincode,pcode)
        time.sleep(3)
        self.click_element(admin_locator.country_dd)
        self.click_element(admin_locator.select_country)
        self.fill_text(admin_locator.phone,lphone)
        self.fill_text(admin_locator.address,laddress)
        self.click_element(admin_locator.save_button)
        time.sleep(5)

    def skills(self,name,desc):
        self.click_element(admin_locator.select_qualification)
        self.click_element(admin_locator.select_skill)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.Name,name)
        time.sleep(1)
        self.fill_text(admin_locator.skill_desc,desc)
        self.click_element(admin_locator.save_button)
        time.sleep(5)

    def education(self,elevel):
        self.click_element(admin_locator.select_qualification)
        self.click_element(admin_locator.select_edu)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.level,elevel)
        self.click_element(admin_locator.save_button)
        time.sleep(5)

    def lanuages(self,lang_name):
        self.click_element(admin_locator.select_qualification)
        self.click_element(admin_locator.select_lang)
        self.click_element(admin_locator.add_title)
        self.fill_text(admin_locator.Name,lang_name)
        self.click_element(admin_locator.save_button)
        time.sleep(3)











    def admin_module_user(self,employee_name,eusername,epassword,cpassword,username):
        self.click_on_admin()
        self.add_user()
        self.e_name(employee_name)
        self.status()
        self.e_username_password(eusername,epassword,cpassword)
        self.system_user(username)
        self.delete_user()


    def admin_job(self,jobtitle,desc,gradename,minsal,maxsal,name):
        self.job(jobtitle,desc)
        self.pay_grade(gradename,minsal,maxsal)
        self.job_category(name)

    def admin_organization(self,register_no,lname,lcity,lstate,pcode,lphone,laddress):
        self.gen_info(register_no)
        self.locations(lname,lcity,lstate,pcode,lphone,laddress)

    def admin_qualification(self,name,desc,elevel,lang_name):
        self.skills(name,desc)
        self.education(elevel)
        self.lanuages(lang_name)



        time.sleep(3)

