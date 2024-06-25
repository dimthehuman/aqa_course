import requests

BASE_URL = "https://petstore.swagger.io/v2/"


class PetstoreInterface:

    def create_pet(self, payload: dict):
        return requests.post(BASE_URL + 'pet/', json=payload)

    def delete_pet(self, pet_id: int):
        return requests.delete(f'{BASE_URL}pet/{pet_id}')

    def find_pet_by_id(self, pet_id: int):
        return requests.get(f'{BASE_URL}pet/{pet_id}')

    def update_pet(self, payload: dict):
        return requests.put(BASE_URL + 'pet/', json=payload)


pet_api = PetstoreInterface()
