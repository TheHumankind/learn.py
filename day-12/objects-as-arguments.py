class Car:

    color = None


class Moto:

    color = None

def change_color(car, color):
    car.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike = Moto()

change_color(car_1, 'red')
change_color(car_2, 'blue')
change_color(car_3, 'white')
change_color(bike, 'black')

print(car_3.color)
print(car_2.color)
print(car_1.color)
print(bike.color)