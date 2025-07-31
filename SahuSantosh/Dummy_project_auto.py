from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class customerRegister:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://sqatools.in/dummy-booking-website/')
        self.driver.maximize_window()
        sleep(1)

    def get_webelment(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def get_webelments(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element_list = wait.until(EC.presence_of_all_elements_located(locator))
        return element_list

    def first_name(self, Fn):
        self.get_webelment(('id', 'firstname')).send_keys(Fn)

    def last_name(self, ln):
        self.get_webelment((By.XPATH, '(//*[@name="firstname"])[2]')).send_keys(ln)

    def click_on_calender_date(self):
        self.get_webelment((By.CSS_SELECTOR, '#birthday')).click()

    def click_on_female_rdbtn(self):
        self.get_webelment(('css selector', '#female')).click()

    def no_of_addi_passengers(self):
        select_passenger = Select(self.get_webelment((By.ID, 'admorepass')))
        select_passenger.select_by_visible_text('Add 2 more passenger (200%)')
        sleep(2)
        select_passenger.select_by_value('2')
        sleep(2)
        select_passenger.select_by_index(3)
        sleep(2)

    def round_trip(self):
        self.get_webelment((By.ID, 'roundtrip')).click()

    def from_to_city(self, fc, tc):
        self.get_webelment(('id', 'fromcity')).send_keys(fc)
        sleep(1)
        self.get_webelment((By.CSS_SELECTOR, '#destcity')).send_keys(tc)

    def travel_details(self):
        self.round_trip()
        sleep(1)
        self.from_to_city('Bangalore', 'Hyderabad')
        sleep(1)
        self.get_webelment((By.CSS_SELECTOR, '#whatsapp')).click()
        sleep(2)

    def billing_name(self, bn):
        self.get_webelment((By.ID, 'billing_name')).send_keys(bn)
        sleep(2)

    def phone_no(self, ph):
        self.get_webelment((By.ID, 'billing_phone')).send_keys(ph)
        sleep(1)

    def email(self, emai):
        self.get_webelment((By.CSS_SELECTOR, '#billing_email')).send_keys(emai)
        sleep(1)

    def street_address(self, sa):
        self.get_webelment((By.CSS_SELECTOR, '#billing_address')).send_keys(sa)
        sleep(2)

    def bill_country_dd(self):
        bill_ddn = Select(self.get_webelment((By.ID, 'billing_country')))
        bill_ddn.select_by_visible_text('Antigua and Barbuda')
        all_countries = bill_ddn.options
        for countries in all_countries:
            print(countries.text)
        sleep(1)

    def post_code(self, pc, pref):
        self.get_webelment(('name', 'postcode')).send_keys(pc)
        sleep(1)
        self.get_webelment((By.NAME, 'prefecture')).send_keys(pref)
        sleep(1)

    def street_address2(self, sa1, sa2):
        self.get_webelment(('css selector', '#street_address1')).send_keys(sa1)
        sleep(1)
        self.get_webelment((By.ID, 'street_address2')).send_keys(sa2)
        sleep(1)

    def billing_details(self):
        self.billing_name('Mega Star Chiranjeevi')
        self.phone_no('7989597411')
        self.email('chirusantosh@123.com')
        self.street_address('Madiwala')
        self.bill_country_dd()
        self.post_code('Bommnahalli', 'Ganesh temple')
        self.street_address2('near AT street', 'Brundha theatre')

    def passenger_details(self):
        self.chosing_option()
        self.first_name("Mega Star")
        sleep(1)
        self.last_name("Chiranjeevi")
        sleep(1)
        self.click_on_calender_date()
        sleep(1)
        self.click_on_female_rdbtn()
        sleep(2)
        self.no_of_addi_passengers()
        sleep(2)
        self.travel_details()
        sleep(2)
        self.billing_details()
        sleep(1)
        self.table_visited_city()
        self.driver.close()

    def chosing_option(self):
        self.get_webelment(
            (By.XPATH, '//*[text()="Dummy hotel booking ticket – $400 "]/preceding-sibling::input')).click()
        sleep(2)

    def table_visited_city(self):
        self.get_webelment((By.XPATH, '//*[text()="6003"]/preceding-sibling::td/input')).click()
        sleep(3)


cust_reg = customerRegister()
cust_reg.passenger_details()
# cust_reg.billing_details()
# cust_reg.bill_country_dd()
# cust_reg.table_visited_city()
# cust_reg.table_visited_city()
# cust_reg.no_of_addi_passengers()
# cust_reg.travel_details()
