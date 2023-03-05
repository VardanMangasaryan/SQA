import pytest

from selenium import webdriver

from selenium_test.wait.wait import Wait


# @pytest.fixture
# def get_driver(request):
#     browser_type: str = request.config.getoption("--browser")
#     if browser_type.lower() == 'chrome':
#         driver = webdriver.Chrome()
#     else:
#         driver = webdriver.Firefox()
#     get_wait = Wait(driver, 10)
#     driver.get("https://courses.letskodeit.com/practice")
#
#     request.cls.driver = driver
#     request.cls.get_wait = get_wait
#
#     yield driver
#     driver.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
