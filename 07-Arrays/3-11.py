# Define the Bubble Sort function
def bubblesort(array):
    n = len(array)
    for i in range(n):  # Loop through each element
        for j in range(0, n-i-1):  # Compare adjacent elements
            if array[j] > array[j+1]:  # If the element is greater than the next, swap them
                array[j], array[j+1] = array[j+1], array[j]
    return array

array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 1, 4, 2, 8]
array3 = [3, 6, 9, 1, 0, -3, -1]

print("Array 1 (Original):", *array1)
print("Array 1 (Sorted):", *bubblesort(array1))

print("Array 2 (Original):", *array2)
print("Array 2 (Sorted):", *bubblesort(array2))

print("Array 3 (Original):", *array3)
print("Array 3 (Sorted):", *bubblesort(array3))