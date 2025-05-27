# 🔐 KyberCryptor [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Quantum-resistant encryption tool implementing Kyber512 (NIST-standardized PQC algorithm) with hybrid encryption capabilities.

> [!WARNING]
> Developed for educational/research purposes only. Not recommended for production use or sensitive data protection.


## 🌟 Features

- **Post-Quantum Secure**: Implements Kyber512 (NIST PQC Finalist)
- **Hybrid Encryption**: Combines Kyber KEM with XOR symmetric encryption
- **Simple CLI Interface**: Easy encrypt/decrypt workflows
- **Cross-Platform**: Supports Linux, macOS, and Windows*
- **Lightweight**: Minimal dependencies with Python 3.8+ compatibility

*Windows requires manual liboqs compilation


## 📋 Prerequisites
- Python 3.8+
- Open Quantum Safe Library (liboqs)
- Python `oqs` bindings


## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/odaysec/kybercryptor.git
cd kybercryptor
```

### 2. Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install OQS Python bindings
pip install oqs
```


## 🛠 Usage Guide Encrypt Message
1. Edit `encrypt.py` to modify default message ("Kyber")
2. Run encryption:
```bash
python encrypt.py
```
Generates:
- `kyber_encrypted.dat` (encrypted payload)
- Keypair and shared secret

### 🔓 Decrypt Message
```bash
python decrypt.py
```
Outputs decrypted message to console

## 📂 File Structure
```
kybercryptor/
├── encrypt.py          # Encryption workflow
├── decrypt.py          # Decryption workflow
├── utils.py            # XOR encryption helpers
├── requirements.txt   # Dependency list
├── LICENSE            # MIT License
└── examples/          # Usage examples (future)
```


## 💻 Example Session
```bash
# Encryption
$ python encrypt.py
Successfully encrypted message to kyber_encrypted.dat

# Decryption 
$ python decrypt.py
Decrypted message: Kyber
```
## 🔄 Process Flow

### Encryption Workflow
```mermaid
sequenceDiagram
    participant User
    participant Encrypt.py
    participant OQS
    participant File
    
    User->>Encrypt.py: Execute script
    Encrypt.py->>OQS: Generate Kyber512 keypair
    OQS-->>Encrypt.py: (pk, sk)
    Encrypt.py->>OQS: Encapsulate shared secret
    OQS-->>Encrypt.py: ciphertext, ss
    Encrypt.py->>Encrypt.py: XOR encrypt message (msg ⊕ ss)
    Encrypt.py->>File: Save pk + ciphertext + encrypted_msg
```

### Decryption Workflow
```mermaid
sequenceDiagram
    participant User
    participant Decrypt.py
    participant OQS
    participant File
    
    User->>Decrypt.py: Execute script
    Decrypt.py->>File: Load encrypted data
    Decrypt.py->>OQS: Decapsulate shared secret (sk, ciphertext)
    OQS-->>Decrypt.py: ss
    Decrypt.py->>Decrypt.py: XOR decrypt message (encrypted_msg ⊕ ss)
    Decrypt.py-->>User: Display plaintext
```



## 📚 Documentation Hybrid Encryption Workflow
1. Kyber512 generates public/private keypair
2. Shared secret established via KEM
3. XOR cipher encrypts payload using shared secret
4. Encrypted data stored with public key


## 📜 License
MIT Licensed - See [LICENSE](LICENSE) for details.
