from selenium.webdriver.remote.webdriver import WebDriver
from automation.tests_HW15.pages.base_page import BasePage
from automation.tests_HW15.utils.by import by


class FormsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.practice_form_btn = by("//span[text()='Practice Form']")
        self.first_name_txt = by("//input[@placeholder='First Name']")
        self.last_name_txt = by("//input[@placeholder='Last Name']")
        self.gender_rbtn = by("//input[@id='gender-radio-1']/parent::div")
        self.mobile_number_txt = by("//input[@placeholder='Mobile Number']")
        self.form_submit_btn = by("//button[@type='submit']")
        self.form_modal = by("//div[text()='Thanks for submitting the form']")

    def open_practice_form(self):
        self.click(self.practice_form_btn)

    def form_submit(self):
        self.type(self.first_name_txt, "Dmyt")
        self.type(self.last_name_txt, "Shch")
        self.click(self.gender_rbtn)
        self.type(self.mobile_number_txt, "1234567890")
        self.click(self.form_submit_btn)
        return self.element_is_displayed(self.form_modal)


