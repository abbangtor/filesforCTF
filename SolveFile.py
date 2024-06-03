from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

# Load the key
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

# Decrypt the file
decrypted_data = decrypt_file("C:\\filesforCTF\\EncryptedFile.txt", key)

# Save the decrypted data to DecryptedFile.txt
with open("C:\\filesforCTF\\DecryptedFile.txt", 'wb') as f:
    f.write(decrypted_data)
