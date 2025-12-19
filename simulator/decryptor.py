from cryptography.fernet import Fernet
import os

def load_key(key_path):
    with open(key_path, "rb") as f:
        return f.read()

def decrypt_folder(folder_path, key_path):
    key = load_key(key_path)
    fernet = Fernet(key)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    encrypted_data = f.read()
                decrypted = fernet.decrypt(encrypted_data)
                with open(file_path, "wb") as f:
                    f.write(decrypted)
            except Exception as e:
                print(f"❌ Failed to decrypt {file_path}: {e}")
