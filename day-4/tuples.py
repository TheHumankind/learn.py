student = ("Ula", 26, "male")

print(student.count("Ula"))
print(student.index("male"))
print(student[student.index("male")])

for i in student:
    print(i)

if 26 in student:
    print("Old")

