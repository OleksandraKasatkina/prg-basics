# Define the 2D array
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Initialize a variable to store the sum
sum_last_column = 0

# Loop through each row in the array
for row in array:
    sum_last_column += row[-1] # Add the value from the last column (last element of the row) to the sum

# Print the result
print("Sum of values in the last column:", sum_last_column)