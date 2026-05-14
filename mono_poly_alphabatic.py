import string
import random

class MonoalphabeticCipher:
    
    def __init__(self, key=None):
        self.alphabet = string.ascii_lowercase
        if key:
            self.key = self._generate_key_from_string(key.lower())
        else:
            self.key = self._generate_random_key()
        
        self.encrypt_map = str.maketrans(self.alphabet + self.alphabet.upper(), 
                                        self.key + self.key.upper())
        self.decrypt_map = str.maketrans(self.key + self.key.upper(), 
                                        self.alphabet + self.alphabet.upper())

    def _generate_key_from_string(self, seed_str):
        # Create a unique key by taking the seed string and appending remaining letters
        key = ""
        for char in seed_str:
            if char in self.alphabet and char not in key:
                key += char
        for char in self.alphabet:
            if char not in key:
                key += char
        return key

    def _generate_random_key(self):
        key_list = list(self.alphabet)
        random.shuffle(key_list)
        return "".join(key_list)

    def encrypt(self, text):
        return text.translate(self.encrypt_map)

    def decrypt(self, text):
        return text.translate(self.decrypt_map)


class PolyalphabeticCipher:
    """
    Implements the Vigenère Cipher (a common Polyalphabetic Substitution Cipher).
    """
    def __init__(self, key):
        self.key = key.lower()
        self.alphabet = string.ascii_lowercase

    def _get_key_sequence(self, text):
        # Repeat the key to match the text length (ignoring non-alpha chars)
        key_seq = []
        key_index = 0
        for char in text:
            if char.lower() in self.alphabet:
                key_seq.append(self.key[key_index % len(self.key)])
                key_index += 1
            else:
                key_seq.append(None)
        return key_seq

    def encrypt(self, text):
        key_seq = self._get_key_sequence(text)
        result = []
        for i, char in enumerate(text):
            if char.lower() in self.alphabet:
                shift = self.alphabet.index(key_seq[i])
                base = ord('a') if char.islower() else ord('A')
                # (P + K) mod 26
                new_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(new_char)
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text):
        key_seq = self._get_key_sequence(text)
        result = []
        for i, char in enumerate(text):
            if char.lower() in self.alphabet:
                shift = self.alphabet.index(key_seq[i])
                base = ord('a') if char.islower() else ord('A')
                # (C - K + 26) mod 26
                new_char = chr((ord(char) - base - shift + 26) % 26 + base)
                result.append(new_char)
            else:
                result.append(char)
        return "".join(result)


def main():
  
    print("1. Monoalphabetic Cipher")
    print("2. Polyalphabetic Cipher (Vigenère)")
    choice = input("Select Cipher (1/2): ").strip()

    if choice == '1':
        print("\n[Monoalphabetic Cipher]")
        mode = input("Generate key from word (w) or random (r)? ").lower()
        if mode == 'w':
            key_word = input("Enter keyword: ")
            cipher = MonoalphabeticCipher(key_word)
        else:
            cipher = MonoalphabeticCipher()
            print(f"Generated Key Alphabet: {cipher.key}")
        
        text = input("Enter text to encrypt: ")
        encrypted = cipher.encrypt(text)
        decrypted = cipher.decrypt(encrypted)
        
        print(f"\nEncrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

    elif choice == '2':
        print("\n[Polyalphabetic Cipher (Vigenère)]")
        key = input("Enter encryption key: ")
        if not key.isalpha():
            print("Error: Key must contain only letters.")
            return
            
        cipher = PolyalphabeticCipher(key)
        text = input("Enter text to encrypt: ")
        
        encrypted = cipher.encrypt(text)
        decrypted = cipher.decrypt(encrypted)
        
        print(f"\nEncrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()