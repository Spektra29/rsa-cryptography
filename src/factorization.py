# factorization.py

import random
import time
import math

import matplotlib.pyplot as plt

from primality import generate_prime
from math_utils import mod_exp

def pollard_rho(n):
    """
    Pollard's Rho integer factorization algorithm.
    Returns a non-trivial factor of n.
    """

    # Handle even numbers
    if n % 2 == 0:
        return 2

    while True:

        # Random function parameters
        x = random.randint(2, n - 1)
        y = x

        c = random.randint(1, n - 1)

        d = 1

        while d == 1:

            # f(x) = x^2 + c mod n
            x = (mod_exp(x, 2, n) + c) % n
            y = (mod_exp(y, 2, n) + c) % n
            y = (mod_exp(y, 2, n) + c) % n

            d = math.gcd(abs(x - y), n)

        if d != n:
            return d


def generate_semiprime(bits):
    """
    Generate semiprime n = p * q.
    """

    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    while p == q:
        q = generate_prime(bits // 2)

    return p * q


def benchmark_factorization(bit_sizes):
    """
    Benchmark factorization times for semiprimes.
    """

    times = []

    print("\n=== Factorization Benchmark ===\n")

    for bits in bit_sizes:

        print(f"Generating {bits}-bit semiprime...")

        n = generate_semiprime(bits)

        print(f"Factoring {bits}-bit semiprime...")

        start_time = time.perf_counter()

        factor = pollard_rho(n)

        end_time = time.perf_counter()

        elapsed = end_time - start_time

        times.append(elapsed)

        print(f"Factor found: {factor}")

        print(f"Time: {elapsed:.4f} seconds\n")

    return times


def plot_results(bit_sizes, times):
    """
    Plot factorization benchmark results.
    """

    plt.figure(figsize=(10, 6))

    plt.plot(bit_sizes, times, marker='o')

    plt.xlabel("Semiprime Bit Size")

    plt.ylabel("Factorization Time (seconds)")

    plt.title("Pollard Rho Factorization Benchmark")

    plt.grid(True)

    plt.savefig("graphs/factorization_results.png")

    plt.show()


if __name__ == "__main__":

    # Small sizes only
    bit_sizes = [16, 24, 32, 40, 48, 64]

    times = benchmark_factorization(bit_sizes)

    plot_results(bit_sizes, times)