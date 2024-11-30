arr = [15, 8, 31, 47, 2, 19]

total_sum = 0
for i in arr:
    total_sum += i

mean = total_sum / len(arr)

print('Array:', *arr)
print('Arithmetic mean:', mean)