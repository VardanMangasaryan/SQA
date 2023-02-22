from selenium.webdriver.common.by import By


def get_by_type(locator_type):
    locator_type = locator_type.lower()
    if locator_type == "id":
        return By.ID
    elif locator_type == "name":
        return By.NAME
    elif locator_type == "xpath":
        return By.XPATH
    elif locator_type == "css selector":
        return By.CSS_SELECTOR
    elif locator_type == "class name":
        return By.CLASS_NAME
    elif locator_type == "link text":
        return By.LINK_TEXT
    elif locator_type == "partial link text":
        return By.PARTIAL_LINK_TEXT
    elif locator_type == "tag name":
        return By.TAG_NAME
    else:
        print("Locator type " + locator_type + " not correct/supported")
    return False
