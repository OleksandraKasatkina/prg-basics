###
# A program that reads an integer number from the keyboard
# and prints that value as a binary and hexadecimal number
#
number = int(input('Enter number: '))
binary = bin(number)
hexadecimal = hex(number)
print(f'Binary number: {binary}')
print(f'Hexadecimal number: {hexadecimal}')