from cryptography.fernet import Fernet
import os

class PasswordManager:
    def __init__(self, key_file='secret.key', passwords_file='passwords.enc'):
        self.key_file = key_file
        self.passwords_file = passwords_file
        self.key = self._load_or_create_key()
        self.fernet = Fernet(self.key)
    
    def _load_or_create_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
    
    def save_password(self, url, password):
        passwords = self.load_all_passwords()
        passwords[url] = password
        data = '\n'.join(f"{u}|{p}" for u, p in passwords.items())
        encrypted = self.fernet.encrypt(data.encode())
        with open(self.passwords_file, 'wb') as f:
            f.write(encrypted)
    
    def get_password(self, url):
        passwords = self.load_all_passwords()
        return passwords.get(url)
    
    def load_all_passwords(self):
        if not os.path.exists(self.passwords_file):
            return {}
        try:
            with open(self.passwords_file, 'rb') as f:
                encrypted = f.read()
            if not encrypted:
                return {}
            decrypted = self.fernet.decrypt(encrypted).decode()
            passwords = {}
            for line in decrypted.split('\n'):
                if '|' in line:
                    url, password = line.split('|', 1)
                    passwords[url] = password
            return passwords
        except Exception as e:
            print(f"Error loading passwords: {e}")
            return {}
    
    def delete_password(self, url):
        passwords = self.load_all_passwords()
        if url in passwords:
            del passwords[url]
            
            if passwords:
                data = '\n'.join(f"{u}|{p}" for u, p in passwords.items())
                encrypted = self.fernet.encrypt(data.encode())
            else:
                encrypted = b''
            
            with open(self.passwords_file, 'wb') as f:
                f.write(encrypted)
            return True
        return False