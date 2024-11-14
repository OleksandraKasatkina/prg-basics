from text73 import count_letter

text = "You never get a second chance to make a first impression"
letter_to_count = 'e'
letter_count = count_letter(text, letter_to_count)

print(f"The number of letter '{letter_to_count}': {letter_count}")