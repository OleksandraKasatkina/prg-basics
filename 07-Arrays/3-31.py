# Define the 2D array
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Initialize variables to track the smallest and largest values and their positions
min_value = array[0][0]  # Start with the first element of the array as the initial minimum
max_value = array[0][0]  # Start with the first element of the array as the initial maximum
min_position = (0, 0)  # Position of the initial minimum
max_position = (0, 0)  # Position of the initial maximum

# Loop through the 2D array using simple indexing
for row_index in range(len(array)):
    for col_index in range(len(array[row_index])):
        value = array[row_index][col_index]
        
        # Check if the current value is smaller than the current minimum
        if value < min_value:
            min_value = value
            min_position = (row_index, col_index)
        
        # Check if the current value is larger than the current maximum
        if value > max_value:
            max_value = value
            max_position = (row_index, col_index)

# Print the results
print(f"Smallest value: {min_value} at row {min_position[0]}, column {min_position[1]}")
print(f"Largest value: {max_value} at row {max_position[0]}, column {max_position[1]}")
