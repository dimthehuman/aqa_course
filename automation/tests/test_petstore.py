import pytest
from automation.HW16.petstore_interface import pet_api
from jsonschema import validate
from automation.HW16 import schemas


class TestPetStore:

    @pytest.mark.hw16
    def test_get_pet_by_id(self, create_pet, clean_up_pet):
        pet_api.create_pet(create_pet)
        get_pets = pet_api.find_pet_by_id(create_pet["id"])
        assert get_pets.status_code == 200
        validate(get_pets.json(), schemas.GET_PETS)

    @pytest.mark.hw16
    def test_create_new_pet(self, create_pet, clean_up_pet):
        post_pets = pet_api.create_pet(create_pet)
        assert post_pets.status_code == 200
        validate(post_pets.json(), schemas.ADD_PET)

    @pytest.mark.hw16
    def test_update_pet(self, create_pet, clean_up_pet):
        pet_api.create_pet(create_pet)
        create_pet["category"]["name"] = "Rex"
        put_pets = pet_api.update_pet(create_pet)
        assert put_pets.status_code == 200
        validate(put_pets.json(), schemas.ADD_PET)

    @pytest.mark.hw16
    def test_delete_pet(self, create_pet):
        pet_api.create_pet(create_pet)
        delete_pets = pet_api.delete_pet(create_pet["id"])
        assert delete_pets.status_code == 200
        validate(delete_pets.json(), schemas.DELETE_PET)
