# Define the arrays
array1 = [1, 3, 5]
array2 = [1, 2, 3, 4, 5, 6]

# Check if array1 is a subset of array2
is_subset = True
for element in array1:
    if element not in array2:
        is_subset = False
        break

# Print the result
if is_subset:
    print("The first array is a subset of the second array.")
else:
    print("The first array is not a subset of the second array.")