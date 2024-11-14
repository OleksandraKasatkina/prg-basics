def f(name):
    words = name.split()
    acronym = ''
    
    for word in words:
        acronym += word[0]
    
    return acronym

print(f('Internet of Things'))
print(f('For Your Information'))
print(f('Python'))