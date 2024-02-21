
# can be applied to strings

number_a = 1000
number_b = 11111
print('The number is {}'.format(number_a))
print(f'The number is {number_a}')
print('The num pi is {:.3f}'.format(number_a))
print('The num pi is {:,}'.format(number_a))
print('The num pi is {:b}'.format(number_a))
print('The num pi is {:o}'.format(number_a))
print('The num pi is {:X}'.format(number_a))
print('The num pi is {:E}'.format(number_a))

print('The numbers is 1:{0} and 2:{1}'.format(number_a, number_b))