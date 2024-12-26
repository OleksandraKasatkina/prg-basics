# thermometer.py file
import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0.0
    
    def turn_on(self):
        self.is_on = True
        print("Thermometer is now on.")
    
    def turn_off(self):
        self.is_on = False
        print("Thermometer is now off.")
    
    def measure_temperature(self):
        if self.is_on:
            # Randomly generate a temperature between 34.0 and 42.0 degrees Celsius (accuracy of 0.1 degrees)
            self.temperature = round(random.uniform(34.0, 42.0), 1)
            print(f"Measured temperature: {self.temperature}C")
        else:
            print("The thermometer is off. Please turn it on first.")
    
    def display_temperature(self):
        if self.is_on:
            if self.temperature >= 41.0:
                print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
            elif self.temperature >= 37.0:
                print(f"Temperature: {self.temperature}C (fever)")
            else:
                print(f"Temperature: {self.temperature}C")
        else:
            print("The thermometer is off. Please turn it on first.")
