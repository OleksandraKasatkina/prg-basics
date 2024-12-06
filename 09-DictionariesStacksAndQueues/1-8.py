# prints a list of products and their prices before the discount
# prints the total value of the products before the discount
# modifies the price list according to the discount (round prices to two decimal places)
# prints a list of products and their prices after the 10% discount
# prints the total value of the products after the discount

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key,value in price_list.items():
   print("A list of products and their prices before the discount:")
   print(f"{key}: {value}")

total = 0
for key,value in price_list.items():
   total += value
print(f"The total value of the products before the discount: {total}")

discount_value = 0
for key,value in price_list.items():
   discount_value = value * 0,9
   print("A list of products and their prices after the discount:")
   print(f"{key}: {discount_value}")

discount_total = 0
for key,value in price_list.items():
   discount_total += discount_value
print(f"The total value of the products after the discount: {discount_total}")