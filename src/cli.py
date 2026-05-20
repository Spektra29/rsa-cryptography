# cli.py

from rsa_core import generate_keypair, encrypt, decrypt


def main():

    public_key = None
    private_key = None

    while True:

        print("\n===== RSA Cryptography System =====")
        print("1. Generate RSA Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # Generate keys
        if choice == "1":

            bits = int(input("Enter key size (256, 512, 1024): "))

            print("\nGenerating keys...")

            public_key, private_key = generate_keypair(bits)

            print("\nPublic Key:")
            print(public_key)

            print("\nPrivate Key:")
            print(private_key)

        # Encrypt
        elif choice == "2":

            if public_key is None:
                print("\nGenerate keys first!")
                continue

            plaintext = input("\nEnter message to encrypt: ")

            ciphertext = encrypt(public_key, plaintext)

            print("\nEncrypted Message:")
            print(ciphertext)

        # Decrypt
        elif choice == "3":

            if private_key is None:
                print("\nGenerate keys first!")
                continue

            ciphertext = int(input("\nEnter ciphertext: "))

            plaintext = decrypt(private_key, ciphertext)

            print("\nDecrypted Message:")
            print(plaintext)

        # Exit
        elif choice == "4":

            print("\nExiting RSA System...")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()