# main.py file
from thermometer import Thermometer  # Import the Thermometer class from thermometer.py

def main():
    # Create a thermometer object
    my_thermometer = Thermometer()

    # Turn the thermometer on
    print("Turning the thermometer on...")
    my_thermometer.turn_on()

    # Measure the temperature
    print("Measuring temperature...")
    my_thermometer.measure_temperature()

    # Display the temperature
    print("Displaying temperature...")
    my_thermometer.display_temperature()

    # Turn the thermometer off
    print("Turning the thermometer off...")
    my_thermometer.turn_off()

if __name__ == "__main__":
    main()
