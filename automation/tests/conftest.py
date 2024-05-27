import pytest
from automation.HW14.store_facade import StoreFacade
from automation.HW15.utils.driver_factory import driver_factory
import random
from automation.HW16.petstore_interface import pet_api
from http.client import HTTPException



@pytest.fixture(scope="class", autouse=True)
def store_class_level():
    print('Class Setup')
    yield
    print('Class Tear down')


@pytest.fixture(name='store')
def store_facade():
    print('Func Setup')
    store = StoreFacade()
    yield store
    print('Func Tear down')
    del store.catalog.phones


@pytest.fixture(name='store_with_req')
def store_facade_req(request):
    print('Func Setup')
    store = StoreFacade()
    request.cls.store = store
    yield
    print('Func Tear down')
    del store.catalog.phones


@pytest.fixture(name='store_with_params', params=[("Iphone", 100), ("Samsung", 120)])
def store_facade_params(request):
    print('Func Setup')
    store = StoreFacade()
    model, price = request.param
    store.add_phone_to_catalog(model, price)
    request.cls.store = store
    yield
    print('Func Tear down')
    del store.catalog.phones


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help=""
    )


@pytest.fixture()
def driver(pytestconfig):
    browser = pytestconfig.getoption("browser")
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    yield driver
    driver.quit()


@pytest.fixture()
def create_pet():
    payload = {
        "id": random.randint(0, 999),
        "category": {
            "id": 2,
            "name": random.choice(["Apollo", "Bandit", "Cash", "Dobby", "Echo", "Fuji", "Goofy"])
        },
        "name": "rand",
        "photoUrls": [
            "https://www.google.com/"
        ],
        "tags": [
            {
                "id": 777,
                "name": "test"
            }
        ],
        "status": "test"
    }

    return payload


@pytest.fixture
def clean_up_pet(create_pet):
    yield
    response = pet_api.delete_pet(pet_id=create_pet["id"])
    if response.status_code != 200:
        raise HTTPException(response.text)
