names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]

for name in names:
    if len(name)>len(longest_name):
        longest_name = name

print("Names:", *names)
print("Longest name:", longest_name)