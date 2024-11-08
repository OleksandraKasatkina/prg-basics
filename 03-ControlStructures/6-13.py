###
# A program that prints a message when the specified car speed, 
# read from the keyboard, has been exceeded
#
speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input('Enter the car speed: '))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Car speed is within the allowed range')