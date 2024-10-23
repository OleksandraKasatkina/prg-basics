###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('Medium size')
elif size == 'L':
    print('Large size')
elif size == 'XL':
    print('Extra large size')

else:
    print('Incorrect symbol')