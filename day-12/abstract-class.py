from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print('u drive a car')


class Motorcycle(Vehicle):

    def go(self):
        print('u ride a moto')


car = Car()
moto = Motorcycle()


car.go()
moto.go()