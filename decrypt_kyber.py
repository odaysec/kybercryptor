# decrypt_kyber.py
import pickle

# Buka file hasil enkripsi
with open("kyber_encrypted.dat", "rb") as f:
    data = pickle.load(f)

encrypted_message = data["encrypted_message"]
shared_secret = data["shared_secret"]

# Lakukan dekripsi (XOR ulang)
decrypted_message = bytes([c ^ k for c, k in zip(encrypted_message, shared_secret)])

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message.decode())
