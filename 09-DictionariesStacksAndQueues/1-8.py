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
print(f"The total value of the products before the discount: ${total:.2f}")

discounted_price_list = {}
for key, value in price_list.items():
    discounted_price = round(value * 0.9, 2)  # Apply 10% discount
    discounted_price_list[key] = discounted_price

# Step 4: Print the list of products and their prices after the discount
print("\nA list of products and their prices after the discount:")
for product, discounted_price in discounted_price_list.items():
    print(f"{product}: ${discounted_price:.2f}")

   
discount_total = 0
for key,value in price_list.items():
   discount_total += discounted_price
print(f"The total value of the products after the discount: ${discount_total}")