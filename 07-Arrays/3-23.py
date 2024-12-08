# Import the MyText module
import MyText

# Input text
text = "An apple a day keeps the doctor away"

# Call functions from MyText module
word_count = MyText.word_count(text)
words_longest = MyText.words_by_length(text)
words_alphabetical = MyText.words_alphabetically(text)

# Print results
print(f"Text: {text}")
print(f"Number of words: {word_count}")
print("Words from the longest: ", end="")
for word in words_longest:
    print(word, end=", ")
print("\nWords ordered alphabetically: ", end="")
for word in words_alphabetical:
    print(word, end=", ")
print()  # Adds a newline at the end