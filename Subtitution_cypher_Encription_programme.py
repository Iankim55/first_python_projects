import random
import string

# Define the character set
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create a shuffled key
key = chars.copy()
random.shuffle(key)

# Display both character sets
print(f"chars: {chars}")
print(f"key: {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# Encrypt each letter
for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)  # Find the index in original chars
        cipher_text += key[index]  # Use the same index to get the letter from the key
    else:
        cipher_text += letter  # If the letter isn't in chars, keep it unchanged

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
