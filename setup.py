import customtkinter as ctk
import os
import sys

class WelcomeScreen:
    def __init__(self):
        self.current_screen = 0
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Elite Password Manager - Welcome")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        try:
            self.root.iconbitmap(icon_path)
        except:
            pass
        
        self.bg_color = "#000000"
        self.text_color = "#ffffff"
        
        self.root.configure(fg_color=self.bg_color)
        
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=40)
        
        self.show_welcome_screen()
        
        self.root.mainloop()
    
    def clear_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_welcome_screen(self):
        """First screen - Welcome"""
        self.clear_frame()
        
        ctk.CTkLabel(self.main_frame, text="", fg_color=self.bg_color).pack(pady=30)
        
        welcome_label = ctk.CTkLabel(
            self.main_frame,
            text="Welcome",
            font=("Arial", 48, "bold"),
            text_color=self.text_color
        )
        welcome_label.pack(pady=(0, 10))
        
        subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Elite Password Manager",
            font=("Arial", 20),
            text_color="#888888"
        )
        subtitle.pack(pady=(0, 60))
        
        start_btn = ctk.CTkButton(
            self.main_frame,
            text="Get Started",
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=self.show_security_screen
        )
        start_btn.pack()
    
    def show_security_screen(self):
        """Second screen - Security info"""
        self.clear_frame()
        
        security_title = ctk.CTkLabel(
            self.main_frame,
            text="Your Security Matters",
            font=("Arial", 28, "bold"),
            text_color=self.text_color
        )
        security_title.pack(pady=(20, 30))
        
        info_text = (
            "Elite Password Manager uses military-grade\n"
            "Fernet encryption (AES-128) to protect your passwords.\n\n"
            "Our source code is completely open and available\n"
            "for review - no backdoors, no data collection,\n"
            "no hidden tricks.\n\n"
            "Your passwords stay on your device,\n"
            "encrypted and secure."
        )
        
        info_label = ctk.CTkLabel(
            self.main_frame,
            text=info_text,
            font=("Arial", 14),
            text_color="#cccccc",
            justify="center"
        )
        info_label.pack(pady=(0, 40))
        
        continue_btn = ctk.CTkButton(
            self.main_frame,
            text="Continue",
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#ffffff",
            text_color="#000000",
            hover_color="#cccccc",
            command=self.launch_main_app
        )
        continue_btn.pack()
    
    def launch_main_app(self):
        """Launch the main app and close welcome screen"""
        self.root.destroy()
        
        import subprocess
        panel_path = os.path.join(os.path.dirname(__file__), "panel.py")
        
        if os.path.exists(panel_path):
            subprocess.Popen([sys.executable, panel_path])
        else:
            app_path = os.path.join(os.path.dirname(__file__), "app.py")
            if os.path.exists(app_path):
                subprocess.Popen([sys.executable, app_path])
        
        try:
            welcome_path = os.path.abspath(__file__)
            if sys.platform == "win32":
                os.system(f'timeout /t 1 /nobreak >nul & del "{welcome_path}"')
            else:
                os.system(f'sleep 1 && rm "{welcome_path}"')
        except:
            pass  # If deletion fails, it's not critical

if __name__ == "__main__":
    app = WelcomeScreen()