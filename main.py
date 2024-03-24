import random
import string


# creating list of chars (to encrypt) and keys (to decrypt)
chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars[:]      # key = chars.copy()
random.shuffle(key)


# ENCRYPT
plain_text = input("Enter message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Encrypted message {cipher_text}")

# resetting plain_text
plain_text = ""


# DECRYPT
ask_to_decrypt = input("Do you want to decrypt the message (y/n)? : ")

if ask_to_decrypt.lower() == "y":
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Decrypted message: {plain_text}")

else:
    print("Exiting ....")

