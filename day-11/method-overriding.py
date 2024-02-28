class Animal:
    def eat(self):
        print('this animal is eat')


class Rabbit(Animal):
    def eat(self):
        print('the rabbit is eating a carrot')


animal = Animal()
rabbit = Rabbit()

animal.eat()
rabbit.eat()

