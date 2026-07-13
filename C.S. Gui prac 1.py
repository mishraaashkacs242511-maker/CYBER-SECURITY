import tkinter as tk
from tkinter import ttk, messagebox

#Monoalphabetic Key
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
            result += cipher[plain.index(ch)]
        else:
            result += ch
    return result

def mono_decrypt(text):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += plain[cipher.index(ch)]
        else:
            result += ch
    return result

#Functions
def encrypt():
    text = message_entry.get()

    if text == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    if combo.get() == "Caesar Cipher":
        try:
            shift = int(shift_entry.get())
            result.set(caesar_encrypt(text, shift))
        except:
            messagebox.showerror("Error", "Enter a valid shift value.")
    else:
        result.set(mono_encrypt(text))


def decrypt():
    text = message_entry.get()

    if text == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    if combo.get() == "Caesar Cipher":
        try:
            shift = int(shift_entry.get())
            result.set(caesar_decrypt(text, shift))
        except:
            messagebox.showerror("Error", "Enter a valid shift value.")
    else:
        result.set(mono_decrypt(text))


def clear():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result.set("")


#Main Window
root = tk.Tk()
root.title("Classical Substitution Cipher")
root.geometry("650x500")
root.configure(bg="#0F172A")
root.resizable(False, False)

#Heading
title = tk.Label(
    root,
    text="🔐 Classical Substitution Cipher System",
    font=("Segoe UI", 20, "bold"),
    bg="#1E3A8A",
    fg="white",
    pady=15
)
title.pack(fill="x")

#Card
card = tk.Frame(root, bg="white", bd=2, relief="ridge")
card.place(relx=0.5, rely=0.52, anchor="center", width=560, height=360)

#Labels
tk.Label(card,
         text="Cipher Technique",
         font=("Segoe UI", 11, "bold"),
         bg="white").place(x=40, y=30)

combo = ttk.Combobox(
    card,
    values=["Caesar Cipher", "Monoalphabetic Cipher"],
    state="readonly",
    width=28,
    font=("Segoe UI", 10)
)
combo.current(0)
combo.place(x=220, y=30)

tk.Label(card,
         text="Enter Message",
         font=("Segoe UI", 11, "bold"),
         bg="white").place(x=40, y=80)

message_entry = tk.Entry(
    card,
    font=("Segoe UI", 11),
    width=32,
    relief="solid",
    bd=1
)
message_entry.place(x=220, y=82)

tk.Label(card,
         text="Shift Value",
         font=("Segoe UI", 11, "bold"),
         bg="white").place(x=40, y=130)

shift_entry = tk.Entry(
    card,
    font=("Segoe UI", 11),
    width=10,
    relief="solid",
    bd=1
)
shift_entry.place(x=220, y=132)

#Buttons
encrypt_btn = tk.Button(
    card,
    text="🔒 Encrypt",
    font=("Segoe UI", 11, "bold"),
    bg="#16A34A",
    fg="white",
    width=12,
    command=encrypt,
    cursor="hand2"
)
encrypt_btn.place(x=55, y=190)

decrypt_btn = tk.Button(
    card,
    text="🔓 Decrypt",
    font=("Segoe UI", 11, "bold"),
    bg="#2563EB",
    fg="white",
    width=12,
    command=decrypt,
    cursor="hand2"
)
decrypt_btn.place(x=215, y=190)

clear_btn = tk.Button(
    card,
    text="🗑 Clear",
    font=("Segoe UI", 11, "bold"),
    bg="#DC2626",
    fg="white",
    width=12,
    command=clear,
    cursor="hand2"
)
clear_btn.place(x=375, y=190)

#Result
tk.Label(card,
         text="Result",
         font=("Segoe UI", 11, "bold"),
         bg="white").place(x=40, y=265)

result = tk.StringVar()

result_box = tk.Entry(
    card,
    textvariable=result,
    font=("Consolas", 12, "bold"),
    width=32,
    justify="center",
    state="readonly",
    readonlybackground="#E0F2FE",
    fg="#0F172A"
)
result_box.place(x=220, y=267)

#Footer
footer = tk.Label(
    root,
    text="Developed using Python Tkinter | Caesar Cipher & Monoalphabetic Cipher",
    font=("Segoe UI", 10),
    bg="#1E3A8A",
    fg="white",
    pady=8
)
footer.pack(side="bottom", fill="x")

root.mainloop()
