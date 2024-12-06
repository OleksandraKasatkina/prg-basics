array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

def difference(array1, array2):
    result = []
    for num in array1:
        if num not in array2:
            result.append(num)
    return result

unique_numbers = difference(array1, array2)

print("Array1:", *array1)
print("Array2:", *array2)
print("Numbers in Array1 not in Array2:", *unique_numbers)