# Array of real numbers
numbers = [1.5, 3.2, 4.8, 2.7, 5.0, 6.3, 3.9]

# Input value from the keyboard
value = float(input("Enter a value: "))

count = 0
for number in numbers:
    if number > value:
        count += 1

# Print the results
print("Array:", numbers)
print(f"Number of elements greater than {value}: {count}")