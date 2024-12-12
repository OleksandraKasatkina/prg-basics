hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

# Function definitions
def hotel_list(hotels):
    """Returns a list of hotel names as a string, separated by commas."""
    hotel_names = ""
    for hotel in hotels:
        hotel_names += hotel["name"] + ", "
    return hotel_names[:-2]  # Remove the trailing comma and space

def avg_price(hotels):
    """Returns the average room price, rounded to an integer."""
    total_price = 0
    for hotel in hotels:
        total_price += hotel["price"]
    return round(total_price / len(hotels))

# Krakow hotels
krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg_price = avg_price(hotels_in_Krakow)
print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg_price}")

# Sopot hotels
sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg_price = avg_price(hotels_in_Sopot)
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg_price}")

# Compare prices
if krakow_avg_price < sopot_avg_price:
    print("Cheaper hotels in: Krakow")
elif sopot_avg_price < krakow_avg_price:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotel prices are equal in Krakow and Sopot.")