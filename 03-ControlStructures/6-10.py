###
# A program that calculates a dog's age in dog's years
#
human_years = float(input('Enter the age of the dog: '))

if human_years < 0:
    print('Age can not be negative')
elif human_years > 0 and human_years <= 2:
    dog_years = human_years * 10.5
elif human_years > 2:
    dog_years = 21 + (human_years - 2) * 4
print(f'The age of the dog in dog years is {dog_years}')