import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import secrets
import string
from cryptography.fernet import Fernet
import base64
import hashlib
import json
from datetime import datetime
import re

class ModernPasswordVault:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoVault Pro")
        self.root.geometry("1100x750")

        self.colors = {
            'bg': '#F2F2F7',
            'card': '#FFFFFF',
            'primary': '#007AFF',
            'secondary': '#5856D6',
            'success': '#34C759',
            'warning': '#FF9500',
            'danger': '#FF3B30',
            'text': '#000000',
            'text_secondary': '#8E8E93',
            'border': '#C6C6C8'
        }

        self.root.configure(bg=self.colors['bg'])
        self.is_authenticated = False
        self.cipher_key = None
        self.current_view = 'all'

        self.show_auth_screen()

    def show_auth_screen(self):
        self.auth_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.auth_frame.pack(fill=tk.BOTH, expand=True)

        center_frame = tk.Frame(self.auth_frame, bg=self.colors['card'], bd=0)
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        logo_frame = tk.Frame(center_frame, bg=self.colors['primary'], width=100, height=100)
        logo_frame.pack(pady=(40, 20))
        logo_frame.pack_propagate(False)

        logo_label = tk.Label(logo_frame, text="🔐", font=("Arial", 48), bg=self.colors['primary'], fg='white')
        logo_label.pack(expand=True)

        title = tk.Label(center_frame, text="CryptoVault Pro", font=("Arial", 28, "bold"), 
                        bg=self.colors['card'], fg=self.colors['text'])
        title.pack(pady=(0, 10))

        subtitle = tk.Label(center_frame, text="Secure Password Management", font=("Arial", 14),
                           bg=self.colors['card'], fg=self.colors['text_secondary'])
        subtitle.pack(pady=(0, 30))

        tk.Label(center_frame, text="Master Password", font=("Arial", 12),
                bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor='w', padx=40)

        self.master_password_entry = tk.Entry(center_frame, font=("Arial", 14), show="●", relief=tk.FLAT,
                                             bg='#F2F2F7', width=30, bd=0, highlightthickness=1,
                                             highlightbackground=self.colors['border'],
                                             highlightcolor=self.colors['primary'])
        self.master_password_entry.pack(pady=(5, 20), padx=40, ipady=10)
        self.master_password_entry.bind('<Return>', lambda e: self.authenticate())

        btn_frame = tk.Frame(center_frame, bg=self.colors['card'])
        btn_frame.pack(pady=(0, 40), padx=40)

        unlock_btn = tk.Button(btn_frame, text="Unlock", command=self.authenticate,
                              font=("Arial", 14, "bold"), bg=self.colors['primary'], fg='white',
                              relief=tk.FLAT, cursor='hand2', width=12, bd=0,
                              activebackground='#0051D5', activeforeground='white')
        unlock_btn.pack(side=tk.LEFT, padx=(0, 10), ipady=8)

        setup_btn = tk.Button(btn_frame, text="Setup New", command=self.setup_master_password,
                             font=("Arial", 14), bg=self.colors['card'], fg=self.colors['primary'],
                             relief=tk.FLAT, cursor='hand2', width=12, bd=0,
                             highlightthickness=1, highlightbackground=self.colors['primary'])
        setup_btn.pack(side=tk.LEFT, ipady=8)

        self.master_password_entry.focus()

    def setup_master_password(self):
        password = self.master_password_entry.get()

        if len(password) < 8:
            messagebox.showerror("Error", "Master password must be at least 8 characters!")
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = sqlite3.connect('vault_config.db')
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS config (key TEXT PRIMARY KEY, value TEXT NOT NULL)')
            cursor.execute("INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)",
                          ('master_password_hash', password_hash))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Master password setup complete!")
            self.master_password_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to setup: {str(e)}")

    def authenticate(self):
        password = self.master_password_entry.get()

        if not password:
            messagebox.showerror("Error", "Please enter master password!")
            return

        try:
            conn = sqlite3.connect('vault_config.db')
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM config WHERE key='master_password_hash'")
            result = cursor.fetchone()
            conn.close()

            if not result:
                messagebox.showerror("Error", "No master password found! Please setup first.")
                return

            stored_hash = result[0]
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if password_hash == stored_hash:
                self.cipher_key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
                self.is_authenticated = True
                self.auth_frame.destroy()
                self.init_database()
                self.create_main_interface()
            else:
                messagebox.showerror("Error", "Incorrect master password!")
                self.master_password_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Authentication failed: {str(e)}")

    def init_database(self):
        self.conn = sqlite3.connect('password_vault_pro.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            category TEXT DEFAULT 'General',
            notes TEXT,
            is_favorite INTEGER DEFAULT 0,
            strength INTEGER DEFAULT 0,
            created_at TEXT,
            updated_at TEXT
        )''')
        self.conn.commit()

    def create_main_interface(self):
        header = tk.Frame(self.root, bg='white', height=80)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)

        tk.Label(header, text="🔐 CryptoVault Pro", font=("Arial", 24, "bold"),
                bg='white', fg=self.colors['text']).pack(side=tk.LEFT, padx=20, pady=20)

        header_btn_frame = tk.Frame(header, bg='white')
        header_btn_frame.pack(side=tk.RIGHT, padx=20)

        tk.Button(header_btn_frame, text="📊 Stats", command=self.show_statistics,
                 font=("Arial", 11), bg=self.colors['secondary'], fg='white',
                 relief=tk.FLAT, cursor='hand2', bd=0, padx=15, pady=8).pack(side=tk.LEFT, padx=5)

        tk.Button(header_btn_frame, text="⚙️ Settings", command=self.show_settings,
                 font=("Arial", 11), bg=self.colors['text_secondary'], fg='white',
                 relief=tk.FLAT, cursor='hand2', bd=0, padx=15, pady=8).pack(side=tk.LEFT, padx=5)

        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.create_sidebar(main_container)

        self.content_area = tk.Frame(main_container, bg=self.colors['bg'])
        self.content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0))

        self.create_content_area()

    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=self.colors['card'], width=250, relief=tk.FLAT, bd=0)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, pady=0)
        sidebar.pack_propagate(False)

        search_frame = tk.Frame(sidebar, bg=self.colors['card'])
        search_frame.pack(fill=tk.X, padx=15, pady=15)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), relief=tk.FLAT,
                                     bg='#F2F2F7', fg=self.colors['text'], bd=0)
        self.search_entry.pack(fill=tk.X, ipady=8, padx=5)
        self.search_entry.insert(0, "🔍 Search passwords...")
        self.search_entry.bind('<FocusIn>', self.on_search_focus_in)
        self.search_entry.bind('<FocusOut>', self.on_search_focus_out)
        self.search_entry.bind('<KeyRelease>', self.search_passwords)

        tk.Label(sidebar, text="CATEGORIES", font=("Arial", 10, "bold"),
                bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor='w', padx=20, pady=(10, 5))

        categories = [
            ("All Passwords", "all", "📁"), ("Favorites", "favorites", "⭐"),
            ("Social Media", "Social Media", "📱"), ("Banking", "Banking", "🏦"),
            ("Email", "Email", "📧"), ("Work", "Work", "💼"),
            ("Shopping", "Shopping", "🛒"), ("General", "General", "📝")
        ]

        for name, category, icon in categories:
            btn = tk.Button(sidebar, text=f"{icon}  {name}",
                           command=lambda c=category: self.filter_by_category(c),
                           font=("Arial", 12), bg=self.colors['card'], fg=self.colors['text'],
                           relief=tk.FLAT, cursor='hand2', anchor='w', bd=0,
                           activebackground='#F2F2F7')
            btn.pack(fill=tk.X, padx=15, pady=2, ipady=8)

        add_btn = tk.Button(sidebar, text="+ Add New Password", command=self.show_add_dialog,
                           font=("Arial", 13, "bold"), bg=self.colors['primary'], fg='white',
                           relief=tk.FLAT, cursor='hand2', bd=0, activebackground='#0051D5')
        add_btn.pack(fill=tk.X, padx=15, pady=20, ipady=12)

    def create_content_area(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

        toolbar = tk.Frame(self.content_area, bg=self.colors['bg'])
        toolbar.pack(fill=tk.X, pady=(0, 15))

        tk.Label(toolbar, text="All Passwords", font=("Arial", 20, "bold"),
                bg=self.colors['bg'], fg=self.colors['text']).pack(side=tk.LEFT)

        action_frame = tk.Frame(toolbar, bg=self.colors['bg'])
        action_frame.pack(side=tk.RIGHT)

        tk.Button(action_frame, text="📤 Export", command=self.export_data,
                 font=("Arial", 11), bg=self.colors['card'], fg=self.colors['primary'],
                 relief=tk.FLAT, cursor='hand2', bd=0, highlightthickness=1,
                 highlightbackground=self.colors['border'], padx=12, pady=6).pack(side=tk.LEFT, padx=5)

        tk.Button(action_frame, text="📥 Import", command=self.import_data,
                 font=("Arial", 11), bg=self.colors['card'], fg=self.colors['primary'],
                 relief=tk.FLAT, cursor='hand2', bd=0, highlightthickness=1,
                 highlightbackground=self.colors['border'], padx=12, pady=6).pack(side=tk.LEFT, padx=5)

        canvas = tk.Canvas(self.content_area, bg=self.colors['bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.content_area, orient="vertical", command=canvas.yview)
        self.cards_frame = tk.Frame(canvas, bg=self.colors['bg'])

        self.cards_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.refresh_password_cards()

    def create_password_card(self, parent, data):
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        card.pack(fill=tk.X, pady=8)

        content = tk.Frame(card, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        top_row = tk.Frame(content, bg=self.colors['card'])
        top_row.pack(fill=tk.X)

        website_label = tk.Label(top_row, text=data[1], font=("Arial", 16, "bold"),
                                bg=self.colors['card'], fg=self.colors['text'])
        website_label.pack(side=tk.LEFT)

        if data[6]:
            tk.Label(top_row, text="⭐", font=("Arial", 14), bg=self.colors['card']).pack(side=tk.LEFT, padx=10)

        category_badge = tk.Label(top_row, text=data[4], font=("Arial", 10),
                                 bg='#F2F2F7', fg=self.colors['text_secondary'], padx=8, pady=2)
        category_badge.pack(side=tk.RIGHT)

        tk.Label(content, text=f"👤 {data[2]}", font=("Arial", 13),
                bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor='w', pady=(5, 10))

        strength = data[7] if len(data) > 7 else 0
        strength_frame = tk.Frame(content, bg=self.colors['card'])
        strength_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(strength_frame, text="Strength:", font=("Arial", 10),
                bg=self.colors['card'], fg=self.colors['text_secondary']).pack(side=tk.LEFT)

        strength_colors = {0: '#FF3B30', 1: '#FF9500', 2: '#FFCC00', 3: '#34C759'}
        strength_labels = {0: 'Weak', 1: 'Fair', 2: 'Good', 3: 'Strong'}

        tk.Label(strength_frame, text=strength_labels.get(strength, 'Weak'),
                font=("Arial", 10, "bold"), bg=self.colors['card'],
                fg=strength_colors.get(strength, '#FF3B30')).pack(side=tk.LEFT, padx=5)

        btn_frame = tk.Frame(content, bg=self.colors['card'])
        btn_frame.pack(fill=tk.X)

        buttons_data = [
            ("👁️ Show", lambda: self.show_password(data[0]), self.colors['primary']),
            ("📋 Copy", lambda: self.copy_password(data[0]), self.colors['success']),
            ("✏️ Edit", lambda: self.edit_password(data[0]), self.colors['warning']),
            ("🗑️ Delete", lambda: self.delete_password(data[0]), self.colors['danger'])
        ]

        for text, command, color in buttons_data:
            btn = tk.Button(btn_frame, text=text, command=command, font=("Arial", 10),
                          bg=color, fg='white', relief=tk.FLAT, cursor='hand2', bd=0, width=10)
            btn.pack(side=tk.LEFT, padx=(0, 8), ipady=5)

    def show_add_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Password")
        dialog.geometry("500x700")
        dialog.configure(bg=self.colors['bg'])
        dialog.transient(self.root)
        dialog.grab_set()

        content = tk.Frame(dialog, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(content, text="Add New Password", font=("Arial", 20, "bold"),
                bg=self.colors['card']).pack(pady=(20, 30))

        fields = [("Website", "website"), ("Username/Email", "username"), 
                 ("Password", "password"), ("Notes", "notes")]

        entries = {}

        for label, key in fields:
            tk.Label(content, text=label, font=("Arial", 12), bg=self.colors['card'],
                    fg=self.colors['text_secondary']).pack(anchor='w', padx=30, pady=(10, 5))

            if key == "password":
                entry_frame = tk.Frame(content, bg=self.colors['card'])
                entry_frame.pack(fill=tk.X, padx=30)

                entry = tk.Entry(entry_frame, font=("Arial", 13), relief=tk.FLAT,
                               bg='#F2F2F7', show="●", bd=0)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 10))
                entries[key] = entry

                gen_btn = tk.Button(entry_frame, text="🎲",
                                  command=lambda e=entry: self.generate_and_insert_password(e),
                                  font=("Arial", 16), bg=self.colors['primary'], fg='white',
                                  relief=tk.FLAT, cursor='hand2', bd=0, width=3)
                gen_btn.pack(side=tk.RIGHT, ipady=8)
            else:
                entry = tk.Entry(content, font=("Arial", 13), relief=tk.FLAT, bg='#F2F2F7', bd=0)
                entry.pack(fill=tk.X, padx=30, ipady=10)
                entries[key] = entry

        tk.Label(content, text="Category", font=("Arial", 12), bg=self.colors['card'],
                fg=self.colors['text_secondary']).pack(anchor='w', padx=30, pady=(10, 5))

        category_var = tk.StringVar(value="General")
        category_menu = ttk.Combobox(content, textvariable=category_var,
                                    values=["General", "Social Media", "Banking", "Email", "Work", "Shopping"],
                                    font=("Arial", 13), state="readonly")
        category_menu.pack(fill=tk.X, padx=30, ipady=8)

        favorite_var = tk.IntVar()
        favorite_check = tk.Checkbutton(content, text="⭐ Add to favorites", variable=favorite_var,
                                       font=("Arial", 12), bg=self.colors['card'],
                                       fg=self.colors['text'], selectcolor=self.colors['card'])
        favorite_check.pack(anchor='w', padx=30, pady=15)

        btn_frame = tk.Frame(content, bg=self.colors['card'])
        btn_frame.pack(pady=30)

        def save_password():
            website = entries['website'].get().strip()
            username = entries['username'].get().strip()
            password = entries['password'].get().strip()
            notes = entries['notes'].get().strip()
            category = category_var.get()
            is_favorite = favorite_var.get()

            if not website or not username or not password:
                messagebox.showerror("Error", "Website, Username, and Password are required!")
                return

            try:
                encrypted_password = self.encrypt_password(password)
                strength = self.calculate_password_strength(password)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.cursor.execute('''INSERT INTO credentials 
                    (website, username, password, category, notes, is_favorite, strength, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (website, username, encrypted_password, category, notes, is_favorite, strength, now, now))

                self.conn.commit()
                self.refresh_password_cards()
                dialog.destroy()
                messagebox.showinfo("Success", "Password added successfully!")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to add password: {str(e)}")

        tk.Button(btn_frame, text="Save Password", command=save_password,
                 font=("Arial", 13, "bold"), bg=self.colors['primary'], fg='white',
                 relief=tk.FLAT, cursor='hand2', bd=0, width=15, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="Cancel", command=dialog.destroy,
                 font=("Arial", 13), bg=self.colors['card'], fg=self.colors['danger'],
                 relief=tk.FLAT, cursor='hand2', bd=0, width=15,
                 highlightthickness=1, highlightbackground=self.colors['border'],
                 pady=10).pack(side=tk.LEFT, padx=10)

    def generate_and_insert_password(self, entry):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(16))
        entry.delete(0, tk.END)
        entry.insert(0, password)

    def calculate_password_strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            strength += 1
        if re.search(r'\\d', password):
            strength += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            strength += 1
        return min(strength, 3)

    def encrypt_password(self, password):
        cipher = Fernet(self.cipher_key)
        return cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        cipher = Fernet(self.cipher_key)
        return cipher.decrypt(encrypted_password.encode()).decode()

    def refresh_password_cards(self, query=None, category=None):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        if category and category != 'all':
            if category == 'favorites':
                self.cursor.execute("SELECT * FROM credentials WHERE is_favorite=1 ORDER BY updated_at DESC")
            else:
                self.cursor.execute("SELECT * FROM credentials WHERE category=? ORDER BY updated_at DESC", (category,))
        elif query:
            search_term = f"%{query}%"
            self.cursor.execute(
                "SELECT * FROM credentials WHERE website LIKE ? OR username LIKE ? ORDER BY updated_at DESC",
                (search_term, search_term))
        else:
            self.cursor.execute("SELECT * FROM credentials ORDER BY updated_at DESC")

        rows = self.cursor.fetchall()

        if not rows:
            tk.Label(self.cards_frame, text="No passwords found", font=("Arial", 14),
                    bg=self.colors['bg'], fg=self.colors['text_secondary']).pack(pady=50)
        else:
            for row in rows:
                self.create_password_card(self.cards_frame, row)

    def filter_by_category(self, category):
        self.current_view = category
        self.refresh_password_cards(category=category)

    def search_passwords(self, event=None):
        query = self.search_entry.get()
        if query and query != "🔍 Search passwords...":
            self.refresh_password_cards(query=query)
        else:
            self.refresh_password_cards()

    def on_search_focus_in(self, event):
        if self.search_entry.get() == "🔍 Search passwords...":
            self.search_entry.delete(0, tk.END)

    def on_search_focus_out(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "🔍 Search passwords...")

    def show_password(self, password_id):
        self.cursor.execute("SELECT password, website FROM credentials WHERE id=?", (password_id,))
        result = self.cursor.fetchone()
        if result:
            decrypted = self.decrypt_password(result[0])
            messagebox.showinfo(f"Password for {result[1]}", f"Password: {decrypted}")

    def copy_password(self, password_id):
        self.cursor.execute("SELECT password FROM credentials WHERE id=?", (password_id,))
        result = self.cursor.fetchone()
        if result:
            decrypted = self.decrypt_password(result[0])
            self.root.clipboard_clear()
            self.root.clipboard_append(decrypted)
            messagebox.showinfo("Success", "Password copied to clipboard!")

    def edit_password(self, password_id):
        self.cursor.execute("SELECT * FROM credentials WHERE id=?", (password_id,))
        data = self.cursor.fetchone()
        if not data:
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Password")
        dialog.geometry("500x700")
        dialog.configure(bg=self.colors['bg'])
        dialog.transient(self.root)
        dialog.grab_set()

        content = tk.Frame(dialog, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(content, text="Edit Password", font=("Arial", 20, "bold"),
                bg=self.colors['card']).pack(pady=(20, 30))

        fields = [
            ("Website", "website", data[1]),
            ("Username/Email", "username", data[2]),
            ("Password", "password", self.decrypt_password(data[3])),
            ("Notes", "notes", data[5] if data[5] else "")
        ]

        entries = {}

        for label, key, value in fields:
            tk.Label(content, text=label, font=("Arial", 12), bg=self.colors['card'],
                    fg=self.colors['text_secondary']).pack(anchor='w', padx=30, pady=(10, 5))

            if key == "password":
                entry_frame = tk.Frame(content, bg=self.colors['card'])
                entry_frame.pack(fill=tk.X, padx=30)

                entry = tk.Entry(entry_frame, font=("Arial", 13), relief=tk.FLAT,
                               bg='#F2F2F7', show="●", bd=0)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 10))
                entry.insert(0, value)
                entries[key] = entry

                gen_btn = tk.Button(entry_frame, text="🎲",
                                  command=lambda e=entry: self.generate_and_insert_password(e),
                                  font=("Arial", 16), bg=self.colors['primary'], fg='white',
                                  relief=tk.FLAT, cursor='hand2', bd=0, width=3)
                gen_btn.pack(side=tk.RIGHT, ipady=8)
            else:
                entry = tk.Entry(content, font=("Arial", 13), relief=tk.FLAT, bg='#F2F2F7', bd=0)
                entry.pack(fill=tk.X, padx=30, ipady=10)
                entry.insert(0, value)
                entries[key] = entry

        tk.Label(content, text="Category", font=("Arial", 12), bg=self.colors['card'],
                fg=self.colors['text_secondary']).pack(anchor='w', padx=30, pady=(10, 5))

        category_var = tk.StringVar(value=data[4])
        category_menu = ttk.Combobox(content, textvariable=category_var,
                                    values=["General", "Social Media", "Banking", "Email", "Work", "Shopping"],
                                    font=("Arial", 13), state="readonly")
        category_menu.pack(fill=tk.X, padx=30, ipady=8)

        favorite_var = tk.IntVar(value=data[6])
        favorite_check = tk.Checkbutton(content, text="⭐ Add to favorites", variable=favorite_var,
                                       font=("Arial", 12), bg=self.colors['card'],
                                       fg=self.colors['text'], selectcolor=self.colors['card'])
        favorite_check.pack(anchor='w', padx=30, pady=15)

        btn_frame = tk.Frame(content, bg=self.colors['card'])
        btn_frame.pack(pady=30)

        def update_password():
            website = entries['website'].get().strip()
            username = entries['username'].get().strip()
            password = entries['password'].get().strip()
            notes = entries['notes'].get().strip()
            category = category_var.get()
            is_favorite = favorite_var.get()

            if not website or not username or not password:
                messagebox.showerror("Error", "Website, Username, and Password are required!")
                return

            try:
                encrypted_password = self.encrypt_password(password)
                strength = self.calculate_password_strength(password)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.cursor.execute('''UPDATE credentials SET website=?, username=?, password=?, 
                    category=?, notes=?, is_favorite=?, strength=?, updated_at=? WHERE id=?''',
                    (website, username, encrypted_password, category, notes, is_favorite, strength, now, password_id))

                self.conn.commit()
                self.refresh_password_cards()
                dialog.destroy()
                messagebox.showinfo("Success", "Password updated successfully!")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to update password: {str(e)}")

        tk.Button(btn_frame, text="Update", command=update_password,
                 font=("Arial", 13, "bold"), bg=self.colors['primary'], fg='white',
                 relief=tk.FLAT, cursor='hand2', bd=0, width=15, pady=10).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="Cancel", command=dialog.destroy,
                 font=("Arial", 13), bg=self.colors['card'], fg=self.colors['danger'],
                 relief=tk.FLAT, cursor='hand2', bd=0, width=15,
                 highlightthickness=1, highlightbackground=self.colors['border'],
                 pady=10).pack(side=tk.LEFT, padx=10)

    def delete_password(self, password_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this password?")
        if confirm:
            try:
                self.cursor.execute("DELETE FROM credentials WHERE id=?", (password_id,))
                self.conn.commit()
                self.refresh_password_cards()
                messagebox.showinfo("Success", "Password deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete: {str(e)}")

    def show_statistics(self):
        self.cursor.execute("SELECT COUNT(*) FROM credentials")
        total = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM credentials WHERE strength < 2")
        weak = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM credentials WHERE is_favorite=1")
        favorites = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT category, COUNT(*) FROM credentials GROUP BY category")
        categories = self.cursor.fetchall()

        stats_text = "Statistics\n" + "="*40 + "\n"
        stats_text += f"Total Passwords: {total}\n"
        stats_text += f"Favorites: {favorites}\n"
        stats_text += f"Weak Passwords: {weak}\n\n"
        stats_text += "Categories:\n"

        for cat, count in categories:
            stats_text += f"  {cat}: {count}\n"

        messagebox.showinfo("Statistics", stats_text)

    def show_settings(self):
        messagebox.showinfo("Settings", "Settings - Change master password, themes, etc.")

    def export_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                               filetypes=[("JSON files", "*.json")])

        if filename:
            try:
                self.cursor.execute("SELECT * FROM credentials")
                rows = self.cursor.fetchall()

                export_data = []
                for row in rows:
                    export_data.append({
                        'website': row[1],
                        'username': row[2],
                        'password': self.decrypt_password(row[3]),
                        'category': row[4],
                        'notes': row[5],
                        'is_favorite': row[6]
                    })

                with open(filename, 'w') as f:
                    json.dump(export_data, f, indent=2)

                messagebox.showinfo("Success", f"Exported {len(export_data)} passwords!")

            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {str(e)}")

    def import_data(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if filename:
            try:
                with open(filename, 'r') as f:
                    import_data = json.load(f)

                count = 0
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                for item in import_data:
                    encrypted_password = self.encrypt_password(item['password'])
                    strength = self.calculate_password_strength(item['password'])

                    self.cursor.execute('''INSERT INTO credentials 
                        (website, username, password, category, notes, is_favorite, strength, created_at, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (item['website'], item['username'], encrypted_password, 
                         item.get('category', 'General'), item.get('notes', ''),
                         item.get('is_favorite', 0), strength, now, now))
                    count += 1

                self.conn.commit()
                self.refresh_password_cards()
                messagebox.showinfo("Success", f"Imported {count} passwords!")

            except Exception as e:
                messagebox.showerror("Error", f"Import failed: {str(e)}")

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPasswordVault(root)
    root.mainloop()
