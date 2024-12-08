# Define the 3x5 array
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Print the array before the column swap
print("Before swapping:")
for row in array:
    print(row)

# Swap the first and last column
for row in array:
    row[0], row[4] = row[4], row[0]

# Print the array after the column swap
print("\nAfter swapping:")
for row in array:
    print(row)