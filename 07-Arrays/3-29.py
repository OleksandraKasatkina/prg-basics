# Function to create a 2D array with dimensions x by y, filled with zeros
def create_2d_arr(x, y):
    return [[0 for i in range(y)] for i in range(x)]

# Create a 2D array with dimensions 3 by 5
array = create_2d_arr(3, 5)

# Print the created 2D array
for row in array:
    print(row)