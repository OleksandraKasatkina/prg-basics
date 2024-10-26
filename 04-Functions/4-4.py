###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    string = str(abs(number))
    sum = 0
    for a in string:
        sum += int(a) 
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')