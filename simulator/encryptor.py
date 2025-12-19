from cryptography.fernet import Fernet
import os

def generate_key(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    return key

def load_key(key_path):
    with open(key_path, "rb") as f:
        return f.read()

def encrypt_folder(folder_path, key_path):
    if not os.path.exists(key_path):
        key = generate_key(key_path)
    else:
        key = load_key(key_path)

    fernet = Fernet(key)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(file_path, "wb") as f:
                f.write(encrypted)
