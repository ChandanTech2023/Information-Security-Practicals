import numpy as np
import string


def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []

    for c in key:
        if c not in matrix and c.isalpha():
            matrix.append(c)

    for c in string.ascii_uppercase:
        if c not in matrix and c != "J":
            matrix.append(c)

    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix


# Finding position of letter in matrix
def find_pos(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i+1 < len(text):
            b = text[i+1]

            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "X")
            i += 1

    return pairs



def encryption(text, matrix):
    pairs = prepare_text(text)
    result = ""

    for p in pairs:
        r1, c1 = find_pos(matrix, p[0])
        r2, c2 = find_pos(matrix, p[1])

        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

        else: 
            result += matrix[r1][c2] + matrix[r2][c1]

    return result



def decryption(cipher, matrix):
    result = ""

    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]

    for p in pairs:
        r1, c1 = find_pos(matrix, p[0])
        r2, c2 = find_pos(matrix, p[1])

        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result



text = input("Enter Plain-text: ")
key = input("Enter Initial Keyword: ")

matrix = create_matrix(key)

for row in matrix:
    print(row)

cipher = encryption(text, matrix)
print("\nCiphertext:", cipher)

decrypted = decryption(cipher, matrix)
print("Decrypted text:", decrypted)