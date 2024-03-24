# VERY SIMPLE AND BASIC TEXT DECRYPTER AND ENCRYPTER

This program encrypts user input text and provides and option if user to want to decrypt it (very silly as it only works for the current program session)

Working:
1. Two lists are created chars and keys with random character.
2. keys copies entire content of chars and shuffles it each time program runs.
3. user input text's each letter fetches its index from chars and uses that index value to get random character from key to fill up cipher_text var.
4. reverse process is used to decrypt it.
