import pytest

from selenium import webdriver

from selenium_test.wait.wait import Wait


@pytest.fixture()
def get_driver(request):
    driver = webdriver.Chrome()
    get_wait = Wait(driver, 10)
    driver.get("https://courses.letskodeit.com/practice")

    request.cls.driver = driver
    request.cls.get_wait = get_wait

    yield driver
    driver.quit()
