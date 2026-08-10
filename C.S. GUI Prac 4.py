import tkinter as tk
from tkinter import messagebox
import hashlib

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


def generate_keys():

    p = 61
    q = 53

    n = p * q

    phi = (p - 1) * (q - 1)

    e = 17

    d = mod_inverse(e, phi)

    return e, d, n

def get_hash(message):

    return hashlib.sha256(
        message.encode()
    ).hexdigest()

def sign_message(message, private_key, n):

    hash_value = int(
        get_hash(message),
        16
    )

    hash_value = hash_value % n

    signature = pow(
        hash_value,
        private_key,
        n
    )

    return signature

def verify_signature(message, signature, public_key, n):

    original_hash = int(
        get_hash(message),
        16
    ) % n

    decrypted_signature = pow(
        signature,
        public_key,
        n
    )

    return original_hash == decrypted_signature

public_key, private_key, n = generate_keys()

BACKGROUND = "#F5F7FB"
WHITE = "#FFFFFF"

NAVY = "#172554"
BLUE = "#2563EB"
PURPLE = "#7C3AED"
LIGHT_PURPLE = "#F3E8FF"

GREEN = "#16A34A"
LIGHT_GREEN = "#DCFCE7"

RED = "#DC2626"
LIGHT_RED = "#FEE2E2"

TEXT = "#172033"
SECONDARY = "#64748B"
BORDER = "#E2E8F0"

LIGHT_BLUE = "#EFF6FF"

def generate_signature():

    message = message_text.get(
        "1.0",
        tk.END
    ).strip()

    if not message:

        messagebox.showwarning(
            "Message Required",
            "Please enter a message before generating the signature."
        )

        return

    signature = sign_message(
        message,
        private_key,
        n
    )

    signature_text.delete(
        "1.0",
        tk.END
    )

    signature_text.insert(
        tk.END,
        str(signature)
    )

    hash_text.delete(
        "1.0",
        tk.END
    )

    hash_text.insert(
        tk.END,
        get_hash(message)
    )

    status_label.config(
        text="✓  SIGNATURE GENERATED",
        fg=PURPLE
    )

    status_description.config(
        text="The message has been successfully signed using the RSA private key.",
        fg=SECONDARY
    )

    result_frame.config(
        highlightbackground=PURPLE
    )

def verify():

    message = message_text.get(
        "1.0",
        tk.END
    ).strip()

    signature = signature_text.get(
        "1.0",
        tk.END
    ).strip()

    if not message:

        messagebox.showwarning(
            "Message Required",
            "Please enter a message."
        )

        return

    if not signature:

        messagebox.showwarning(
            "Signature Required",
            "Please generate or enter a digital signature."
        )

        return

    try:

        signature = int(signature)

    except ValueError:

        messagebox.showerror(
            "Invalid Signature",
            "The digital signature must be a valid number."
        )

        return

    valid = verify_signature(
        message,
        signature,
        public_key,
        n
    )

    # Update hash
    hash_text.delete(
        "1.0",
        tk.END
    )

    hash_text.insert(
        tk.END,
        get_hash(message)
    )

    if valid:

        status_label.config(
            text="✓  SIGNATURE VALID",
            fg=GREEN
        )

        status_description.config(
            text="Authenticity verified • Message integrity confirmed",
            fg=GREEN
        )

        result_frame.config(
            highlightbackground=GREEN
        )

        messagebox.showinfo(
            "Verification Successful",
            "DIGITAL SIGNATURE VALID\n\n"
            "✓ The message is authentic.\n"
            "✓ The message has not been modified."
        )

    else:

        status_label.config(
            text="✕  SIGNATURE INVALID",
            fg=RED
        )

        status_description.config(
            text="The message or digital signature may have been modified.",
            fg=RED
        )

        result_frame.config(
            highlightbackground=RED
        )

        messagebox.showerror(
            "Verification Failed",
            "DIGITAL SIGNATURE INVALID\n\n"
            "⚠ The message may have been modified.\n"
            "⚠ Authenticity could not be confirmed."
        )

def copy_signature():

    signature = signature_text.get(
        "1.0",
        tk.END
    ).strip()

    if not signature:

        messagebox.showwarning(
            "Nothing to Copy",
            "Generate a digital signature first."
        )

        return

    root.clipboard_clear()

    root.clipboard_append(
        signature
    )

    messagebox.showinfo(
        "Copied",
        "Digital signature copied successfully."
    )

def clear_all():

    message_text.delete(
        "1.0",
        tk.END
    )

    signature_text.delete(
        "1.0",
        tk.END
    )

    hash_text.delete(
        "1.0",
        tk.END
    )

    status_label.config(
        text="●  READY",
        fg=SECONDARY
    )

    status_description.config(
        text="Enter a message to begin the digital signing process.",
        fg=SECONDARY
    )

    result_frame.config(
        highlightbackground=BORDER
    )

root = tk.Tk()

root.title(
    "RSA Digital Signature | SecureTech"
)

root.geometry(
    "1120x780"
)

root.resizable(
    False,
    False
)

root.configure(
    bg=BACKGROUND
)

header = tk.Frame(
    root,
    bg=NAVY,
    height=105
)

header.pack(
    fill="x"
)

header.pack_propagate(False)

icon = tk.Label(
    header,
    text="🔐",
    font=("Segoe UI Emoji", 30),
    bg=NAVY,
    fg="white"
)

icon.pack(
    side="left",
    padx=(40, 15)
)

title_area = tk.Frame(
    header,
    bg=NAVY
)

title_area.pack(
    side="left"
)


title = tk.Label(
    title_area,
    text="RSA DIGITAL SIGNATURE",
    font=("Segoe UI", 22, "bold"),
    bg=NAVY,
    fg="white"
)

title.pack(
    anchor="w",
    pady=(20, 0)
)


subtitle = tk.Label(
    title_area,
    text="Secure message authentication & integrity verification",
    font=("Segoe UI", 10),
    bg=NAVY,
    fg="#CBD5E1"
)

subtitle.pack(
    anchor="w"
)

system_status = tk.Label(
    header,
    text="●  SYSTEM READY",
    font=("Segoe UI", 10, "bold"),
    bg="#1E3A8A",
    fg="#BFDBFE",
    padx=16,
    pady=9
)

system_status.pack(
    side="right",
    padx=40
)

main = tk.Frame(
    root,
    bg=BACKGROUND
)

main.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=25
)

key_card = tk.Frame(
    main,
    bg=WHITE,
    highlightthickness=1,
    highlightbackground=BORDER
)

key_card.pack(
    fill="x",
    pady=(0, 18)
)

key_heading = tk.Label(
    key_card,
    text="🔑  RSA KEY INFORMATION",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=TEXT
)

key_heading.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    padx=22,
    pady=(18, 12)
)

public_box = tk.Frame(
    key_card,
    bg=LIGHT_BLUE,
    highlightthickness=1,
    highlightbackground="#BFDBFE"
)

public_box.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=(22, 10),
    pady=(0, 18)
)


public_title = tk.Label(
    public_box,
    text="PUBLIC KEY",
    font=("Segoe UI", 9, "bold"),
    bg=LIGHT_BLUE,
    fg=BLUE
)

public_title.pack(
    anchor="w",
    padx=15,
    pady=(12, 3)
)


public_value = tk.Label(
    public_box,
    text=f"(e = {public_key}, n = {n})",
    font=("Consolas", 11),
    bg=LIGHT_BLUE,
    fg=TEXT
)

public_value.pack(
    anchor="w",
    padx=15,
    pady=(0, 12)
)

private_box = tk.Frame(
    key_card,
    bg="#FFF7ED",
    highlightthickness=1,
    highlightbackground="#FED7AA"
)

private_box.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=(10, 22),
    pady=(0, 18)
)


private_title = tk.Label(
    private_box,
    text="PRIVATE KEY",
    font=("Segoe UI", 9, "bold"),
    bg="#FFF7ED",
    fg="#EA580C"
)

private_title.pack(
    anchor="w",
    padx=15,
    pady=(12, 3)
)


private_value = tk.Label(
    private_box,
    text=f"(d = {private_key}, n = {n})",
    font=("Consolas", 11),
    bg="#FFF7ED",
    fg=TEXT
)

private_value.pack(
    anchor="w",
    padx=15,
    pady=(0, 12)
)


key_card.columnconfigure(
    0,
    weight=1
)

key_card.columnconfigure(
    1,
    weight=1
)

content = tk.Frame(
    main,
    bg=BACKGROUND
)

content.pack(
    fill="both",
    expand=True
)

message_card = tk.Frame(
    content,
    bg=WHITE,
    highlightthickness=1,
    highlightbackground=BORDER
)

message_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 9)
)

message_heading = tk.Label(
    message_card,
    text="📝  MESSAGE",
    font=("Segoe UI", 13, "bold"),
    bg=WHITE,
    fg=TEXT
)

message_heading.pack(
    anchor="w",
    padx=22,
    pady=(20, 4)
)


message_subtitle = tk.Label(
    message_card,
    text="Enter the message you want to digitally sign.",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg=SECONDARY
)

message_subtitle.pack(
    anchor="w",
    padx=22
)

message_text = tk.Text(
    message_card,
    height=8,
    font=("Segoe UI", 11),
    bg="#F8FAFC",
    fg=TEXT,
    insertbackground=PURPLE,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=PURPLE,
    padx=15,
    pady=14,
    wrap="word"
)

message_text.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=14
)

hash_heading = tk.Label(
    message_card,
    text="SHA-256 HASH",
    font=("Segoe UI", 9, "bold"),
    bg=WHITE,
    fg=SECONDARY
)

hash_heading.pack(
    anchor="w",
    padx=22
)

hash_text = tk.Text(
    message_card,
    height=3,
    font=("Consolas", 9),
    bg="#F8FAFC",
    fg="#0369A1",
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER,
    padx=12,
    pady=9,
    wrap="word"
)

hash_text.pack(
    fill="x",
    padx=22,
    pady=(6, 20)
)

signature_card = tk.Frame(
    content,
    bg=WHITE,
    highlightthickness=1,
    highlightbackground=BORDER
)

signature_card.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(9, 0)
)

signature_heading = tk.Label(
    signature_card,
    text="✍  DIGITAL SIGNATURE",
    font=("Segoe UI", 13, "bold"),
    bg=WHITE,
    fg=TEXT
)

signature_heading.pack(
    anchor="w",
    padx=22,
    pady=(20, 4)
)


signature_subtitle = tk.Label(
    signature_card,
    text="RSA signature generated from the message hash.",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg=SECONDARY
)

signature_subtitle.pack(
    anchor="w",
    padx=22
)

signature_text = tk.Text(
    signature_card,
    height=8,
    font=("Consolas", 12),
    bg="#FAF5FF",
    fg=PURPLE,
    insertbackground=PURPLE,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#DDD6FE",
    highlightcolor=PURPLE,
    padx=15,
    pady=14,
    wrap="word"
)

signature_text.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=14
)

copy_button = tk.Button(
    signature_card,
    text="📋  COPY SIGNATURE",
    command=copy_signature,
    font=("Segoe UI", 9, "bold"),
    bg=LIGHT_PURPLE,
    fg=PURPLE,
    activebackground="#E9D5FF",
    activeforeground=PURPLE,
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=8
)

copy_button.pack(
    anchor="e",
    padx=22,
    pady=(0, 20)
)

button_area = tk.Frame(
    main,
    bg=BACKGROUND
)

button_area.pack(
    fill="x",
    pady=20
)

generate_button = tk.Button(
    button_area,
    text="🔏  GENERATE SIGNATURE",
    command=generate_signature,
    font=("Segoe UI", 10, "bold"),
    bg=PURPLE,
    fg="white",
    activebackground="#6D28D9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=11
)

generate_button.pack(
    side="left",
    padx=(0, 10)
)

verify_button = tk.Button(
    button_area,
    text="✓  VERIFY SIGNATURE",
    command=verify,
    font=("Segoe UI", 10, "bold"),
    bg=BLUE,
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=11
)

verify_button.pack(
    side="left",
    padx=10
)
clear_button = tk.Button(
    button_area,
    text="↻  CLEAR",
    command=clear_all,
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=TEXT,
    activebackground="#E2E8F0",
    activeforeground=TEXT,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER,
    cursor="hand2",
    padx=25,
    pady=10
)

clear_button.pack(
    side="right"
)

result_frame = tk.Frame(
    main,
    bg=WHITE,
    highlightthickness=2,
    highlightbackground=BORDER
)

result_frame.pack(
    fill="x"
)

status_label = tk.Label(
    result_frame,
    text="●  READY",
    font=("Segoe UI", 14, "bold"),
    bg=WHITE,
    fg=SECONDARY
)

status_label.pack(
    pady=(13, 2)
)

status_description = tk.Label(
    result_frame,
    text="Enter a message to begin the digital signing process.",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg=SECONDARY
)

status_description.pack(
    pady=(0, 13)
)

root.mainloop()
