
squares = []

for i in range(1, 11):
    squares.append(i * i)

print(squares)

squares = [i * i for i in range(1, 11)]

print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

passed = list(filter(lambda x: x > 60, students))

passed = [i for i in students if i > 60]
passed = [i if i >= 60 else 'Failed' for i in students]

print(passed)