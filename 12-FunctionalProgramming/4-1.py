employees = [
    "SMITH Lucy", "JONES Janet", "LEE Jerry",
    "JACKSON Peter", "JOHNSON Rick",
    "LEWIS Terry", "CLARKE Robin"
]

emp_J = list(filter(lambda e: e.split()[0][0] == "J", employees))

print("Employees whose surnames start with 'J':")
for employee in emp_J:
    print(employee)