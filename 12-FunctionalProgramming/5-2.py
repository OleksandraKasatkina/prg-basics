from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

sum_of_evens = reduce(lambda x, y: x + y, even_numbers)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", sum_of_evens)