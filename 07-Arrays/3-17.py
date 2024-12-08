tuple1 = (50,20,40,50,30,50)

value_to_count = 40

# Counting occurrences of the value
count = 0
for item in tuple1:
    if item == value_to_count:
        count += 1

print("Tuple:", end=" ")
for elem in tuple1:
    print(elem, end=",")
print("\b ")

print("Value:", value_to_count)
print("Number of occurrences:", count)