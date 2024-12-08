# Initial array
arr = [7, 9, 2, 4, 5, 6]

# Separate even and odd numbers
even = []  # To store even numbers
odd = []   # To store odd numbers
for num in arr:
    if num % 2 == 0:  # Check if the number is even
        even.append(num)
    else:             # Otherwise, it's odd
        odd.append(num)

# Combine even and odd numbers
arr = even + odd

# Print the result
print("Separated array:", arr)