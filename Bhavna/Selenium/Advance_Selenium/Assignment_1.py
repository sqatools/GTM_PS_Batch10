# Assignment_1 - 24/07/2025 Session
# Automate the entire dummy website page with framework concept.
# https://sqatools.in/dummy-booking-website/


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class Automatewebsite:

    website_url = "https://sqatools.in/dummy-booking-website/"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.launch_website_url(url=self.website_url)

    def get_element(self,locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def get_elements(self,locator):
        element_list = self.wait.until(ec.presence_of_all_elements_located(locator))
        return element_list

    def launch_website_url(self,url):
        self.driver.get(url)
        time.sleep(2)

    def choose(self):
        self.get_element(locator=(By.XPATH,"//input[@value='radio_345']")).click()
        time.sleep(2)

    def Name(self,user_name,last_name):
        self.get_element(locator=(By.NAME,"firstname")).send_keys(user_name)
        self.get_element(locator=(By.XPATH, "//td[text()='Mumbai']//preceding::input[@id='firstname'][1]")).send_keys(last_name)
        time.sleep(2)

    def DOB(self,date):
        self.get_element(locator=(By.ID,"birthday")).send_keys(date)
        time.sleep(2)

    def Sex(self):
        self.get_element(locator=(By.ID,"female")).click()
        time.sleep(1)

    def Add_passangers(self,value):
        Passanger = self.get_element(locator=(By.ID,"admorepass"))
        Passanger1 = Select(Passanger)
        Passanger1.select_by_value(value)
        time.sleep(2)

    def travel_details(self):
        self.get_element(locator=(By.XPATH,"//input[@id='oneway']")).click()
        time.sleep(2)

    def f_d_city(self,city,city2):
        self.get_element(locator=(By.NAME,"fromcity")).send_keys(city)
        self.get_element(locator=(By.NAME,"destcity")).send_keys(city2)
        time.sleep(2)

    def date(self,d_date,r_date,v_date):
        self.get_element(locator=(By.NAME,"departdate")).send_keys(d_date)
        self.get_element(locator=(By.NAME,"returndate")).send_keys(r_date)
        self.get_element(locator=(By.ID,"visadate")).send_keys(v_date)
        time.sleep(2)

    def dummy_ticket(self):
        self.get_element(locator=(By.XPATH,"//td[text()='Mumbai']//preceding::input[@id='female'][1]")).click()
        time.sleep(1)

    def Billing_Details(self,b_name,phone,email,address):
        self.get_element(locator=(By.ID,"billing_name")).send_keys(b_name)
        self.get_element(locator=(By.ID,"billing_phone")).send_keys(phone)
        self.get_element(locator=(By.ID,"billing_email")).send_keys(email)
        self.get_element(locator=(By.ID,"billing_address")).send_keys(address)
        time.sleep(1)

    def Address(self,p_code,sa_1,sa_2):
        self.get_element(locator=(By.XPATH,"//option[@vlaue='IN']")).click()
        self.get_element(locator=(By.NAME,"postcode")).send_keys(p_code)
        self.get_element(locator=(By.XPATH,"//b[text()='Street address*']//following::input[@id='street_address1']")).send_keys(sa_1)
        self.get_element(locator=(By.XPATH,"//input[@id='street_address2']")).send_keys(sa_2)
        time.sleep(1)

    def visited_cities(self):
        self.get_element(locator=(By.XPATH,"//td[text()='Delhi']//preceding::input[@type='checkbox'][1]")).click()
        time.sleep(2)




    def Dummy_Ticket_Details(self):
        self.choose()
        self.Name('Riya','Agrawal')
        self.DOB("07-07-2007")
        self.Sex()
        self.Add_passangers("2")
        self.travel_details()
        self.f_d_city("Dubai","Delhi")
        self.date('01-08-2025','08-08-2025','31-07-2025')
        self.dummy_ticket()
        self.Billing_Details("Rajesh Agrawal","9878987898","rajesh@gmail.com","Abc Street")
        self.Address('440018','House no.6','Bangalore')
        self.visited_cities()

        time.sleep(5)
        self.driver.close()


obj = Automatewebsite()
obj.Dummy_Ticket_Details()
















'''
    def select_dropdown(self,locator):
        dropdown_element = self.get_element(locator)
        select = Select(dropdown_element)
        return select

    def select_value_by_visible_text(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        time.sleep(5)
        dd_element = self.get_element(locator=(By.LINK_TEXT))

'''