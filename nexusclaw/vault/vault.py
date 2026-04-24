from cryptography.fernet import Fernet
import os

class Vault:
    def __init__(self, key_path: str):
        self.key_path = key_path
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)

    def _load_or_generate_key(self) -> bytes:
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(key)
            return key

    def encrypt(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)

# Example usage:
# vault = Vault('/path/to/keyfile.key')
# encrypted = vault.encrypt(b'secret data')
# decrypted = vault.decrypt(encrypted)
# print(decrypted)
