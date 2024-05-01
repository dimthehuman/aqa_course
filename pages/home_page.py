from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.alerts_page import AlertsPage
from pages.forms_page import FormsPage
from pages.books_page import BooksPage
from utils.by import by


class HomePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.forms_btn = by("//div[@class='card mt-4 top-card'][2]")
        self.books_btn = by("//div[@class='card mt-4 top-card'][6]")
        self.alerts_btn = by("//div[@class='card mt-4 top-card'][3]")

    def click_on_forms_btn(self):
        self.click(self.forms_btn)
        return FormsPage(self.driver)

    def click_on_alerts_btn(self):
        self.click(self.alerts_btn)
        return AlertsPage(self.driver)

    def click_on_books_btn(self):
        self.click(self.books_btn)
        return BooksPage(self.driver)
