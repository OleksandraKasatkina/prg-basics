employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

formatted_employees = list(map(lambda emp: f"{emp[0].upper()}, {emp[1]}", employees))

for emp in formatted_employees:
    print(emp)