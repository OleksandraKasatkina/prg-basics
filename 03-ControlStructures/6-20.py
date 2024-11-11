###
# A program that converts a decimal number into a binary number
#
decimal_number = int(input('Enter decimal number: '))

quotient = decimal_number
remainders = []

while quotient > 0:
    remainder = quotient % 2  
    remainders.append(remainder)  
    quotient = quotient // 2  

binary_number = ''.join(map(str, remainders[::-1]))
print(f'{decimal_number}(10) = {binary_number}(2)')