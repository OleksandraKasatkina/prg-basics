###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Enter something: ')
print(f'You entered {letter}')

string = int("20303")
print(f'Number representing the string: {string}')

number1 = bin(304)
print(f'Binary string representing decimal number 304: {number1}')

number2 = hex(304)
print(f'Hexadecimal string representing decimal number 304: {number2}')

unicode_code = int(ord('€'))
print(f'Integer representing the Unicode code of the € sign: {unicode_code}')

absolute_value = abs(-17)
print(f'absolute value of -17 is {absolute_value}')