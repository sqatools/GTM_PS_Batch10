"""
1. implicit wait:
2. explicit wait
3. fluent wait
4. static wait :  time.sleep(10) is considered as static wait time.
"""

import time
from Common_driver_class import *
from Common_driver_class import DriverClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumWaits(DriverClass):


    def __init__(self, browser='chrome'):
        super(SeleniumWaits, self).__init__(browser)


    def implicit_wait_time(self):
        """
        Implicit wait time auto apply on each of the web element & it is maximum timeout for the
        element to be visible in the DOM structure.

        If driver is not able to find the element with given locator then it raise the exception.

        selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate
        element: {"method":"css selector","selector":"[name="email1234"]"}
        (Session info: chrome=138.0.7204.169); For documentation on this error, please visit:
        https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
        Stacktrace:

        :return:
        """

        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/")

        t1 = time.time()
        try:
            self.driver.find_element(By.NAME, "email1234").send_keys("user1@gmail.com")
        except Exception as e:
            print(e)
            raise

        t2 = time.time()
        print("Total time taken :", t2-t1)



    def explicit_and_fluet_wait_time(self):
        """
        >> Explicit wait is maximum timeout to find the element in DOM structure same as like implicit
        wait
        >> Explicit wait applies on specific element explicitly.
        >> Explicit wait provide different wait conditions through which we can find the element on the
        basis of specific condition is True or not.
        >> Polling frequency in the explicit wait is a fluent wait condition where it checks for
        element visibility with given frequency and that we can change as per our requirement.
        :return:
        """
        self.driver.get("https://www.facebook.com/")
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=5)
        t1 = time.time()
        try:
            element = self.wait.until(ec.presence_of_element_located((By.NAME, "email")))
            element.send_keys("user1@gmail.com")
        except Exception as e:
            print(e)

        t2 = time.time()
        print("Total time: ", t2-t1)


obj = SeleniumWaits()
obj.explicit_and_fluet_wait_time()
# obj.implicit_wait_time()
# Total time taken : 0.10952353477478027
