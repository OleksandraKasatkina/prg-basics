from thermometer import Thermometer

def main():
    my_thermometer = Thermometer()

    print("Turning the thermometer on...")
    my_thermometer.turn_on()

    print("Measuring temperature...")
    my_thermometer.measure_temperature()

    print("Displaying temperature...")
    my_thermometer.display_temperature()

    print("Turning the thermometer off...")
    my_thermometer.turn_off()

if __name__ == "__main__":
    main()
