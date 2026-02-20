import os
import hashlib
import base64
from cryptography.fernet import Fernet

class SecureMemoryEnclave:
    def __init__(self, agent_id: str, secret_key: str):
        # Derive a key from Agent ID + Secret
        key_material = f'{agent_id}:{secret_key}'.encode()
        self.key = base64.urlsafe_b64encode(hashlib.sha256(key_material).digest())
        self.cipher = Fernet(self.key)

    def encrypt(self, data: str) -> bytes:
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data: bytes) -> str:
        return self.cipher.decrypt(encrypted_data).decode()

# Example Usage
if __name__ == '__main__':
    enclave = SecureMemoryEnclave('protocol-zero', 'top-secret')
    memory = 'Sensitive Mission Data'
    encrypted = enclave.encrypt(memory)
    print(f'Encrypted: {encrypted}')
    print(f'Decrypted: {enclave.decrypt(encrypted)}')
