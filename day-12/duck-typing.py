class Duck:

    def walk(self):
        print('this duck is walk')

    def talk(self):
        print('this duck is qwuacking')

class Children:

    def walk(self):
        print('this children is walk')

    def talk(self):
        print('this children is talking')

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('u caught the critter')

duck = Duck()
children = Children()
person = Person()

person.catch(children)