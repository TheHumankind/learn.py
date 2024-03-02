import functools

letters = ['H', 'E', 'L', 'L', 'O']

add_letters = lambda x, y: x + y

word = functools.reduce(add_letters, letters)

print(word)

numbers = [5, 4, 3, 2, 1]

calc_fact = lambda x, y: x * y

fact = functools.reduce(calc_fact, numbers)

print(fact)
