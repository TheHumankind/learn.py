
try:
    numerator = int(input('ent a num to divide: '))
    denominator = int(input('ent a num to divide by: '))
    res = numerator / denominator
except ZeroDivisionError as e:
    print('u cant div by zero')
    print(e)
except ValueError as e:
    print('Only numbers allowed')
    print(e)
except Exception as e:
    print('smth went wrong :-(')
    print(e)
else:
    print(res)
finally:
    print('program ex')

