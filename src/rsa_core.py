# rsa_core.py

import random

from math_utils import gcd, mod_inverse, mod_exp
from primality import generate_prime


def generate_keypair(bits=512):
    """
    Generate RSA public and private keys.
    """

    print("Generating prime p...")
    p = generate_prime(bits)

    print("Generating prime q...")
    q = generate_prime(bits)

    while q == p:
        q = generate_prime(bits)

    # Compute modulus
    n = p * q

    # Euler Totient
    phi = (p - 1) * (q - 1)

    # Common public exponent
    e = 65537

    # Ensure e and phi are coprime
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute private exponent
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(public_key, plaintext):
    """
    Encrypt plaintext using RSA public key.
    """

    e, n = public_key

    # Convert message to bytes then integer
    message_bytes = plaintext.encode('utf-8')
    message_int = int.from_bytes(message_bytes, byteorder='big')

    # RSA encryption
    ciphertext = mod_exp(message_int, e, n)

    return ciphertext


def decrypt(private_key, ciphertext):
    """
    Decrypt ciphertext using RSA private key.
    """

    d, n = private_key

    # RSA decryption
    decrypted_int = mod_exp(ciphertext, d, n)

    # Convert integer back to bytes
    byte_length = (decrypted_int.bit_length() + 7) // 8

    decrypted_bytes = decrypted_int.to_bytes(byte_length, byteorder='big')

    return decrypted_bytes.decode('utf-8')


if __name__ == "__main__":

    print("Generating RSA keypair...\n")

    public_key, private_key = generate_keypair(256)

    print("\nPublic Key:")
    print(public_key)

    print("\nPrivate Key:")
    print(private_key)

    message = "Hello RSA Cryptography"

    print("\nOriginal Message:")
    print(message)

    encrypted = encrypt(public_key, message)

    print("\nEncrypted Message:")
    print(encrypted)

    decrypted = decrypt(private_key, encrypted)

    print("\nDecrypted Message:")
    print(decrypted)