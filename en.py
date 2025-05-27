import oqs

message = b"Name Test Test Name"

# Buat KEM (Key Encapsulation Mechanism) Kyber512
with oqs.KeyEncapsulation('Kyber512') as client:
    public_key = client.generate_keypair()
    
    with oqs.KeyEncapsulation('Kyber512') as server:
        ciphertext, shared_secret_server = server.encap_secret(public_key)
        shared_secret_client = client.decap_secret(ciphertext)

        # Enkripsi pesan pendek dengan XOR (hanya contoh)
        encrypted_message = bytes([m ^ k for m, k in zip(message, shared_secret_client)])
        decrypted_message = bytes([c ^ k for c, k in zip(encrypted_message, shared_secret_server)])

print("Original Message :", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
