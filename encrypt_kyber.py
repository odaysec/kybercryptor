import oqs
import pickle

message = b"Kyber"

with oqs.KeyEncapsulation('Kyber512') as client:
    public_key = client.generate_keypair()
    
    with oqs.KeyEncapsulation('Kyber512') as server:
        ciphertext, shared_secret_server = server.encap_secret(public_key)
        shared_secret_client = client.decap_secret(ciphertext)

        # Enkripsi pesan
        encrypted_message = bytes([m ^ k for m, k in zip(message, shared_secret_client)])

        # Simpan semua data untuk decrypt
        data = {
            "ciphertext": ciphertext,
            "shared_secret": shared_secret_server,
            "encrypted_message": encrypted_message
        }

        with open("kyber_encrypted.dat", "wb") as f:
            pickle.dump(data, f)

print("Pesan berhasil dienkripsi dan disimpan ke file `kyber_encrypted.dat`")
