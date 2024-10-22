###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1, 100)
dice_roll_2 = random.randint(1, 100)
dice_roll_3 = random.randint(1, 100)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'Results: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')
print(f'The sum of dice rolled: {total}')