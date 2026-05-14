import math

def get_column_order(key):
    # Returns the indices of the columns in the order they should be read
    # Example: 'HACK' -> H:7, A:0, C:2, K:10 -> Sorted: A(0), C(2), H(7), K(10)
    # Order: [1, 2, 0, 3] (indices of A, C, H, K in 'HACK')
    key_list = sorted(list(enumerate(key)), key=lambda x: x[1])
    return [item[0] for item in key_list]

def encrypt_row_transposition(text, key):
    key_len = len(key)
    # Remove spaces and pad with 'X'
    text = text.replace(" ", "").upper()
    while len(text) % key_len != 0:
        text += 'X'
    
    rows = len(text) // key_len
    order = get_column_order(key)
    
    # Create the grid
    grid = [text[i:i + key_len] for i in range(0, len(text), key_len)]
    
    # Read columns in order
    ciphertext = ""
    for col_idx in order:
        for row in range(rows):
            ciphertext += grid[row][col_idx]
            
    return ciphertext

def decrypt_row_transposition(ciphertext, key):
    key_len = len(key)
    rows = len(ciphertext) // key_len
    order = get_column_order(key)
    
    # Create empty grid
    grid = [['' for _ in range(key_len)] for _ in range(rows)]
    
    # Fill columns in order
    idx = 0
    for col_idx in order:
        for row in range(rows):
            grid[row][col_idx] = ciphertext[idx]
            idx += 1
            
    # Read row by row
    plaintext = ""
    for r in range(rows):
        plaintext += "".join(grid[r])
        
    return plaintext

def main():
    print("--- Row Transposition Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Select option (1/2): ")
    
    text = input("Enter message: ")
    key = input("Enter keyword (e.g., HACK): ").upper()
    
    if not key:
        print("Error: Key cannot be empty.")
        return

    if choice == '1':
        result = encrypt_row_transposition(text, key)
        print(f"Ciphertext: {result}")
    elif choice == '2':
        result = decrypt_row_transposition(text, key)
        print(f"Plaintext: {result}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
