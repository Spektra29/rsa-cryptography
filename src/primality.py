import random


def is_prime(n: int, k: int = 10) -> bool:
    """
    Miller-Rabin primality test.

    Args:
        n (int): Number to test for primality.
        k (int): Number of testing rounds for accuracy.

    Returns:
        bool: True if n is probably prime, False otherwise.
    """

    # Handle small numbers and edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n - 1 as (2^r) * d
    r = 0
    d = n - 1

    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform Miller-Rabin test k times
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        # If x is 1 or n - 1, continue to next round
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def generate_prime(bits: int = 512) -> int:
    """
    Generate a random prime number with the specified bit length.

    Args:
        bits (int): Desired bit length of the prime.

    Returns:
        int: A probably prime number.
    """

    while True:
        # Generate random odd number with correct bit length
        candidate = random.getrandbits(bits)

        # Ensure highest bit and oddness
        candidate |= (1 << bits - 1) | 1

        if is_prime(candidate):
            return candidate


if __name__ == "__main__":
    print("Generating a 128-bit prime number...")
    prime = generate_prime(128)

    print(f"Prime number generated:\n{prime}")
