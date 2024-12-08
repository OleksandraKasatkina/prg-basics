def identity_matrix(n):
    """Creates and returns an identity matrix of size n."""
    # Initialize a 2D array of size n with all elements set to 0
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Set diagonal elements to 1
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def print_2d_array(array):
    """Prints a 2D array row by row"""
    for row in array:
        for element in row:
            print(element, end=" ")
        print()  # Moves to the next line after printing a row

# Main program
# Identity matrices with sizes 3, 5, and 8
sizes = [3, 5, 8]
for size in sizes:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    print_2d_array(matrix)
    print()  # Add a blank line between matrices for clarity