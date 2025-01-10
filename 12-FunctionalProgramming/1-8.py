initials = lambda name,surname : name[0].upper()+surname[0].upper()

name = input("Enter your first name: ")
surname = input("Enter your surname: ")

print(f"Your initials are: {initials(name, surname)}")