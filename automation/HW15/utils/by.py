from selenium.webdriver.common.by import By


def by(locator: str) -> tuple:
    if locator.startswith('//'):
        return By.XPATH, locator
    elif locator.startswith('name='):
        return By.NAME, locator[5:]
    elif locator.startswith('id='):
        return By.ID, locator[3:]
    elif locator.startswith('contain_text='):
        return By.XPATH, f"//*[contains(text(), '{locator[13:]}')]"
    elif locator.startswith("class="):
        return By.CLASS_NAME, locator[6:]
