# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.surname = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student4 = Student()

    student1.name = "Dominic"
    student1.age = 19
    student1.surname = "Smith"
    student2.name = "Olivia"
    student2.age = 21
    student2.surname = "Gray"
    student3.name = "Pedro"
    student3.age = 49
    student3.surname = "Pascal"
    student4.name = "Henry"
    student4.age = 41
    student4.surname = "Cavill"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name} {student1.surname}, {student1.age} years old')
    print(f'{student2.name} {student2.surname}, {student2.age} years old')
    print(f'{student3.name} {student3.surname}, {student3.age} years old')
    print(f'{student4.name} {student4.surname}, {student4.age} years old')

if __name__ == "__main__":
    main()