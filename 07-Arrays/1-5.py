arr = [1, 2, 3, 4, 5]

arr[0] -= 1
print('Array: ', arr)

arr[len(arr)-1] += 4
print('Array: ', arr)

middle = (len(arr)//2)
arr[middle] *= 2
print('Array: ', arr)