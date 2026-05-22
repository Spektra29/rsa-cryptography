# cli.py

from rsa_core import generate_keypair, encrypt, decrypt

from benchmarking import (
    benchmark_prime_generation,
    benchmark_key_generation,
    plot_results
)

from factorization import (
    benchmark_factorization,
    plot_results as plot_factorization_results
)


def main():

    public_key = None
    private_key = None

    while True:

        print("\n===================================")
        print("      RSA Cryptography System")
        print("===================================")

        print("1. Generate RSA Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Run Benchmark Tests")
        print("5. Run Factorization Benchmark")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        # ==========================================
        # Generate Keys
        # ==========================================
        if choice == "1":

            try:
                bits = int(input(
                    "\nEnter key size (128, 256, 512, 1024): "
                ))

                if bits < 128:
                    print("Key size too small.")
                    continue

            except ValueError:
                print("Invalid number.")
                continue

            print("\nGenerating RSA keys...\n")

            try:

                public_key, private_key = generate_keypair(bits)

                print("RSA Keys Generated Successfully!")

                print("\nPublic Key:")
                print(public_key)

                print("\nPrivate Key:")
                print(private_key)

            except Exception as e:
                print(f"Key generation failed: {e}")

        # ==========================================
        # Encrypt Message
        # ==========================================
        elif choice == "2":

            if public_key is None:
                print("\nGenerate keys first!")
                continue

            plaintext = input("\nEnter message to encrypt: ")

            try:

                ciphertext = encrypt(public_key, plaintext)

                print("\nEncrypted Message:")
                print(ciphertext)

            except Exception as e:
                print(f"Encryption failed: {e}")

        # ==========================================
        # Decrypt Message
        # ==========================================
        elif choice == "3":

            if private_key is None:
                print("\nGenerate keys first!")
                continue

            try:

                ciphertext = int(input("\nEnter ciphertext: "))

            except ValueError:
                print("Ciphertext must be an integer.")
                continue

            try:

                plaintext = decrypt(private_key, ciphertext)

                print("\nDecrypted Message:")
                print(plaintext)

            except Exception as e:
                print(f"Decryption failed: {e}")

        # ==========================================
        # Benchmark Tests
        # ==========================================
        elif choice == "4":

            print("\nRunning Benchmark Tests...\n")

            bit_sizes = [128, 256, 512, 1024]

            try:

                # Prime generation benchmark
                prime_times = benchmark_prime_generation(bit_sizes)

                # RSA key generation benchmark
                key_times = benchmark_key_generation(bit_sizes)

                # Generate graph
                plot_results(
                    bit_sizes,
                    prime_times,
                    key_times
                )

                print("\nBenchmark graph generated:")
                print("graphs/benchmark_results.png")

            except Exception as e:
                print(f"Benchmark failed: {e}")

        # ==========================================
        # Factorization Benchmark
        # ==========================================
        elif choice == "5":

            print("\nRunning Factorization Benchmark...\n")

            bit_sizes = [16, 24, 32, 40, 48, 64]

            try:

                factor_times = benchmark_factorization(bit_sizes)

                plot_factorization_results(
                    bit_sizes,
                    factor_times
                )

                print("\nFactorization graph generated:")
                print("graphs/factorization_results.png")

            except Exception as e:
                print(f"Factorization benchmark failed: {e}")

        # ==========================================
        # Exit
        # ==========================================
        elif choice == "6":

            print("\nExiting RSA Cryptography System...")
            break

        # ==========================================
        # Invalid Choice
        # ==========================================
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()