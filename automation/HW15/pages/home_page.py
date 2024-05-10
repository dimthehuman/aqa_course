from selenium.webdriver.remote.webdriver import WebDriver
from automation.HW15.pages.base_page import BasePage
from automation.HW15.pages.alerts_page import AlertsPage
from automation.HW15.pages.forms_page import FormsPage
from automation.HW15.pages.books_page import BooksPage
from automation.HW15.utils.by import by


class HomePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.forms_btn = by("contain_text=Forms")
        self.books_btn = by("contain_text=Book Store")
        self.alerts_btn = by("contain_text=Alerts")

    def click_on_forms_btn(self):
        self.click(self.forms_btn)
        return FormsPage(self.driver)

    def click_on_alerts_btn(self):
        self.click(self.alerts_btn)
        return AlertsPage(self.driver)

    def click_on_books_btn(self):
        self.click(self.books_btn)
        return BooksPage(self.driver)
