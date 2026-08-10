print("=" * 50)
print("       DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 50)

p = int(input("Enter a prime number (p): "))
g = int(input("Enter a generator (g): "))

print("\n--- AASHKA ---")
a = int(input("Enter Aashka's private key (a): "))

print("\n--- DEESHA ---")
b = int(input("Enter Deesha's private key (b): "))

A = pow(g, a, p)

B = pow(g, b, p)

Aashka_shared_key = pow(B, a, p)
Deesha_shared_key = pow(A, b, p)

print("\n" + "=" * 50)
print("             KEY EXCHANGE RESULTS")
print("=" * 50)

print("\nPublic Parameters:")
print("Prime number (p) :", p)
print("Generator (g)    :", g)

print("\nAashka:")
print("Private Key      :", a)
print("Public Key       :", A)

print("\nDeesha:")
print("Private Key      :", b)
print("Public Key       :", B)

print("\nShared Secret:")
print("Aashka's Key     :", Aashka_shared_key)
print("Deesha's Key     :", Deesha_shared_key)

if Aashka_shared_key == Deesha_shared_key:
    print("\n✓ KEY EXCHANGE SUCCESSFUL")
    print("Both users have generated the same shared secret key.")
else:
    print("\n✗ KEY EXCHANGE FAILED")
    print("The shared keys do not match.")

print("=" * 50)
