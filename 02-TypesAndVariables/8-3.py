###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = input('Enter temperature in Celsius: ') # Read temperature in Celsius from the keyboard
celsius = float(celsius)
kelvin = celsius + 273.15 # Convert Celsius to Kelvin
fahrenheit = (celsius * (9 / 5)) + 32 # Convert Celsius to Fahrenheit
#  Print the results
print(f'Temperature in degrees Celsius: {celsius}')
print(f'Temperature in degrees Kelvin: {kelvin}')
print(f'Temperature in degrees Fahrenheit: {fahrenheit}')