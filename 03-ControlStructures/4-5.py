###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    # add one to the character's code
    code = ord(char) + 1
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_character = chr(code)
    # add encrypted character to encrypted text
    encrypted_text += encrypted_character

print(plain_text)
print(encrypted_text)