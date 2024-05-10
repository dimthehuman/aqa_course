import pytest
from automation.HW15.pages.home_page import HomePage


class TestDemoQA:

    @pytest.mark.hw15
    def test_form_submit(self, driver):
        home_page = HomePage(driver)
        form_page = home_page.click_on_forms_btn()
        form_page.open_practice_form()
        form_page.form_submit()
        assert form_page.check_if_form_modal_displayed()

    @pytest.mark.hw15
    def test_accept_alert(self, driver):
        home_page = HomePage(driver)
        alerts_page = home_page.click_on_alerts_btn()
        alerts_page.click_on_alerts_options_btn()
        alerts_page.click_on_instant_alert_btn()
        assert alerts_page.get_alert_text() == "You clicked a button"

    @pytest.mark.hw15
    def test_book_search(self, driver):
        home_page = HomePage(driver)
        books_page = home_page.click_on_books_btn()
        books_page.search_for_book()
        assert books_page.check_if_book_displayed()
