from selenium import webdriver
from selenium.webdriver.common.by import By
from wait.wait import Wait

driver = webdriver.Chrome()


def browser_navigation():
    # Keep drivers in PATH
    global driver
    driver.get("https://www.demoblaze.com/")

    # Refresh
    driver.refresh()

    # Navigate, back and forward
    driver.get('https://google.com')
    driver.back()
    driver.forward()

    # Get title
    tab_title = driver.title

    # Get current url
    current_url = driver.current_url

    # Maximize window
    driver.maximize_window()

    # Minimize window
    driver.minimize_window()
    driver.switch_to.new_window()

    # Switch to new tab
    driver.switch_to.new_window('tab')
    driver.get('https://www.facebook.com')

    # Open new window
    driver.switch_to.new_window('window')

    # Number of open tabs
    len(driver.window_handles)

    # Get page source
    page_source = driver.page_source

    # Quit browser
    driver.quit()


class Tests:

    def test_login(self):
        global driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        get_wait = Wait(driver, 10)

        username = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[name="username"]')
        username.click()
        username.send_keys('Admin')

        password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password.click()
        password.send_keys('admin123')

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        assert get_wait.wait_for_element(By.CSS_SELECTOR, 'span[class="oxd-userdropdown-tab"]').is_displayed()

    def test_second(self):
        self.test_login()
        global driver

        get_wait = Wait(driver, 10)
        get_wait.wait_for_element(By.CSS_SELECTOR, 'ul[class="oxd-main-menu"] li')
        navigation_elements = driver.find_elements(By.CSS_SELECTOR, 'ul[class="oxd-main-menu"] li')
        navigation_elements[0].click()

        assert get_wait.wait_for_element(By.CSS_SELECTOR, 'div[class="oxd-table-filter"]').is_displayed()
        username = driver.find_elements(By.CSS_SELECTOR, 'input[class="oxd-input oxd-input--active"]')[1]
        username.click()
        username.send_keys("Kalbas")
        driver.find_element(By.CSS_SELECTOR, 'button[class="oxd-button oxd-button--medium oxd-button--ghost"]').click()
