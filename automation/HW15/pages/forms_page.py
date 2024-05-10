from selenium.webdriver.remote.webdriver import WebDriver
from automation.HW15.pages.base_page import BasePage
from automation.HW15.utils.by import by


class FormsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.practice_form_btn = by("contain_text=Practice Form")
        self.first_name_txt = by("id=firstName")
        self.last_name_txt = by("id=lastName")
        self.gender_rbtn = by("//input[@id='gender-radio-1']/parent::div")
        self.mobile_number_txt = by("id=userNumber")
        self.form_submit_btn = by("id=submit")
        self.form_modal = by("contain_text=Thanks for submitting the form")

    def open_practice_form(self):
        self.click(self.practice_form_btn)

    def form_submit(self):
        self.type(self.first_name_txt, "Dmyt")
        self.type(self.last_name_txt, "Shch")
        self.click(self.gender_rbtn)
        self.type(self.mobile_number_txt, "1234567890")
        self.click(self.form_submit_btn)

    def check_if_form_modal_displayed(self):
        return self.element_is_displayed(self.form_modal)


