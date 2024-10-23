###
# A program that checks what number was entered from the keyboard and prints one of the messages below
# Number ... is positive
# Number ... is negative
# Number is 0
#
number = int(input('Enter the number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
elif number == 0:
    print('Number is 0')