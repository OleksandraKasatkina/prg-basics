def f(palindrome):
    cleaned_palindrome = ''
    for char in palindrome:
        cleaned_palindrome += char.lower()
    return cleaned_palindrome == cleaned_palindrome[::-1]

print(f('radar'))
print(f('12-11-21'))
print(f('book'))