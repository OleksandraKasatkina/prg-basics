###
# a program that prints the name entered from the keyboard, 
# provided it is a female name
#
name = input('Enter the name: ')

if name[-1] == 'a':
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a Polish female name')