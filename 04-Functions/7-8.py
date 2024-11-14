def f(number, even):
    total_sum = 0
    for digit in str(number):  
        digit = int(digit)
        if even and digit % 2 == 0:
            total_sum += digit
        elif not even and digit % 2 != 0:
            total_sum += digit
    return total_sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))