from selenium.webdriver.remote.webdriver import WebDriver
from automation.tests_HW15.pages.base_page import BasePage
from automation.tests_HW15.utils.by import by


class AlertsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.alerts_options_btn = by("//span[text()='Alerts']")
        self.instant_alert_btn = by("//button[@id='alertButton']")

    def click_on_alerts_options_btn(self):
        self.click(self.alerts_options_btn)

    def click_on_instant_alert_btn(self):
        self.click(self.instant_alert_btn)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
