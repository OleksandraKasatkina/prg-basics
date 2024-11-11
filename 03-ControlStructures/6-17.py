###
# A program that allows you to convert time in 24-hour format to 12-hour format
#

hours_24 = int(input('Enter hours (in 24-hour format): '))
minutes = int(input('Enter minutes: '))

if hours_24 == 0:
    hours_12 = 12
    period = 'am'
elif 1 <= hours_24 < 12:
    hours_12 = hours_24
    period = 'am'
elif hours_24 == 12:
    hours_12 = 12
    period = 'pm'
else:
    hours_12 = hours_24 - 12
    period = 'pm'

print(f'Time in 12-hour format: {hours_12:02d}:{minutes:02d} {period}')