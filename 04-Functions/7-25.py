def f(text):
    result = ''
    for i in range(len(text)):
        result += text[i]
        if i < len(text) - 1:
            result += '-'
    return result

print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))