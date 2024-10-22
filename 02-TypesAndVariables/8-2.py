###
# Calculation of circle area and circumference 
#
# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math
r = input('Enter radius: ')
r = int(r)
pi = math.pi
area = pi * r ** 2
circumference = 2 * r * pi
print(f'Circle area: {area}')
print(f'Circumference: {circumference}')