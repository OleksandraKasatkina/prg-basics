def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

result = sum(10)
print("The sum of natural numbers from 1 to 10 is:", result)