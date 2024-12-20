class Phone():
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
        self.is_on = True

    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False

    def display_info(self):
        print(f"Smartphone name: {self.name}")
        print(f"Smartphone color: {self.color}")
        print(f"Is the smartphone on?")
        if self.is_on:
            print("Yes, it is.")
        else:
            print("No, it is not.")

def main():
    my_phone = Phone("Iphone 13","Whine",True)
    my_phone.display_info()

if __name__ =="__main__":
    main()