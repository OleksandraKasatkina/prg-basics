###
# A program that prints the first twenty words of the Fibonacci sequence

a = 0
b = 1

for i in range(20):
    print(a, end=" ")
    a, b = b, a + b