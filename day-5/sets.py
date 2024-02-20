
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cap", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.update(dishes)

dinner_table = utensils.union(dishes)

for i in dinner_table:
    print(i)

print(dinner_table.difference(dishes))
print(dinner_table.intersection(utensils))
