class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            # Check if the current channel is within the available channels
            if 0 < self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]  # Get the channel name (1-indexed)
                print(f"TV is on, channel {self.channel_no} ({channel_name}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        # Set the new channel number
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        # Set the list of available channels
        self.channels = channels_list

    def show_channels(self):
        # Print the list of available channels
        if self.channels:
            print("Channel list:")
            index = 1
            for channel in self.channels:
                print(f"{index}. {channel}")
                index += 1
        else:
            print("No channels available")

    def increase_volume(self):
        # Increase the volume by 1, ensuring it's between 0 and 10
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume is at maximum level.")

    def decrease_volume(self):
        # Decrease the volume by 1, ensuring it's between 0 and 10
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is at minimum level.")