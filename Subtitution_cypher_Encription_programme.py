import random
import string
chars=string.punctuation+string.digits + string.ascii_letters
chars = list(chars)
key=chars.copy()
random.shuffle(key)

print(f"chars:{chars}")
print(f"key: {key}")
#ENCRYPT
plain_text=input("Enter a message to encypt:")
cipher_text=""

for letter in plain_text:
    index= key.index(letter)
    cipher_text+=chars[index]


print(f"encrypted message:{cipher_text}")
print(f"original message;{plain_text}")