from string import ascii_lowercase, punctuation
from random import randint

def run_atbash_cipher(text):
    cipher_text = ""
    for character in text:
        if character in punctuation or character.isspace():
            cipher_text += character
        else:
            original_index = ascii_lowercase.index(character) + 1
            cipher_character = ascii_lowercase[-original_index]
            cipher_text += cipher_character

    return cipher_text

welcome_message = """
    Welcome to [**Enter names here**] 'Atbash Cipher' app!

    In this app, you'll enter text and then 
    choose to encrypt or decrypt it using the
    Atbash Cipher. Note that the text will be
    all lowercase for encryption or decryption,
    regardless of how you enter the text.
"""

print(welcome_message)

ENCRYPT = 1
DECRYPT = 2
encrypted_text = ""

text = input("Enter the text you'd like to encrypt or decrypt: ").lower()

# Hint type cast this as a number
option = ??(input("Would you like to (1) encrypt or (2) decrypt the text? "))

?? option ?? ENCRYPT:
    encrypted_text ?? run_atbash_cipher(text)
    print(f"Your encrypted text is: {encrypted_text}")
?? option ?? DECRYPT:
    decrypted_text ?? run_atbash_cipher(text)
    print(f"Your decrypted text is: {decrypted_text}")
# provide error handling code here for invalid input
# hint: use else