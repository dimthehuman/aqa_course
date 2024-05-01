import pytest

from utils.driver_factory import driver_factory


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help=""
    )

@pytest.fixture()
def driver(request, pytestconfig):

    driver = driver_factory(pytestconfig.getoption("browser"))
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    yield driver
    driver.quit()
