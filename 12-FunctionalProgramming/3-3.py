# List of products in stock (quantity, unit price)
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Calculate total value for each product and sum them up
total_value = sum(map(lambda item: item[0] * item[1], stock))

# Display results
print("Products in stock:", stock)
print(f"Total value: {total_value:.2f}")