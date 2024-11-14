def f(n):
    result = ''
    for i in range(n):
        result += '*'
        if i < n - 1:
            result += '/'
    return result

print(f(4))
print(f(1))