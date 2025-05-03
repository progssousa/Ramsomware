from cryptography.fernet import Fernet
import os

target_dir = "C:\\RansomTest"
encrypted_ext = ".locked"

with open(os.path.join(target_dir, "key.txt"), "rb") as keyfile:
    key = keyfile.read()

cipher = Fernet(key)

for filename in os.listdir(target_dir):
    if not filename.endswith(encrypted_ext):
        continue
    file_path = os.path.join(target_dir, filename)

    with open(file_path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)
    original_path = file_path.replace(encrypted_ext, "")

    with open(original_path, "wb") as f:
        f.write(decrypted)

    os.remove(file_path)

print("[✔] Arquivos restaurados com sucesso.")
