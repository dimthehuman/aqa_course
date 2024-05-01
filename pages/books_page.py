from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from utils.by import by


class BooksPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.books_search_txt = by("//input[@id='searchBox']")
        self.book = by("//a[contains(text(), 'JS')]")

    def search_for_book(self):
        self.type(self.books_search_txt, "JS")
        return self.element_is_displayed(self.book)

