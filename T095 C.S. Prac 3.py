import hmac, hashlib, secrets

def generate_mac(key: bytes, message: bytes, algo: str = "sha256") -> str:
    """Create a HMAC tag for a message using a secret key."""
    return hmac.new(key, message, algo).hexdigest()

def verify_mac(key: bytes, message: bytes, mac: str, algo: str = "sha256") -> bool:
    """Check a MAC in constant time to avoid timing attacks."""
    return hmac.compare_digest(generate_mac(key, message, algo), mac)

def get_key() -> bytes:
    choice = input("Type your own key or generate one? [t/g]: ").strip().lower()
    if choice == "g":
        key = secrets.token_bytes(32)
        print(f"Generated key (hex): {key.hex()}")
        print(">>> Save this — you'll need it to verify later. <<<")
        return key
    return input("Enter secret key: ").encode()

def get_algo() -> str:
    algo = input("Hash algorithm [sha256/sha384/sha512, default sha256]: ").strip().lower()
    return algo if algo in ("sha256", "sha384", "sha512") else "sha256"

def main():
    print("=== HMAC Generator / Verifier ===")
    while True:
        action = input("\nGenerate, verify, or quit? [g/v/q]: ").strip().lower()

        if action == "q":
            print("Goodbye.")
            break

        elif action == "g":
            key = get_key()
            algo = get_algo()
            message = input("Enter message: ").encode()
            mac = generate_mac(key, message, algo)
            print(f"\nMAC ({algo}): {mac}")

        elif action == "v":
            key = get_key()
            algo = get_algo()
            message = input("Enter message: ").encode()
            mac = input("Enter MAC to verify: ").strip()
            if verify_mac(key, message, mac, algo):
                print("\nValid: message is intact and authentic.")
            else:
                print("\nInvalid: message or key does not match this MAC.")

        else:
            print("Please enter 'g', 'v', or 'q'.")

if __name__ == "__main__":
    main()
