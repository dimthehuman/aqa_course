import pytest


class TestStore:

    @pytest.mark.hw14
    def test_get_empty_catalog(self, store):
        result = store.show_catalog()
        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.hw14
    @pytest.mark.parametrize('model, price, result', [
        ("iPhone", 100, "iPhone at 100"),
        ("Samsung", 120, "Samsung at 120"),
    ])
    def test_add_phone_to_catalog(self, model, price, result, store):
        store.add_phone_to_catalog(model, price)
        catalog = store.show_catalog()
        assert str(catalog[0]) == result

    @pytest.mark.hw14
    def test_remove_phone_from_catalog(self, store_with_req):
        self.store.add_phone_to_catalog("iPhone", 100)
        result = self.store.remove_phone_from_catalog("iPhone")
        assert str(result) == "iPhone at 100"

    @pytest.mark.hw14
    def test_catalog_can_hold_multiple_phones(self, store_with_req):
        self.store.add_phone_to_catalog("iPhone", 100)
        self.store.add_phone_to_catalog("Samsung", 120)
        result = self.store.show_catalog()
        assert len(result) == 2

    @pytest.mark.hw14
    def test_get_catalog(self, store_with_params):
        result = self.store.show_catalog()
        assert isinstance(result, list)
        assert len(result) != 0
