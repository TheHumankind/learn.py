# students = ['Squid', 'Sponge', 'Sandy', 'Patrick', 'Krabs']
#
# students.sort()
# sorted_names = sorted(students)
#
# for i in sorted_names:
#     print(i)

students = [('Squid', 'F', 60), ('Sponge', 'A', 33), ('Sandy', 'B', 22), ('Patrick', 'S', 100), ('Krabs', 'G', 10)]

age = lambda age: age[2]
students.sort(key=age)

print(students)
