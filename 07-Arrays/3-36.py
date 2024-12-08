def flatten_2d_to_1d(array):
    """Converts a 2D array to a 1D array."""
    # Using list comprehension to flatten the 2D array
    return [element for row in array for element in row]

def print_1d_array(array):
    """Prints a 1D array."""
    for element in array:
        print(element, end=" ")
    print()  # Newline after printing all elements

# Main program
# Given 2D arrays
arrays = [
    [[2, 3], [1, 5]],  # 2x2 matrix
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],  # 2x5 matrix
    [[2, 1], [3, 5], [7, 4], [2, 6]]  # 4x2 matrix
]

# Convert each 2D array to a 1D array and print it
for array in arrays:
    # Print the 2D array row by row
    for row in array:
        for num in row:
            print(num, end=" ")  # Print each element on the same line
        print()  # Move to the next line after each row
    
    print("Converted to 1D array:")
    flattened = flatten_2d_to_1d(array)
    print_1d_array(flattened)
    print()  # Blank line between arrays