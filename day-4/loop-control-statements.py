trigger = True

while trigger:
    name = input("Enter u name: ")
    if name != "":
        break

phone_number = "123-456-789"
new_phone_number = ""

for i in phone_number:
    if i == "-":
        continue
    new_phone_number += i

print(new_phone_number)

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)