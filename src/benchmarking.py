# benchmarking.py

import time
import matplotlib.pyplot as plt

from primality import generate_prime
from rsa_core import generate_keypair


def benchmark_prime_generation(bit_sizes):
    """
    Benchmark prime generation times.
    """

    times = []

    print("\n=== Prime Generation Benchmark ===\n")

    for bits in bit_sizes:

        print(f"Generating {bits}-bit prime...")

        start_time = time.perf_counter()

        generate_prime(bits)

        end_time = time.perf_counter()

        elapsed = end_time - start_time

        times.append(elapsed)

        print(f"{bits}-bit prime generated in {elapsed:.4f} seconds\n")

    return times


def benchmark_key_generation(bit_sizes):
    """
    Benchmark RSA keypair generation times.
    """

    times = []

    print("\n=== RSA Key Generation Benchmark ===\n")

    for bits in bit_sizes:

        print(f"Generating RSA keypair with {bits}-bit primes...")

        start_time = time.perf_counter()

        generate_keypair(bits)

        end_time = time.perf_counter()

        elapsed = end_time - start_time

        times.append(elapsed)

        print(f"Keypair generated in {elapsed:.4f} seconds\n")

    return times


def plot_results(bit_sizes, prime_times, key_times):
    """
    Plot benchmark results.
    """

    plt.figure(figsize=(10, 6))

    plt.plot(bit_sizes, prime_times, marker='o', label='Prime Generation')

    plt.plot(bit_sizes, key_times, marker='o', label='RSA Key Generation')

    plt.xlabel("Bit Size")

    plt.ylabel("Time (seconds)")

    plt.title("RSA Benchmarking")

    plt.legend()

    plt.grid(True)

    plt.savefig("graphs/benchmark_results.png")

    plt.show()


if __name__ == "__main__":

    bit_sizes = [128, 256, 512, 1024]

    # Benchmark prime generation
    prime_times = benchmark_prime_generation(bit_sizes)

    # Benchmark RSA key generation
    key_times = benchmark_key_generation(bit_sizes)

    # Plot results
    plot_results(bit_sizes, prime_times, key_times)