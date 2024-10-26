###
# A program that asks for the number of hours of parking, 
# then calculates and prints the correct fee
#
hours = int(input('Enter the number of hours the car was parked: '))

if hours >=1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
print(f'The parking fee is: {fee}')