from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    return encrypted_data

# Load the key
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

# Encrypt the file
encrypted_data = encrypt_file("C:\\filesforCTF\\UnEncryptedFile.txt", key)

# Save the encrypted data to EncryptedFile.txt
with open("C:\\filesforCTF\\EncryptedFile.txt", 'wb') as f:
    f.write(encrypted_data)
