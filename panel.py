import customtkinter as ctk
from main import PasswordManager
import os
import random
import string

class ElitePasswordManager:
    def __init__(self):
        self.pm = PasswordManager()
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Elite Password Manager")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        try:
            self.root.iconbitmap(icon_path)
        except:
            pass
        
        self.bg_color = "#000000"
        self.fg_color = "#1a1a1a"
        self.text_color = "#ffffff"
        
        self.root.configure(fg_color=self.bg_color)
        
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=40)
        
        self.show_home_screen()
        
        self.root.mainloop()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_home_screen(self):
        self.clear_frame()
        
        welcome = ctk.CTkLabel(
            self.main_frame,
            text="Welcome",
            font=("Arial", 32, "bold"),
            text_color=self.text_color
        )
        welcome.pack(pady=(10, 30))
        
        checkmark = ctk.CTkLabel(
            self.main_frame,
            text="✓",
            font=("Arial", 120, "bold"),
            text_color="#00ff00"
        )
        checkmark.pack(pady=(0, 10))
        
        status = ctk.CTkLabel(
            self.main_frame,
            text="Passwords secure",
            font=("Arial", 18),
            text_color="#888888"
        )
        status.pack(pady=(0, 30))
        
        view_btn = ctk.CTkButton(
            self.main_frame,
            text="View Passwords",
            width=250,
            height=50,
            font=("Arial", 16),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=self.show_password_list
        )
        view_btn.pack(pady=(0, 40))
        
        panels_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        panels_frame.pack(fill="x")
        
        panel1 = ctk.CTkFrame(panels_frame, fg_color=self.fg_color, corner_radius=10)
        panel1.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(
            panel1,
            text="🔒 Military-Grade Encryption",
            font=("Arial", 14, "bold"),
            text_color=self.text_color,
            anchor="w"
        ).pack(padx=20, pady=(15, 5), anchor="w")
        
        ctk.CTkLabel(
            panel1,
            text="AES-128 Fernet encryption keeps your data safe",
            font=("Arial", 12),
            text_color="#888888",
            anchor="w"
        ).pack(padx=20, pady=(0, 15), anchor="w")
        
        panel2 = ctk.CTkFrame(panels_frame, fg_color=self.fg_color, corner_radius=10)
        panel2.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(
            panel2,
            text="💾 Local Storage Only",
            font=("Arial", 14, "bold"),
            text_color=self.text_color,
            anchor="w"
        ).pack(padx=20, pady=(15, 5), anchor="w")
        
        ctk.CTkLabel(
            panel2,
            text="Your passwords never leave your device",
            font=("Arial", 12),
            text_color="#888888",
            anchor="w"
        ).pack(padx=20, pady=(0, 15), anchor="w")
        
        panel3 = ctk.CTkFrame(panels_frame, fg_color=self.fg_color, corner_radius=10)
        panel3.pack(fill="x")
        
        ctk.CTkLabel(
            panel3,
            text="👁️ Open Source & Transparent",
            font=("Arial", 14, "bold"),
            text_color=self.text_color,
            anchor="w"
        ).pack(padx=20, pady=(15, 5), anchor="w")
        
        ctk.CTkLabel(
            panel3,
            text="No backdoors, no tracking, fully auditable code",
            font=("Arial", 12),
            text_color="#888888",
            anchor="w"
        ).pack(padx=20, pady=(0, 15), anchor="w")
    
    def show_password_list(self):
        self.clear_frame()
        
        header_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        header_frame.pack(fill="x", pady=(0, 20))
        
        back_btn = ctk.CTkButton(
            header_frame,
            text="← Back",
            width=80,
            height=35,
            font=("Arial", 14),
            fg_color="#333333",
            text_color="#ffffff",
            hover_color="#444444",
            command=self.show_home_screen
        )
        back_btn.pack(side="left")
        
        title = ctk.CTkLabel(
            header_frame,
            text="Saved Passwords",
            font=("Arial", 24, "bold"),
            text_color=self.text_color
        )
        title.pack(side="left", padx=20)
        
        add_btn = ctk.CTkButton(
            header_frame,
            text="+ Add Password",
            width=140,
            height=35,
            font=("Arial", 14),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=self.show_add_password
        )
        add_btn.pack(side="right")
        
        passwords = self.pm.load_all_passwords()
        
        if not passwords:
            empty_label = ctk.CTkLabel(
                self.main_frame,
                text="No passwords saved yet\n\nClick 'Add Password' to get started",
                font=("Arial", 16),
                text_color="#888888"
            )
            empty_label.pack(pady=50)
        else:
            scroll_frame = ctk.CTkScrollableFrame(
                self.main_frame,
                fg_color=self.bg_color,
                height=450
            )
            scroll_frame.pack(fill="both", expand=True)
            
            for website in sorted(passwords.keys()):
                password_btn = ctk.CTkButton(
                    scroll_frame,
                    text=website,
                    width=480,
                    height=60,
                    font=("Arial", 16),
                    fg_color=self.fg_color,
                    text_color=self.text_color,
                    hover_color="#2a2a2a",
                    anchor="w",
                    command=lambda w=website: self.show_password_detail(w)
                )
                password_btn.pack(pady=5, padx=10)
    
    def show_add_password(self):
        popup = ctk.CTkToplevel(self.root)
        popup.title("Add New Password")
        popup.geometry("450x400")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()
        
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        try:
            popup.iconbitmap(icon_path)
        except:
            pass
        
        popup.configure(fg_color=self.bg_color)
        
        main_container = ctk.CTkFrame(popup, fg_color=self.bg_color)
        main_container.pack(fill="both", expand=True, padx=30, pady=30)
        
        title = ctk.CTkLabel(
            main_container,
            text="Add New Password",
            font=("Arial", 24, "bold"),
            text_color=self.text_color
        )
        title.pack(pady=(0, 30))
        
        ctk.CTkLabel(
            main_container,
            text="Website URL",
            font=("Arial", 14),
            text_color="#888888",
            anchor="w"
        ).pack(anchor="w", pady=(0, 5))
        
        url_entry = ctk.CTkEntry(
            main_container,
            width=350,
            height=40,
            font=("Arial", 14),
            fg_color=self.fg_color,
            border_color="#333333",
            border_width=2,
            text_color=self.text_color,
            placeholder_text="example.com"
        )
        url_entry.pack(pady=(0, 20))
        
        ctk.CTkLabel(
            main_container,
            text="Password",
            font=("Arial", 14),
            text_color="#888888",
            anchor="w"
        ).pack(anchor="w", pady=(0, 5))
        
        password_entry = ctk.CTkEntry(
            main_container,
            width=350,
            height=40,
            font=("Arial", 14),
            fg_color=self.fg_color,
            border_color="#333333",
            border_width=2,
            text_color=self.text_color,
            placeholder_text="Enter password"
        )
        password_entry.pack(pady=(0, 10))
        
        generate_btn = ctk.CTkButton(
            main_container,
            text="Generate Random Password",
            width=250,
            height=35,
            font=("Arial", 13),
            fg_color="#333333",
            text_color="#ffffff",
            hover_color="#444444",
            command=lambda: self.generate_and_fill(password_entry)
        )
        generate_btn.pack(pady=(0, 30))
        
        def save_password():
            url = url_entry.get().strip()
            password = password_entry.get().strip()
            
            if not url or not password:
                error_label = ctk.CTkLabel(
                    main_container,
                    text="Please fill in both fields",
                    font=("Arial", 12),
                    text_color="#ff3333"
                )
                error_label.pack()
                popup.after(2000, error_label.destroy)
                return
            
            self.pm.save_password(url, password)
            popup.destroy()
            self.show_password_list()
        
        button_frame = ctk.CTkFrame(main_container, fg_color=self.bg_color)
        button_frame.pack()
        
        cancel_btn = ctk.CTkButton(
            button_frame,
            text="Cancel",
            width=160,
            height=45,
            font=("Arial", 14),
            fg_color="#333333",
            text_color="#ffffff",
            hover_color="#444444",
            command=popup.destroy
        )
        cancel_btn.pack(side="left", padx=(0, 10))
        
        save_btn = ctk.CTkButton(
            button_frame,
            text="Save Password",
            width=160,
            height=45,
            font=("Arial", 14),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=save_password
        )
        save_btn.pack(side="left")
    
    def generate_and_fill(self, entry_widget):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(16))
        entry_widget.delete(0, "end")
        entry_widget.insert(0, password)
    
    def show_password_detail(self, website):
        popup = ctk.CTkToplevel(self.root)
        popup.title(f"Password - {website}")
        popup.geometry("450x350")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()
        
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        try:
            popup.iconbitmap(icon_path)
        except:
            pass
        
        popup.configure(fg_color=self.bg_color)
        
        main_container = ctk.CTkFrame(popup, fg_color=self.bg_color)
        main_container.pack(fill="both", expand=True, padx=30, pady=30)
        
        site_label = ctk.CTkLabel(
            main_container,
            text=f"Site: {website}",
            font=("Arial", 14),
            text_color="#888888"
        )
        site_label.pack(pady=(0, 20))
        
        section_label = ctk.CTkLabel(
            main_container,
            text="Saved password for this site",
            font=("Arial", 16, "bold"),
            text_color=self.text_color
        )
        section_label.pack(pady=(0, 15))
        
        password_box = ctk.CTkEntry(
            main_container,
            width=350,
            height=45,
            font=("Courier", 16),
            fg_color=self.fg_color,
            border_color="#333333",
            border_width=2,
            text_color=self.text_color,
            state="readonly"
        )
        password_box.pack(pady=(0, 20))
        
        password = self.pm.get_password(website)
        password_visible = [False]
        
        password_box.configure(state="normal")
        password_box.insert(0, "*" * 12)
        password_box.configure(state="readonly")
        
        button_frame = ctk.CTkFrame(main_container, fg_color=self.bg_color)
        button_frame.pack()
        
        def toggle_password():
            password_box.configure(state="normal")
            password_box.delete(0, "end")
            
            if password_visible[0]:
                password_box.insert(0, "*" * 12)
                show_btn.configure(text="Show password")
                password_visible[0] = False
            else:
                password_box.insert(0, password)
                show_btn.configure(text="Hide password")
                password_visible[0] = True
            
            password_box.configure(state="readonly")
        
        def copy_password():
            popup.clipboard_clear()
            popup.clipboard_append(password)
            popup.update()
            
            original_text = show_btn.cget("text")
            show_btn.configure(text="✓ Copied!")
            popup.after(1500, lambda: show_btn.configure(text=original_text))
        
        show_btn = ctk.CTkButton(
            button_frame,
            text="Show password",
            width=160,
            height=40,
            font=("Arial", 14),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=toggle_password
        )
        show_btn.pack(side="left", padx=(0, 10))
        
        copy_btn = ctk.CTkButton(
            button_frame,
            text="Copy to clipboard",
            width=160,
            height=40,
            font=("Arial", 14),
            fg_color="#333333",
            text_color="#ffffff",
            hover_color="#444444",
            command=copy_password
        )
        copy_btn.pack(side="left")
        
        delete_btn = ctk.CTkButton(
            main_container,
            text="Delete Password",
            width=160,
            height=40,
            font=("Arial", 14),
            fg_color="#ff3333",
            text_color="#ffffff",
            hover_color="#cc0000",
            command=lambda: self.delete_password(website, popup)
        )
        delete_btn.pack(pady=(20, 0))
    
    def delete_password(self, website, popup):
        self.pm.delete_password(website)
        popup.destroy()
        self.show_password_list()

if __name__ == "__main__":
    app = ElitePasswordManager()