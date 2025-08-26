# 22/05/2025 Session continue

"""
1. implicit wait:
2. explicit wait
3. fluent wait
4. static wait :  time.sleep(10) is considered as static wait time.
"""
from Bhavna.Selenium.Basic_Selenium.common_driver_class import *
from Bhavna.Selenium.Basic_Selenium.common_driver_class import DriverClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class seleniumwait(DriverClass):
    def __init__(self, browser='chrome'):
        super(seleniumwait,self).__init__(browser)
        #self.wait = WebDriverWait(self.driver, 10)

    def implicit_wait_time(self):
        """
                implicit wait time auto apply on each of the web element and it is maximum timeout for the element to
                be visible in the DOM structure.

                if driver is not able to find the element with given locator, then it raise a exception
                selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[name="email123"]"}
                  (Session info: chrome=138.0.7204.158); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
                Stacktrace:
                :return:
                """
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/")

        t1 = time.time()
        try:
            self.driver.find_element(By.NAME,"email").send_keys("user@gmail.com")

        except Exception as e:
            print(e)
            raise

        t2 = time.time()
        print("total time taken:",t2-t1)


    def explicit_and_fluent_wait_time(self):
        """
                ->  Explicit wait is maximum timeout to find the element in DOM structure same as like implicit wait
                ->  Explicit wait applies on specific element explicitly.
                ->  Explicit wait provide different wait condition, through which we can find the element on the basis of
                    specific condition is True or not.
                ->  Polling frequency in the explicit wait is a fluent wait condition, where it checks for element visibility
                   with given frequency and that we can change as per our requirement.

        :return:
        """

        self.driver.get("https://www.facebook.com/")
        # changed the polling frequency to update the fluent wait
        self.wait = WebDriverWait(self.driver,20,poll_frequency=5)
        t1 = time.time()

        try:
            element = self.wait.until(ec.presence_of_element_located((By.NAME,"email")))
            element.send_keys("user@gmail.com")
        except Exception as e:
            print(e)

        t2 = time.time()
        print("total time:",t2-t1)

obj = seleniumwait()
# obj.implicit_wait_time()
obj.explicit_and_fluent_wait_time()