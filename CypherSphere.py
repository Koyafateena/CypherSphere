from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the encryption key (must be 16, 24, or 32 bytes long)
key = get_random_bytes(32)

# Sample data to encrypt
data = b"This is a secret message!"

# Create a cipher object
cipher = AES.new(key, AES.MODE_GCM)

# Encrypt the data
ciphertext, auth_tag = cipher.encrypt_and_digest(data)

print(f"Encrypted data: {ciphertext.hex()}")
print(f"Authentication tag: {auth_tag.hex()}")

# Decrypt the ciphertext
decrypted_data = cipher.decrypt_and_verify(ciphertext, auth_tag)

print(f"Decrypted data: {decrypted_data.decode()}")