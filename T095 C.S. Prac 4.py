
import hashlib

# ---------------- RSA FUNCTIONS ----------------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


# ---------------- KEY GENERATION ----------------

def generate_keys():
    # Two prime numbers
    p = 61
    q = 53

    # Calculate n
    n = p * q

    # Euler's Totient
    phi = (p - 1) * (q - 1)

    # Public exponent
    e = 17

    # Private exponent
    d = mod_inverse(e, phi)

    return e, d, n


# ---------------- HASH FUNCTION ----------------

def hash_message(message):
    hash_value = hashlib.sha256(message.encode()).hexdigest()

    # Convert hexadecimal hash into integer
    hash_integer = int(hash_value, 16)

    return hash_integer


# ---------------- DIGITAL SIGNATURE ----------------

def sign_message(message, d, n):
    hash_value = hash_message(message)

    # Make hash suitable for this small demonstration RSA key
    hash_value = hash_value % n

    # Signature = hash^d mod n
    signature = pow(hash_value, d, n)

    return signature


# ---------------- SIGNATURE VERIFICATION ----------------

def verify_signature(message, signature, e, n):
    hash_value = hash_message(message)
    hash_value = hash_value % n

    # Recover hash using public key
    decrypted_hash = pow(signature, e, n)

    return decrypted_hash == hash_value


# ---------------- MAIN PROGRAM ----------------

print("========================================")
print("       RSA DIGITAL SIGNATURE")
print("========================================")

# Generate RSA keys
e, d, n = generate_keys()

print("\nPublic Key  :", (e, n))
print("Private Key :", (d, n))

# User enters message
message = input("\nEnter the message: ")

# Generate digital signature
signature = sign_message(message, d, n)

print("\nDigital Signature:")
print(signature)

# Ask user whether to verify
choice = input("\nDo you want to verify the signature? (yes/no): ")

if choice.lower() == "yes":

    verify_message = input("\nEnter the message again for verification: ")

    try:
        entered_signature = int(
            input("Enter the digital signature: ")
        )

        if verify_signature(
            verify_message,
            entered_signature,
            e,
            n
        ):
            print("\n✓ DIGITAL SIGNATURE VALID")
            print("The message is authentic and unchanged.")

        else:
            print("\n✗ DIGITAL SIGNATURE INVALID")
            print("The message may have been modified.")

    except ValueError:
        print("\nInvalid signature. Please enter a number.")

else:
    print("\nVerification skipped.")

print("\n========================================")
print("             PROGRAM END")
print("========================================")
