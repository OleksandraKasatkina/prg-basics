###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    lines = file.readlines()

line_number = 1

for line in lines:
    print(f'{line_number}. {line}', end='')
    line_number +=1