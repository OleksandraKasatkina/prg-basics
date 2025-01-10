from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce with an anonymous function to sum the numbers
result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 15
