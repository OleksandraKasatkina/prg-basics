def f(binary_number):
    for char in binary_number:
        if char != '1' and char != '0':
            return False
    return True

f1 = f('101101')
print(f'{f1}')
f2 = f('1311a10100')
print(f'{f2}')