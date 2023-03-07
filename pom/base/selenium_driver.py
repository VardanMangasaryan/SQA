import os
import time
import selenium.common.exceptions as Ex


class SeleniumDriver:
    """Not all methods implemented"""
    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    def navigate_to_url(self, url: str):
        self.driver.get(url)

    def get_current_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.forward()

    def find_element_by(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
        except Ex.NoSuchElementException:
            print('Element not found')
        return element

    def find_list_of_elements(self, locator):
        elements = None
        try:
            elements = self.driver.find_elements(*locator)
        except Ex.NoSuchElementException:
            print('Element not found')
        return elements

    def click(self, element):
        if element:
            try:
                element.click()
                return True
            except (Ex.NoSuchElementException, Ex.ElementNotInteractableException,
                    Ex.ElementClickInterceptedException) as error:
                print(error)
                return False
        print("Element reference is None")
        return False

    def is_element_displayed(self, locator):
        displayed = False
        if locator:
            element = self.find_element_by(*locator)
            try:
                displayed = element.is_displayed()
            except (Ex.NoSuchElementException, Ex.ElementNotVisibleException) as error:
                print("Element is not displayed: Error: " + error)

        return displayed

    def take_screenshot(self):
        file_name = str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(destination_file, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)

        except:
            print("### Exception Occurred when taking screenshot ###")

