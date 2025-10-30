###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
expanded = ' '
new_text = ' '

for char in plain_text:
    expanded = ord(char)
    expanded = expanded + 1
    new_char = chr(new_char)
    new = new_text + new_char

    # read the character's code (use ord())
    # add one to the character's code
    # replace new character code with its
    # corresponding character (use chr())
    # add encrypted character to encrypted text

print(plain_text)
print(encrypted_text)