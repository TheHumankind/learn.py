sym = ''
length = 0
columns = 0

while not (len(sym) == 1) or length <= 0 or columns <= 0:
    sym = input("Enter 1 symbol: ")
    length = int(input("Enter positive number for length: "))
    columns = int(input("Enter positive number for columns: "))

for i in range(1, length + 1, 1):
    for j in range(1, columns + 1, 1):
        print(sym, end="")
    print()
