import math
import tkinter as tk
from tkinter import ttk, messagebox


# --- Cryptographic Helper Functions ---
def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def extended_gcd(a: int, b: int):
    """Extended Euclidean Algorithm to calculate modular inverse."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e: int, phi: int) -> int:
    """Computes d = e^(-1) mod phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % phi


# --- Tkinter GUI Application ---
class RSAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RSA Encryption / Decryption Simulator")
        self.geometry("700x650")
        self.resizable(False, False)

        # Apply a clean theme
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Key variables
        self.public_key = None  # (e, n)
        self.private_key = None # (d, n)

        self._build_ui()

    def _build_ui(self):
        # Header
        header = ttk.Label(
            self,
            text="RSA Key Generation & Cipher Demonstration",
            font=("Segoe UI", 14, "bold")
        )
        header.pack(pady=10)

        # 1. Key Generation Section
        key_frame = ttk.LabelFrame(self, text=" 1. Key Generation ", padding=10)
        key_frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(key_frame, text="Prime p:").grid(row=0, column=0, sticky="w", padx=5)
        self.p_entry = ttk.Entry(key_frame, width=10)
        self.p_entry.insert(0, "61")
        self.p_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(key_frame, text="Prime q:").grid(row=0, column=2, sticky="w", padx=5)
        self.q_entry = ttk.Entry(key_frame, width=10)
        self.q_entry.insert(0, "53")
        self.q_entry.grid(row=0, column=3, padx=5, pady=5)

        gen_btn = ttk.Button(key_frame, text="Generate Keys", command=self.generate_keys)
        gen_btn.grid(row=0, column=4, padx=15, pady=5)

        # Display calculated key parameter values
        self.key_info_label = ttk.Label(
            key_frame,
            text="Key status: No keys generated yet.",
            font=("Consolas", 9),
            foreground="#555555",
            justify="left"
        )
        self.key_info_label.grid(row=1, column=0, columnspan=5, sticky="w", padx=5, pady=5)

        # 2. Encryption Section
        enc_frame = ttk.LabelFrame(self, text=" 2. Encryption (c = m^e mod n) ", padding=10)
        enc_frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(enc_frame, text="Plaintext Message:").pack(anchor="w")
        self.plain_entry = ttk.Entry(enc_frame, width=75)
        self.plain_entry.insert(0, "Hello RSA!")
        self.plain_entry.pack(pady=5)

        enc_btn = ttk.Button(enc_frame, text="Encrypt Message", command=self.encrypt_message)
        enc_btn.pack(anchor="e", pady=2)

        ttk.Label(enc_frame, text="Ciphertext (Integer List):").pack(anchor="w")
        self.cipher_entry = ttk.Entry(enc_frame, width=75)
        self.cipher_entry.pack(pady=5)

        # 3. Decryption Section
        dec_frame = ttk.LabelFrame(self, text=" 3. Decryption (m = c^d mod n) ", padding=10)
        dec_frame.pack(fill="x", padx=15, pady=5)

        dec_btn = ttk.Button(dec_frame, text="Decrypt Ciphertext", command=self.decrypt_message)
        dec_btn.pack(anchor="e", pady=2)

        ttk.Label(dec_frame, text="Decrypted Result:").pack(anchor="w")
        self.decrypted_entry = ttk.Entry(dec_frame, width=75)
        self.decrypted_entry.pack(pady=5)

        # Auto-generate default keys on load
        self.generate_keys()

    def generate_keys(self):
        try:
            p = int(self.p_entry.get().strip())
            q = int(self.q_entry.get().strip())

            if not is_prime(p) or not is_prime(q):
                messagebox.showerror("Error", "Both p and q must be prime numbers!")
                return
            if p == q:
                messagebox.showerror("Error", "Primes p and q must be distinct!")
                return

            n = p * q
            phi = (p - 1) * (q - 1)

            # Pick public exponent e
            e = 65537
            if math.gcd(e, phi) != 1:
                e = 3
                while math.gcd(e, phi) != 1:
                    e += 2

            d = mod_inverse(e, phi)

            self.public_key = (e, n)
            self.private_key = (d, n)

            # Update label display
            info = f"n = {n}  |  ϕ(n) = {phi}\nPublic Key (e, n): ({e}, {n})\nPrivate Key (d, n): ({d}, {n})"
            self.key_info_label.config(text=info, foreground="#006600")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer primes for p and q.")

    def encrypt_message(self):
        if not self.public_key:
            messagebox.showwarning("Warning", "Generate keys first!")
            return

        plaintext = self.plain_entry.get()
        if not plaintext:
            messagebox.showwarning("Warning", "Enter a plaintext message to encrypt.")
            return

        e, n = self.public_key
        # Ensure characters fit within modulus n
        for char in plaintext:
            if ord(char) >= n:
                messagebox.showerror(
                    "Error", 
                    f"Modulus n={n} is too small for ASCII code {ord(char)} of character '{char}'. Use larger primes!"
                )
                return

        # Perform RSA Modular Exponentiation: c = m^e mod n
        cipher_blocks = [pow(ord(char), e, n) for char in plaintext]
        
        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, str(cipher_blocks))

    def decrypt_message(self):
        if not self.private_key:
            messagebox.showwarning("Warning", "Generate keys first!")
            return

        cipher_str = self.cipher_entry.get().strip()
        if not cipher_str:
            messagebox.showwarning("Warning", "No ciphertext to decrypt.")
            return

        try:
            # Parse string representation of list back to integer list
            cipher_blocks = eval(cipher_str)
            if not isinstance(cipher_blocks, list):
                raise ValueError

            d, n = self.private_key
            # Perform RSA Decryption: m = c^d mod n
            decrypted_chars = [chr(pow(c, d, n)) for c in cipher_blocks]
            decrypted_text = "".join(decrypted_chars)

            self.decrypted_entry.delete(0, tk.END)
            self.decrypted_entry.insert(0, decrypted_text)

        except Exception:
            messagebox.showerror("Error", "Invalid ciphertext format! Must be a list of integers like [123, 456].")


if __name__ == "__main__":
    app = RSAApp()
    app.mainloop()
