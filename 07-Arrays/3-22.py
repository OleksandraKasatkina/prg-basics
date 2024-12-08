import random

# Define the function to return a random element from the array
def rand_elem(array):
    return random.choice(array)

# Example array
numbers = [10, 20, 30, 40, 50, 60]

# Print a few randomly selected elements using the function
print("Array:", numbers)
print("Randomly selected element 1:", rand_elem(numbers))
print("Randomly selected element 2:", rand_elem(numbers))
print("Randomly selected element 3:", rand_elem(numbers))