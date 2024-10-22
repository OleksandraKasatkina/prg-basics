### 
# A program that checks whether the vehicle speed entered from the keyboard is correct
# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h
speed = input('Enter vehicle speed: ')
speed = int(speed)
valid = 40 <= speed <= 140
print(f'Speed is valid: {valid}')