from selenium.webdriver.remote.webdriver import WebDriver
from automation.HW15.pages.base_page import BasePage
from automation.HW15.utils.by import by


class BooksPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.books_search_txt = by("id=searchBox")
        self.book = by("contain_text=JS")

    def search_for_book(self):
        self.type(self.books_search_txt, "JS")

    def check_if_book_displayed(self):
        return self.element_is_displayed(self.book)

