class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    
    def __str__(self):
        # Create the base string with surname, first letter of the name, and seniority
        result = f'{self.surname.lower()}{self.name[0].upper()}{self.seniority}'
        
        # Check if the employee is an adult (age >= 18)
        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()

# Testing the class with the given examples
employee1 = C("Anna", "May", 17, 7)
employee2 = C("George", "Brown", 21, 4)

# Displaying the results
print(employee1)  # Output: maya7
print(employee2)  # Output: BROWNG4
