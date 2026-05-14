def encrypt_rail_fence(text, rails):
    # Create a matrix to mark the positions of characters in the zigzag pattern
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Fill the fence matrix with characters in zigzag order
    for i in range(len(text)):
        fence[rail][i] = text[i]
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    # Read the characters row by row to get the ciphertext
    result = []
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                result.append(fence[i][j])
    return "".join(result)

def decrypt_rail_fence(cipher, rails):
    # Create a matrix to mark the positions of characters in the zigzag pattern
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    
    # First, mark the positions with a placeholder '*'
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    # Fill the placeholders with the actual ciphertext characters row by row
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1
                
    # Read the matrix in zigzag order to recover the plaintext
    result = []
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
            
    return "".join(result)

def main():
    print("--- Rail Fence Cipher (Transposition) ---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Select option (1/2): ")
    
    text = input("Enter message: ")
    try:
        rails = int(input("Enter number of rails: "))
    except ValueError:
        print("Invalid number of rails.")
        return

    if choice == '1':
        result = encrypt_rail_fence(text, rails)
        print(f"Ciphertext: {result}")
    elif choice == '2':
        result = decrypt_rail_fence(text, rails)
        print(f"Plaintext: {result}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
