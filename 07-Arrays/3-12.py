array = [2,3,2,5,8,1,9,8]

def find_unique_elements(array):
    unique = []  # List to store unique elements
    for i in array:
        if array.count(i) == 1:  # Check if the element appears only once
            unique.append(i)
    return unique

unique_elements = find_unique_elements(array)

print("Array:", *array)
print("Unique elements:", *unique_elements)