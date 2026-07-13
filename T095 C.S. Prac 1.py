plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"


#Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


#Monoalphabetic Cipher
def mono_encrypt(text):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            index = plain.index(ch)
            result += cipher[index]
        else:
            result += ch
    return result


def mono_decrypt(text):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            index = cipher.index(ch)
            result += plain[index]
        else:
            result += ch
    return result


#Main Program
while True:

    print("\n===== CLASSICAL SUBSTITUTION CIPHERS =====")
    print("1. Caesar Cipher")
    print("2. Monoalphabetic Cipher")
    print("3. Exit")

    choice = input("Choose Technique: ")

    if choice == "1":

        print("\n1. Encrypt")
        print("2. Decrypt")

        op = input("Choose Option: ")
        msg = input("Enter Message: ")
        shift = int(input("Enter Shift Value: "))

        if op == "1":
            print("Encrypted Message :", caesar_encrypt(msg, shift))
        elif op == "2":
            print("Decrypted Message :", caesar_decrypt(msg, shift))
        else:
            print("Invalid Option!")

    elif choice == "2":

        print("\n1. Encrypt")
        print("2. Decrypt")

        op = input("Choose Option: ")
        msg = input("Enter Message: ")

        if op == "1":
            print("Encrypted Message :", mono_encrypt(msg))
        elif op == "2":
            print("Decrypted Message :", mono_decrypt(msg))
        else:
            print("Invalid Option!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
