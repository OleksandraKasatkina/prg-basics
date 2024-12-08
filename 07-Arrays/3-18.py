# Importing the module
import MyArrays

# Sequence of numbers
numbers = [7, 3, 8, 5, 2]

# Calculating results using functions from the module
second_largest = MyArrays.second_largest(numbers)
median = MyArrays.median(numbers)
min_max = MyArrays.min_max(numbers)

# Manually creating a string with "-" separator for the numbers
numbers_as_string = ""
for i in range(len(numbers)):
    if i != 0:  # Adding separator for all elements except the first one
        numbers_as_string += "-"
    numbers_as_string += str(numbers[i])

# Printing results
print(f"Numbers:", *numbers)
print(f"Second largest number: {second_largest}")
print(f"Median: {median}")
print(f"Smallest and largest number: {min_max[0]}, {min_max[1]}")
print(f"Numbers: {numbers_as_string}")