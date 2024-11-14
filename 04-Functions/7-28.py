def factorial(n):
    # Base case: 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

result = factorial(5)
print("The factorial of 5 is:", result)