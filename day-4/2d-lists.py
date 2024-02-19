
drinks = ["coffee", "soda", "tea"]
dinners = ["pizza", "hamburger", "hotdog"]
desert = ["cake", "icecream"]

food = [drinks, dinners, desert]

# print(food[0][0])

for i in food:
    for j in i:
        print(j + " ", end="")
    print()