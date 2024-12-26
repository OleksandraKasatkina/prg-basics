from tv import TV  # Import the TV class

def main():
    # Create a TV object
    tv = TV()

    # Use the TV object
    print("Create TV set")
    tv.show_status()  # Show initial status

    print("Turn TV on")
    tv.turn_on()  # Turn on the TV
    tv.show_status()  # Show status

    print("Show available channels before setting")
    tv.show_channels()

    print("Set available channels")
    available_channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    tv.set_channels(available_channels)

    # Show available channels after setting
    tv.show_channels()  

    print("Change TV channel to 5")
    tv.set_channel(5)
    tv.show_status()

    print("Increase volume")
    tv.increase_volume()
    tv.show_status()

    # Decrease volume and display status
    print("Decrease volume")
    tv.decrease_volume()
    tv.show_status()

    print("Change TV channel to 2")
    tv.set_channel(2)
    tv.show_status()

    print("Change TV channel to 6")
    tv.set_channel(6)
    tv.show_status()

    print("Turn TV off")
    tv.turn_off()  # Turn off the TV
    tv.show_status()  # Show status

if __name__ == "__main__":
   main() 