###
# A program that calculates the distance to the horizon
# from a height given in meters from the keyboard
#
import math
h = input("Please enter the height in meters: ")
h = float(h)
d = 3.57 * math.sqrt(h)
print("distance to the horizon in kilometers =", d)