# security/encryption.py
from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data.encode()).decode()

# Usage
# enc = Encryption()
# encrypted_text = enc.encrypt("Sensitive Data")
# print(enc.decrypt(encrypted_text))
