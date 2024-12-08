def transpose_matrix(m):
    """Returns the transposed matrix of m."""
    rows = len(m)
    cols = len(m[0])
    # Create an empty matrix with swapped dimensions
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]
    return transposed

def print_2d_array(array):
    """Prints a 2D array in rows and columns."""
    for row in array:
        for element in row:
            print(element, end=" ")
        print()  # Move to the next line after printing a row

# Main program
# Matrices to transpose
matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # 3x3 matrix
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],  # 2x5 matrix
    [[5, 6, 7, 8]]  # 1x4 matrix
]

# Transpose and print each matrix
index = 1  # Manual index tracker
for matrix in matrices:
    print(f"Matrix {index}:")
    print_2d_array(matrix)
    print("Transposed Matrix:")
    transposed = transpose_matrix(matrix)
    print_2d_array(transposed)
    print()  # Blank line between matrices
    index += 1  # Increment the manual index
