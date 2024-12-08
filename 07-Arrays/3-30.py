# Initialize a 5x5 array with zeros
array = [[0, 0, 0, 0, 0] for _ in range(5)]

# Modify the array to create the multiplication table
for i in range(5):
    for j in range(5):
        array[i][j] = (i + 1) * (j + 1)

# Print the array as a multiplication table
for row in array:
    for num in row:
        print(num, end=" ")
    print()  # To move to the next line after each row