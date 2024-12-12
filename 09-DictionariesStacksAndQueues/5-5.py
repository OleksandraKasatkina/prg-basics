### a program that counts how many times each word appears in a paragraph
# 

paragraph = "cat dog mouse cat rat cat mouse"

words = paragraph.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1  # Increment count if the word is already in the dictionary
    else:
        word_counts[word] = 1 # Add the word to the dictionary with a count of 1

for word, count in word_counts.items():
    print(f"{word}: {count}")