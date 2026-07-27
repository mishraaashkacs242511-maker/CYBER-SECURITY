import hmac
import hashlib
import secrets
import tkinter as tk
from tkinter import ttk, messagebox

COLOR_APP_BG      = "#eef0f6"
COLOR_HEADER      = "#171a2b"
COLOR_HEADER_SUB  = "#9aa0c3"
COLOR_ACCENT      = "#5b5bf0"
COLOR_ACCENT_DARK = "#4646c9"
COLOR_ACCENT_SOFT = "#eeeeff"

COLOR_CARD        = "#ffffff"
COLOR_CARD_BORDER = "#e3e5ef"
COLOR_SHADOW      = "#d9dbea"

COLOR_TEXT        = "#1c1f2e"
COLOR_MUTED       = "#7a7f97"
COLOR_BORDER      = "#dfe1ec"

COLOR_SUCCESS     = "#0f7a4d"
COLOR_SUCCESS_BG  = "#e5f7ee"
COLOR_SUCCESS_BD  = "#b7e8cf"

COLOR_ERROR       = "#c0223a"
COLOR_ERROR_BG    = "#fdecef"
COLOR_ERROR_BD    = "#f6bfc9"

COLOR_NEUTRAL_BG  = "#f3f4fa"
COLOR_NEUTRAL_BD  = "#e3e5ef"

FONT_FAMILY = "Segoe UI"
FONT_MONO   = "Consolas"


def generate_mac(key: bytes, message: bytes, algo: str) -> str:
    """Create an HMAC tag for a message using a secret key."""
    return hmac.new(key, message, algo).hexdigest()


def verify_mac(key: bytes, message: bytes, mac: str, algo: str) -> bool:
    """Check a MAC in constant time to avoid timing attacks.
    Trims whitespace and normalizes case, since pasted MACs commonly
    pick up trailing newlines or get capitalized by the source app.
    """
    try:
        expected = generate_mac(key, message, algo)
        return hmac.compare_digest(expected, mac.strip().lower())
    except ValueError:
        return False


class MacApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HMAC Studio")
        self.resizable(True, True)
        self.minsize(660, 720)
        self.configure(bg=COLOR_APP_BG)

        self._configure_styles()
        self._build_header()
        self._build_body()

        self.update_idletasks()
        req_w = max(self.winfo_reqwidth() + 24, 660)
        req_h = max(self.winfo_reqheight() + 24, 720)

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight() - 80 
        win_w = min(req_w, screen_w - 40)
        win_h = min(req_h, screen_h)
        self.geometry(f"{win_w}x{win_h}")

    def _configure_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Bg.TFrame", background=COLOR_APP_BG)
        style.configure("Card.TFrame", background=COLOR_CARD)
        style.configure("Header.TFrame", background=COLOR_HEADER)

        style.configure(
            "HeaderTitle.TLabel", background=COLOR_HEADER, foreground="#ffffff",
            font=(FONT_FAMILY, 18, "bold"),
        )
        style.configure(
            "HeaderSub.TLabel", background=COLOR_HEADER, foreground=COLOR_HEADER_SUB,
            font=(FONT_FAMILY, 10),
        )
        style.configure(
            "SectionTitle.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT,
            font=(FONT_FAMILY, 12, "bold"),
        )
        style.configure(
            "FieldLabel.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT,
            font=(FONT_FAMILY, 9, "bold"),
        )
        style.configure(
            "Hint.TLabel", background=COLOR_CARD, foreground=COLOR_MUTED,
            font=(FONT_FAMILY, 8),
        )
        style.configure(
            "Card.TCheckbutton", background=COLOR_CARD, foreground=COLOR_MUTED,
            font=(FONT_FAMILY, 9),
        )

        style.configure(
            "App.TEntry", fieldbackground="#ffffff", bordercolor=COLOR_BORDER,
            lightcolor=COLOR_BORDER, darkcolor=COLOR_BORDER, padding=8,
            relief="flat",
        )
        style.map("App.TEntry", bordercolor=[("focus", COLOR_ACCENT)])

        style.configure(
            "Primary.TButton", background=COLOR_ACCENT, foreground="#ffffff",
            font=(FONT_FAMILY, 10, "bold"), padding=(18, 10), borderwidth=0,
            relief="flat",
        )
        style.map(
            "Primary.TButton",
            background=[("active", COLOR_ACCENT_DARK), ("pressed", COLOR_ACCENT_DARK)],
        )

        style.configure(
            "Secondary.TButton", background="#ffffff", foreground=COLOR_TEXT,
            font=(FONT_FAMILY, 10, "bold"), padding=(14, 9), borderwidth=1,
            relief="flat", bordercolor=COLOR_BORDER,
        )
        style.map(
            "Secondary.TButton",
            background=[("active", COLOR_NEUTRAL_BG)],
        )

        style.configure(
            "Ghost.TButton", background=COLOR_CARD, foreground=COLOR_ACCENT,
            font=(FONT_FAMILY, 9, "bold"), borderwidth=0, padding=(10, 6),
        )
        style.map("Ghost.TButton", foreground=[("active", COLOR_ACCENT_DARK)])

        style.configure(
            "Segment.TButton", background=COLOR_NEUTRAL_BG, foreground=COLOR_MUTED,
            font=(FONT_MONO, 10, "bold"), padding=(16, 9), borderwidth=0,
        )
        style.map("Segment.TButton", background=[("active", COLOR_ACCENT_SOFT)])

        style.configure(
            "SegmentActive.TButton", background=COLOR_ACCENT, foreground="#ffffff",
            font=(FONT_MONO, 10, "bold"), padding=(16, 9), borderwidth=0,
        )
        style.map("SegmentActive.TButton", background=[("active", COLOR_ACCENT_DARK)])

    def _build_header(self):
        header = tk.Frame(self, bg=COLOR_HEADER)
        header.pack(fill="x", side="top")

        inner = ttk.Frame(header, style="Header.TFrame", padding=(24, 20))
        inner.pack(fill="x")

        badge = tk.Canvas(inner, width=40, height=40, bg=COLOR_HEADER, highlightthickness=0)
        badge.grid(row=0, column=0, rowspan=2, padx=(0, 14))
        badge.create_oval(2, 2, 38, 38, fill=COLOR_ACCENT, outline="")
        badge.create_text(20, 21, text="🔒", font=(FONT_FAMILY, 15))

        ttk.Label(inner, text="HMAC Studio", style="HeaderTitle.TLabel").grid(
            row=0, column=1, sticky="w"
        )
        ttk.Label(
            inner,
            text="Generate & verify keyed message authentication codes — fully offline.",
            style="HeaderSub.TLabel",
        ).grid(row=1, column=1, sticky="w")

    def _build_body(self):

        container = tk.Frame(self, bg=COLOR_APP_BG)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=COLOR_APP_BG, highlightthickness=0)
        vsb = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        canvas.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        outer = ttk.Frame(canvas, style="Bg.TFrame", padding=24)
        outer_window = canvas.create_window((0, 0), window=outer, anchor="nw")
        outer.grid_columnconfigure(0, weight=1)

        def _sync_scrollregion(_event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def _sync_width(event):
            canvas.itemconfigure(outer_window, width=event.width)

        outer.bind("<Configure>", _sync_scrollregion)
        canvas.bind("<Configure>", _sync_width)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        card1 = self._make_card(outer, row=0, title="1 · Secret Key & Algorithm")
        card1.grid_columnconfigure(0, weight=1)

        ttk.Label(card1, text="SECRET KEY", style="FieldLabel.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        key_row = ttk.Frame(card1, style="Card.TFrame")
        key_row.grid(row=1, column=0, columnspan=2, sticky="we", pady=(6, 0))
        key_row.grid_columnconfigure(0, weight=1)

        self.key_var = tk.StringVar()
        self.key_entry = ttk.Entry(
            key_row, textvariable=self.key_var, show="•", style="App.TEntry",
            font=(FONT_MONO, 10),
        )
        self.key_entry.grid(row=0, column=0, sticky="we", ipady=2)

        self.show_key_var = tk.BooleanVar()
        ttk.Checkbutton(
            key_row, text="Show", variable=self.show_key_var,
            command=self._toggle_key_visibility, style="Card.TCheckbutton",
        ).grid(row=0, column=1, padx=(10, 0))

        ttk.Button(
            card1, text="🎲  Generate Random Key", style="Ghost.TButton",
            command=self._generate_key,
        ).grid(row=2, column=0, sticky="w", pady=(6, 0))

        ttk.Separator(card1, orient="horizontal").grid(
            row=3, column=0, columnspan=2, sticky="we", pady=16
        )

        ttk.Label(card1, text="HASH ALGORITHM", style="FieldLabel.TLabel").grid(
            row=4, column=0, sticky="w"
        )
        self.algo_var = tk.StringVar(value="sha256")
        seg_row = ttk.Frame(card1, style="Card.TFrame")
        seg_row.grid(row=5, column=0, sticky="w", pady=(8, 0))
        self._algo_buttons = {}
        for i, algo in enumerate(["sha256", "sha384", "sha512"]):
            b = ttk.Button(
                seg_row, text=algo.upper(),
                style="SegmentActive.TButton" if algo == "sha256" else "Segment.TButton",
                command=lambda a=algo: self._select_algo(a),
            )
            b.grid(row=0, column=i, padx=(0 if i == 0 else 2, 0))
            self._algo_buttons[algo] = b

        card2 = self._make_card(outer, row=1, title="2 · Message & MAC")
        card2.grid_columnconfigure(0, weight=1)

        ttk.Label(card2, text="MESSAGE", style="FieldLabel.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        text_frame = tk.Frame(card2, bg=COLOR_BORDER, bd=0)
        text_frame.grid(row=1, column=0, sticky="we", pady=(6, 0))
        self.message_text = tk.Text(
            text_frame, width=58, height=4, wrap="word",
            relief="flat", bd=10, font=(FONT_FAMILY, 10),
            bg="#ffffff", fg=COLOR_TEXT, insertbackground=COLOR_TEXT,
            highlightthickness=0,
        )
        self.message_text.pack(fill="both", expand=True, padx=1, pady=1)

        ttk.Label(
            card2, text="MAC (HEX) — LEAVE BLANK WHEN GENERATING",
            style="FieldLabel.TLabel",
        ).grid(row=2, column=0, sticky="w", pady=(16, 0))
        self.mac_var = tk.StringVar()
        self.mac_entry = ttk.Entry(
            card2, textvariable=self.mac_var, style="App.TEntry", font=(FONT_MONO, 9)
        )
        self.mac_entry.grid(row=3, column=0, sticky="we", pady=(6, 0), ipady=2)

        actions = ttk.Frame(outer, style="Bg.TFrame")
        actions.grid(row=2, column=0, sticky="w", pady=(16, 10))
        ttk.Button(
            actions, text="⚡  Generate MAC", style="Primary.TButton",
            command=self._on_generate,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            actions, text="✓  Verify MAC", style="Primary.TButton",
            command=self._on_verify,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            actions, text="Copy Result", style="Secondary.TButton",
            command=self._copy_result,
        ).pack(side="left")

        outer.grid_rowconfigure(3, weight=1)
        shadow = tk.Frame(outer, bg=COLOR_SHADOW)
        shadow.grid(row=3, column=0, sticky="we")
        self.result_card = tk.Frame(
            shadow, bg=COLOR_NEUTRAL_BG, highlightbackground=COLOR_NEUTRAL_BD,
            highlightthickness=1, bd=0,
        )
        self.result_card.pack(fill="both", expand=True, padx=(0, 2), pady=(0, 2))

        pad_inner = tk.Frame(self.result_card, bg=COLOR_NEUTRAL_BG)
        pad_inner.pack(fill="both", expand=True, padx=16, pady=14)

        self.result_icon_var = tk.StringVar(value="ℹ")
        head_row = tk.Frame(pad_inner, bg=COLOR_NEUTRAL_BG)
        head_row.pack(fill="x", anchor="w")

        self.result_icon_label = tk.Label(
            head_row, textvariable=self.result_icon_var, bg=COLOR_NEUTRAL_BG,
            fg=COLOR_MUTED, font=(FONT_FAMILY, 11, "bold"),
        )
        self.result_icon_label.pack(side="left")

        self.result_title_var = tk.StringVar(value="RESULT")
        self.result_title_label = tk.Label(
            head_row, textvariable=self.result_title_var, bg=COLOR_NEUTRAL_BG,
            fg=COLOR_MUTED, font=(FONT_FAMILY, 9, "bold"),
        )
        self.result_title_label.pack(side="left", padx=(6, 0))

        self.result_var = tk.StringVar(value="No result yet — generate or verify a MAC above.")
        self.result_label = tk.Label(
            pad_inner, textvariable=self.result_var, wraplength=560,
            justify="left", bg=COLOR_NEUTRAL_BG, fg=COLOR_TEXT,
            font=(FONT_MONO, 10),
        )
        self.result_label.pack(anchor="w", pady=(8, 0))

        footer = ttk.Frame(outer, style="Bg.TFrame")
        footer.grid(row=4, column=0, sticky="we", pady=(10, 0))
        ttk.Label(
            footer,
            text="All computation happens locally — nothing is sent over the network.",
            style="Hint.TLabel",
            background=COLOR_APP_BG,
        ).pack(anchor="w")

    def _make_card(self, parent, row, title):
        shadow = tk.Frame(parent, bg=COLOR_SHADOW)
        shadow.grid(row=row, column=0, sticky="we", pady=(0, 12))
        card = tk.Frame(
            shadow, bg=COLOR_CARD, highlightbackground=COLOR_CARD_BORDER,
            highlightthickness=1, bd=0,
        )
        card.pack(fill="both", expand=True, padx=(0, 2), pady=(0, 2))

        header = tk.Frame(card, bg=COLOR_CARD)
        header.pack(fill="x", padx=18, pady=(16, 0))
        tk.Label(
            header, text=title, bg=COLOR_CARD, fg=COLOR_TEXT,
            font=(FONT_FAMILY, 11, "bold"),
        ).pack(anchor="w")

        inner = ttk.Frame(card, style="Card.TFrame", padding=(18, 12, 18, 18))
        inner.pack(fill="both", expand=True)
        return inner

    def _select_algo(self, algo):
        self.algo_var.set(algo)
        for a, btn in self._algo_buttons.items():
            btn.configure(style="SegmentActive.TButton" if a == algo else "Segment.TButton")

    def _toggle_key_visibility(self):
        self.key_entry.config(show="" if self.show_key_var.get() else "•")

    def _generate_key(self):
        key_hex = secrets.token_bytes(32).hex()
        self.key_var.set(key_hex)
        self.show_key_var.set(True)
        self._toggle_key_visibility()
        messagebox.showinfo(
            "Key generated",
            "A random 32-byte key was generated and inserted.\n"
            "Save it — you'll need it to verify this MAC later.",
        )

    def _get_key_bytes(self) -> bytes:
        raw = self.key_var.get().strip() 
        if not raw:
            raise ValueError("Key is empty.")
        return raw.encode("utf-8")

    def _set_result(self, icon: str, title: str, message: str, tone: str):
        """tone: 'success' | 'error' | 'neutral'"""
        palette = {
            "success": (COLOR_SUCCESS_BG, COLOR_SUCCESS_BD, COLOR_SUCCESS),
            "error":   (COLOR_ERROR_BG, COLOR_ERROR_BD, COLOR_ERROR),
            "neutral": (COLOR_NEUTRAL_BG, COLOR_NEUTRAL_BD, COLOR_TEXT),
        }
        bg, border, fg = palette[tone]
        self.result_card.config(bg=bg, highlightbackground=border)
        for child in self.result_card.winfo_children():
            child.config(bg=bg)
            for grandchild in child.winfo_children():
                grandchild.config(bg=bg)
        self.result_icon_var.set(icon)
        self.result_icon_label.config(fg=fg)
        self.result_title_var.set(title)
        self.result_title_label.config(fg=fg)
        self.result_var.set(message)
        self.result_label.config(fg=fg if tone != "neutral" else COLOR_TEXT)

    def _on_generate(self):
        try:
            key = self._get_key_bytes()
            message = self.message_text.get("1.0", "end-1c").encode("utf-8")
            algo = self.algo_var.get()
            mac = generate_mac(key, message, algo)
            self.mac_var.set(mac)
            self._set_result("✓", f"MAC GENERATED · {algo.upper()}", mac, "success")
        except Exception as e:
            self._set_result("✕", "ERROR", str(e), "error")

    def _on_verify(self):
        try:
            key = self._get_key_bytes()
            message = self.message_text.get("1.0", "end-1c").encode("utf-8")
            algo = self.algo_var.get()
            mac = self.mac_var.get()
            if not mac:
                raise ValueError("Enter a MAC to verify.")
            ok = verify_mac(key, message, mac, algo)
            if ok:
                self._set_result("✓", "VALID", "Message is intact and authentic.", "success")
            else:
                self._set_result(
                    "✕", "INVALID", "Message, key, or MAC does not match.", "error"
                )
        except Exception as e:
            self._set_result("✕", "ERROR", str(e), "error")

    def _copy_result(self):
        mac = self.mac_var.get()
        if mac:
            self.clipboard_clear()
            self.clipboard_append(mac)
            messagebox.showinfo("Copied", "MAC copied to clipboard.")
        else:
            messagebox.showwarning("Nothing to copy", "There's no MAC value yet.")


if __name__ == "__main__":
    app = MacApp()
    app.mainloop()
