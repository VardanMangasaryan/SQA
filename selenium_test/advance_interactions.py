from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_test.wait.wait import Wait
from selenium.webdriver.support.select import Select

driver: WebDriver
get_wait: Wait


def get_url(url):
    global driver, get_wait
    driver = webdriver.Chrome()
    driver.get(url)
    get_wait = Wait(driver, 10)


class TestActions:

    def test_scroll(self):
        get_url("https://courses.letskodeit.com/practice")
        home_element = get_wait.wait_for_element((By.CSS_SELECTOR, 'li[data-id="41191"]'))

        # Scroll into element
        driver.execute_script("arguments[0].scrollIntoView();", home_element)

        # Scroll up to 500 px
        driver.execute_script("window.scrollBy(0, -500);")

        # Scroll down to 500 px
        driver.execute_script("window.scrollBy(0, 500);")

        # Scroll right to 500 px
        driver.execute_script("window.scrollBy(500, 0);")

        # Scroll left to 500 px
        driver.execute_script("window.scrollBy(-500, 0);")

    def test_checkbox_buttons(self):
        get_url('https://courses.letskodeit.com/practice')
        bmw_checkbox = get_wait.wait_for_element((By.CSS_SELECTOR, 'input[id="bmwcheck"]'))
        assert not bmw_checkbox.is_selected()
        bmw_checkbox.click()
        # assert get_wait.wait_for_element_to_be_selected(bmw_checkbox)
        assert bmw_checkbox.is_selected()

    def test_radio_buttons_buttons(self):
        get_url('https://courses.letskodeit.com/practice')
        benz_radiobutton = get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="benzradio"]')
        assert not benz_radiobutton.is_selected()
        benz_radiobutton.click()
        # assert get_wait.wait_for_element_to_be_selected(bmw_checkbox)
        assert benz_radiobutton.is_selected()

        honda_radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[id="hondaradio"]')
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        assert not benz_radiobutton.is_selected()

    def test_dropdown(self):
        get_url('https://courses.letskodeit.com/practice')
        cars = get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)

        # Selecting by index
        cars_select.select_by_index(0)

        # Selecting by value
        cars_select.select_by_value("honda")

        # Selecting by text
        cars_select.select_by_visible_text("Benz")

        # Returns selected option
        assert cars_select.first_selected_option == "Benz"

    def test_hidden_elements(self):
        get_url('https://courses.letskodeit.com/practice')

        show_text = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[id="show-textbox"]')
        hide_text = driver.find_element(By.CSS_SELECTOR, 'input[id="hide-textbox"]')
        hidden_input = driver.find_element(By.CSS_SELECTOR, 'input[id="displayed-text"]')

        some_text = "some text"

        assert hidden_input.is_displayed()

        hide_text.click()
        assert not hidden_input.is_displayed()

        show_text.click()
        assert hidden_input.is_displayed()

        hidden_input.click()
        hidden_input.send_keys(some_text)

        hide_text.click()
        show_text.click()

        assert hidden_input.get_attribute('value') == some_text

    def test_disabled(self):
        get_url('https://courses.letskodeit.com/practice')
        disabled_text = "Disabled text"
        disabled_input = get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="enabled-example-input"]')

        assert disabled_input.is_enabled()
        disabled_input.send_keys(disabled_text)

        disable_button = driver.find_element(By.CSS_SELECTOR, 'input[id="disabled-button"]')
        disable_button.click()

        assert not disabled_input.is_enabled()

        enable_button = driver.find_element(By.CSS_SELECTOR, 'input[id="enabled-button"]')
        enable_button.click()

        assert disabled_input.is_enabled()

        assert disabled_input.get_attribute('value') == disabled_text

    def test_alert(self):
        get_url('https://courses.letskodeit.com/practice')

        first_name = "Gagik"
        second_name = "Vazgen"

        input_alert = get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="name"]')
        input_alert.send_keys(first_name)

        driver.find_element(By.CSS_SELECTOR, 'input[id="alertbtn"]').click()
        first_alert = driver.switch_to.alert

        assert first_alert.text == f'Hello {first_name}, share this practice page and share your knowledge'
        first_alert.accept()

        input_alert.send_keys(second_name)
        driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]').click()

        second_alert = driver.switch_to.alert

        assert second_alert.text == f'Hello {second_name}, Are you sure you want to confirm?'
        second_alert.dismiss()

    def test_hover(self):
        get_url('https://courses.letskodeit.com/practice')
        input_name = "Armen"

        mouse_hover = get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)

        driver.find_element(By.CSS_SELECTOR, 'input[id="name"]').send_keys(input_name)

        actions = ActionChains(driver)
        actions.move_to_element(mouse_hover).perform()

        driver.find_element(By.CSS_SELECTOR, 'div[class="mouse-hover-content"] > a:nth-child(2)').click()

        # get_attribute('value') -> returns text in input field
        assert get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="name"]').get_attribute('value') != input_name

    def test_drag_drop(self):
        get_url('https://jqueryui.com/droppable/')

        driver.switch_to.frame(0)

        draggable = get_wait.wait_for_element(By.CSS_SELECTOR, 'div[id="draggable"]')
        droppable = driver.find_element(By.CSS_SELECTOR, 'div[id="droppable"]')

        assert draggable.value_of_css_property('left') == '0px'

        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

        # Another way
        # actions.click_and_hold(draggable).move_to_element(droppable).release().perform()

        assert draggable.value_of_css_property('left') == '163px'
        assert droppable.text == "Dropped!"
