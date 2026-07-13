#Rail Fence Cipher
def rail_encrypt(text, key):
    rail = [''] * key
    row, step = 0, 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return ''.join(rail)


def rail_decrypt(cipher, key):
    n = len(cipher)
    mark = [[0] * n for _ in range(key)]

    row, step = 0, 1
    for i in range(n):
        mark[row][i] = 1
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    k = 0
    for i in range(key):
        for j in range(n):
            if mark[i][j]:
                mark[i][j] = cipher[k]
                k += 1

    row, step = 0, 1
    text = ""
    for i in range(n):
        text += mark[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return text


#Columnar Transposition
def col_encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text += "X" * (rows * cols - len(text))

    matrix = [list(text[i:i + cols]) for i in range(0, len(text), cols)]
    order = sorted(range(cols), key=lambda i: key[i])

    cipher = ""
    for c in order:
        for r in matrix:
            cipher += r[c]
    return cipher


def col_decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols

    order = sorted(range(cols), key=lambda i: key[i])

    matrix = [[''] * cols for _ in range(rows)]

    k = 0
    for c in order:
        for r in range(rows):
            matrix[r][c] = cipher[k]
            k += 1

    text = ""
    for r in matrix:
        text += "".join(r)

    return text.rstrip("X")


#Main Menu
while True:

    print("\n===== TRANSPOSITION CIPHERS =====")
    print("1. Rail Fence Cipher")
    print("2. Columnar Transposition")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "3":
        print("Thank You!")
        break

    print("\n1. Encrypt")
    print("2. Decrypt")
    op = input("Enter option: ")

    msg = input("Enter Message: ")

    if choice == "1":
        key = int(input("Enter Rail Key: "))

        if op == "1":
            print("Encrypted:", rail_encrypt(msg, key))
        elif op == "2":
            print("Decrypted:", rail_decrypt(msg, key))
        else:
            print("Invalid Option!")

    elif choice == "2":
        key = input("Enter Key (Example: ZEBRA): ").upper()

        if op == "1":
            print("Encrypted:", col_encrypt(msg, key))
        elif op == "2":
            print("Decrypted:", col_decrypt(msg, key))
        else:
            print("Invalid Option!")

    else:
        print("Invalid Choice!")
