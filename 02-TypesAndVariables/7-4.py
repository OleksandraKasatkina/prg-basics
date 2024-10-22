###
# A program that, based on the circumference of the tree entered from the keyboard, 
# calculates and prints the value True if the tree can be cut down, 
# or print the value False otherwise
# A tree may be cut down if its diameter is at least 50 cm

circumference = float(input('Enter circumference of the tree in cm: '))
import math
diameter = circumference / math.pi
can_be_cut_down = diameter >= 50
print(f'Tree can be cut down: {can_be_cut_down}')