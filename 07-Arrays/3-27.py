# Define the 2D array (2 by 4 array)
array = [
    [1, 2, 3, 4],  # First row
    [5, 6, 7, 8]   # Second row
]

# Loop through each row in the 2D array
for row in array:
    for item in row:
        print(item, end=" ") # Print each element in the row, followed by a space
    print() # Move to the next line after printing a row