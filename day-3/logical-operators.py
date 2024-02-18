# logical operator not flip true => false, false => true

temp = int(input("What temp outside: "))

if temp >= 0 and temp <= 30:
    print("Temp is good today! Go outside")
elif temp < 0 or temp > 30:
    print("The temp is bad today! Stay home")
