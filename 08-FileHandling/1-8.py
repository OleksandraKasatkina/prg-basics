with open('pets.txt', 'r') as file:
    content = file.readlines()

total_words = 0 

for line in content:
    print(line, end='')
    words = line.split()
    total_words += len(words)

print(f'\nTotal number of words: {total_words}')