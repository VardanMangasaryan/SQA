from selenium.webdriver import ActionChains

from pom.base.selenium_driver import SeleniumDriver
from pom.wait.wait import Wait


class BasePage(SeleniumDriver):
    """Could be more functional"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_wait(self):
        return Wait(self.driver, 10)

    def get_actions(self):
        return ActionChains(self.driver)


