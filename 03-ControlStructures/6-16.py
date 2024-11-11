###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0

jacket_time = 40
underwear_time = 70
shoes_time = 20
rinse_time = 15
spin_time = 9

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if program == 'j':
    total_washing_time += jacket_time
elif program == 'u':
    total_washing_time += underwear_time
elif program == 's':
    total_washing_time += shoes_time
else:
    print('Invalid washing program selected.')

if extra_rinse == 'y':
    total_washing_time += rinse_time

if extra_spin == 'y':
    total_washing_time += spin_time

print(f'Total washing time: {total_washing_time} minutes')