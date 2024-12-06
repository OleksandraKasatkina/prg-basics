def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
        return True
    return False

array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

array3 = [True, False]
array4 = [True, False, True]

array5 = [5, 3, 1]
array6 = [5, 3, 1]

array7 = [3, 2, 1]
array8 = [3, 2]

def print_comparison(array1, array2):
    print("Array1:", *array1)
    print("Array2:", *array2)

    if compare(array1, array2):
        print("Comparison: arrays are the same\n")
    else:
        print("Comparison: arrays are different\n")

print_comparison(array1, array2)
print_comparison(array3, array4)
print_comparison(array5, array6)
print_comparison(array7, array8)