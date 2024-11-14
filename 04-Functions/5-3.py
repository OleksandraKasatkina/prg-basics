###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard53

# Reads employee's data from keyboard
first_name = keyboard53.input_string('Enter name: ')
last_name = keyboard53.input_string('Enter last name: ')
age = keyboard53.input_integer('Enter age: ')
salary = keyboard53.input_real('Enter salary: ')
is_salary_hidden = keyboard53.input_boolean('Hide salary?(y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if is_salary_hidden == False:
    print('Salary', salary)
elif is_salary_hidden == True:
    print('Salary: Hidden')