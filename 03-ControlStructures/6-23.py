### 
# A program that creates a multiplication table 
# in the range 1 to 10 for any number entered by the user
#

number = int(input('Enter the number: '))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')