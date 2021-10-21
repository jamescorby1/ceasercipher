
alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift=3):
    cipher = ""

    for letter in message:
        index = (letter_to_index[letter] + shift) % len(alphabet)
        shifted_letter = index_to_letter[index]

        cipher += shifted_letter
    return cipher

def decrypt(ciphered_message, shift=3):
    decrypted = ""
    for letter in ciphered_message:
        index = (letter_to_index[letter] - shift) % len(alphabet)
        shifted_letter = index_to_letter[index]

        decrypted += shifted_letter
    return decrypted 

def main():
    message = input("Enter message: ")
    encrypted_message = encrypt(message, shift=3)
    decrypt_message = decrypt(encrypted_message, shift=3)

    print("Original message " + message)
    print("Encrypted message " + encrypted_message)
    print("Decrypted message " + decrypt_message)

main()