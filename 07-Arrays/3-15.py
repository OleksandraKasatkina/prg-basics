tuple1 = (10,20,30,40,50)

# Reversing the tuple
reversed_tuple = tuple1[::-1]

print("Tuple:", end=" ")
for elem in tuple1:
    print(elem, end=",")
print("\b ")  # Remove the trailing comma

print("Reverse order:", end=" ")
for elem in reversed_tuple:
    print(elem, end=",")
print("\b ")  # Remove the trailing comma