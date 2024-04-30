import pytest
from automation.tests_HW15.utils.driver_factory import driver_factory


@pytest.fixture()
def driver(request):
    driver = driver_factory("chrome")
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    yield driver
    driver.quit()
