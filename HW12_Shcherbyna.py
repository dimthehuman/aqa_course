import abc


# Task 1
class AbstractDevice(abc.ABC):

    @abc.abstractmethod
    def turn_on(self):
        pass

    @abc.abstractmethod
    def turn_off(self):
        pass


class ConcreteDevice(AbstractDevice):

    def turn_on(self):
        print("Device is turning on.")

    def turn_off(self):
        print("Device is turning off.")


# Task 2
class TV:
    def turn_on(self):
        print("TV is turning on.")

    def turn_off(self):
        print("TV is turning off.")


class Lights:
    def turn_on(self):
        print("Lights are turning on.")

    def turn_off(self):
        print("Lights are turning off.")


class Heating:
    def turn_on(self):
        print("Heating is turning on.")

    def turn_off(self):
        print("Heating is turning off.")


class HomeFacade:

    def __init__(self):
        self.__tv = TV()
        self.__lights = Lights()
        self.__heating = Heating()

    @property
    def tv(self):
        return self.__tv

    @property
    def lights(self):
        return self.__lights

    @property
    def heating(self):
        return self.__heating

    def come_home(self):
        self.tv.turn_on()
        self.lights.turn_on()
        self.heating.turn_on()

    def go_out(self):
        self.tv.turn_off()
        self.lights.turn_off()
        self.heating.turn_off()


# Task 3
class MyContextManager:

    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"An exception occurred: {exc_type}")
        self.file.close()

