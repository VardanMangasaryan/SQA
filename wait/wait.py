from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

from wait.get_by import get_by_type

class Wait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type, locator,
                         timeout=10):
        element = None
        try:
            by_type = get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(condition.visibility_of_element_located((by_type, locator)))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return element

    def wait_for_element_to_be_clickable(self, locator_type, locator,
                         timeout=10):
        element = None
        try:
            by_type = get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(condition.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return element
