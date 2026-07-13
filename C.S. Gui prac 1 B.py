import tkinter as tk
from tkinter import ttk, messagebox

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

#Columnar Cipher
def col_encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text += "X" * (rows * cols - len(text))

    matrix = [list(text[i:i+cols]) for i in range(0, len(text), cols)]
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

#Functions
def encrypt():
    msg = message.get()

    if msg == "":
        messagebox.showwarning("Warning", "Enter a message!")
        return

    try:
        if cipher_type.get() == "Rail Fence Cipher":
            key = int(key_entry.get())
            result.set(rail_encrypt(msg, key))
        else:
            key = key_entry.get().upper()
            result.set(col_encrypt(msg, key))
    except:
        messagebox.showerror("Error", "Invalid Key!")

def decrypt():
    msg = message.get()

    if msg == "":
        messagebox.showwarning("Warning", "Enter a message!")
        return

    try:
        if cipher_type.get() == "Rail Fence Cipher":
            key = int(key_entry.get())
            result.set(rail_decrypt(msg, key))
        else:
            key = key_entry.get().upper()
            result.set(col_decrypt(msg, key))
    except:
        messagebox.showerror("Error", "Invalid Key!")

def clear():
    message.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result.set("")

#GUI
root = tk.Tk()
root.title("Transposition Cipher")
root.geometry("650x500")
root.configure(bg="#0F172A")
root.resizable(False, False)

# Header
tk.Label(
    root,
    text="🔐 Transposition Substitution Techniques",
    font=("Segoe UI", 20, "bold"),
    bg="#1E3A8A",
    fg="white",
    pady=15
).pack(fill="x")

# Card
card = tk.Frame(root, bg="white", bd=2, relief="ridge")
card.place(relx=0.5, rely=0.52, anchor="center", width=560, height=360)

# Technique
tk.Label(card, text="Technique", font=("Segoe UI",11,"bold"),
         bg="white").place(x=40, y=30)

cipher_type = ttk.Combobox(
    card,
    values=["Rail Fence Cipher", "Columnar Transposition"],
    state="readonly",
    width=28,
    font=("Segoe UI",10)
)
cipher_type.current(0)
cipher_type.place(x=220, y=30)

# Message
tk.Label(card, text="Message", font=("Segoe UI",11,"bold"),
         bg="white").place(x=40, y=80)

message = tk.Entry(card, width=32, font=("Segoe UI",11))
message.place(x=220, y=80)

# Key
tk.Label(card, text="Key", font=("Segoe UI",11,"bold"),
         bg="white").place(x=40, y=130)

key_entry = tk.Entry(card, width=15, font=("Segoe UI",11))
key_entry.place(x=220, y=130)

# Buttons
tk.Button(card, text="🔒 Encrypt",
          bg="#16A34A", fg="white",
          font=("Segoe UI",11,"bold"),
          width=12,
          command=encrypt).place(x=45, y=190)

tk.Button(card, text="🔓 Decrypt",
          bg="#2563EB", fg="white",
          font=("Segoe UI",11,"bold"),
          width=12,
          command=decrypt).place(x=210, y=190)

tk.Button(card, text="🗑 Clear",
          bg="#DC2626", fg="white",
          font=("Segoe UI",11,"bold"),
          width=12,
          command=clear).place(x=375, y=190)

# Result
tk.Label(card, text="Result",
         font=("Segoe UI",11,"bold"),
         bg="white").place(x=40, y=270)

result = tk.StringVar()

tk.Entry(card,
         textvariable=result,
         font=("Consolas",12,"bold"),
         width=32,
         justify="center",
         state="readonly",
         readonlybackground="#E0F2FE").place(x=220, y=270)

# Footer
tk.Label(
    root,
    text="Rail Fence Cipher & Columnar Transposition | Python Tkinter",
    bg="#1E3A8A",
    fg="white",
    font=("Segoe UI",10),
    pady=8
).pack(side="bottom", fill="x")

root.mainloop()
