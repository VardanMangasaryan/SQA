from selenium.webdriver import ActionChains

from pom.base.selenium_driver import SeleniumDriver
from pom.wait.wait import Wait


class BasePage(SeleniumDriver):
    """Could be more functional"""

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = Wait(self.driver, 10)

    def get_wait(self):
        return self.wait

    def get_actions(self):
        return ActionChains(self.driver)

    def wait_for_page_load(self):
        self.get_wait().wait_for_page()

    def verify_page_title(self, title):
        return self.driver.get_current_page_title() == title

    def verify_page_url(self, url):
        return self.driver.get_current_url() == url
