class Animal:
    alive = True

    def eat(self):
        print('i\'m eat')

    def sleeping(self):
        print('i\'m sleeping')


class Rabbit(Animal):

    def eat(self):
        print('nonono')

    def run(self):
        print('i\'m running')


class Fish(Animal):
    def swim(self):
        print('i\'m swimming')


class Bird(Animal):
    def fly(self):
        print('i\'m flying')


rabbit = Rabbit()
fish = Fish()
bird = Bird()

rabbit.eat()
fish.eat()
rabbit.run()
fish.swim()
bird.fly()