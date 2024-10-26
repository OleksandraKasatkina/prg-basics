###
# A program that asks the user for their age 
# and then checks which age group they belong to
#
age = int(input('Enter your age: '))

if age < 13:
    print('You are a child')
elif 13 <= age <= 19:
    print('You are a teen')
elif 20 <= age <= 64:
    print('You are an adult')
elif age >= 65:
    print('You are a senior')