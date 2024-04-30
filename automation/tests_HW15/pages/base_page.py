from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    def wait_until(self, locator: tuple, condition, **kwargs) -> WebElement:
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until(condition(locator))

    def wait_until_not(self, locator: tuple, condition, **kwargs):
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until_not(condition(locator))

    def scroll_into_view(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def click(self, locator: tuple):
        condition = ec.element_to_be_clickable
        element = self.wait_until(locator, condition)
        self.scroll_into_view(element).click()

    def type(self, locator: tuple, value: str):
        condition = ec.visibility_of_element_located
        self.wait_until(locator, condition).send_keys(value)

    def text(self, locator: tuple):
        condition = ec.visibility_of_element_located
        element = self.wait_until(locator, condition)
        return element.text

    def element_is_displayed(self, locator: tuple):
        condition = ec.visibility_of_element_located
        element = self.wait_until(locator, condition)
        return element.is_displayed()


