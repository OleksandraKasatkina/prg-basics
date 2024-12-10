import re

def count_vowels(text):
    # Regular expression pattern for vowels (both uppercase and lowercase)
    pattern = r'[aeiouAEIOU]'
    # Find all vowels in the text
    vowels = re.findall(pattern, text)
    # Return the count of vowels
    return len(vowels)

# Prompt the user to enter text
user_input = input("Enter text: ")

# Calculate the number of vowels
vowel_count = count_vowels(user_input)

# Display the result
print(f"The number of vowels in the text is: {vowel_count}")
