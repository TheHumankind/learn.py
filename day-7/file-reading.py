
try:
    with open('file-reading.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('file not found')

print(file.closed)
