def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def rail_fence_encrypt(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    rail, direction = 0, 1
    for i in range(len(text)):
        fence[rail][i] = text[i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return "".join(fence[i][j] for i in range(rails) for j in range(len(text)) if fence[i][j] != '\n')

def rail_fence_decrypt(cipher, rails):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    rail, direction = 0, 1
    for i in range(len(cipher)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1
                
    result, rail, direction = [], 0, 1
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return "".join(result)

def product_encrypt(text, shift, rails):
    # Step 1: Substitution
    substituted = caesar_cipher(text, shift)
    # Step 2: Transposition
    ciphered = rail_fence_encrypt(substituted, rails)
    return ciphered

def product_decrypt(cipher, shift, rails):
    # Step 1: Reverse Transposition
    transposed_back = rail_fence_decrypt(cipher, rails)
    # Step 2: Reverse Substitution
    original = caesar_cipher(transposed_back, shift, encrypt=False)
    return original

def main():
    print("--- Product Cipher (Substitution + Transposition) ---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Select option (1/2): ")
    
    text = input("Enter message: ")
    try:
        shift = int(input("Enter substitution shift (e.g., 3): "))
        rails = int(input("Enter transposition rails (e.g., 2): "))
    except ValueError:
        print("Invalid input for shift or rails.")
        return

    if choice == '1':
        result = product_encrypt(text, shift, rails)
        print(f"Final Ciphertext: {result}")
    elif choice == '2':
        result = product_decrypt(text, shift, rails)
        print(f"Decrypted Message: {result}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
