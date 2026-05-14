def caesar_cipher_encryption(text , shift):
    ciphertext = ""

    for i in range(len(text)):
        char = text[i]

        if char == " ":
            ciphertext += " "

        elif char.islower():
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            ciphertext += chr((ord(char) + shift - 65) % 26 + 65)

    return ciphertext
    

encrypted_text = caesar_cipher_encryption("I am studying Data Encryption" , 4)

print(f"Original Text: Ansh Juneja\nEncrypted Text: {encrypted_text}") 


def caesar_cipher_decryption(text , shift):
    plaintext = ""

    for i in range(len(text)):
        char = text[i]

        if char == " ":
            plaintext += " "

        elif char.islower():
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            plaintext += chr((ord(char) - shift - 65) % 26 + 65)

    return plaintext


encrypted_text = "Erwl Nyrine"
decrypted_text = caesar_cipher_decryption(encrypted_text , 4)

print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")