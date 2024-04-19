class Animal:
    is_domestic = True

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    def voice(self):
        print("Stays silent.")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        self.__breed = breed
        super().__init__(name, age)

    @property
    def breed(self):
        return self.__breed

    def voice(self):
        print("Bark!!!")

    def sit(self):
        if self.breed.lower() == "corgi":
            print("Nope.")
        else:
            print("Sits calmly.")

    def fetch(self, item_to_fetch: str):
        items = ["ball", "stick", "frisbie"]
        if item_to_fetch.lower() in items:
            print(f"{self.name.capitalize()} is running after {item_to_fetch.lower()}.")
        else:
            print("Nothing to fetch.")

