from module74 import is_in_range

number = int(input('Enter the number: '))
x = int(input('Enter the start of the range: '))
y = int(input('Enter the end of the range: '))

in_range = is_in_range(number, x, y)

if in_range:
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")