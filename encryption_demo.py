from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def symmetric_demo():
    print("--- Symmetric Encryption (Fernet/AES) ---")
    # 1. Key Generation
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # 2. Input
    message = b"Secret Message: Hello World"

    # 3. Encryption
    cipher_text = cipher_suite.encrypt(message)

    # 4. Decryption
    plain_text = cipher_suite.decrypt(cipher_text)

    print(f"Key: {key.decode()}")
    print(f"Input: {message.decode()}")
    print(f"Output: {cipher_text.decode()}")
    print(f"Decrypted: {plain_text.decode()}\n")

def asymmetric_demo():
    print("--- Asymmetric Encryption (RSA) ---")
    # 1. Key Generation (Private & Public)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # 2. Input
    message = b"Secret Message: RSA Info"

    # 3. Encryption (using Public Key)
    cipher_text = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 4. Decryption (using Private Key)
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(f"Input: {message.decode()}")
    print(f"Encrypted Output (Hex): {cipher_text.hex()[:50]}...") # Shortened for display
    print(f"Decrypted: {plain_text.decode()}\n")

if __name__ == "__main__":
    symmetric_demo()
    asymmetric_demo()
