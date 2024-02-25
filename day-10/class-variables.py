from car import Car


car_1 = Car('Ford', 'Mustang', 1991, 'white')

Car.wheels = 2

print('Class 1 - ' + str(Car.wheels))
print('Inst 1 - ' + str(car_1.wheels))

car_1.wheels = 4

print('Class 2 - ' + str(Car.wheels))
print('Inst 2 - ' + str(car_1.wheels))

Car.wheels = 3

print('Class 3 - ' + str(Car.wheels))
print('Inst 3 - ' + str(car_1.wheels))
