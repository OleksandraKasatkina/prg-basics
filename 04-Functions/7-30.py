def power(x, n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: multiply x by power(x, n - 1)
    return x * power(x, n - 1)

result = power(5, 3)
print('The result of 5^3 is:', result)