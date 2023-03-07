from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser_type):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser_type = browser_type

    def get_web_driver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        URL = "https://opensource-demo.orangehrmlive.com"
        if self.browser_type == "edge":
            driver = webdriver.Edge()
        elif self.browser_type == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.get(URL)
        return driver
