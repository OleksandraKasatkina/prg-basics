translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

# Get the word to translate from the user
word = input("Enter an English word to translate to Polish: ")

# Check if the word is in the dictionary
if word in translations:
    print(f"The translation of '{word}' is: {translations[word]}")
else:
    print(f"Translation for '{word}' is unavailable.")