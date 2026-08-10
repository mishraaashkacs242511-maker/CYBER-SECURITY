import tkinter as tk
from tkinter import messagebox
import random

def calculate():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())
        a = int(aashka_private_entry.get())
        b = int(deesha_private_entry.get())

        if p <= 1:
            messagebox.showerror(
                "Invalid Input",
                "Prime number p must be greater than 1."
            )
            return

        if g <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Generator g must be greater than 0."
            )
            return

        if a <= 0 or b <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Private keys must be positive numbers."
            )
            return

        if g >= p:
            messagebox.showerror(
                "Invalid Input",
                "Generator g should be smaller than p."
            )
            return

        aashka_public = pow(g, a, p)

        deesha_public = pow(g, b, p)

        aashka_shared = pow(deesha_public, a, p)

        deesha_shared = pow(aashka_public, b, p)

        aashka_public_value.config(
            text=str(aashka_public),
            fg="#5EE7DF"
        )

        deesha_public_value.config(
            text=str(deesha_public),
            fg="#A78BFA"
        )

        aashka_shared_value.config(
            text=str(aashka_shared),
            fg="#A7F3D0"
        )

        deesha_shared_value.config(
            text=str(deesha_shared),
            fg="#A7F3D0"
        )

        calculation_text.delete(
            "1.0",
            tk.END
        )

        calculation_text.insert(
            tk.END,
            "DIFFIE–HELLMAN KEY EXCHANGE PROCESS\n"
            "════════════════════════════════════════════════════\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 1 — PUBLIC PARAMETERS\n\n"
        )

        calculation_text.insert(
            tk.END,
            f"Prime number (p) = {p}\n"
            f"Generator (g)    = {g}\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 2 — AASHKA GENERATES PUBLIC KEY\n\n"
        )

        calculation_text.insert(
            tk.END,
            f"A = g^a mod p\n"
            f"A = {g}^{a} mod {p}\n"
            f"A = {aashka_public}\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 3 — DEESHA GENERATES PUBLIC KEY\n\n"
        )

        calculation_text.insert(
            tk.END,
            f"B = g^b mod p\n"
            f"B = {g}^{b} mod {p}\n"
            f"B = {deesha_public}\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 4 — AASHKA CALCULATES SHARED SECRET\n\n"
        )

        calculation_text.insert(
            tk.END,
            f"Kₐ = B^a mod p\n"
            f"Kₐ = {deesha_public}^{a} mod {p}\n"
            f"Kₐ = {aashka_shared}\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 5 — DEESHA CALCULATES SHARED SECRET\n\n"
        )

        calculation_text.insert(
            tk.END,
            f"Kᵦ = A^b mod p\n"
            f"Kᵦ = {aashka_public}^{b} mod {p}\n"
            f"Kᵦ = {deesha_shared}\n\n"
        )

        calculation_text.insert(
            tk.END,
            "STEP 6 — VERIFY SHARED KEY\n\n"
        )

        if aashka_shared == deesha_shared:

            calculation_text.insert(
                tk.END,
                "✓ SUCCESS!\n\n"
                "Aashka's shared key = Deesha's shared key\n"
                f"Shared Secret Key = {aashka_shared}\n\n"
                "The Diffie–Hellman key exchange was successful."
            )

            status_label.config(
                text="●  KEY EXCHANGE SUCCESSFUL",
                fg="#4ADE80"
            )

            status_box.config(
                bg="#123C2C"
            )

        else:

            calculation_text.insert(
                tk.END,
                "✗ ERROR!\n\n"
                "The shared keys do not match."
            )

            status_label.config(
                text="●  KEY EXCHANGE FAILED",
                fg="#FB7185"
            )

            status_box.config(
                bg="#421B24"
            )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )

def reset_all():

    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)

    aashka_private_entry.delete(0, tk.END)
    deesha_private_entry.delete(0, tk.END)

    p_entry.insert(0, "23")
    g_entry.insert(0, "5")

    aashka_private_entry.insert(0, "6")
    deesha_private_entry.insert(0, "15")

    aashka_public_value.config(
        text="—",
        fg="#5EE7DF"
    )

    deesha_public_value.config(
        text="—",
        fg="#A78BFA"
    )

    aashka_shared_value.config(
        text="—",
        fg="#A7F3D0"
    )

    deesha_shared_value.config(
        text="—",
        fg="#A7F3D0"
    )

    calculation_text.delete(
        "1.0",
        tk.END
    )

    calculation_text.insert(
        tk.END,
        "Enter the parameters and click\n"
        "\"GENERATE SHARED KEY\" to begin.\n\n"
        "The complete Diffie–Hellman\n"
        "calculation will appear here."
    )

    status_label.config(
        text="●  WAITING FOR KEY EXCHANGE",
        fg="#FBBF24"
    )

    status_box.config(
        bg="#332A12"
    )

def generate_random_keys():

    try:

        p = int(p_entry.get())

        if p <= 10:

            messagebox.showwarning(
                "Prime Number",
                "Enter a larger value of p first."
            )

            return

        aashka_private_entry.delete(
            0,
            tk.END
        )

        deesha_private_entry.delete(
            0,
            tk.END
        )

        aashka_private_entry.insert(
            0,
            str(random.randint(2, p - 2))
        )

        deesha_private_entry.insert(
            0,
            str(random.randint(2, p - 2))
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid value for p."
        )
root = tk.Tk()

root.title(
    "Diffie–Hellman Key Exchange | Aashka & Deesha"
)

root.geometry(
    "1200x800"
)

root.minsize(
    1050,
    700
)

root.configure(
    bg="#07111F"
)

BG = "#07111F"
CARD = "#0D1B2A"
CARD2 = "#102235"
BORDER = "#1E3A5F"

WHITE = "#F8FAFC"
TEXT = "#CBD5E1"
MUTED = "#7891AA"

CYAN = "#5EE7DF"
GREEN = "#4ADE80"
YELLOW = "#FBBF24"
RED = "#FB7185"

header = tk.Frame(
    root,
    bg=BG,
    height=100
)

header.pack(
    fill="x",
    padx=35,
    pady=(25, 0)
)

logo = tk.Label(
    header,
    text="🔐",
    font=("Segoe UI Emoji", 32),
    bg=BG,
    fg=CYAN
)

logo.pack(
    side="left",
    padx=(0, 15)
)

title_frame = tk.Frame(
    header,
    bg=BG
)

title_frame.pack(
    side="left"
)


title = tk.Label(
    title_frame,
    text="DIFFIE–HELLMAN",
    font=("Segoe UI", 26, "bold"),
    bg=BG,
    fg=WHITE
)

title.pack(
    anchor="w"
)


subtitle = tk.Label(
    title_frame,
    text="SECURE KEY EXCHANGE SIMULATOR",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=CYAN
)

subtitle.pack(
    anchor="w",
    pady=(2, 0)
)


version = tk.Label(
    header,
    text="CRYPTOGRAPHY • PRACTICAL",
    font=("Segoe UI", 9, "bold"),
    bg=BG,
    fg=MUTED
)

version.pack(
    side="right",
    pady=10
)

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=15
)

left = tk.Frame(
    main,
    bg=BG,
    width=470
)

left.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

left.pack_propagate(False)

param_card = tk.Frame(
    left,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

param_card.pack(
    fill="x",
    pady=(0, 15)
)


tk.Label(
    param_card,
    text="  PUBLIC PARAMETERS",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20,
    pady=(18, 3)
)


tk.Label(
    param_card,
    text="These values can be exchanged publicly.",
    font=("Segoe UI", 9),
    bg=CARD,
    fg=MUTED
).pack(
    anchor="w",
    padx=20,
    pady=(0, 15)
)


def create_input(parent, label, default):

    frame = tk.Frame(
        parent,
        bg=CARD
    )

    frame.pack(
        fill="x",
        padx=20,
        pady=6
    )

    tk.Label(
        frame,
        text=label,
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=TEXT,
        width=22,
        anchor="w"
    ).pack(
        side="left"
    )

    entry = tk.Entry(
        frame,
        font=("Consolas", 11),
        bg="#081522",
        fg=WHITE,
        insertbackground=CYAN,
        relief="flat",
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=CYAN
    )

    entry.pack(
        side="right",
        fill="x",
        expand=True,
        ipady=7
    )

    entry.insert(
        0,
        default
    )

    return entry


p_entry = create_input(
    param_card,
    "Prime number (p)",
    "23"
)

g_entry = create_input(
    param_card,
    "Generator (g)",
    "5"
)


tk.Label(
    param_card,
    text="",
    bg=CARD
).pack(
    pady=3
)

users_card = tk.Frame(
    left,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

users_card.pack(
    fill="x",
    pady=(0, 15)
)


tk.Label(
    users_card,
    text="  PARTICIPANTS",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20,
    pady=(18, 15)
)

aashka_frame = tk.Frame(
    users_card,
    bg="#0C2730"
)

aashka_frame.pack(
    fill="x",
    padx=15,
    pady=(0, 8)
)


tk.Label(
    aashka_frame,
    text="👩",
    font=("Segoe UI Emoji", 20),
    bg="#0C2730"
).pack(
    side="left",
    padx=12
)


aashka_info = tk.Frame(
    aashka_frame,
    bg="#0C2730"
)

aashka_info.pack(
    side="left",
    fill="x",
    expand=True
)


tk.Label(
    aashka_info,
    text="AASHKA",
    font=("Segoe UI", 10, "bold"),
    bg="#0C2730",
    fg=CYAN
).pack(
    anchor="w",
    pady=(7, 0)
)


tk.Label(
    aashka_info,
    text="Private key (a)",
    font=("Segoe UI", 9),
    bg="#0C2730",
    fg=MUTED
).pack(
    anchor="w"
)


aashka_private_entry = tk.Entry(
    aashka_frame,
    font=("Consolas", 11, "bold"),
    width=8,
    bg="#081522",
    fg=WHITE,
    insertbackground=CYAN,
    relief="flat",
    justify="center"
)

aashka_private_entry.pack(
    side="right",
    padx=15,
    ipady=5
)

aashka_private_entry.insert(
    0,
    "6"
)

deesha_frame = tk.Frame(
    users_card,
    bg="#171F35"
)

deesha_frame.pack(
    fill="x",
    padx=15,
    pady=(0, 15)
)


tk.Label(
    deesha_frame,
    text="👩",
    font=("Segoe UI Emoji", 20),
    bg="#171F35"
).pack(
    side="left",
    padx=12
)


deesha_info = tk.Frame(
    deesha_frame,
    bg="#171F35"
)

deesha_info.pack(
    side="left",
    fill="x",
    expand=True
)


tk.Label(
    deesha_info,
    text="DEESHA",
    font=("Segoe UI", 10, "bold"),
    bg="#171F35",
    fg="#A78BFA"
).pack(
    anchor="w",
    pady=(7, 0)
)


tk.Label(
    deesha_info,
    text="Private key (b)",
    font=("Segoe UI", 9),
    bg="#171F35",
    fg=MUTED
).pack(
    anchor="w"
)


deesha_private_entry = tk.Entry(
    deesha_frame,
    font=("Consolas", 11, "bold"),
    width=8,
    bg="#081522",
    fg=WHITE,
    insertbackground=CYAN,
    relief="flat",
    justify="center"
)

deesha_private_entry.pack(
    side="right",
    padx=15,
    ipady=5
)

deesha_private_entry.insert(
    0,
    "15"
)
button_frame = tk.Frame(
    left,
    bg=BG
)

button_frame.pack(
    fill="x"
)


generate_button = tk.Button(
    button_frame,
    text="⚡  GENERATE SHARED KEY",
    command=calculate,
    font=("Segoe UI", 11, "bold"),
    bg="#0EA5A4",
    fg="white",
    activebackground="#14B8A6",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    bd=0
)

generate_button.pack(
    fill="x",
    ipady=11,
    pady=(0, 8)
)


random_button = tk.Button(
    button_frame,
    text="🎲  RANDOMIZE PRIVATE KEYS",
    command=generate_random_keys,
    font=("Segoe UI", 10, "bold"),
    bg=CARD2,
    fg=TEXT,
    activebackground=BORDER,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    bd=0
)

random_button.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8,
    padx=(0, 5)
)


reset_button = tk.Button(
    button_frame,
    text="↻  RESET",
    command=reset_all,
    font=("Segoe UI", 10, "bold"),
    bg=CARD2,
    fg=TEXT,
    activebackground=BORDER,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    bd=0
)

reset_button.pack(
    side="right",
    fill="x",
    expand=True,
    ipady=8,
    padx=(5, 0)
)

right = tk.Frame(
    main,
    bg=BG
)

right.pack(
    side="right",
    fill="both",
    expand=True
)

exchange_card = tk.Frame(
    right,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

exchange_card.pack(
    fill="x",
    pady=(0, 15)
)


tk.Label(
    exchange_card,
    text="  KEY EXCHANGE VISUALIZATION",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20,
    pady=(15, 10)
)


visual = tk.Frame(
    exchange_card,
    bg=CARD
)

visual.pack(
    fill="x",
    padx=20,
    pady=(0, 18)
)

aashka_visual = tk.Frame(
    visual,
    bg="#0C2730",
    width=150,
    height=95
)

aashka_visual.pack(
    side="left",
    fill="both",
    expand=True
)

aashka_visual.pack_propagate(False)


tk.Label(
    aashka_visual,
    text="👩",
    font=("Segoe UI Emoji", 24),
    bg="#0C2730"
).pack(
    pady=(7, 0)
)


tk.Label(
    aashka_visual,
    text="AASHKA",
    font=("Segoe UI", 10, "bold"),
    bg="#0C2730",
    fg=CYAN
).pack()

tk.Label(
    visual,
    text="  ───────►\nPUBLIC KEY",
    font=("Consolas", 8, "bold"),
    bg=CARD,
    fg=CYAN
).pack(
    side="left",
    padx=8
)

middle_visual = tk.Frame(
    visual,
    bg="#101C2C",
    width=150,
    height=95
)

middle_visual.pack(
    side="left",
    fill="both",
    expand=True
)

middle_visual.pack_propagate(False)


tk.Label(
    middle_visual,
    text="🔑",
    font=("Segoe UI Emoji", 24),
    bg="#101C2C"
).pack(
    pady=(7, 0)
)


tk.Label(
    middle_visual,
    text="SHARED SECRET",
    font=("Segoe UI", 9, "bold"),
    bg="#101C2C",
    fg=GREEN
).pack()

tk.Label(
    visual,
    text="PUBLIC KEY\n◄───────  ",
    font=("Consolas", 8, "bold"),
    bg=CARD,
    fg="#A78BFA"
).pack(
    side="left",
    padx=8
)

deesha_visual = tk.Frame(
    visual,
    bg="#171F35",
    width=150,
    height=95
)

deesha_visual.pack(
    side="left",
    fill="both",
    expand=True
)

deesha_visual.pack_propagate(False)


tk.Label(
    deesha_visual,
    text="👩",
    font=("Segoe UI Emoji", 24),
    bg="#171F35"
).pack(
    pady=(7, 0)
)


tk.Label(
    deesha_visual,
    text="DEESHA",
    font=("Segoe UI", 10, "bold"),
    bg="#171F35",
    fg="#A78BFA"
).pack()

result_frame = tk.Frame(
    right,
    bg=BG
)

result_frame.pack(
    fill="x",
    pady=(0, 15)
)

aashka_result = tk.Frame(
    result_frame,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

aashka_result.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 7)
)


tk.Label(
    aashka_result,
    text="AASHKA'S PUBLIC KEY",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=MUTED
).pack(
    pady=(12, 2)
)


aashka_public_value = tk.Label(
    aashka_result,
    text="—",
    font=("Consolas", 20, "bold"),
    bg=CARD,
    fg=CYAN
)

aashka_public_value.pack(
    pady=(0, 12)
)

deesha_result = tk.Frame(
    result_frame,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

deesha_result.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(7, 0)
)


tk.Label(
    deesha_result,
    text="DEESHA'S PUBLIC KEY",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=MUTED
).pack(
    pady=(12, 2)
)


deesha_public_value = tk.Label(
    deesha_result,
    text="—",
    font=("Consolas", 20, "bold"),
    bg=CARD,
    fg="#A78BFA"
)

deesha_public_value.pack(
    pady=(0, 12)
)

shared_card = tk.Frame(
    right,
    bg="#0B2520",
    highlightbackground="#1F5B4A",
    highlightthickness=1
)

shared_card.pack(
    fill="x",
    pady=(0, 15)
)


tk.Label(
    shared_card,
    text="🔑  SHARED SECRET KEY",
    font=("Segoe UI", 11, "bold"),
    bg="#0B2520",
    fg=GREEN
).pack(
    pady=(12, 5)
)


shared_values = tk.Frame(
    shared_card,
    bg="#0B2520"
)

shared_values.pack(
    fill="x",
    padx=25,
    pady=(0, 12)
)


aashka_shared_value = tk.Label(
    shared_values,
    text="—",
    font=("Consolas", 20, "bold"),
    bg="#0B2520",
    fg="#A7F3D0"
)

aashka_shared_value.pack(
    side="left",
    fill="x",
    expand=True
)


tk.Label(
    shared_values,
    text="=",
    font=("Consolas", 18, "bold"),
    bg="#0B2520",
    fg=MUTED
).pack(
    side="left"
)


deesha_shared_value = tk.Label(
    shared_values,
    text="—",
    font=("Consolas", 20, "bold"),
    bg="#0B2520",
    fg="#A7F3D0"
)

deesha_shared_value.pack(
    side="left",
    fill="x",
    expand=True
)

calc_card = tk.Frame(
    right,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

calc_card.pack(
    fill="both",
    expand=True
)


tk.Label(
    calc_card,
    text="  STEP-BY-STEP CALCULATION",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20,
    pady=(12, 7)
)


calculation_text = tk.Text(
    calc_card,
    font=("Consolas", 9),
    bg="#081522",
    fg=TEXT,
    insertbackground=CYAN,
    relief="flat",
    bd=0,
    wrap="word"
)

calculation_text.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)


calculation_text.insert(
    tk.END,
    "Enter the parameters and click\n"
    "\"GENERATE SHARED KEY\" to begin.\n\n"
    "The complete Diffie–Hellman\n"
    "calculation will appear here."
)

status_box = tk.Frame(
    root,
    bg="#332A12",
    height=42
)

status_box.pack(
    fill="x",
    padx=35,
    pady=(0, 20)
)


status_label = tk.Label(
    status_box,
    text="●  WAITING FOR KEY EXCHANGE",
    font=("Segoe UI", 9, "bold"),
    bg="#332A12",
    fg=YELLOW
)

status_label.pack(
    pady=11
)

root.mainloop()
