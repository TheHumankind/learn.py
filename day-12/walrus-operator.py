# := - walrus


foods = list()
while food := input('What food do u like: ') != 'quit':
    foods.append(food)

print(foods)