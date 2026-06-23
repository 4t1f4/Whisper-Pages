from cryptography.fernet import Fernet
import os

cipher = Fernet(os.getenv("ENCRYPTION_KEY").encode())


def encrypt_text(text):
  return cipher.encrypt(text.encode()).decode()



def decrypt_text(text):
  return cipher.decrypt(text.encode()).decode()


# encode() = str -> bytes
# decode() = bytes -> str
# Fernet encrypt/decrypt works only with bytes
