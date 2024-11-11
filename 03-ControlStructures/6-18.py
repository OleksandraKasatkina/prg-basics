###
# A program that determines in which quadrant of the coordinate system the point P(x, y) is located 
# or on which axis it is located, or that it is located in the position (0,0) of the coordinate system

x = int(input('Enter x coordinate: '))
y = int(input('Enter y coordinate: '))

if x == 0 and y == 0:
    print(f'Point P({x},{y}) is in the the position (0,0) of the coordinate system')
elif x == 0:
    print(f'Point P({x},{y}) is located on y-axis of the coordinate system')
elif y == 0:
    print(f'Point P({x},{y}) is located on x-axis of the coordinate system')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')