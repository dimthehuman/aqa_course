import pytest
from store_facade import StoreFacade


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
