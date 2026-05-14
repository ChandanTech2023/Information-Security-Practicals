import numpy as np

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def get_key_matrix(key_str, size):
    key_str = key_str.upper().replace(" ", "")
    key_matrix = []
    for char in key_str:
        key_matrix.append(ord(char) - ord('A'))
    return np.array(key_matrix[:size*size]).reshape(size, size)

def encrypt(msg, key_matrix):
    size = key_matrix.shape[0]
    msg = msg.upper().replace(" ", "")
    
    # Padding
    while len(msg) % size != 0:
        msg += 'X'
    
    msg_coords = [ord(c) - ord('A') for c in msg]
    msg_matrix = np.array(msg_coords).reshape(-1, size)
    
    # C = (P * K) mod 26 
    # Note: Using Row vectors (msg * key) is common in some textbooks, 
    # while Column vectors (key * msg) is common in others. 
    # I'll stick to (P * K) to match your initial logic.
    cipher_matrix = np.matmul(msg_matrix, key_matrix) % 26
    
    return "".join(chr(int(c) + ord('A')) for c in cipher_matrix.flatten())

def decrypt(cipher_text, key_matrix):
    size = key_matrix.shape[0]
    
    # 1. Find determinant
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    
    # 2. Find modular inverse of determinant
    det_inv = modInverse(det, 26)
    if det_inv is None:
        return "Error: Matrix is not invertible mod 26 (GCD(det, 26) != 1)"
    
    # 3. Find adjugate matrix (for 2x2)
    if size == 2:
        adj = np.array([[key_matrix[1,1], -key_matrix[0,1]], 
                        [-key_matrix[1,0], key_matrix[0,0]]])
    else:
        # General adjugate using cofactor matrix (for size > 2)
        # Simplified for practicals, usually 2x2 is used.
        return "Decryption for size > 2 not implemented in this simple script."

    # 4. Inverse matrix = det_inv * adj mod 26
    inv_matrix = (det_inv * adj) % 26
    
    cipher_coords = [ord(c) - ord('A') for c in cipher_text]
    cipher_matrix = np.array(cipher_coords).reshape(-1, size)
    
    # P = (C * K_inv) mod 26
    plain_matrix = np.matmul(cipher_matrix, inv_matrix) % 26
    
    return "".join(chr(int(round(p)) + ord('A')) for p in plain_matrix.flatten())

def main():
    print("--- Hill Cipher (2x2 Matrix) ---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Select option (1/2): ")

    key_input = input("Enter 4-letter key (e.g., 'HILL' or 'GYBN'): ")
    if len(key_input) < 4:
        print("Error: Key must be at least 4 letters for 2x2 matrix.")
        return
    
    key_matrix = get_key_matrix(key_input, 2)
    print(f"Key Matrix:\n{key_matrix}")

    if choice == '1':
        msg = input("Enter message to encrypt: ")
        result = encrypt(msg, key_matrix)
        print(f"Encrypted Text: {result}")
    elif choice == '2':
        msg = input("Enter message to decrypt: ")
        result = decrypt(msg, key_matrix)
        print(f"Decrypted Text: {result}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()