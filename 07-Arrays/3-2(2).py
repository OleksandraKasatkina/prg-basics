arr = [15, 8, 31, 47, 2, 19]

print("existed array:", end=" ")
for num in arr:
    print(num, end=" ")
print()

print("reverse array:", end=" ")
for i in range(len(arr) - 1, -1, -1):  # Start from the last index, step backwards
    print(arr[i], end=" ")